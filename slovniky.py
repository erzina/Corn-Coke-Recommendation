item = {"title": "Čajová konvička s hrnky", "price": 899, "in_stock": True}
key = input("ktery klic?")
item[key] = 0.9
if key in item:
    print(f"Hmotnost je {item[key]}")
else:
    print ("Hmotnost nezname")