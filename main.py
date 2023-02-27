import requests
import random

url = 'https://ngl.link/api/submit'
headers = {
    'Cookie': '_ga_5DV1ZR5ZHG34=GS1.341.16347509341c56.341.1.167750953415.0.0.0; _ga=GA1.1.41343334205344.1634734347509153473 __stripe_mid=DD34E02-12343495-4f4334d-8034f7-606153344534734b571833442590b',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    'Origin': 'https://ngl.link',
    'Dnt': '1',
    'Referer': 'https://ngl.link//',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'Te': 'trailers'
}
# You need to create a txt file with this name "questions" or use the one i created, within this file write anything you want per line!
with open('questions.txt', 'r') as f:
    questions = f.readlines()
# Change the username to the username you want
data = {
    'username': 'changeusernamehere',
    'deviceId': 'aa',
    'gameSlug': '',
    'referrer': ''
}

while True:
    question = random.choice(questions).strip()
    data['question'] = question

    response = requests.post(url, headers=headers, data=data)

    print(f'Response: {response.status_code}')
    print(response.content.decode())
