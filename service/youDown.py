from yt_dlp import YoutubeDL

def youConfig():
    ydl_opts = {
        "quiet": True,
        "skip_download": True,
        "format": "bestvideo+bestaudio"
    }

    with YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info("https://youtube.com/watch?v=xxxx", download=False)
        print(info["url"])


def youProcess(downType):
    if downType=="VIDEO":
        def downvideo():

    if downType=="AUDIO":
        def downaudio():



