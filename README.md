# Image Steganography Web App

This is a web application for image steganography. Image Steganography is the process of hiding information which can be text, image or video inside a cover image. The secret information is hidden in a way that it not visible to the human eyes. This application in built using HTML, CSS, Bootstrap, JavaScript, Python and Flask.

## LSB Steganography

LSB Steganography is an image steganography technique in which messages are hidden inside an image by replacing each pixel’s least significant bit with the bits of the message to be hidden. We are also taking a key which will generate random sequence of pixles for hiding message. We will have to use the same key to extract the hidden message.

## How to run

- Python is required for running this application.
- install the other requirements using: 
	> pip install -r requirements.txt
- run the flask application using: 
	> python app.py 
- open a browser and go to http://127.0.0.1:5000
- Navigate to the "Embed" tab to embed secret text into an image.
- Navigate to the "Extract" tab to extract secret text from an image.
