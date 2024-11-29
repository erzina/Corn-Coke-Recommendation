school_report = {
    "Český jazyk": 1,
    "Anglický jazyk": 1,
    "Matematika": 1,
    "Přírodopis": 2,
    "Dějepis": 1,
    "Fyzika": 2,
    "Hudební výchova": 4,
    "Výtvarná výchova": 2,
    "Tělesná výchova": 3,
    "Chemie": 4,
}
prumerna_ynamka = 0
for predmet, value in school_report.items():
    prumerna_ynamka += value/(len(school_report))
print(prumerna_ynamka)

soucet = sum(school_report.values())
delka = len(school_report)
prumer = soucet / delka
print(f'prumerna znamka je {prumer}')