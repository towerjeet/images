import logging
import os
from flask import Flask, request, send_from_directory

app = Flask(__name__)

# Configure logging
logging.basicConfig(filename='webhook.log', level=logging.INFO)

@app.route('/webhook', methods=['POST'])
def webhook():
    # Retrieve the payload from the request
    payload = request.json

    # Log the received payload
    logging.info('Received webhook payload: %s', payload)

    # Process the payload
    # Your code to handle the webhook payload goes here

    # Return a response (optional)
    return 'Webhook received successfully'

@app.route('/images/<path:image_name>')
def serve_image(image_name):
    # Serve the image from the 'uploaded_images' directory
    return send_from_directory('uploaded_images', image_name)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050)