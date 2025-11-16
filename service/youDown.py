import yt_dlp
from yt_dlp import YoutubeDL

def you_config():
    ydl_opts = {
        "quiet": True,
        "skip_download": True,
        "format": "bestvideo+bestaudio"
    }

    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info("https://youtube.com/watch?v=xxxx", download=False)
        print(info["url"])


def you_process(downType):
    if downType=='VIDEO':
        def down_video():
            


    if downType=='AUDIO':
        def down_audio():
            url_in=[input("Cole o URL: ")]
            yt_opts={
                'format':'m4a/bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'wav',
                }]
            }

            with yt_dlp.YoutubeDL(yt_opts) as ydl:
                error_code = ydl.download(url_in)












