import yt_dlp

def download_instagram(url):
    ydl_opts = {
        'outtmpl': 'downloads/instagram/%(title)s.%(ext)s',
        'format': 'best',
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
