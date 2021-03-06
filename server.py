from flask import Flask
from flask import request
from flask.json import jsonify
from sort_strings import sort_strings
app = Flask(__name__)

@app.route("/sort", methods=['POST'])
def sorter():
  strings = request.get_json()['strings']
  res = {"sorted_strings": sort_strings(strings)}
  return jsonify(res)

if __name__ == "__main__":
    app.run()