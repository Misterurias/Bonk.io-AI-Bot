from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import http.server
import json
import threading
import time
import socket
import os
import requests
import sys

DATA_FILE = "game_state.json"
OBSERVERBOT_PORT = 8080  # Port to listen for commands
RESULT_SERVER_PORT = 8081  # Port to send results back
monitoring_game = False  # Flag to control monitoring

# Set up headless Chrome browser
def setup_browser():
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    service = Service("/Users/papijorge/Downloads/chromedriver-mac-arm64/chromedriver")
    return webdriver.Chrome(service=service, options=options)

# Enforce visibility of elements
def force_visibility(driver, element_id):
    driver.execute_script(f"""
        var elem = document.getElementById("{element_id}");
        if (elem) {{
            elem.style.visibility = "visible";
            elem.style.opacity = "1";
            elem.style.display = "block";
        }}
    """)

# Join game as a guest
def join_game(driver, game_link):
    try:
        print(f"Navigating to: {game_link}")
        driver.get(game_link)

        # Switch to iframe containing the game
        iframe = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "maingameframe"))
        )
        print("Iframe found. Switching...")
        driver.switch_to.frame(iframe)

        # Click 'Play as Guest' buttons
        print("Looking for the first 'Play as Guest' button...")
        click_element(driver, "guestOrAccountContainer_guestButton")
        print("Looking for the second 'Play as Guest' button...")
        click_element(driver, "guestPlayButton")

        print("ObserverBot has successfully joined the game as a guest!")
    except Exception as e:
        print(f"Error joining the game: {e}")

# Click an element by ID
def click_element(driver, element_id):
    try:
        force_visibility(driver, element_id)
        element = WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.ID, element_id))
        )
        element.click()
        print(f"Clicked element with ID: {element_id}")
    except Exception as e:
        print(f"Error clicking element with ID: {element_id}: {e}")


# Extract game data
def extract_game_data(driver):
    try:
        force_visibility(driver, "ingamewinner")
        ingamewinner = driver.find_element(By.ID, "ingamewinner")

        winner_element = ingamewinner.find_element(By.ID, "ingamewinner_top")
        winner_text = winner_element.get_attribute("innerText").strip()

        players_element = ingamewinner.find_element(By.ID, "ingamewinner_scores_left")
        players = players_element.get_attribute("innerText").strip().splitlines()

        scores_element = ingamewinner.find_element(By.ID, "ingamewinner_scores_right")
        scores = scores_element.get_attribute("innerText").strip().splitlines()

        return players, scores, winner_text
    except Exception:
        
        return [], [], ""
    

def extract_valid_game_data(driver):
    """
    Continuously extracts game data and returns valid data for logging.
    """
    while True:
        players, scores, winner_text = extract_game_data(driver)
        if players and scores and winner_text:  # Ensure all required data is valid
            return players, scores, winner_text
        print("Invalid game data. Retrying data extraction...")
        time.sleep(1)

# Monitor game

def extract_game_mode(driver):
    """
    Extracts the game mode from the nested layout in the HTML.
    """
    try:
        # Navigate to the game mode text element
        force_visibility(driver, "newbonklobby_modetext")
        game_mode_element = driver.find_element(By.ID, "newbonklobby_modetext")
        game_mode = game_mode_element.get_attribute("innerText").strip()
        print("Extracted Game Mode:", game_mode)
        return game_mode
    except Exception as e:
        print(f"Error extracting game mode: {e}")
        return "Unknown"  # Default value if extraction fails

