import os
import tempfile
from flask import Flask, request, send_file, render_template, redirect, url_for
from flask_cors import CORS
import yt_dlp

app = Flask(__name__)
CORS(app)  # ✅ CORS enabled for all routes

# ----------- Platform Detector Function -----------
def detect_platform(url):
    if "youtube.com" in url or "youtu.be" in url:
        return "youtube"
    return "unsupported"

# ----------- Home Route ----------- 
@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']
        platform = detect_platform(url)

        if platform == 'youtube':
            return redirect(url_for('download_page', url=url))  # Correct redirect
        else:
            return "❌ Invalid URL or unsupported platform."
    return render_template('index.html')

# ----------- Show Download Options Page ----------- 
@app.route('/download', methods=['GET', 'POST'])
def download_page():
    if request.method == 'POST':
        video_url = request.form['video_url']
    else:
        video_url = request.args.get('url')
        
    print(f"Video URL: {video_url}")  # For debugging
    try:
        ydl_opts = {'format': 'best', 'quiet': True, 'nocheckcertificate': True}
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(video_url, download=False)
            title = info.get('title', 'Unknown Title')
            thumbnail = info.get('thumbnail', '')
            return render_template('download.html', title=title, thumbnail=thumbnail, video_url=video_url)
    except Exception as e:
        print(f"Error: {e}")  # Log the error
        return f"❌ Error fetching video info: {str(e)}"

# ----------- Download Video Route -----------
@app.route('/download_video', methods=['GET'])
def download_video():
    video_url = request.args.get('video_url')
    print(f"Download Video URL: {video_url}")
    try:
        temp_dir = tempfile.gettempdir()
        ydl_opts = {
            'outtmpl': os.path.join(temp_dir, '%(title)s.%(ext)s'),
            'format': 'best[ext=mp4]/best'
        }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(video_url, download=True)
            filename = ydl.prepare_filename(info)
        return send_file(filename, as_attachment=True, download_name=os.path.basename(filename))
    except Exception as e:
        print(f"Error: {e}")
        return f"❌ Error downloading video: {str(e)}"

# ----------- Run App -----------
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
