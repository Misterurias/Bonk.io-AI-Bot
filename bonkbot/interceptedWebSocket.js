const WebSocket = require('ws');

class InterceptedWebSocket extends WebSocket {
    constructor(address, protocols) {
        super(address, protocols);

        // Only intercept specific WebSocket URLs
        if (address.includes("socket.io/?EIO=3&transport=websocket&sid=")) {
            this.addEventListener('open', () => {
                console.log('WebSocket open:', address);
            });

            this.addEventListener('message', (event) => {
                const message = event.data;
                console.log('WebSocket message received:', message);
                if (message.startsWith('42[48,{"state"') || message.startsWith('42[21,{"map"')) {
                    processWebSocketMessage(message);
                }
            });

            const originalSend = this.send;
            this.send = function(data) {
                console.log('WebSocket send:', data);
                if (typeof data === 'string' && data.includes("socket.io/?EIO=3&transport=websocket&sid=")) {
                    processWebSocketMessage(data);
                }
                return originalSend.apply(this, arguments);
            };
        }
    }
}

// function processWebSocketMessage(message) {
//     console.log('Processing WebSocket message:', message);
//     // Add logic to handle the specific map data messages
//     if (message.startsWith('42[48,{"state"')) {
//         console.log('State message found:', message);
//         // You can add logic here to handle the state message
//     } else if (message.startsWith('42[21,{"map"')) {
//         console.log('Map message found:', message);
//         // You can add logic here to handle the map message
//     }
// }

function processWebSocketMessage(message) {
    console.log('Processing WebSocket message:', message);
    if (message.startsWith('42[48,{"state"')) {
        console.log('State message found:', message);
        // You can add logic here to handle the state message
    } else if (message.startsWith('42[21,{"map"')) {
        console.log('Map message found:', message);
        // Extract and save map data
        const mapData = JSON.parse(message.slice(2)); // Assuming JSON structure starts after "42"
        get_map_data(mapData);
    }
}

function get_map_data(mapData) {
    fs.writeFileSync('map_data.json', JSON.stringify(mapData, null, 2));
    console.log("Map data saved to map_data.json");
}

module.exports = InterceptedWebSocket;
