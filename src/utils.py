def get_platform_from_url(url):
    if 'instagram.com' in url:
        return 'instagram'
    elif 'youtube.com' in url or 'youtu.be' in url:
        return 'youtube'
    elif 'facebook.com' in url:
        return 'facebook'
    else:
        return None
