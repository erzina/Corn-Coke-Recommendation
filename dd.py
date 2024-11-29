names = ['Roman', 'Jana', 'Radek', 'Petra', 'Vlasta']

with open('uzivatele.txt', mode='w', encoding='utf-8') as output_file:
    for name in names:
        print(name, file=output_file)