def monitor_game(driver):
    """
    Monitors the game state, tracks rounds, and writes data to a file for BonkBot to use.
    """
    match_store = {"matches": []}  # Centralized match store
    current_match = {"match_id": 1, "rounds": [], "final_winner": "", "final_scores": []}
    round_id = 1
    previous_state = None
    global monitoring_game

    match_logged = False  # Track if the match has been logged

    # Ensure the file exists
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, "w") as f:
            json.dump({"matches": []}, f)

    while True:
        if monitoring_game:
            players, scores, winner_text = extract_game_data(driver)
            game_state = get_game_state(driver)
            print("CURRENT GAME STATE:", game_state)
            game_mode = extract_game_mode(driver)

            if game_state != previous_state:
                match_logged = False  # Reset match logging for a new state

            if game_state == "WINS" and not match_logged:  # Process WINS state only once
                print("SOMEONE HAS WON THE GAME!!!!!!")
                if players and scores and winner_text:  # Ensure valid data
                    print("Valid data extracted for API:")
                    print("Players:", players)
                    print("Scores:", scores)
                    print("Winner:", winner_text)

                    success = log_match_to_api(players, scores, winner_text, game_mode)  # Log match to API
                    if success:
                        match_logged = True  # Mark the match as logged
                    else:
                        print("Match logging failed after retries.")

                    # Start a new match
                    current_match = {
                        "match_id": current_match["match_id"] + 1,
                        "rounds": [],
                        "final_winner": "",
                        "final_scores": [],
                    }
                    round_id = 1
                else:
                    print("Skipping WINS state processing due to invalid data.")

            elif game_state == "DRAW":
                round_data = {
                    "round_id": round_id,
                    "players": players,
                    "scores": scores,
                    "result": "DRAW",
                }
                log_round(current_match, match_store, round_data)
                round_id += 1

            elif game_state == "SCORES":
                if players and scores and winner_text:
                    round_data = {
                        "round_id": round_id,
                        "players": players,
                        "scores": scores,
                        "result": winner_text,
                    }
                    log_round(current_match, match_store, round_data)
                    round_id += 1
                else:
                    print("Waiting for valid SCORES data...")

            previous_state = game_state  # Update previous state

        time.sleep(1)



def log_match_to_api(players, scores, winner_text, game_mode, max_retries=3, retry_delay=2):
    api_url = "http://localhost:3000/api/v1/matches"

    # Clean player names by removing trailing colons
    cleaned_players = [player.rstrip(':') for player in players]

    match_data = {
        "match": {
            "game_mode": game_mode,  # You can dynamically set this
            "logged_at": time.strftime("%Y-%m-%dT%H:%M:%S"),  # Current time in ISO format
            "winner_bonk_username": winner_text,
            "final_scores": " - ".join(scores),  # Convert scores to a string
            "players": cleaned_players  # Use cleaned player names
        }
    }

    attempts = 0
    while attempts < max_retries:
        try:
            response = requests.post(api_url, json=match_data)
            if response.status_code == 201:
                print("Match logged successfully!")
                return True  # Exit after successful logging
            else:
                print(f"Failed to log match: {response.status_code} - {response.json()}")
        except Exception as e:
            print(f"Error logging match to API: {e}")
        
        # Retry logic
        attempts += 1
        if attempts < max_retries:
            print(f"Retrying... ({attempts}/{max_retries})")
            time.sleep(retry_delay)
        else:
            print("Max retries reached. Match logging failed.")
            return False

def log_round(current_match, match_store, round_data):
    """
    Logs a round to the current match and writes to the JSON file.
    """
    # Prevent duplicate rounds
    if current_match["rounds"] and current_match["rounds"][-1]["scores"] == round_data["scores"] and current_match["rounds"][-1]["result"] == round_data["result"]:
        print("Duplicate round detected. Skipping logging.")
        return

    current_match["rounds"].append(round_data)
    save_to_file(match_store)


def finalize_match(current_match, match_store):
    """
    Finalizes a match by adding it to the match store and saving it to the JSON file.
    """
    if current_match["rounds"]:
        match_store["matches"].append(current_match)
        save_to_file(match_store)
    else:
        print("No rounds played in the match. Skipping finalization.")


def save_to_file(match_store):
    """
    Writes the current match store to the JSON file.
    """
    with open(DATA_FILE, "w") as f:
        json.dump(match_store, f, indent=4)
    print("Match store saved to file.")



