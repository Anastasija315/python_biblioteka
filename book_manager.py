import json

dati = "data/library_data.json"

def load_books():
    """nolasa grāmatu datus"""
  
    try:
        with open(dati, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_books(books):
    """saglabā grāmatu datus"""

    with open(dati, "w", encoding="utf-8") as file:
        json.dump(books, file, ensure_ascii=False, indent=4)


def add_or_update_book():
    """atjaunina vai pievieno jaunu grāmatu"""

    books = load_books()
    nosaukums = input("Nosaukums: ").strip()
    autors = input("Autors: ").strip()

    try:
        cena = float(input("Cena: "))
        pieejamas = int(input("Pieejamais eksemplāru skaits: "))
    except ValueError:
        print("Kļūda! Cena un pieejamais grāmatu skaits jāievada kā skaitļi!")
        return
    
    if cena < 0 or pieejamas < 0:
        print("Kļūda! Cena un pieejamais grāmatu skaits nevar būt negatīvi!")
        return

    # pārbauda, vai grāmata jau eksistē
    for book in books:
        if book["nosaukums"].lower() == nosaukums.lower():
            book["autors"] = autors
            book["cena"] = cena
            book["pieejamas"] = pieejamas
            print("Grāmata ir atjaunināta")
            save_books(books)
            return
        
    # ja neeksistē - pievieno jaunu
    new_book = {
        "nosaukums": nosaukums,
        "autors": autors,
        "cena": cena,
        "pieejamas": pieejamas,
        "izsniegtas": 0
    }

    books.append(new_book)
    save_books(books)
    print("Grāmata ir pievienota")


def show_all_books():
    """visu grāmatu saraksta apskate"""

    books = load_books()
    print("\n--- Visas pieejamas grāmatas ---")

    if not books:
        print("Nav grāmatu")
        return

    for book in books:
        print("-----------------------------")
        print(f"Nosaukums: {book['nosaukums']}")
        print(f"Autors: {book['autors']}")
        print(f"Cena: {book['cena']} EUR")
        print(f"Pieejamas: {book['pieejamas']}")
        print(f"Izsniegtas: {book['izsniegtas']}")
        print("-----------------------------")


def top_5_popular():
    """top 5 visvairāk izsniegtās grāmatas"""

    books = load_books()
    print("\n--- Top 5 visvairāk izsniegtas grāmatas ---")
    sorted_books = sorted(books, key=lambda x: x["izsniegtas"], reverse=True) # sakārto grāmatas pēc mainīgā "izsniegtas"

    for book in sorted_books[:5]:
        print(book["nosaukums"], "-", book["izsniegtas"])


def top_5_expensive():
    """top 5 dārgākās grāmatas"""

    books = load_books()
    print("\n--- Top 5 dārgākās grāmatas ---")
    sorted_books = sorted(books, key=lambda x: x["cena"], reverse=True) # sakārto grāmatas pēc mainīgā "cena"

    for book in sorted_books[:5]:
        print(book["nosaukums"], "-", book["cena"], "EUR")
