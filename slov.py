sales = {
    "Zkus mě chytit": 4165,
    "Vrah zavolá v deset": 5681,
    "Zločinný steh": 2565,
}
#nazvy knih
for key, value in sales.items():
    print(key)
for key, value in sales.items():
    print(f"Knihy {key} bylo prodáno {value} výtisků.")
sales_values = sales.values()
total_sales = sum(sales_values)
print(total_sales)
total_sales=0
for key, value in sales.items():
    total_sales = total_sales + value
print(total_sales)
print(len(sales))