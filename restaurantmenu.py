#Restorant menu
menu = {
    "Pizza": 8.50,
    "Fish": 7.00,
    "Pasta": 5.00,
    "Salad": 4.50,
    "Water": 1.00,
    "Lemon Soda": 1.50
}

def take_order():
    order = {}
    while True:
        display_menu()
        item = input("Shkruaj emrin e produktit qe deshironi te porosisni (ose shkruani 'done' per te perfunduar porosine): ")
        if item.lower() == 'done':
            break
        elif item in menu:
            quantity = int(input(f"Sa {item}(a) deshironi te porosisni? "))
            if item in order:
                order[item] += quantity
            else:
                order[item] = quantity
        else:
            print("Produkti qe keni shkruar nuk ekziston ne menu. Provoni perseri.")
    return order

def display_menu():
    print("Menuja e restorantit:")
    for item, price in menu.items():
        print(f"{item}: ${price:.2f}")

def calculate_total(order):
    total = 0
    for item, quantity in order.items():
        total += menu[item] * quantity
    return total

def run_restorant():
    while True:
        print("Miresevini ne restorantin tone!")
        order = take_order()
        if order:
            total = calculate_total(order)
            print(f"Shuma totale per porosine tuaj eshte: ${total:.2f}")
        else:
            print("Nuk keni bere asnje porosi.")
        another_order = input("deshironi te beni nje porosi tjeter? (po/jo) ")
        if another_order.lower() != 'po':
            print("Faleminderit qe vizituat restorantin. Jeni qdo here te mireseardhur!")
            break
run_restorant()