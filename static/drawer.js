const drawCanvas = document.getElementById('drawer-canvas');
const submitCanvas = document.getElementById('submit-canvas');
const drawerCanvasContext = drawCanvas.getContext('2d');
const submitCanvasContext = submitCanvas.getContext('2d');
const stringContentField = document.getElementById("string-content");
const toStringButton = document.getElementById("to-string-button");
const defaultInteger = -1;
const pixelsOffset = 10;
const stringPixelsDelimeter = "/";
const pixelsDelimeter = ",";
const submitRadius = 5;

let isDrawing = false;
let pixelX = 0;
let pixelY = 0;
let previousX = defaultInteger;
let previousY = defaultInteger;
let pictureList = [];

class PixelModel {
    constructor(x, y) {
        this.x = x;
        this.y = y;
    }

    toModel() {
        return {
            "x": this.x,
            "y": this.y
        };
    }
}

class PixelListModel {
    constructor(pixels) {
        this.pixels = pixels;
    }

    toModel() {
        let models = [];
        this.pixels.forEach(pixel => {
            models.push(pixel.toModel());
        });

        return {
            "pixels": models
        };
    }
}

drawCanvas.addEventListener('mousedown', (e) => {
    isDrawing = true;
    [pixelX, pixelY] = [e.offsetX, e.offsetY];
});

drawCanvas.addEventListener('mousemove', (e) => {
    if (isDrawing) {
        const newX = e.offsetX;
        const newY = e.offsetY;
        if (previousX === defaultInteger) previousX = newX;
        if (previousY === defaultInteger) previousY = newY;
        drawLine(pixelX, pixelY, newX, newY, drawerCanvasContext);
        if (isValidToAdd(previousX, previousY, newX, newY, pixelsOffset)) {
            previousX = newX;
            previousY = newY;
            //pictureList.push([newX, newY]);
            //drawPoint(newX, newY, submitCanvasContext, submitRadius);
        }
        [pixelX, pixelY] = [newX, newY];
    }
});

drawCanvas.addEventListener('mouseup', () => {
    isDrawing = false;
});

toStringButton.addEventListener("click", async () => {
    console.log(pictureList);
    const str = pixels2DListToString(pictureList, pixelsDelimeter, stringPixelsDelimeter);
    console.log(str);
    console.log(pixels2DListToModel(pictureList));
    try {
        const response = await fetch('http://127.0.0.1:5000/signature', {
            method: 'POST',
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({"signature": str, "login": "empty", "email": "empty"})
        });

        const result = await response.json();
        if (response.ok) {
            alert(result.message);
        } else {
            alert(result.message);
        }
    } catch (error) {
        console.error('Error:', error);
        alert('An error occurred while submitting the form.');
    }
});

function isValidToAdd(previousX, previousY, x, y, offset) {
    return Math.pow(x - previousX, 2) + Math.pow(y - previousY, 2) >= offset * offset;
}

function pixels2DListToString(pixels, delimeter, betweenDelimeter) {
    const length = pixels.length;
    let string = "";

    for (let i = 0; i < length; i++) {
        const pixel = pixels[i];
        string = string.concat(pixel[0]).concat(delimeter).concat(pixel[1]);
        if (i < length-1) {
            string = string.concat(betweenDelimeter);
        }
    }

    return string;
}

function pixels2DListToModel(pixels) {
    const length = pixels.length;
    let pixelsList = [];

    for (let i = 0; i < length; i++) {
        const pixel = pixels[i];
        const pixelModel = new PixelModel(pixel[0], pixel[1]);
        pixelsList.push(pixelModel);
    }

    let pixelsListModel = new PixelListModel(pixelsList);

    return pixelsListModel.toModel();
}

function drawLine(fromX, fromY, toX, toY, canvasContext) {
    canvasContext.beginPath();
    canvasContext.moveTo(fromX, fromY);
    canvasContext.lineTo(toX, toY);
    canvasContext.stroke();
}

function drawPoint(x, y, canvasContext, radius) {
    canvasContext.beginPath();
    canvasContext.arc(x, y, radius, 0, 2 * Math.PI, false);
    canvasContext.fillStyle = 'green';
    canvasContext.fill();
    canvasContext.stroke();
}
