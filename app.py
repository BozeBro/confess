from flask import Flask, request
from post import makeManyIMG
app = Flask(__name__)

"""
JSON FORMAT
{
    "ids" : [...]
}
"""
@app.route("/get_image", methods=['POST'])
def get_image():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        json = request.json
        return list(makeManyIMG(json['ids']))
    else:
        return 'Content-Type not supported!'