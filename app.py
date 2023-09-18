from flask import Flask,request
import transformer
import os
# import json

# with open('min.json', 'r',encoding="utf8") as f:
#     data = json.load(f)

app = Flask(__name__)

@app.route("/translate")
def convert():
    data = request.args.get('s')
    return transformer.translate_json(data)

if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)