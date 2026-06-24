from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    # Yahan aap apne asal YouTube videos ke IDs 'id' mein daal sakte hain
    # Jaise aapki video ka link agar youtube.com/watch?v=XYZ ho, to ID 'XYZ' hogi
    videos = [
        {"title": "The Beauty of Islamic Character", "id": "dQw4w9WgXcQ", "category": "Bayan"},
        {"title": "Understanding the Essence of Deen", "id": "dQw4w9WgXcQ", "category": "Shorts"},
        {"title": "Daily Reminders for a Peaceful Life", "id": "dQw4w9WgXcQ", "category": "Reminders"}
    ]
    
    # Website par dikhane ke liye stats counters
    stats = [
        {"count": "100K+", "label": "Community Members"},
        {"count": "500+", "label": "Islamic Reminders"},
        {"count": "1M+", "label": "Total Views"}
    ]
    
    return render_template('index.html', videos=videos, stats=stats)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
