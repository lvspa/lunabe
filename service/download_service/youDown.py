import yt_dlp
from imageio.plugins.ffmpeg import download
from yt_dlp import YoutubeDL
import os
import area_76
from service.download_service.area_76 import clearUrl


# implementar contador de minutagem em função a parte

def you_process(downType):

    if downType=='VIDEO':
        url_link =input('Cole o URL do seu VIDEO aqui: ')

        def down_video():
            clean_link = clearUrl(url_link)

            yt_opts = {
                'format': 'best',
            }
            with yt_dlp.YoutubeDL(yt_opts) as ydl:
                os.chdir('/home/Alexandre/Vídeos/')

                final_product=ydl.download(clean_link)

            return final_product

        return down_video()


    elif downType=='AUDIO':
        def down_audio():

            url_link = input('Cole o URL do seu AUDIO aqui: ')

            clean_link = clearUrl(url_link)

            yt_opts={
                'format':'m4a/bestaudio/best',

                'postprocessors': [{
                    'key': 'FFmpegExtractAudio',
                    'preferredcodec': 'wav',
                }],
            }
            with yt_dlp.YoutubeDL(yt_opts) as ydl:

                 os.chdir('/home/Alexandre/Músicas/')

                 str_link=clean_link[0]

                 info=ydl.extract_info(str_link, download=False)

                 duration=(info.get('duration'))
                 mins=duration//60
                 secs_rest=duration%60

                 print(f'Sua midia tem {mins} minutos e {secs_rest} segundos.')

                 midia = ydl.download(clean_link)
            return midia;
    else:
        print('Tipo de arquivo desconhecido')

    return down_audio()




products=you_process(input('Qual o tipo de arquivo?[AUDIO OU VIDEO]: ').upper())








