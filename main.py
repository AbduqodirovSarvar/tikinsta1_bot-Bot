def instag(link):
    
    import requests

    url = "https://instagram-downloader-download-instagram-videos-stories.p.rapidapi.com/index"

    querystring = {"url": link}

    headers = {
        "X-RapidAPI-Key": "e862f6eac5msh6227fdf6678b8dcp1b7cf7jsnef217d785d61",
        "X-RapidAPI-Host": "instagram-downloader-download-instagram-videos-stories.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    import json
    rest=json.loads(response.text)
    print("INSTAGR = ",rest)
    return rest
    

def tiktok(link):      
    import requests

    url = "https://tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com/vid/index"

    querystring = {"url": link}

    headers = {
            "X-RapidAPI-Key": "e862f6eac5msh6227fdf6678b8dcp1b7cf7jsnef217d785d61",
            "X-RapidAPI-Host": "tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    import json
    rest = json.loads(response.text)
    print("TIKTOK = ", rest)
    return rest
  

def youtube(link):
      
    link=link[17:]
    import requests

    url = "https://youtube-media-downloader.p.rapidapi.com/v2/video/details"

    querystring = {"videoId":link}

    headers = {
        "X-RapidAPI-Key": "e862f6eac5msh6227fdf6678b8dcp1b7cf7jsnef217d785d61",
        "X-RapidAPI-Host": "youtube-media-downloader.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)
    
    import json
    rest = json.loads(response.text)
    # print(len(rest['videos']['items']))
    json1 = rest['videos']['items']
    # for k in json1:
    #     if k['hasAudio']:
    #         print(k)
            
    return json1

    
    
youtube('https://youtu.be/0cq59Huyx_w')
    

# tiktok('https://www.instagram.com/p/CWarspYsb6-/')
# print("###############################################################################################################################")
# print("###############################################################################################################################")
# tiktok('https://vt.tiktok.com/ZSdvP6P9N/?k=1')



a = [
  {
    'url': 'https://redirector.googlevideo.com/videoplayback?expire=1655759212&ei=DI2wYqzvE4WUhwaRkoHADw&ip=18.208.214.162&id=o-ANjhikHXo9ALHwCepBIF00MPvt8_mYt4FLr0e6972l-e&itag=18&source=youtube&requiressl=yes&mh=fj&mm=31%2C29&mn=sn-p5qddn7d%2Csn-p5qlsn7l&ms=au%2Crdu&mv=m&mvi=1&pl=18&initcwndbps=603750&spc=4ocVC5IE7Zn65gw46xx6HHpJ8RuDiOqaIB8e6DZ7tkKb&vprv=1&mime=video%2Fmp4&ns=2Imu4XagMPciSvhz4GvBWn8G&gir=yes&clen=9934996&ratebypass=yes&dur=172.570&lmt=1649561623578954&mt=1655737257&fvip=3&fexp=24001373%2C24007246&c=WEB&txp=4538434&n=NsC449tOphFplA&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Cmime%2Cns%2Cgir%2Cclen%2Cratebypass%2Cdur%2Clmt&sig=AOq0QJ8wRQIgUvBYMjbDl8VcxWBJ_EA2YIwgd72mY6z8TIoIJK-cWZoCIQDXpZNzLDC0D4-eM5C5IvUC96wKMnuqiSFeduoS00BisQ%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRAIgFM2HyRROMYXKMJ2yGJ7UYrp04jQflRtokGIql-W_sCwCIDuu4nN-JFCTGONgzseKD5YuT0WDfmXpgwd8h8TBWBLo&range=0-',
    'lengthMs': 172570,
    'mimeType': 'video/mp4; codecs="avc1.42001E, mp4a.40.2"',
    'extension': 'mp4',
    'lastModified': 1649561623578954,
    'size': 9934996,
    'sizeText': '9.5MB',
    'hasAudio': True,
    'quality': '360p',
    'width': 640,
    'height': 360
  },
  {
    'url': 'https://redirector.googlevideo.com/videoplayback?expire=1655759212&ei=DI2wYqzvE4WUhwaRkoHADw&ip=18.208.214.162&id=o-ANjhikHXo9ALHwCepBIF00MPvt8_mYt4FLr0e6972l-e&itag=22&source=youtube&requiressl=yes&mh=fj&mm=31%2C29&mn=sn-p5qddn7d%2Csn-p5qlsn7l&ms=au%2Crdu&mv=m&mvi=1&pl=18&initcwndbps=603750&spc=4ocVC5IE7Zn65gw46xx6HHpJ8RuDiOqaIB8e6DZ7tkKb&vprv=1&mime=video%2Fmp4&ns=2Imu4XagMPciSvhz4GvBWn8G&cnr=14&ratebypass=yes&dur=172.570&lmt=1649564968851467&mt=1655737257&fvip=3&fexp=24001373%2C24007246&c=WEB&txp=4532434&n=NsC449tOphFplA&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Cmime%2Cns%2Ccnr%2Cratebypass%2Cdur%2Clmt&sig=AOq0QJ8wRAIgQWXBKZuQW6FigM9rb1ofKpJ7aqhgj-ChUNMkl6rZ8PMCIHBfo1ftAWns5OJd1OjIIZ2pTMO1Vlg-7n_tXm3DaR6e&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRAIgFM2HyRROMYXKMJ2yGJ7UYrp04jQflRtokGIql-W_sCwCIDuu4nN-JFCTGONgzseKD5YuT0WDfmXpgwd8h8TBWBLo&range=0-',
    'lengthMs': 172570,
    'mimeType': 'video/mp4; codecs="avc1.64001F, mp4a.40.2"',
    'extension': 'mp4',
    'lastModified': 1649564968851467,
    'size': 10786712,
    'sizeText': '10.3MB',
    'hasAudio': True,
    'quality': '720p',
    'width': 1280,
    'height': 720
  },
  {
    'url': 'https://redirector.googlevideo.com/videoplayback?expire=1655759212&ei=DI2wYqzvE4WUhwaRkoHADw&ip=18.208.214.162&id=o-ANjhikHXo9ALHwCepBIF00MPvt8_mYt4FLr0e6972l-e&itag=137&aitags=133%2C134%2C135%2C136%2C137%2C160%2C242%2C243%2C244%2C247%2C248%2C278%2C394%2C395%2C396%2C397%2C398%2C399&source=youtube&requiressl=yes&mh=fj&mm=31%2C29&mn=sn-p5qddn7d%2Csn-p5qlsn7l&ms=au%2Crdu&mv=m&mvi=1&pl=18&initcwndbps=603750&spc=4ocVC5IE7Zn65gw46xx6HHpJ8RuDiOqaIB8e6DZ7tkKb&vprv=1&mime=video%2Fmp4&ns=YIhMiSWLMG7l-H1wTDVp-TUG&gir=yes&clen=31969065&dur=172.520&lmt=1649564640711807&mt=1655737257&fvip=3&keepalive=yes&fexp=24001373%2C24007246&c=WEB&txp=4535434&n=dsKIgUVTPCNlmw&sparams=expire%2Cei%2Cip%2Cid%2Caitags%2Csource%2Crequiressl%2Cspc%2Cvprv%2Cmime%2Cns%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRgIhAMxhCKDrg1DS4LG3xdku2f1Q_veDCP80tbM7062NfsvyAiEA6xwJ42hdy5n4b_-dcWh4xCaNEnXguCj7raUd0YjvqfQ%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRAIgFM2HyRROMYXKMJ2yGJ7UYrp04jQflRtokGIql-W_sCwCIDuu4nN-JFCTGONgzseKD5YuT0WDfmXpgwd8h8TBWBLo&range=0-',
    'lengthMs': 172520,
    'mimeType': 'video/mp4; codecs="avc1.640028"',
    'extension': 'mp4',
    'lastModified': 1649564640711807,
    'size': 31969065,
    'sizeText': '30.5MB',
    'hasAudio': False,
    'quality': '1080p',
    'width': 1920,
    'height': 1080
  },
  {
    'url': 'https://redirector.googlevideo.com/videoplayback?expire=1655759212&ei=DI2wYqzvE4WUhwaRkoHADw&ip=18.208.214.162&id=o-ANjhikHXo9ALHwCepBIF00MPvt8_mYt4FLr0e6972l-e&itag=248&aitags=133%2C134%2C135%2C136%2C137%2C160%2C242%2C243%2C244%2C247%2C248%2C278%2C394%2C395%2C396%2C397%2C398%2C399&source=youtube&requiressl=yes&mh=fj&mm=31%2C29&mn=sn-p5qddn7d%2Csn-p5qlsn7l&ms=au%2Crdu&mv=m&mvi=1&pl=18&initcwndbps=603750&spc=4ocVC5IE7Zn65gw46xx6HHpJ8RuDiOqaIB8e6DZ7tkKb&vprv=1&mime=video%2Fwebm&ns=YIhMiSWLMG7l-H1wTDVp-TUG&gir=yes&clen=20658048&dur=172.520&lmt=1649570433300996&mt=1655737257&fvip=3&keepalive=yes&fexp=24001373%2C24007246&c=WEB&txp=4535434&n=dsKIgUVTPCNlmw&sparams=expire%2Cei%2Cip%2Cid%2Caitags%2Csource%2Crequiressl%2Cspc%2Cvprv%2Cmime%2Cns%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRQIgT13lhiuPKjCkWqPJjyzBlzQQRi1jCGicfuZTsB-8xPcCIQDWmJAe9dJZ7cl9bvFgKeLXxlBceu8Pv3s_vAuT9f77lQ%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRAIgFM2HyRROMYXKMJ2yGJ7UYrp04jQflRtokGIql-W_sCwCIDuu4nN-JFCTGONgzseKD5YuT0WDfmXpgwd8h8TBWBLo&range=0-',
    'lengthMs': 172520,
    'mimeType': 'video/webm; codecs="vp9"',
    'extension': 'webm',
    'lastModified': 1649570433300996,
    'size': 20658048,
    'sizeText': '19.7MB',
    'hasAudio': False,
    'quality': '1080p',
    'width': 1920,
    'height': 1080
  },
  {
    'url': 'https://redirector.googlevideo.com/videoplayback?expire=1655759212&ei=DI2wYqzvE4WUhwaRkoHADw&ip=18.208.214.162&id=o-ANjhikHXo9ALHwCepBIF00MPvt8_mYt4FLr0e6972l-e&itag=399&aitags=133%2C134%2C135%2C136%2C137%2C160%2C242%2C243%2C244%2C247%2C248%2C278%2C394%2C395%2C396%2C397%2C398%2C399&source=youtube&requiressl=yes&mh=fj&mm=31%2C29&mn=sn-p5qddn7d%2Csn-p5qlsn7l&ms=au%2Crdu&mv=m&mvi=1&pl=18&initcwndbps=603750&spc=4ocVC5IE7Zn65gw46xx6HHpJ8RuDiOqaIB8e6DZ7tkKb&vprv=1&mime=video%2Fmp4&ns=YIhMiSWLMG7l-H1wTDVp-TUG&gir=yes&clen=17328373&dur=172.520&lmt=1649563707350833&mt=1655737257&fvip=3&keepalive=yes&fexp=24001373%2C24007246&c=WEB&txp=4532434&n=dsKIgUVTPCNlmw&sparams=expire%2Cei%2Cip%2Cid%2Caitags%2Csource%2Crequiressl%2Cspc%2Cvprv%2Cmime%2Cns%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRQIgWOlEgWXzypyI2ZIWhwS8VdmCzl5QBBUMwm5RS9TRDzkCIQCbb-7urUNHsN8vdAyuauyIhe2kaOhOxI3CQyO-k385UA%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRAIgFM2HyRROMYXKMJ2yGJ7UYrp04jQflRtokGIql-W_sCwCIDuu4nN-JFCTGONgzseKD5YuT0WDfmXpgwd8h8TBWBLo&range=0-',
    'lengthMs': 172520,
    'mimeType': 'video/mp4; codecs="av01.0.08M.08"',
    'extension': 'mp4',
    'lastModified': 1649563707350833,
    'size': 17328373,
    'sizeText': '16.5MB',
    'hasAudio': False,
    'quality': '1080p',
    'width': 1920,
    'height': 1080
  },
  {
    'url': 'https://redirector.googlevideo.com/videoplayback?expire=1655759212&ei=DI2wYqzvE4WUhwaRkoHADw&ip=18.208.214.162&id=o-ANjhikHXo9ALHwCepBIF00MPvt8_mYt4FLr0e6972l-e&itag=136&aitags=133%2C134%2C135%2C136%2C137%2C160%2C242%2C243%2C244%2C247%2C248%2C278%2C394%2C395%2C396%2C397%2C398%2C399&source=youtube&requiressl=yes&mh=fj&mm=31%2C29&mn=sn-p5qddn7d%2Csn-p5qlsn7l&ms=au%2Crdu&mv=m&mvi=1&pl=18&initcwndbps=603750&spc=4ocVC5IE7Zn65gw46xx6HHpJ8RuDiOqaIB8e6DZ7tkKb&vprv=1&mime=video%2Fmp4&ns=YIhMiSWLMG7l-H1wTDVp-TUG&gir=yes&clen=8003576&dur=172.520&lmt=1649564957849461&mt=1655737257&fvip=3&keepalive=yes&fexp=24001373%2C24007246&c=WEB&txp=4535434&n=dsKIgUVTPCNlmw&sparams=expire%2Cei%2Cip%2Cid%2Caitags%2Csource%2Crequiressl%2Cspc%2Cvprv%2Cmime%2Cns%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRgIhAInZqRhyLm4DRi4W2h2z-nrkHIzYBo6O9A5JKJPgRpMoAiEAwRPPETadDCBklHCxQTQc6wDwb-542jdk5udi2KVUA4s%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRAIgFM2HyRROMYXKMJ2yGJ7UYrp04jQflRtokGIql-W_sCwCIDuu4nN-JFCTGONgzseKD5YuT0WDfmXpgwd8h8TBWBLo&range=0-',
    'lengthMs': 172520,
    'mimeType': 'video/mp4; codecs="avc1.4d401f"',
    'extension': 'mp4',
    'lastModified': 1649564957849461,
    'size': 8003576,
    'sizeText': '7.6MB',
    'hasAudio': False,
    'quality': '720p',
    'width': 1280,
    'height': 720
  },
  {
    'url': 'https://redirector.googlevideo.com/videoplayback?expire=1655759212&ei=DI2wYqzvE4WUhwaRkoHADw&ip=18.208.214.162&id=o-ANjhikHXo9ALHwCepBIF00MPvt8_mYt4FLr0e6972l-e&itag=247&aitags=133%2C134%2C135%2C136%2C137%2C160%2C242%2C243%2C244%2C247%2C248%2C278%2C394%2C395%2C396%2C397%2C398%2C399&source=youtube&requiressl=yes&mh=fj&mm=31%2C29&mn=sn-p5qddn7d%2Csn-p5qlsn7l&ms=au%2Crdu&mv=m&mvi=1&pl=18&initcwndbps=603750&spc=4ocVC5IE7Zn65gw46xx6HHpJ8RuDiOqaIB8e6DZ7tkKb&vprv=1&mime=video%2Fwebm&ns=YIhMiSWLMG7l-H1wTDVp-TUG&gir=yes&clen=7120818&dur=172.520&lmt=1649571807955389&mt=1655737257&fvip=3&keepalive=yes&fexp=24001373%2C24007246&c=WEB&txp=4535434&n=dsKIgUVTPCNlmw&sparams=expire%2Cei%2Cip%2Cid%2Caitags%2Csource%2Crequiressl%2Cspc%2Cvprv%2Cmime%2Cns%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRQIgS8Ij4F_RaFUtl3IAZnsvwz3_aWxFZRXbmKD1B997HAMCIQC433TN9vUnBv_6wqsKgk0YkoIbEDVpohh93Q9N1CgZAA%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRAIgFM2HyRROMYXKMJ2yGJ7UYrp04jQflRtokGIql-W_sCwCIDuu4nN-JFCTGONgzseKD5YuT0WDfmXpgwd8h8TBWBLo&range=0-',
    'lengthMs': 172520,
    'mimeType': 'video/webm; codecs="vp9"',
    'extension': 'webm',
    'lastModified': 1649571807955389,
    'size': 7120818,
    'sizeText': '6.8MB',
    'hasAudio': False,
    'quality': '720p',
    'width': 1280,
    'height': 720
  },
  {
    'url': 'https://redirector.googlevideo.com/videoplayback?expire=1655759212&ei=DI2wYqzvE4WUhwaRkoHADw&ip=18.208.214.162&id=o-ANjhikHXo9ALHwCepBIF00MPvt8_mYt4FLr0e6972l-e&itag=398&aitags=133%2C134%2C135%2C136%2C137%2C160%2C242%2C243%2C244%2C247%2C248%2C278%2C394%2C395%2C396%2C397%2C398%2C399&source=youtube&requiressl=yes&mh=fj&mm=31%2C29&mn=sn-p5qddn7d%2Csn-p5qlsn7l&ms=au%2Crdu&mv=m&mvi=1&pl=18&initcwndbps=603750&spc=4ocVC5IE7Zn65gw46xx6HHpJ8RuDiOqaIB8e6DZ7tkKb&vprv=1&mime=video%2Fmp4&ns=YIhMiSWLMG7l-H1wTDVp-TUG&gir=yes&clen=9525533&dur=172.520&lmt=1649562111133758&mt=1655737257&fvip=3&keepalive=yes&fexp=24001373%2C24007246&c=WEB&txp=4532434&n=dsKIgUVTPCNlmw&sparams=expire%2Cei%2Cip%2Cid%2Caitags%2Csource%2Crequiressl%2Cspc%2Cvprv%2Cmime%2Cns%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRAIgep9sRX9wpRFPXO8DugcW0ySiAy4DM34Kh8i_q1B7vZwCIHrF9d0c1gPe-VTP-AKufv730pv6iF3kHGKgFXmzAQZ_&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRAIgFM2HyRROMYXKMJ2yGJ7UYrp04jQflRtokGIql-W_sCwCIDuu4nN-JFCTGONgzseKD5YuT0WDfmXpgwd8h8TBWBLo&range=0-',
    'lengthMs': 172520,
    'mimeType': 'video/mp4; codecs="av01.0.05M.08"',
    'extension': 'mp4',
    'lastModified': 1649562111133758,
    'size': 9525533,
    'sizeText': '9.1MB',
    'hasAudio': False,
    'quality': '720p',
    'width': 1280,
    'height': 720
  },
  {
    'url': 'https://redirector.googlevideo.com/videoplayback?expire=1655759212&ei=DI2wYqzvE4WUhwaRkoHADw&ip=18.208.214.162&id=o-ANjhikHXo9ALHwCepBIF00MPvt8_mYt4FLr0e6972l-e&itag=135&aitags=133%2C134%2C135%2C136%2C137%2C160%2C242%2C243%2C244%2C247%2C248%2C278%2C394%2C395%2C396%2C397%2C398%2C399&source=youtube&requiressl=yes&mh=fj&mm=31%2C29&mn=sn-p5qddn7d%2Csn-p5qlsn7l&ms=au%2Crdu&mv=m&mvi=1&pl=18&initcwndbps=603750&spc=4ocVC5IE7Zn65gw46xx6HHpJ8RuDiOqaIB8e6DZ7tkKb&vprv=1&mime=video%2Fmp4&ns=YIhMiSWLMG7l-H1wTDVp-TUG&gir=yes&clen=4129665&dur=172.520&lmt=1649564938315358&mt=1655737257&fvip=3&keepalive=yes&fexp=24001373%2C24007246&c=WEB&txp=4535434&n=dsKIgUVTPCNlmw&sparams=expire%2Cei%2Cip%2Cid%2Caitags%2Csource%2Crequiressl%2Cspc%2Cvprv%2Cmime%2Cns%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRQIhAIv8Am6VFC6aPnBgaQu0NS1abfy5wXihhl8CtL1X-Ie4AiB40y_Q9FztfWLVfO7rxFxTL-gn4Ci55kecBaoeQdkRDg%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRAIgFM2HyRROMYXKMJ2yGJ7UYrp04jQflRtokGIql-W_sCwCIDuu4nN-JFCTGONgzseKD5YuT0WDfmXpgwd8h8TBWBLo&range=0-',
    'lengthMs': 172520,
    'mimeType': 'video/mp4; codecs="avc1.4d401e"',
    'extension': 'mp4',
    'lastModified': 1649564938315358,
    'size': 4129665,
    'sizeText': '3.9MB',
    'hasAudio': False,
    'quality': '480p',
    'width': 854,
    'height': 480
  },
  {
    'url': 'https://redirector.googlevideo.com/videoplayback?expire=1655759212&ei=DI2wYqzvE4WUhwaRkoHADw&ip=18.208.214.162&id=o-ANjhikHXo9ALHwCepBIF00MPvt8_mYt4FLr0e6972l-e&itag=244&aitags=133%2C134%2C135%2C136%2C137%2C160%2C242%2C243%2C244%2C247%2C248%2C278%2C394%2C395%2C396%2C397%2C398%2C399&source=youtube&requiressl=yes&mh=fj&mm=31%2C29&mn=sn-p5qddn7d%2Csn-p5qlsn7l&ms=au%2Crdu&mv=m&mvi=1&pl=18&initcwndbps=603750&spc=4ocVC5IE7Zn65gw46xx6HHpJ8RuDiOqaIB8e6DZ7tkKb&vprv=1&mime=video%2Fwebm&ns=YIhMiSWLMG7l-H1wTDVp-TUG&gir=yes&clen=4122804&dur=172.520&lmt=1649571828185387&mt=1655737257&fvip=3&keepalive=yes&fexp=24001373%2C24007246&c=WEB&txp=4535434&n=dsKIgUVTPCNlmw&sparams=expire%2Cei%2Cip%2Cid%2Caitags%2Csource%2Crequiressl%2Cspc%2Cvprv%2Cmime%2Cns%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRQIgI8nD186P0-cW-DsKX7BEVt_hq-w_-wQmTwuMjr1lgsYCIQDajglTSbckJaX9_RwV2wN8EjjuL2fxWA7iLWibcgmP1w%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRAIgFM2HyRROMYXKMJ2yGJ7UYrp04jQflRtokGIql-W_sCwCIDuu4nN-JFCTGONgzseKD5YuT0WDfmXpgwd8h8TBWBLo&range=0-',
    'lengthMs': 172520,
    'mimeType': 'video/webm; codecs="vp9"',
    'extension': 'webm',
    'lastModified': 1649571828185387,
    'size': 4122804,
    'sizeText': '3.9MB',
    'hasAudio': False,
    'quality': '480p',
    'width': 854,
    'height': 480
  },
  {
    'url': 'https://redirector.googlevideo.com/videoplayback?expire=1655759212&ei=DI2wYqzvE4WUhwaRkoHADw&ip=18.208.214.162&id=o-ANjhikHXo9ALHwCepBIF00MPvt8_mYt4FLr0e6972l-e&itag=397&aitags=133%2C134%2C135%2C136%2C137%2C160%2C242%2C243%2C244%2C247%2C248%2C278%2C394%2C395%2C396%2C397%2C398%2C399&source=youtube&requiressl=yes&mh=fj&mm=31%2C29&mn=sn-p5qddn7d%2Csn-p5qlsn7l&ms=au%2Crdu&mv=m&mvi=1&pl=18&initcwndbps=603750&spc=4ocVC5IE7Zn65gw46xx6HHpJ8RuDiOqaIB8e6DZ7tkKb&vprv=1&mime=video%2Fmp4&ns=YIhMiSWLMG7l-H1wTDVp-TUG&gir=yes&clen=4722643&dur=172.520&lmt=1649563092612298&mt=1655737257&fvip=3&keepalive=yes&fexp=24001373%2C24007246&c=WEB&txp=4532434&n=dsKIgUVTPCNlmw&sparams=expire%2Cei%2Cip%2Cid%2Caitags%2Csource%2Crequiressl%2Cspc%2Cvprv%2Cmime%2Cns%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRgIhAJ5w8v0RBYtAELdtDKoS_6XNQWr4z07cyPQ-TuSnDxWcAiEAp2yoKVUMtTNLhDlZcn8YmmrpGiOdzWc2k7W125SKpuc%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRAIgFM2HyRROMYXKMJ2yGJ7UYrp04jQflRtokGIql-W_sCwCIDuu4nN-JFCTGONgzseKD5YuT0WDfmXpgwd8h8TBWBLo&range=0-',
    'lengthMs': 172520,
    'mimeType': 'video/mp4; codecs="av01.0.04M.08"',
    'extension': 'mp4',
    'lastModified': 1649563092612298,
    'size': 4722643,
    'sizeText': '4.5MB',
    'hasAudio': False,
    'quality': '480p',
    'width': 854,
    'height': 480
  },
  {
    'url': 'https://redirector.googlevideo.com/videoplayback?expire=1655759212&ei=DI2wYqzvE4WUhwaRkoHADw&ip=18.208.214.162&id=o-ANjhikHXo9ALHwCepBIF00MPvt8_mYt4FLr0e6972l-e&itag=134&aitags=133%2C134%2C135%2C136%2C137%2C160%2C242%2C243%2C244%2C247%2C248%2C278%2C394%2C395%2C396%2C397%2C398%2C399&source=youtube&requiressl=yes&mh=fj&mm=31%2C29&mn=sn-p5qddn7d%2Csn-p5qlsn7l&ms=au%2Crdu&mv=m&mvi=1&pl=18&initcwndbps=603750&spc=4ocVC5IE7Zn65gw46xx6HHpJ8RuDiOqaIB8e6DZ7tkKb&vprv=1&mime=video%2Fmp4&ns=YIhMiSWLMG7l-H1wTDVp-TUG&gir=yes&clen=2627098&dur=172.520&lmt=1649564935740108&mt=1655737257&fvip=3&keepalive=yes&fexp=24001373%2C24007246&c=WEB&txp=4535434&n=dsKIgUVTPCNlmw&sparams=expire%2Cei%2Cip%2Cid%2Caitags%2Csource%2Crequiressl%2Cspc%2Cvprv%2Cmime%2Cns%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRQIhAOTeEiewUnrzVnxMGbqtkT_XdFoSg2qQmg_KXTrNX-hXAiAE1dJGFKh2ad9UuWCzNJtRHVkeKSS7iHb7gdEnDBRICg%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRAIgFM2HyRROMYXKMJ2yGJ7UYrp04jQflRtokGIql-W_sCwCIDuu4nN-JFCTGONgzseKD5YuT0WDfmXpgwd8h8TBWBLo&range=0-',
    'lengthMs': 172520,
    'mimeType': 'video/mp4; codecs="avc1.4d401e"',
    'extension': 'mp4',
    'lastModified': 1649564935740108,
    'size': 2627098,
    'sizeText': '2.5MB',
    'hasAudio': False,
    'quality': '360p',
    'width': 640,
    'height': 360
  },
  {
    'url': 'https://redirector.googlevideo.com/videoplayback?expire=1655759212&ei=DI2wYqzvE4WUhwaRkoHADw&ip=18.208.214.162&id=o-ANjhikHXo9ALHwCepBIF00MPvt8_mYt4FLr0e6972l-e&itag=243&aitags=133%2C134%2C135%2C136%2C137%2C160%2C242%2C243%2C244%2C247%2C248%2C278%2C394%2C395%2C396%2C397%2C398%2C399&source=youtube&requiressl=yes&mh=fj&mm=31%2C29&mn=sn-p5qddn7d%2Csn-p5qlsn7l&ms=au%2Crdu&mv=m&mvi=1&pl=18&initcwndbps=603750&spc=4ocVC5IE7Zn65gw46xx6HHpJ8RuDiOqaIB8e6DZ7tkKb&vprv=1&mime=video%2Fwebm&ns=YIhMiSWLMG7l-H1wTDVp-TUG&gir=yes&clen=2667772&dur=172.520&lmt=1649571804459553&mt=1655737257&fvip=3&keepalive=yes&fexp=24001373%2C24007246&c=WEB&txp=4535434&n=dsKIgUVTPCNlmw&sparams=expire%2Cei%2Cip%2Cid%2Caitags%2Csource%2Crequiressl%2Cspc%2Cvprv%2Cmime%2Cns%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRAIgfIwMNJ1GyfP7zVVxdJEgF-nMqB2sU69nBiIk510W3I4CIDODX0X8It2u6JT715ZICrDVpM6sYmFePNZ2OOnrp_Wo&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRAIgFM2HyRROMYXKMJ2yGJ7UYrp04jQflRtokGIql-W_sCwCIDuu4nN-JFCTGONgzseKD5YuT0WDfmXpgwd8h8TBWBLo&range=0-',
    'lengthMs': 172520,
    'mimeType': 'video/webm; codecs="vp9"',
    'extension': 'webm',
    'lastModified': 1649571804459553,
    'size': 2667772,
    'sizeText': '2.5MB',
    'hasAudio': False,
    'quality': '360p',
    'width': 640,
    'height': 360
  },
  {
    'url': 'https://redirector.googlevideo.com/videoplayback?expire=1655759212&ei=DI2wYqzvE4WUhwaRkoHADw&ip=18.208.214.162&id=o-ANjhikHXo9ALHwCepBIF00MPvt8_mYt4FLr0e6972l-e&itag=396&aitags=133%2C134%2C135%2C136%2C137%2C160%2C242%2C243%2C244%2C247%2C248%2C278%2C394%2C395%2C396%2C397%2C398%2C399&source=youtube&requiressl=yes&mh=fj&mm=31%2C29&mn=sn-p5qddn7d%2Csn-p5qlsn7l&ms=au%2Crdu&mv=m&mvi=1&pl=18&initcwndbps=603750&spc=4ocVC5IE7Zn65gw46xx6HHpJ8RuDiOqaIB8e6DZ7tkKb&vprv=1&mime=video%2Fmp4&ns=YIhMiSWLMG7l-H1wTDVp-TUG&gir=yes&clen=2616703&dur=172.520&lmt=1649562678789217&mt=1655737257&fvip=3&keepalive=yes&fexp=24001373%2C24007246&c=WEB&txp=4532434&n=dsKIgUVTPCNlmw&sparams=expire%2Cei%2Cip%2Cid%2Caitags%2Csource%2Crequiressl%2Cspc%2Cvprv%2Cmime%2Cns%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRgIhAISPtHBdVz5LaztPIsUp12OYP6dvAuVW4j3qKkGadvt0AiEAgztGBFjvjZ_U2x-YMeR63NPm6JwJl3-DqhLejaamEyw%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRAIgFM2HyRROMYXKMJ2yGJ7UYrp04jQflRtokGIql-W_sCwCIDuu4nN-JFCTGONgzseKD5YuT0WDfmXpgwd8h8TBWBLo&range=0-',
    'lengthMs': 172520,
    'mimeType': 'video/mp4; codecs="av01.0.01M.08"',
    'extension': 'mp4',
    'lastModified': 1649562678789217,
    'size': 2616703,
    'sizeText': '2.5MB',
    'hasAudio': False,
    'quality': '360p',
    'width': 640,
    'height': 360
  },
  {
    'url': 'https://redirector.googlevideo.com/videoplayback?expire=1655759212&ei=DI2wYqzvE4WUhwaRkoHADw&ip=18.208.214.162&id=o-ANjhikHXo9ALHwCepBIF00MPvt8_mYt4FLr0e6972l-e&itag=133&aitags=133%2C134%2C135%2C136%2C137%2C160%2C242%2C243%2C244%2C247%2C248%2C278%2C394%2C395%2C396%2C397%2C398%2C399&source=youtube&requiressl=yes&mh=fj&mm=31%2C29&mn=sn-p5qddn7d%2Csn-p5qlsn7l&ms=au%2Crdu&mv=m&mvi=1&pl=18&initcwndbps=603750&spc=4ocVC5IE7Zn65gw46xx6HHpJ8RuDiOqaIB8e6DZ7tkKb&vprv=1&mime=video%2Fmp4&ns=YIhMiSWLMG7l-H1wTDVp-TUG&gir=yes&clen=1348393&dur=172.520&lmt=1649564935650583&mt=1655737257&fvip=3&keepalive=yes&fexp=24001373%2C24007246&c=WEB&txp=4535434&n=dsKIgUVTPCNlmw&sparams=expire%2Cei%2Cip%2Cid%2Caitags%2Csource%2Crequiressl%2Cspc%2Cvprv%2Cmime%2Cns%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRQIhAN_bu6BCt3YOVdfjy7_sKWI_4CfniKLAy_sbOt2mSXWEAiBRjaaaUDFg42vF5vpJiVyK3WXocXKp6rZZQx0WYql-pw%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRAIgFM2HyRROMYXKMJ2yGJ7UYrp04jQflRtokGIql-W_sCwCIDuu4nN-JFCTGONgzseKD5YuT0WDfmXpgwd8h8TBWBLo&range=0-',
    'lengthMs': 172520,
    'mimeType': 'video/mp4; codecs="avc1.4d4015"',
    'extension': 'mp4',
    'lastModified': 1649564935650583,
    'size': 1348393,
    'sizeText': '1.3MB',
    'hasAudio': False,
    'quality': '240p',
    'width': 426,
    'height': 240
  },
  {
    'url': 'https://redirector.googlevideo.com/videoplayback?expire=1655759212&ei=DI2wYqzvE4WUhwaRkoHADw&ip=18.208.214.162&id=o-ANjhikHXo9ALHwCepBIF00MPvt8_mYt4FLr0e6972l-e&itag=242&aitags=133%2C134%2C135%2C136%2C137%2C160%2C242%2C243%2C244%2C247%2C248%2C278%2C394%2C395%2C396%2C397%2C398%2C399&source=youtube&requiressl=yes&mh=fj&mm=31%2C29&mn=sn-p5qddn7d%2Csn-p5qlsn7l&ms=au%2Crdu&mv=m&mvi=1&pl=18&initcwndbps=603750&spc=4ocVC5IE7Zn65gw46xx6HHpJ8RuDiOqaIB8e6DZ7tkKb&vprv=1&mime=video%2Fwebm&ns=YIhMiSWLMG7l-H1wTDVp-TUG&gir=yes&clen=1596885&dur=172.520&lmt=1649571813922584&mt=1655737257&fvip=3&keepalive=yes&fexp=24001373%2C24007246&c=WEB&txp=4535434&n=dsKIgUVTPCNlmw&sparams=expire%2Cei%2Cip%2Cid%2Caitags%2Csource%2Crequiressl%2Cspc%2Cvprv%2Cmime%2Cns%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRQIgDTHO2qvH81dTOJK1DWhX1pB-R6C7nNJDhYTeP56IGjoCIQC5VEpUCKcfeisgBd5XYzR-3RP91cp4CCe3EV0qO2QQzQ%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRAIgFM2HyRROMYXKMJ2yGJ7UYrp04jQflRtokGIql-W_sCwCIDuu4nN-JFCTGONgzseKD5YuT0WDfmXpgwd8h8TBWBLo&range=0-',
    'lengthMs': 172520,
    'mimeType': 'video/webm; codecs="vp9"',
    'extension': 'webm',
    'lastModified': 1649571813922584,
    'size': 1596885,
    'sizeText': '1.5MB',
    'hasAudio': False,
    'quality': '240p',
    'width': 426,
    'height': 240
  },
  {
    'url': 'https://redirector.googlevideo.com/videoplayback?expire=1655759212&ei=DI2wYqzvE4WUhwaRkoHADw&ip=18.208.214.162&id=o-ANjhikHXo9ALHwCepBIF00MPvt8_mYt4FLr0e6972l-e&itag=395&aitags=133%2C134%2C135%2C136%2C137%2C160%2C242%2C243%2C244%2C247%2C248%2C278%2C394%2C395%2C396%2C397%2C398%2C399&source=youtube&requiressl=yes&mh=fj&mm=31%2C29&mn=sn-p5qddn7d%2Csn-p5qlsn7l&ms=au%2Crdu&mv=m&mvi=1&pl=18&initcwndbps=603750&spc=4ocVC5IE7Zn65gw46xx6HHpJ8RuDiOqaIB8e6DZ7tkKb&vprv=1&mime=video%2Fmp4&ns=YIhMiSWLMG7l-H1wTDVp-TUG&gir=yes&clen=1333476&dur=172.520&lmt=1649561817220600&mt=1655737257&fvip=3&keepalive=yes&fexp=24001373%2C24007246&c=WEB&txp=4532434&n=dsKIgUVTPCNlmw&sparams=expire%2Cei%2Cip%2Cid%2Caitags%2Csource%2Crequiressl%2Cspc%2Cvprv%2Cmime%2Cns%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRAIgBxudL83BKW2i-Pnp_LFT1UZa7QtqLyDSfZo0Oegn_MwCICTUwQ2TEfV6tCVV4ycMf5v-Y2cIMZJ2i8b1XQTVtklK&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRAIgFM2HyRROMYXKMJ2yGJ7UYrp04jQflRtokGIql-W_sCwCIDuu4nN-JFCTGONgzseKD5YuT0WDfmXpgwd8h8TBWBLo&range=0-',
    'lengthMs': 172520,
    'mimeType': 'video/mp4; codecs="av01.0.00M.08"',
    'extension': 'mp4',
    'lastModified': 1649561817220600,
    'size': 1333476,
    'sizeText': '1.3MB',
    'hasAudio': False,
    'quality': '240p',
    'width': 426,
    'height': 240
  },
  {
    'url': 'https://redirector.googlevideo.com/videoplayback?expire=1655759212&ei=DI2wYqzvE4WUhwaRkoHADw&ip=18.208.214.162&id=o-ANjhikHXo9ALHwCepBIF00MPvt8_mYt4FLr0e6972l-e&itag=160&aitags=133%2C134%2C135%2C136%2C137%2C160%2C242%2C243%2C244%2C247%2C248%2C278%2C394%2C395%2C396%2C397%2C398%2C399&source=youtube&requiressl=yes&mh=fj&mm=31%2C29&mn=sn-p5qddn7d%2Csn-p5qlsn7l&ms=au%2Crdu&mv=m&mvi=1&pl=18&initcwndbps=603750&spc=4ocVC5IE7Zn65gw46xx6HHpJ8RuDiOqaIB8e6DZ7tkKb&vprv=1&mime=video%2Fmp4&ns=YIhMiSWLMG7l-H1wTDVp-TUG&gir=yes&clen=745917&dur=172.520&lmt=1649564936485061&mt=1655737257&fvip=3&keepalive=yes&fexp=24001373%2C24007246&c=WEB&txp=4535434&n=dsKIgUVTPCNlmw&sparams=expire%2Cei%2Cip%2Cid%2Caitags%2Csource%2Crequiressl%2Cspc%2Cvprv%2Cmime%2Cns%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRAIgduK1ZolaJ7mGJNfLBGZ5Dp6Mi4FVAMMMMPaCFB4mw3ECIBPGpQnHhX5HWwYdZoU4avca0T3sgPMwI_W6KLs7qQVO&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRAIgFM2HyRROMYXKMJ2yGJ7UYrp04jQflRtokGIql-W_sCwCIDuu4nN-JFCTGONgzseKD5YuT0WDfmXpgwd8h8TBWBLo&range=0-',
    'lengthMs': 172520,
    'mimeType': 'video/mp4; codecs="avc1.4d400c"',
    'extension': 'mp4',
    'lastModified': 1649564936485061,
    'size': 745917,
    'sizeText': '728.4KB',
    'hasAudio': False,
    'quality': '144p',
    'width': 256,
    'height': 144
  },
  {
    'url': 'https://redirector.googlevideo.com/videoplayback?expire=1655759212&ei=DI2wYqzvE4WUhwaRkoHADw&ip=18.208.214.162&id=o-ANjhikHXo9ALHwCepBIF00MPvt8_mYt4FLr0e6972l-e&itag=278&aitags=133%2C134%2C135%2C136%2C137%2C160%2C242%2C243%2C244%2C247%2C248%2C278%2C394%2C395%2C396%2C397%2C398%2C399&source=youtube&requiressl=yes&mh=fj&mm=31%2C29&mn=sn-p5qddn7d%2Csn-p5qlsn7l&ms=au%2Crdu&mv=m&mvi=1&pl=18&initcwndbps=603750&spc=4ocVC5IE7Zn65gw46xx6HHpJ8RuDiOqaIB8e6DZ7tkKb&vprv=1&mime=video%2Fwebm&ns=YIhMiSWLMG7l-H1wTDVp-TUG&gir=yes&clen=1232880&dur=172.520&lmt=1649571819074979&mt=1655737257&fvip=3&keepalive=yes&fexp=24001373%2C24007246&c=WEB&txp=4535434&n=dsKIgUVTPCNlmw&sparams=expire%2Cei%2Cip%2Cid%2Caitags%2Csource%2Crequiressl%2Cspc%2Cvprv%2Cmime%2Cns%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRQIhALT3uUeuRBOR3zAqPAy5MKQvjVfaw72HKtJg_9FHw8ZHAiBrrRwNiENUW9wldIbRbg7_NajntAHRwvJTgu61Jh7DXw%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRAIgFM2HyRROMYXKMJ2yGJ7UYrp04jQflRtokGIql-W_sCwCIDuu4nN-JFCTGONgzseKD5YuT0WDfmXpgwd8h8TBWBLo&range=0-',
    'lengthMs': 172520,
    'mimeType': 'video/webm; codecs="vp9"',
    'extension': 'webm',
    'lastModified': 1649571819074979,
    'size': 1232880,
    'sizeText': '1.2MB',
    'hasAudio': False,
    'quality': '144p',
    'width': 256,
    'height': 144
  },
  {
    'url': 'https://redirector.googlevideo.com/videoplayback?expire=1655759212&ei=DI2wYqzvE4WUhwaRkoHADw&ip=18.208.214.162&id=o-ANjhikHXo9ALHwCepBIF00MPvt8_mYt4FLr0e6972l-e&itag=394&aitags=133%2C134%2C135%2C136%2C137%2C160%2C242%2C243%2C244%2C247%2C248%2C278%2C394%2C395%2C396%2C397%2C398%2C399&source=youtube&requiressl=yes&mh=fj&mm=31%2C29&mn=sn-p5qddn7d%2Csn-p5qlsn7l&ms=au%2Crdu&mv=m&mvi=1&pl=18&initcwndbps=603750&spc=4ocVC5IE7Zn65gw46xx6HHpJ8RuDiOqaIB8e6DZ7tkKb&vprv=1&mime=video%2Fmp4&ns=YIhMiSWLMG7l-H1wTDVp-TUG&gir=yes&clen=1232075&dur=172.520&lmt=1649561679247213&mt=1655737257&fvip=3&keepalive=yes&fexp=24001373%2C24007246&c=WEB&txp=4532434&n=dsKIgUVTPCNlmw&sparams=expire%2Cei%2Cip%2Cid%2Caitags%2Csource%2Crequiressl%2Cspc%2Cvprv%2Cmime%2Cns%2Cgir%2Cclen%2Cdur%2Clmt&sig=AOq0QJ8wRQIgFLwDQlOvpMphIjAC0fe4exTAERJiWiFnlLa_ZrDvbi4CIQDEopWvyhaiXHwF5U4jSvV5P7HVw0B5vapQCGSHAbOsVg%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRAIgFM2HyRROMYXKMJ2yGJ7UYrp04jQflRtokGIql-W_sCwCIDuu4nN-JFCTGONgzseKD5YuT0WDfmXpgwd8h8TBWBLo&range=0-',
    'lengthMs': 172520,
    'mimeType': 'video/mp4; codecs="av01.0.00M.08"',
    'extension': 'mp4',
    'lastModified': 1649561679247213,
    'size': 1232075,
    'sizeText': '1.2MB',
    'hasAudio': False,
    'quality': '144p',
    'width': 256,
    'height': 144
  }
]

b = [
  {
    'url': 'https://redirector.googlevideo.com/videoplayback?expire=1655759212&ei=DI2wYqzvE4WUhwaRkoHADw&ip=18.208.214.162&id=o-ANjhikHXo9ALHwCepBIF00MPvt8_mYt4FLr0e6972l-e&itag=18&source=youtube&requiressl=yes&mh=fj&mm=31%2C29&mn=sn-p5qddn7d%2Csn-p5qlsn7l&ms=au%2Crdu&mv=m&mvi=1&pl=18&initcwndbps=603750&spc=4ocVC5IE7Zn65gw46xx6HHpJ8RuDiOqaIB8e6DZ7tkKb&vprv=1&mime=video%2Fmp4&ns=2Imu4XagMPciSvhz4GvBWn8G&gir=yes&clen=9934996&ratebypass=yes&dur=172.570&lmt=1649561623578954&mt=1655737257&fvip=3&fexp=24001373%2C24007246&c=WEB&txp=4538434&n=NsC449tOphFplA&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Cmime%2Cns%2Cgir%2Cclen%2Cratebypass%2Cdur%2Clmt&sig=AOq0QJ8wRQIgUvBYMjbDl8VcxWBJ_EA2YIwgd72mY6z8TIoIJK-cWZoCIQDXpZNzLDC0D4-eM5C5IvUC96wKMnuqiSFeduoS00BisQ%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRAIgFM2HyRROMYXKMJ2yGJ7UYrp04jQflRtokGIql-W_sCwCIDuu4nN-JFCTGONgzseKD5YuT0WDfmXpgwd8h8TBWBLo&range=0-',
    'lengthMs': 172570,
    'mimeType': 'video/mp4; codecs="avc1.42001E, mp4a.40.2"',
    'extension': 'mp4',
    'lastModified': 1649561623578954,
    'size': 9934996,
    'sizeText': '9.5MB',
    'hasAudio': True,
    'quality': '360p',
    'width': 640,
    'height': 360
  },
  {
    'url': 'https://redirector.googlevideo.com/videoplayback?expire=1655759212&ei=DI2wYqzvE4WUhwaRkoHADw&ip=18.208.214.162&id=o-ANjhikHXo9ALHwCepBIF00MPvt8_mYt4FLr0e6972l-e&itag=22&source=youtube&requiressl=yes&mh=fj&mm=31%2C29&mn=sn-p5qddn7d%2Csn-p5qlsn7l&ms=au%2Crdu&mv=m&mvi=1&pl=18&initcwndbps=603750&spc=4ocVC5IE7Zn65gw46xx6HHpJ8RuDiOqaIB8e6DZ7tkKb&vprv=1&mime=video%2Fmp4&ns=2Imu4XagMPciSvhz4GvBWn8G&cnr=14&ratebypass=yes&dur=172.570&lmt=1649564968851467&mt=1655737257&fvip=3&fexp=24001373%2C24007246&c=WEB&txp=4532434&n=NsC449tOphFplA&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Cmime%2Cns%2Ccnr%2Cratebypass%2Cdur%2Clmt&sig=AOq0QJ8wRAIgQWXBKZuQW6FigM9rb1ofKpJ7aqhgj-ChUNMkl6rZ8PMCIHBfo1ftAWns5OJd1OjIIZ2pTMO1Vlg-7n_tXm3DaR6e&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=AG3C_xAwRAIgFM2HyRROMYXKMJ2yGJ7UYrp04jQflRtokGIql-W_sCwCIDuu4nN-JFCTGONgzseKD5YuT0WDfmXpgwd8h8TBWBLo&range=0-',
    'lengthMs': 172570,
    'mimeType': 'video/mp4; codecs="avc1.64001F, mp4a.40.2"',
    'extension': 'mp4',
    'lastModified': 1649564968851467,
    'size': 10786712,
    'sizeText': '10.3MB',
    'hasAudio': True,
    'quality': '720p',
    'width': 1280,
    'height': 720
  }
]

# for j in b:
#     print("url= ", j["url"])
#     print("size=", j['sizeText'])
#     print("formati = ", j['quality'])