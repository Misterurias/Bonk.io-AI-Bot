// const BonkBot = require("bonkbot");
// const { decodeFromDatabase } = require('./decoder');
// const OpenAI = require("openai");
// const readline = require('readline');
// const fs = require('fs');
// const { spawn } = require('child_process');
// require('dotenv').config();

// const openai = new OpenAI({
//     apiKey: process.env.OPEN_AI_API_KEY
// });

// const rl = readline.createInterface({
//     input: process.stdin,
//     output: process.stdout
// });

// rl.question('How many bots do you want to create? ', (numBots) => {
//     if (isNaN(numBots) || numBots <= 0) {
//         console.error("Invalid number of bots.");
//         process.exit(1);
//     }

//     let botLinks = [];

//     function askForLink(index) {
//         if (index < numBots) {
//             rl.question(`Please enter the game link for bot ${index + 1}: `, (gameLink) => {
//                 if (!gameLink) {
//                     console.error("No game link provided.");
//                     process.exit(1);
//                 }
//                 botLinks.push(gameLink);
//                 askForLink(index + 1);
//             });
//         } else {
//             rl.close();
//             for (let i = 0; i < numBots; i++) {
//                 createAndStartBot(`BonkBot${i + 1}`, "Teamj#1234", botLinks[i]);
//             }
//         }
//     }

//     askForLink(0);
// });

// function get_map_data(decodedMapData) {
//     fs.writeFileSync('map_data.json', JSON.stringify(decodedMapData, null, 2));
//     console.log("Map data saved to map_data.json");
// }

// function get_player_data(playerData) {
//     fs.writeFileSync('player_data.json', JSON.stringify(playerData, null, 2));
//     console.log("Player data saved to player_data.json");
// }

// function update_player_data(player, action, packet) {
//     let playerData = [];
//     try {
//         const data = fs.readFileSync('player_data.json', 'utf8');
//         playerData = JSON.parse(data);
//     } catch (err) {
//         console.error(err);
//         playerData = new Array(50).fill(null); // Initialize with 50 null values if file read fails
//     }

//     if (packet != "None") {
//         playerData[player] = null;
//     } else if (action === "join") {
//         const index = playerData.findIndex(p => p === null);
//         if (index !== -1) {
//             playerData[index] = player;
//         } else {
//             playerData.push(player);
//         }
//     } else if (action === "leave") {
//         const index = playerData.findIndex(p => p && p.id === player.id);
//         if (index !== -1) {
//             playerData[index] = null;
//         }
//     }

//     fs.writeFileSync('player_data.json', JSON.stringify(playerData, null, 2));
//     console.log("Player data updated in player_data.json");
// }

// function filterMessage(message, botNumber) {
//     return new Promise((resolve, reject) => {
//         const pythonProcess = spawn('python', ['ping_filter.py', message, botNumber]);

//         pythonProcess.stdout.on('data', (data) => {
//             resolve(data.toString().trim());
//         });

//         pythonProcess.stderr.on('data', (data) => {
//             reject(data.toString());
//         });
//     });
// }

// function createAndStartBot(username, password, gameLink) {
//     let bot = BonkBot.createBot({
//         account: {
//             username: username,
//             password: password,
//             guest: true,
//         },
//         // skin: "{skin_object_here}"
//     });

//     let botId = null; // Variable to store the bot's ID

//     bot.events.on("ready", async () => {
//         console.log(`${username} is ready`);

//         let fromurl = await bot.getAddressFromLink(gameLink);
//         bot.setAddress(fromurl);
//         bot.connect();
//     });

//     bot.events.on("connect", () => {
//         const playerCount = 0;
//         console.log(`${username} connected to room!`);
//         bot.chat(`Hello everyone! I am ${username}! If you want to ask me questions, use ping @${username.toLowerCase()} in your question :D`);
//         botId = bot.id; // Store the bot's ID

//         bot.events.on("packet", async (packet) => {
//             bot.autoHandlePacket(packet);
//             // ignore spammy packets
//             if (packet.type == "timesync" || packet.type == "ping") return;

//             if (packet.type == "mapswap") {
//                 let encodedMapData = packet.data;  // Encoded map data string
//                 let decodedMapData = decodeFromDatabase(encodedMapData);
                
//                 // Send the map data to a separate file
//                 get_map_data(decodedMapData);

//                 console.log("Decoded Map Data:", decodedMapData);
//             }

