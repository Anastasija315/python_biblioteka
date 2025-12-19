import json

def load_books():
    """nolasa grāmatu datus"""
  
    with open("data/library_data.json", "r", encoding="utf-8") as file:
        return json.load(file)


def save_books(books):
    """saglabā grāmatu datus"""

    with open("data/library_data.json", "w", encoding="utf-8") as file:
        json.dump(books, file, ensure_ascii=False, indent=4)


def add_or_update_book():
    """atjaunina vai pievieno jaunu grāmatu"""

    books = load_books()
    nosaukums = input("Nosaukums: ")
    autors = input("Autors: ")
    cena = float(input("Cena: "))
    eksemplari = int(input("Pieejamais eksemplāru skaits: "))

    # pārbauda, vai grāmata jau eksistē
    for book in books:
        if book["nosaukums"].lower() == nosaukums.lower():
            book["autors"] = autors
            book["cena"] = cena
            book["eksemplari"] += eksemplari
            print("Grāmata ir atjaunināta")
            save_books(books)
            return
        
        # ja neeksistē - pievieno jaunu
        new_book = {
          "nosaukums": nosaukums,
          "autors": autors,
          "cena": cena,
          "eksemplari": eksemplari,
          "izsniegtais": 0
        }

        books.append(new_book)
        save_books(books)
        print("Grāmata ir pievienota")
