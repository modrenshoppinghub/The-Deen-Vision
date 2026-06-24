from flask import Flask, render_template
import requests
import os

app = Flask(__name__)

# Official Active Credentials
API_KEY = "AIzaSyB3K2pOe7pb8U6aiTmv-4LhehLG4_vbFCE"
CHANNEL_ID = "UCignGBS20R65blQr7axPAVg"

def get_automated_feed():
    try:
        # YouTube API Call for Latest Videos
        url = f"https://www.googleapis.com/youtube/v3/search?key={API_KEY}&channelId={CHANNEL_ID}&part=snippet,id&order=date&maxResults=12&type=video"
        response = requests.get(url).json()
        
        dynamic_videos = []
        for item in response.get("items", []):
            video_title = item["snippet"]["title"]
            video_id = item["id"]["videoId"]
            
            # Smart Tagging System based on titles
            if "short" in video_title.lower() or "status" in video_title.lower():
                cat = "Shorts"
            elif "bayan" in video_title.lower() or "lecture" in video_title.lower():
                cat = "Bayan"
            else:
                cat = "Reminders"
                
            dynamic_videos.append({
                "title": video_title, 
                "id": video_id, 
                "category": cat
            })
            
        if not dynamic_videos:
            return [{"title": "The Deen Vision Official Core Media", "id": "dQw4w9WgXcQ", "category": "Featured"}]
        return dynamic_videos
    except Exception:
        return [{"title": "The Deen Vision Official Core Media", "id": "dQw4w9WgXcQ", "category": "Featured"}]

@app.route('/')
def home():
    videos = get_automated_feed()
    
    # Premium Analytical Dashboard Stats
    stats = [
        {"count": "100K+", "label": "Active Audience", "icon": "fa-users"},
        {"count": "500+", "label": "Media Releases", "icon": "fa-video"},
        {"count": "1M+", "label": "Digital Footprint", "icon": "fa-chart-line"},
        {"count": "24/7", "label": "Global Stream", "icon": "fa-globe"}
    ]
    
    # Advanced FAQ Component Data
    faqs = [
        {"q": "What is the primary vision of this platform?", "a": "To present authentic Islamic knowledge through high-quality visual production and modern digital media standards."},
        {"q": "How often does the media stream update?", "a": "The system is fully automated. As soon as a video goes live on YouTube, it reflects here inside the ecosystem instantly."},
        {"q": "Can I share these videos directly?", "a": "Yes, all embedded streams feature native controls allowing immediate sharing across external communication channels."}
    ]
    
    return render_template('index.html', videos=videos, stats=stats, faqs=faqs)

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
