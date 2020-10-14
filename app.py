from flask import Flask, request
import requests

app = Flask(__name__)


@app.errorhandler(404)
def not_found(error):
    try:
        r = requests.get(request.full_path[1:])
        if r.status_code == 200:
            return r.text
    except Exception as e:
        return 'failed'


if __name__ == '__main__':
    app.run()
