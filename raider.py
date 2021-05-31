import requests, time, random, threading, os

os.system('cls')
os.system('title Discord Token Raider - By Pepe ツ#9999')

banner_text = '''
    ____                   __  __          __           
   / __ \_  _______________\ \/ /__  ___  / /____  _____
  / / / / |/_/ ___/ ___/ __ \  / _ \/ _ \/ __/ _ \/ ___/
 / /_/ />  <(__  ) /__/ /_/ / /  __/  __/ /_/  __/ /    
/_____/_/|_/____/\___/\____/_/\___/\___/\__/\___/_/     
                                                        
 Coded by: ➬ Pepe ツ#9999    
'''   
print(banner_text)


file = input('Input name of Proxy file: ')
try:
    with open(file, 'r+') as f:
        proxyarray = f.read().splitlines()
except Exception:
    print("Invalid Proxy File name. Closing...")
    time.sleep(5)
filetokens = input('Input name of Token file: ')
try:
    with open(filetokens, 'r+') as f:
        tokens = f.read().splitlines()
        tokens.sort()
except Exception:
    print("Invalid Token File name. Closing...")
    time.sleep(5)

invitecode = input('Enter the Invite Code: ')

def joinserver(invite, token):
    posturl = f"https://discord.com/api/v8/invites/{invite}"

    proxy = random.choice(proxyarray)

    proxies = {
        'http': 'http://' + proxy,
        'https': 'http://' + proxy
    }

    headers = {
        'accept': '*/*',
        'accept-encoding': 'gzip, deflate, br',
        'accept-language': 'de',
        'authorization': token,
        'content-length': '0',
        'cookie': '''__cfduid=d29b03c861c9946a94d03a0496cd094881618767505; __dcfduid=39c9736a6f12e98b7067efa27ab53c6a; locale=de; _ga=GA1.2.1440912255.1618809286; _gid=GA1.2.384772034.1618809286; __stripe_mid=392b57df-a061-4026-82e7-7d7d04e2097907427b; __stripe_sid=b7eb9154-6794-4726-9097-04dbc28cd69216e93c''',
        'origin': 'https://discord.com',
        'referer': 'https://discord.com/channels/@me',
        'sec-ch-ua': '''"Google Chrome";v="89", "Chromium";v="89", ";Not A Brand";v="99"''',
        'sec-ch-ua-mobile': '?0',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.128 Safari/537.36',
        'x-context-properties': 'eyJsb2NhdGlvbiI6IkpvaW4gR3VpbGQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6IjMyNTAxNzA5ODU5MjA1OTM5MiIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI2Njc0NzQ2MjYzMzAyMzA3ODQiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjB9',
        'x-super-properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImRlLURFIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzg5LjAuNDM4OS4xMjggU2FmYXJpLzUzNy4zNiIsImJyb3dzZXJfdmVyc2lvbiI6Ijg5LjAuNDM4OS4xMjgiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6ODI1OTAsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGx9'
    }

    try:
        requests.post(posturl, headers=headers, proxies=proxies, timeout=0.5)
    except Exception:
        joinserver(invite, token)

for token in tokens:
    threading.Thread(target=joinserver, args=(invitecode, token, )).start()