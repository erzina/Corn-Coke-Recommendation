import json

with open ('absolventi.json', encoding='utf-8') as file:
    absolvents = json.load (file)

print (absolvents[0])
