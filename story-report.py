import requests
import time
import json
import uuid
uid = str(uuid.uuid4())
LOGIN = False
r1 = requests.session()
see = None
s1  = None
coo = None
ids_store = []
class givt():
    def __init__(self):
        self.username = input("[-] Username:")#"navarroriz"
        self.password = input("[-] Password:") #"hsopass"
        self.target = input("[?] Enter Target:")
        self.login()
    def work(self):
        global ids_store,coo,see,s1
        for api in ids_store:
            url = "https://www.instagram.com/reports/web/get_frx_prompt/"
            headers = {
                "Host": "www.instagram.com",
                "User-Agent": "Mozilla/5.0 (X11; Linux i686; rv:78.0) Gecko/20100101 Firefox/78.0/",
                "Accept": "*/*",
                "Accept-Language": "en-US,en;q=0.5",
                "Accept-Encoding": "gzip, deflate, br",
                "Referer": f"https://www.instagram.com/stories/{self.target}/{api}/",
                "X-CSRFToken": "zPnq799h349OuQc1Ahuw4BH98BDPujEC",
                "X-Instagram-AJAX": "3c8826838272",
                "X-IG-App-ID": "936619743392459",
                "X-IG-WWW-Claim": "hmac.AR12Fs18fzvYP9jCne1dhLjB5a8pdPtPh17yqrMQzdvWj5eu",
                "Content-Type": "application/x-www-form-urlencoded",
                "X-Requested-With": "XMLHttpRequest",
                "Content-Length": "123",
                "Origin": "https://www.instagram.com",
                "DNT": "1",
                "Connection": "keep-alive",
                "Cookie": f"ig_cb=2; ig_did=4CA12CAF-9430-4ACF-80DA-7D64D33399D9; mid=YBhesAAEAAEuiDl5OVfmlJNtVmH0; shbid=482; shbts=1618225557.0733764; datr=azslYEfwg6RU7z0vwH_Rka-T; ig_nrcb=1; csrftoken=zPnq799h349OuQc1Ahuw4BH98BDPujEC; ds_user_id={s1}; sessionid={see}; rur=RVA",
                "TE": "Trailers"}
            data = f'entry_point=1&location=4&object_type=1&object_id={api}&container_module=StoriesPage&frx_prompt_request_type=1'
            r = r1.post(url,headers=headers,data=data,cookies=coo)
            try:
                s = str(r.json()['response']['context'])
                url_report = "https://www.instagram.com/reports/web/get_frx_prompt/"
                headers_report = {
                    "Host": "www.instagram.com",
                    "User-Agent": "Mozilla/5.0 (X11; Linux i686; rv:78.0) Gecko/20100101 Firefox/78.0",
                    "Accept": "*/*",
                    "Accept-Language": "en-US,en;q=0.5",
                    "Referer": f"https://www.instagram.com/stories/{self.target}/{api}/",
                    "X-CSRFToken": "zPnq799h349OuQc1Ahuw4BH98BDPujEC",
                    "X-Instagram-AJAX": "7a2b9f55ccdb",
                    "X-IG-App-ID": "936619743392459",
                    "X-IG-WWW-Claim": "hmac.AR12Fs18fzvYP9jCne1dhLjB5a8pdPtPh17yqrMQzdvWjzJd",
                    "Content-Type": "application/x-www-form-urlencoded",
                    "X-Requested-With": "XMLHttpRequest",
                    "Content-Length": "2947",
                    "Origin": "https://www.instagram.com",
                    "DNT": "1",
                    "Connection": "keep-alive",
                    "Cookie": f"ig_cb=2; ig_did=4CA12CAF-9430-4ACF-80DA-7D64D33399D9; mid=YBhesAAEAAEuiDl5OVfmlJNtVmH0; shbid=482; shbts=1618225557.0733764; datr=azslYEfwg6RU7z0vwH_Rka-T; ig_nrcb=1; csrftoken=zPnq799h349OuQc1Ahuw4BH98BDPujEC; ds_user_id={s1}; sessionid={see}; rur=RVA",}
                data_report = {
                    "entry_point":"1",
                    "location":"4",
                    "object_type":"1",
                    "object_id":api,
                    "container_module":"StoriesPage",
                    "context":s,
                    "action_type":"2",
                    "frx_prompt_request_type":"4"
                }
                r2 = r1.post(url_report,headers=headers_report,data=data_report,cookies=coo)
                if r2.text.find('Thanks for reporting this post')>=0:
                    print(f"[+] Done Report :{api}")
                else:
                    print(f"[-] Error Report :{api}")
            except:
                print("[-] Somethings Error !")
    def get_ids_store(self):
        global ids_store,coo,see,s1
        r77 = r1.get(f'https://instagram.com/{self.target}/?__a=1').json()
        user_id = str(r77["logging_page_id"])
        apis = str(user_id.split("_")[1])
        self.api = apis
        headers = {
            "Host": "i.instagram.com",
            "User-Agent": "Mozilla/5.0 (X11; Linux i686; rv:78.0) Gecko/20100101 Firefox/78.0",
            "Accept": "*/*",
            "Accept-Language": "en-US,en;q=0.5",
            "Referer": "https://www.instagram.com/",
            "X-IG-App-ID": "936619743392459",
            "X-IG-WWW-Claim": "hmac.AR12Fs18fzvYP9jCne1dhLjB5a8pdPtPh17yqrMQzdvWj2dQ",
            "Origin": "https://www.instagram.com",
            "DNT": "1",
            "Connection": "keep-alive"}
        url_store = f"https://i.instagram.com/api/v1/feed/reels_media/?reel_ids={self.api}"
        r = r1.get(url_store, headers=headers, cookies=coo)
        a = 0
        while True:
            try:
                s1 = str(r.json()['reels'][f"{self.api}"]['items'][a]['pk'])
                print(f"\r[+] Done Get Story ID ---> {a}",end="")
                ids_store.append(s1)
                a+=1
            except:
                print("\n[+] Done Get ID Storys")
                break
        if a == 0:
            print("\n[!] No Story Found or private account")
            input('')
            exit()
        else:
            self.work()
    def login(self):
        global LOGIN,r1,s1,see,coo
        url = 'https://www.instagram.com/accounts/login/ajax/'
        headers = {
            'accept': '*/*',
            'accept-encoding': 'gzip, deflate, br',
            'accept-language': 'ar,en-US;q=0.9,en;q=0.8',
            'content-length': '291',
            'content-type': 'application/x-www-form-urlencoded',
            'cookie': 'ig_did=3E70DB93-4A27-43EB-8463-E0BFC9B02AE1; mid=YCAadAALAAH35g_7e7h0SwBbFzBt; ig_nrcb=1; csrftoken=COmXgzKurrq8awSnRS1xf3u9rL6QsGZI',
            'origin': 'https://www.instagram.com',
            'referer': 'https://www.instagram.com/',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36',
            'x-csrftoken': 'COmXgzKurrq8awSnRS1xf3u9rL6QsGZI',
            'x-ig-app-id': '936619743392459',
            'x-ig-www-claim': '0',
            'x-instagram-ajax': '1cb44f68ffec',
            'x-requested-with': 'XMLHttpRequest'}
        data_login = {
            'username': self.username,
            'enc_password': f'#PWD_INSTAGRAM_BROWSER:0:1613414957:{self.password}',
            'queryParams': '{}',
            'optIntoOneTap': 'false'}
        r = r1.post(url, headers=headers, data=data_login)
        if r.text.find('"authenticated":true') >= 0:
            see = r.cookies['sessionid']
            s1 = r.cookies['ds_user_id']
            coo = r.cookies
            print("[=] Done Login")
            self.get_ids_store()
        else:
            LOGIN = False
            print("[X] Error login:", r.text)
            self.__init__()

givt()