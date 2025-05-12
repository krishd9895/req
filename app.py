from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/fetch')
def fetch():
    url = request.args.get('url')
    if not url:
        return "Missing 'url' parameter", 400
    try:
        res = requests.get(url)
        return res.text, 200, {'Content-Type': 'text/html'}
    except Exception as e:
        return str(e), 500

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