def log_to_file_and_notify(match_store, match, round_data, event_type):
    """
    Logs game data to a file and notifies BonkBot.
    """
    try:
        # Only append the match if it is not already in the store
        if match not in match_store["matches"]:
            match_store["matches"].append(match)

        # Write the updated match store to the file
        with open(DATA_FILE, "w") as f:
            json.dump(match_store, f, indent=4)

        # Notify BonkBot
        if event_type == "round_end" and round_data:
            notify_bonkbot({"event": event_type, "round_data": round_data})
            print(f"Round {round_data['round_id']} logged and notified.")
        elif event_type == "match_end":
            notify_bonkbot({"event": event_type, "match_data": match})
            print(f"Match {match['match_id']} logged and notified.")
    except Exception as e:
        print(f"Error logging or notifying: {e}")

def get_game_state(driver):
    """
    Reads ingamewinner_bottom to determine the game state: SCORES, WINS, or DRAW.
    """
    try:
        force_visibility(driver, "ingamewinner")
        bottom_element = driver.find_element(By.ID, "ingamewinner_bottom")
        bottom_text = bottom_element.get_attribute("innerText").strip()
        return bottom_text  # Will be "SCORES", "WINS", or "DRAW"
    except Exception:
        return ""



# Notify BonkBot with match results
def notify_bonkbot(results):
    try:
        print(f"Sending to BonkBot: {results}")
        client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        client.connect(('127.0.0.1', RESULT_SERVER_PORT))
        client.sendall(json.dumps(results).encode('utf-8'))
        print("Match results sent to BonkBot.")
        client.close()
    except Exception as e:
        print(f"Failed to send match results to BonkBot: {e}")


# HTTP Request Handler for commands
class ObserverBotHandler(http.server.BaseHTTPRequestHandler):
    def do_POST(self):
        global monitoring_game
        content_length = int(self.headers.get('Content-Length', 0))
        post_data = self.rfile.read(content_length).decode('utf-8')

        try:
            print(f"Raw POST data received: {post_data}")
            command = json.loads(post_data)
            print(f"Parsed command: {command}")

            if command.get("action") == "join_game":
                game_link = command.get("link")
                print(f"Joining game at link: {game_link}")
                driver.get(game_link)
                observer_join_game(driver)
            elif command.get("action") == "start_monitoring":
                monitoring_game = True
                print("Started monitoring the game.")
            elif command.get("action") == "stop_monitoring":
                monitoring_game = False
                print("Stopped monitoring the game.")

            # Respond with success
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"status": "success"}).encode('utf-8'))
        except json.JSONDecodeError as e:
            print(f"Invalid JSON received: {post_data}. Error: {e}")
            self.send_response(400)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(json.dumps({"status": "error", "message": str(e)}).encode('utf-8'))


def observer_join_game(driver):
    """
    Joins the game as an observer by interacting with the web page elements.
    """
    print("Navigating to game page...")
    try:
        # Switch to iframe
        iframe = WebDriverWait(driver, 20).until(
            EC.presence_of_element_located((By.ID, "maingameframe"))
        )
        print("Iframe found. Switching...")
        driver.switch_to.frame(iframe)

        # Click first 'Play as Guest' button
        print("Looking for the first 'Play as Guest' button...")
        click_element(driver, "guestOrAccountContainer_guestButton")

        # Click second 'Play as Guest' button
        print("Looking for the second 'Play as Guest' button...")
        click_element(driver, "guestPlayButton")

        print("ObserverBot has successfully joined the game as a guest!")
    except Exception as e:
        print(f"Failed to join the game: {e}")



# Start ObserverBot server
def observer_server():
    server_address = ('', OBSERVERBOT_PORT)
    httpd = http.server.HTTPServer(server_address, ObserverBotHandler)
    print(f"ObserverBot server listening on port {OBSERVERBOT_PORT}")
    httpd.serve_forever()


# Main function
if __name__ == "__main__":
    driver = setup_browser()
    threading.Thread(target=observer_server, daemon=True).start()
    monitor_game(driver)
