from rembg import remove
from PIL import Image
from io import BytesIO
from flask import Flask, request, jsonify, send_file

app = Flask(__name__)

@app.route('/remove_background', methods=['POST'])
def remove_background():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'})

    image_file = request.files['image']
    
    try:
        input_image = Image.open(image_file)
        output_image = remove(input_image)
        
        # Convert the output image to bytes
        output_bytes = BytesIO()
        output_image.save(output_bytes, format='PNG')
        output_bytes.seek(0)

        # Return the processed image as a response
        return send_file(output_bytes, mimetype='image/png')
    
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run()