//             if (packet.type == "roomjoin") {
//                 get_player_data(packet.playerdata);
//             }

//             if (packet.type == "hostleave") {
//                 update_player_data(packet.oldid, "join", "Host Left");
//             }


//             console.log(packet)
//         });

//         bot.events.on("banned", async () => {
//             console.log(`${username} was banned from the room!`);
//         });

//         bot.events.on("disconnected", async () => {
//             console.log(`${username} disconnected from the room!`);
//         });

//         bot.events.on("chatmessage", async (playerchatevent) => {
//             let pce = playerchatevent;
//             console.log(`${pce.username}: ${pce.message}`);

//             // Ignore messages from the bot itself

//             let messageContent = "None";
//             // Respond to messages directed at the bot
//             const botNumber = username.slice(-1);
//             try {

//                 if (pce.username === username) {
//                     messageContent = "None"
//                 } 
                
//                 else {
//                     messageContent = await filterMessage(pce.message, botNumber);
//                 };

//                 if (messageContent != "None") {
//                     const response = await openai.chat.completions.create({
//                         model: "gpt-3.5-turbo",
//                         messages: [{ role: "user", content: messageContent }],
//                         max_tokens: 150, // Limit the response length to manage token usage
//                     });
//                     const reply = response.choices[0].message.content.trim();
//                     bot.chat(`@${pce.username} ${reply}`);
//                 }
//             } catch (error) {
//                 console.error('Error generating response:', error);
//                 bot.chat("Sorry, I couldn't process that request.");
//             }
//         });

//         bot.events.on("join", async (playerjoinevent) => {
//             let joiningPlayer = {
//                 id: playerjoinevent.id,
//                 username: playerjoinevent.username,
//                 peerID: playerjoinevent.peerid,
//                 level: playerjoinevent.level,
//                 guest: playerjoinevent.guest,
//                 tabbed: playerjoinevent.tabbed,
//                 skin: playerjoinevent.skin,
//                 ready: false,
//                 here: true,
//             };
//             console.log(`${joiningPlayer.username} joined the room!`);
//             bot.chat(`Welcome @${joiningPlayer.username}!`);

//             // Update the player data
//             update_player_data(joiningPlayer, "join", "None");
//         });

//         bot.events.on("leave", async (playerleaveevent) => {
//             let leavingPlayer = bot.getPlayerByID(playerleaveevent.id);

//             console.log(`${leavingPlayer.username} left the room!`);
//             bot.chat(`Cya @${leavingPlayer.username}!`);

//             // Update the player data
//             update_player_data(leavingPlayer, "leave", "None");
//         });
//     });

//     bot.init();
// }

// examplebot.js
// const BonkBot = require('./bonkbot.js');

// const { decodeFromDatabase } = require('./decoder');
// const OpenAI = require("openai");
// const readline = require('readline');
// const fs = require('fs');
// const { spawn } = require('child_process');
// const { classifyQuestion } = require('./classifier'); // Import the classifier module
// const { type } = require("os");
// require('dotenv').config();

// let host = 0;

// const openai = new OpenAI({
//     apiKey: process.env.OPEN_AI_API_KEY
// });

// const rl = readline.createInterface({
//     input: process.stdin,
//     output: process.stdout
// });

// rl.question('How many bots do you want to create? ', (numBots) => {
//     if (isNaN(numBots) || numBots <= 0) {
//         console.error("Invalid number of bots.");
//         process.exit(1);
//     }

//     let botLinks = [];

//     function askForLink(index) {
//         if (index < numBots) {
//             rl.question(`Please enter the game link for bot ${index + 1}: `, (gameLink) => {
//                 if (!gameLink) {
//                     console.error("No game link provided.");
//                     process.exit(1);
//                 }
//                 botLinks.push(gameLink);
//                 askForLink(index + 1);
//             });
//         } else {
//             rl.close();
//             for (let i = 0; i < numBots; i++) {
//                 createAndStartBot(`BonkBot${i + 1}`, "Teamj#1234", botLinks[i]);
//             }
//         }
//     }

//     askForLink(0);
// });

// function get_map_data(decodedMapData) {
//     fs.writeFileSync('map_data.json', JSON.stringify(decodedMapData, null, 2));
//     console.log("Map data saved to map_data.json");
// }

