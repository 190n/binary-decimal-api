let binary, decimal;

function setup() {
    createCanvas(600, 600);

    // Ask the user for a binary number and store it in `binary`
    binary = prompt('Enter binary number');

    // Send a request to our Python script with the binary number and call `gotData` with the result
    loadJSON('/scripts/binary-decimal.py?binary=' + binary, gotData);
}

function gotData(data) {
    // Store the decimal result
    decimal = data.decimal;
}

function draw() {
    background(255);
    fill(0);
    textSize(24);
    text('What is ' + binary + ' in decimal?', 100, 100);

    // If we know the decimal number (if our request completed), draw it under the binary number
    if (decimal !== undefined) {
        text(decimal, 100, 150);
    }
}
