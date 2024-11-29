import json
with open('zavod.json', encoding='utf-8') as file:
    runners = json.load(file)

finishers = []

for runner in runners:
    jmeno = runner['jmeno']
    casy = runner['casy']
    ofc = casy['oficialni']
    if  ofc != 'DNF':
        finishers.append([jmeno, ofc])
    
print (finishers)
print (finishers[1])