// function get_player_data(playerData) {
//     fs.writeFileSync('player_data.json', JSON.stringify(playerData, null, 2));
//     console.log("Player data saved to player_data.json");
// }

// function update_player_data(player, action, packet) {
//     let playerData = [];
//     try {
//         const data = fs.readFileSync('player_data.json', 'utf8');
//         playerData = JSON.parse(data);
//     } catch (err) {
//         console.error(err);
//         playerData = new Array(50).fill(null); // Initialize with 50 null values if file read fails
//     }

//     if (packet != "None") {
//         playerData[player] = null;
//     } else if (action === "join") {
//         const index = playerData.findIndex(p => p === null);
//         if (index !== -1) {
//             playerData[index] = player;
//         } else {
//             playerData.push(player);
//         }
//     } else if (action === "leave") {
//         const index = playerData.findIndex(p => p && p.id === player.id);
//         if (index !== -1) {
//             playerData[index] = null;
//         }
//     }

//     // Update the host information
//     if (action === "host") {
//         playerData.forEach(p => {
//             if (p) p.isHost = false;
//         });
//         const hostIndex = playerData.findIndex(p => p && p.id === player.id);
//         if (hostIndex !== -1) {
//             playerData[hostIndex].isHost = true;
//         }
//     }

//     fs.writeFileSync('player_data.json', JSON.stringify(playerData, null, 2));
//     console.log("Player data updated in player_data.json");
// }

// function filterMessage(message, botNumber) {
//     return new Promise((resolve, reject) => {
//         const pythonProcess = spawn('python', ['ping_filter.py', message, botNumber]);

//         pythonProcess.stdout.on('data', (data) => {
//             resolve(data.toString().trim());
//         });

//         pythonProcess.stderr.on('data', (data) => {
//             reject(data.toString());
//         });
//     });
// }

// function createAndStartBot(username, password, gameLink) {
//     let bot = BonkBot.createBot({
//         account: {
//             username: username,
//             password: password,
//             guest: true,
//         },
//         // skin: "{skin_object_here}"
//     });

//     let botId = null; // Variable to store the bot's ID

//     bot.events.on("ready", async () => {
//         console.log(`${username} is ready`);

//         let fromurl = await bot.getAddressFromLink(gameLink);
//         bot.setAddress(fromurl);
//         bot.connect();
//     });

//     bot.events.on("connect", () => {
//         const playerCount = 0;
//         console.log(`${username} connected to room!`);
//         bot.chat(`Hello everyone! I am ${username}! If you want to ask me questions, use ping @${username.toLowerCase()} in your question :D`);
//         botId = bot.id; // Store the bot's ID

//         bot.events.on("packet", async (packet) => {
//             bot.autoHandlePacket(packet);
//             // ignore spammy packets
//             if (packet.type == "timesync" || packet.type == "ping") return;

//             if (packet.type == "mapswap") {
//                 let encodedMapData = packet.data;  // Encoded map data string
//                 let decodedMapData = decodeFromDatabase(encodedMapData);
                
//                 // Send the map data to a separate file
//                 get_map_data(decodedMapData);

//                 console.log("Decoded Map Data:", decodedMapData);
//             }

//             if (packet.type == "roomjoin") {
//                 host = packet.hostid;
//                 get_player_data(packet.playerdata);
//             }

//             if (packet.type == "hostleave") {
//                 host = packet.newid;
//                 update_player_data(packet.oldid, "join", "Host Left");
//             }

//             if (packet.type == "hosttransfer") {
//                 host = packet.newHost;
//             }

//             if (packet.type == "gamestart") {
//                 console.log("The game has started")
//             }


//             console.log(packet)
//         });

//         bot.events.on("banned", async () => {
//             console.log(`${username} was banned from the room!`);
//         });

//         bot.events.on("disconnected", async () => {
//             console.log(`${username} disconnected from the room!`);
//         });

//         bot.events.on("chatmessage", async (playerchatevent) => {
//             let pce = playerchatevent;
//             console.log(`${pce.username}: ${pce.message}`);
        
//             // Ignore messages from the bot itself
//             if (pce.username === username) return;
        
//             // Check if the bot is pinged
//             if (!pce.message.toLowerCase().includes(`@${username.toLowerCase()}`)) return;
        
//             const botNumber = username.slice(-1);
        
//             try {
//                 const playerData = JSON.parse(fs.readFileSync('player_data.json', 'utf8'));
//                 const mapData = JSON.parse(fs.readFileSync('map_data.json', 'utf8'));
        
