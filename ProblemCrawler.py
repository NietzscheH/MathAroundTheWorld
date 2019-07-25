import requests, json

r = requests.get('https://opentdb.com/api.php?amount=2&category=19&difficulty=easy&type=multiple')
for i in json.loads(r.text)['results']:
    print(i, i['question'])
