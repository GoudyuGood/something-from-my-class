import requests

people = requests.get('http://api.open-notify.org/astros.json')

people_json = people.json()

print('The number of people in space today:', people_json['number'], '. These are their names:')


for p in people_json['people']:
    print(p['name'], end=', ')