//                 // Determine the type of question
//                 const questionType = classifyQuestion(pce.message.replace(`@${username.toLowerCase()}`, '').trim());
//                 console.log("QUESTION TYPE:", questionType);
        
//                 let responseMessage = null;
        
//                 switch (questionType) {
//                     case 'current_map':
//                         responseMessage = mapData.mapName ? `The current map is: ${mapData.mapName}` : "Map information isn't available.";
//                         break;
//                     case 'host':
//                         if (typeof host === 'string') {
//                             const hostName = playerData[host].username;
//                             responseMessage = `The host is: ${hostName}`;
//                         }
//                         else {
//                             responseMessage = "No host found.";
//                         }
//                         break;
//                     case 'player_count':
//                         const playerCount = playerData.filter(p => p !== null).length;
//                         responseMessage = `There are ${playerCount} players in the game.`;
//                         break;
//                     case 'game_mode':
//                         responseMessage = mapData.gameMode ? `The current game mode is: ${mapData.gameMode}` : "Game mode information isn't available.";
//                         break;
//                     case 'player_level':
//                         const playerName = pce.message.split("level")[1].trim();

//                         const player = playerData.find(p => p && p.username.toLowerCase() === playerName.toLowerCase());
//                         responseMessage = player ? `${playerName} is at level: ${player.level}` : `Player ${playerName} not found.`;
//                         break;
//                     default:
//                         const messageContent = await filterMessage(pce.message, botNumber);
//                         if (messageContent != "None") {
//                             const response = await openai.chat.completions.create({
//                                 model: "gpt-3.5-turbo",
//                                 messages: [{ role: "user", content: messageContent }],
//                                 max_tokens: 150, // Limit the response length to manage token usage
//                             });
//                             responseMessage = response.choices[0].message.content.trim();
//                         } else {
//                             responseMessage = "I'm not sure how to answer that.";
//                         }
//                         break;
//                 }
        
//                 if (responseMessage) {
//                     bot.chat(`@${pce.username} ${responseMessage}`);
//                 }
        
//             } catch (error) {
//                 console.error('Error generating response:', error);
//                 bot.chat("Sorry, I couldn't process that request.");
//             }
//         });
        
        
//         bot.events.on("join", async (playerjoinevent) => {
//             let joiningPlayer = {
//                 id: playerjoinevent.id,
//                 username: playerjoinevent.username,
//                 peerID: playerjoinevent.peerid,
//                 level: playerjoinevent.level,
//                 guest: playerjoinevent.guest,
//                 tabbed: playerjoinevent.tabbed,
//                 skin: playerjoinevent.skin,
//                 ready: false,
//                 here: true,
//             };
//             console.log(`${joiningPlayer.username} joined the room!`);
//             bot.chat(`Welcome @${joiningPlayer.username}!`);

//             // Update the player data
//             update_player_data(joiningPlayer, "join", "None");
//         });

//         bot.events.on("leave", async (playerleaveevent) => {
//             let leavingPlayer = bot.getPlayerByID(playerleaveevent.id);

//             console.log(`${leavingPlayer.username} left the room!`);
//             bot.chat(`Cya @${leavingPlayer.username}!`);

//             // Update the player data
//             update_player_data(leavingPlayer, "leave", "None");
//         });
//     });

//     bot.init();
// }

const express = require("express"); // Use express for simplicity
const BonkBot = require('./bonkbot.js');
const { decodeFromDatabase } = require('./decoder');
const http = require('http');
const net = require('net');
const fs = require('fs');
require('dotenv').config();

const app = express(); // Create an express app
app.use(express.json()); // Middleware to parse JSON request bodies

const OBSERVERBOT_PORT = 8080; // Port to communicate with ObserverBot
const RESULT_SERVER_PORT = 8081; // Port to receive results from ObserverBot
const SERVER_PORT = 3001; // HTTP server port for handling requests
let botInstance = null; // To hold the bot instance for result server communication

/**
 * API Endpoint to join a game
 */
app.post("/join_game", (req, res) => {
    const { link } = req.body;

    if (!link) {
        return res.status(400).json({ status: "error", message: "Game link is required" });
    }

    console.log(`BonkBot invited to join game at link: ${link}`);

    // Start a new BonkBot instance for the game
    botInstance = createAndStartBot("BonkBot1", "Teamj#1234", link);

    // Notify ObserverBot to join the game
    notifyObserverBot({ action: "join_game", link });

    res.json({ status: "success", message: "BonkBot invited and joined the game!" });
});

