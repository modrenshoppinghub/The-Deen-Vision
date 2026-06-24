from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    videos = [
        {"title": "Bayan 1: Haqooq-ul-Ibad", "id": "VIDEO_ID_1"},
        {"title": "Bayan 2: Seerat-un-Nabi", "id": "VIDEO_ID_2"},
        {"title": "Bayan 3: Ramzan ki Fazeelat", "id": "VIDEO_ID_3"}
    ]
    return render_template('index.html', videos=videos)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
