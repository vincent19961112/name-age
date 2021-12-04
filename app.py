from controllers.user_controller import UserController
from flask_cors import CORS
from flask import Flask
import sys
import os
curPath = os.path.abspath(os.path.dirname(__file__))
rootPath = os.path.split(curPath)[0]
sys.path.append(rootPath)


app = Flask(__name__)
CORS(app)


@app.route("/user", methods=['GET'])
def get_user():
    result = UserController.get_user()
    return result


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))
