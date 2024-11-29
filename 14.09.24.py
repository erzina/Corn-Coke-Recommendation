teploty = [22, 32, 28, 30, 21, 33, 29]
ceny_ubytovani = [42000, 30000, 18000, 40000, 25000, 27000]
def najdi_hodnot_mensich_nez(seznam, limit):
    pocet=0
    for hodnota in seznam:
        if hodnota <= limit:
            pocet = pocet + 1
    return pocet
chlad = najdi_hodnot_mensich_nez(teploty, 30)
levne_ubyt = najdi_hodnot_mensich_nez(ceny_ubytovani, 35000)
print (levne_ubyt)