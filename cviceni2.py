books = [
    {"title": "Vražda s příliš mnoha notami", "pages": 450, "rating": 5},
    {"title": "Vražda podle knihy", "pages": 524, "rating": 9},
    {"title": "Past", "pages": 390, "rating": 4},
    {"title": "Popel popelu", "pages": 411, "rating": 10},
    {"title": "Noc, která mě zabila", "pages": 159, "rating": 7},
    {"title": "Vražda, kouř a stíny", "pages": 258, "rating": 6},
    {"title": "Zločinný steh", "pages": 542, "rating": 8},
    {"title": "Zkus mě chytit", "pages": 247, "rating": 7},
    {"title": "Vrah zavolá v deset", "pages": 396, "rating": 6},
]

total_pages = 0
for book in books:
    total_pages += book["pages"]
print(f"Celkem bylo precteno {total_pages} pages.")

    if book['rating'] >= 8:
        print (book['title'])
        
for item in books:
    def najdi_hodnot_mensich_nez(seznam, limit):
    pocet=0
    for hodnota in seznam:
        if hodnota <= limit:
            pocet = pocet + 1
    return pocet
Vice_ney_8 = najdi_hodnot_mensich_nez(rating, 8)
print (Vice_ney_8)