let colorValue = 125275;

// Convert to hexadecimal
let hexColor = colorValue.toString(16).padStart(6, '0');
console.log(`Hex color: #${hexColor}`);  // Should output "2CFE29"

// Convert hexadecimal to RGB
function colorGrabber(hex) {
    if (hex.length === 3) {
        hex = hex.replace(/./g, '$&$&');
    }
    return [
        parseInt(hex.slice(0, 2), 16), 
        parseInt(hex.slice(2, 4), 16), 
        parseInt(hex.slice(4, 6), 16)
    ];
}

let rgbColor = HEX2RGB(hexColor);
console.log(`RGB color: rgb(${rgbColor[0]}, ${rgbColor[1]}, ${rgbColor[2]})`);  // Should output [44, 254, 41]
