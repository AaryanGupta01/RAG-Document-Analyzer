import os
from flask import Flask, jsonify, send_from_directory

# Serve static files (index.html) from the repo root
app = Flask(__name__, static_folder='.')


@app.route('/api/config', methods=['GET'])
def get_config():
    return jsonify({
        "chatflowId": os.getenv("FLOWISE_CHATFLOW_ID"),
        "apiHost": os.getenv("FLOWISE_API_HOST")
    })


@app.route('/', methods=['GET'])
def index():
    return send_from_directory('.', 'index.html')


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)