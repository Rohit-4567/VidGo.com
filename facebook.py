import yt_dlp

def download_facebook(url):
    ydl_opts = {
        'outtmpl': 'downloads/facebook/%(title)s.%(ext)s',
        'format': 'best',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