/**
 * Notify ObserverBot with a message.
 * @param {Object} message - The message to send to ObserverBot.
 */
function notifyObserverBot(message) {
    const postData = JSON.stringify(message);

    const options = {
        hostname: "127.0.0.1",
        port: OBSERVERBOT_PORT,
        path: "/",
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "Content-Length": Buffer.byteLength(postData),
        },
    };

    const req = http.request(options, (res) => {
        console.log(`ObserverBot STATUS: ${res.statusCode}`);
        res.setEncoding("utf8");
        res.on("data", (chunk) => {
            console.log(`ObserverBot RESPONSE: ${chunk}`);
        });
    });

    req.on("error", (e) => {
        console.error(`ObserverBot Request Error: ${e.message}`);
    });

    req.write(postData);
    req.end();
}

/**
 * Create and start a BonkBot instance.
 * @param {string} username - The username for the bot.
 * @param {string} password - The password for the bot.
 * @param {string} gameLink - The game link to join.
 */
function createAndStartBot(username, password, gameLink) {
    let bot = BonkBot.createBot({
        account: {
            username: username,
            password: password,
            guest: true,
        },
    });

    bot.events.on("ready", async () => {
        console.log(`${username} is ready`);

        let fromurl = await bot.getAddressFromLink(gameLink);
        bot.setAddress(fromurl);
        bot.connect();
    });

    bot.events.on("connect", () => {
        console.log(`${username} connected to room!`);
        bot.chat(`Hello! I am ${username}, here to assist!`);

        // Start result server for receiving match logs
        startResultServer(bot);

        // Notify ObserverBot to start monitoring when the game starts
        bot.events.on("packet", async (packet) => {
            bot.autoHandlePacket(packet);

            if (packet.type === "mapswap") {
                let decodedMapData = decodeFromDatabase(packet.data);
                fs.writeFileSync("map_data.json", JSON.stringify(decodedMapData, null, 2));
                console.log("Map data saved to map_data.json");
            }

            if (packet.type === "gamestart") {
                console.log("The game has started");
                bot.chat("The game has started");
                notifyObserverBot({ action: "start_monitoring" });
            }

            if (packet.type === "gamecancel") {
                console.log("The host canceled the game");
                bot.chat("The host canceled the game");
                notifyObserverBot({ action: "stop_monitoring" });
            }
        });

        bot.events.on("chatmessage", (playerchatevent) => {
            console.log(`${playerchatevent.username}: ${playerchatevent.message}`);
        });
    });

    bot.events.on("disconnect", () => {
        console.log(`${username} disconnected from the room!`);
    });

    bot.init();

    return bot; // Return the bot instance
}

/**
 * Start a result server to receive match results from ObserverBot.
 * @param {Object} bot - The bot instance to broadcast messages.
 */
function startResultServer(bot) {
    const resultServer = net.createServer((socket) => {
        socket.on("data", (data) => {
            try {
                const message = JSON.parse(data.toString());
                console.log("Game state received from ObserverBot:", message);

                if (message.event === "round_end") {
                    const { round_id, players, scores, result } = message.round_data;
                    if (result === "DRAW") {
                        bot.chat(`Round ${round_id || ""} ended in a DRAW.`);
                    } else {
                        bot.chat(`Round ${round_id} ended. Winner: ${result}. Scores: ${players.join(", ")} - ${scores.join(", ")}`);
                    }
                } else if (message.event === "match_end") {
                    const { final_winner, final_scores } = message.match_data;
                    bot.chat(`Match ended! Winner: ${final_winner}. Final Scores: ${final_scores.join(" - ")}`);
                }
            } catch (error) {
                console.error("Error processing game state from ObserverBot:", error.message);
            }
        });

        socket.on("error", (err) => {
            console.error("Error on result server:", err.message);
        });
    });

    resultServer.listen(RESULT_SERVER_PORT, "127.0.0.1", () => {
        console.log(`Result server listening for ObserverBot on port ${RESULT_SERVER_PORT}`);
    });
}

// Start the HTTP server
app.listen(SERVER_PORT, () => {
    console.log(`BonkBot HTTP server running on port ${SERVER_PORT}`);
});