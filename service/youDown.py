import yt_dlp
from yt_dlp import YoutubeDL
import os

def you_process(downType):

    if downType=='VIDEO':
        url_in = [input('Cole o URL do seu VIDEO aqui: ')]

        def down_video():
            yt_opts = {
                'format': 'best',
            }
            with yt_dlp.YoutubeDL(yt_opts) as ydl:
                os.chdir('/home/Alexandre/Vídeos/')
                final_product=ydl.download(url_in)
            return final_product

        return down_video()

    elif downType=='AUDIO':
        def down_audio():
            url_in = [input('Cole o URL do seu AUDIO aqui: ')]
            yt_opts={
                'format':'m4a/bestaudio/best',

                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'wav',
                }],
            }
            with yt_dlp.YoutubeDL(yt_opts) as ydl:
                 os.chdir('/home/Alexandre/Músicas/')
                 midia = ydl.download(url_in)
            return midia;
    else:
        print('Tipo de arquivo desconhecido')

    return down_audio()



products=you_process(input('Qual o tipo de arquivo? ').upper())
print(products)







