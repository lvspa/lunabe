import yt_dlp
from yt_dlp import YoutubeDL
import os
import area_76
from service.download_service.area_76 import clearUrl


############################################
# possibilidade: oferecer dowload em listas #
#############################################

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
                 midia = ydl.download(clean_link)
            return midia;
    else:
        print('Tipo de arquivo desconhecido')

    return down_audio()




products=you_process(input('Qual o tipo de arquivo? ').upper())
print(products)







