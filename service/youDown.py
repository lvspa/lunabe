import yt_dlp
from yt_dlp import YoutubeDL

def you_process(downType):
    if downType=='VIDEO':
        def down_video(url_in,info,*,incomplete):
            duration=info.get('duration')
            if duration and duration<5:
                return 'Video muito curto :('
            yt_opts={
                'match_filter':down_video(),
            }
            with yt_dlp.YoutubeDL(yt_opts) as ydl:
                final_product=ydl.download(url_in)
            return final_product

    
    elif downType=='AUDIO':
        def down_audio():
            url_in = [input('Cole o URL do seu AUDIO aqui: ')]
            yt_opts={
                'format':'m4a/bestaudio/best',
                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'wav',
                }]
            }
            with yt_dlp.YoutubeDL(yt_opts) as ydl:
                 midia = ydl.download(url_in)
            return midia;
    else:
        print('Tipo de arquivo desconhecido')

    return down_audio()
    return down_video()


products=you_process(input('Qual o tipo de arquivo? ').upper())
print(products)







