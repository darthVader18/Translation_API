from flask import Flask, request
from app import translate

app = Flask(__name__)

@app.route("/translate", methods=['POST', 'GET'])
def translation():
    if request.method == 'POST':
        lang_from = request.args.get('from')
        lang_to = request.args.get('to')
        text = request.args.get('text')
        return str(translate(lang_from, lang_to, text))

@app.route("/")
def home():
    return "For Translate go to /translate."

if __name__ == "__main__":
    app.run(debug = True, port = 8000)