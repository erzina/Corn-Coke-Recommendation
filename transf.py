result = {}

with open ('words.txt', encoding = 'utf-8') as file:
    for row in file:
        word = row.strip()
        first_letter = word[0]

        if first_letter not in result:
            result[first_letter] = word
        else:
            result[first_letter].append(word)

print (result['a'])
for letter, words in result.items():
    words.sort()