from flask import Flask, render_template, request, jsonify 
app = Flask(__name__)
 
@app.route('/')
def render_static():
    return render_template('index.html')

@app.route('/image_endpoint', methods=['POST'])
def image_endpoint():
    return jsonify({"name": request.get_data()})

if __name__ == '__main__':
    app.run(debug=True, port=5000)