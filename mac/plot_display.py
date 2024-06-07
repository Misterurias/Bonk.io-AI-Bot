import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV file
file_path = '/Users/papijorge/bonkio_ai_bot/game_data.csv'  # Replace with your file path
data = pd.read_csv(file_path)

# Filter data for frames 99 to 297
filtered_data = data[(data['frame'] >= 297) & (data['frame'] <= 409)]

# Separate player and arrow data
player_data = filtered_data[filtered_data['object_type'] == 'player']
arrow_data = filtered_data[filtered_data['object_type'] == 'arrow']

# Plot the movements
plt.figure(figsize=(12, 8))

# Plot player movements
plt.scatter(player_data['object_x'], player_data['object_y'], c='green', label='Player', alpha=0.6, edgecolors='w', s=100)

# Plot arrow movements
plt.scatter(arrow_data['object_x'], arrow_data['object_y'], c='red', label='Arrow', alpha=0.6, edgecolors='w', s=100)

# Add titles and labels
plt.title('Player and Arrow Movements from Frame 297 to 409')
plt.xlabel('X Position')
plt.ylabel('Y Position')
plt.legend()

# Show plot
plt.gca().invert_yaxis()  # Invert y-axis to match the coordinate system used in images
plt.grid(True)
plt.show()
