import requests

response = requests.get('https://api.kodim.cz/python-data/people')
data = response.json()

print(len(data))
clovek = data[0]
print(clovek.keys())

num_genders = {}
for person in data:
    gender = person['gender']
    if gender not in num_genders:
        num_genders[gender] = 1
    else:
        num_genders[gender] += 1

print(num_genders)