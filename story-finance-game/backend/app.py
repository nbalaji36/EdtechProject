from flask import Flask, jsonify, send_from_directory
from pathlib import Path
from story_data import game_data

app = Flask(__name__, static_folder="../frontend", static_url_path="")

@app.route("/api/story")
def get_story():
    return jsonify(game_data)

@app.route("/")
def index():
    frontend_path = Path(app.static_folder)
    return send_from_directory(frontend_path, "index.html")

@app.route("/<path:path>")
def static_proxy(path):
    frontend_path = Path(app.static_folder)
    file_path = frontend_path / path

    if file_path.exists():
        return send_from_directory(frontend_path, path)

    return send_from_directory(frontend_path, "index.html")


if __name__ == "__main__":
    app.run(debug=True, port=5000)
