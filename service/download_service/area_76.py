def clearUrl(link):

    if 'https://www.youtube.com' in link:
        clean_link = link[0:43]

    elif 'https://youtu.be' in link:
        clean_link = link[0:48]

    return [clean_link]




















#print(link[0:46])
