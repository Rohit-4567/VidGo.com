import yt_dlp

def download_youtube(url):
    ydl_opts = {
        'outtmpl': 'downloads/youtube/%(title)s.%(ext)s',
        'format': 'best',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
