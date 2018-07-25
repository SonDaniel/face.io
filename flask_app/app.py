from flask import Flask, render_template, request, jsonify, send_file 
import requests
import io
app = Flask(__name__)
 
@app.route('/')
def render_static():
    return render_template('index.html')

@app.route('/download_image/', methods=['GET'])
def download_image():
    image_url = request.args.get('image_url')
    image_data = requests.get(image_url).content
    return send_file(
                     io.BytesIO(image_data),
                     attachment_filename='yoda.jpeg',
                     mimetype='image/jpg'
    ) 


@app.route('/image_endpoint', methods=['POST'])
def image_endpoint():
    return jsonify({"yoda_binary": request.get_data()})

if __name__ == '__main__':
    app.run(debug=True, port=5000)