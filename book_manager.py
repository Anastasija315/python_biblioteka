import json

dati = "data/library_data.json"

# Vienas grāmatas apraksts
class Book:
    def __init__(self, nosaukums, autors, cena, pieejamas, izsniegtas=0):
        self.nosaukums = nosaukums
        self.autors = autors
        self.cena = cena
        self.pieejamas = pieejamas
        self.izsniegtas = izsniegtas

    def convert(self):
        """Pārvērš Book par vārdnīcu (JSON saglabāšanai)"""

        return {
            "nosaukums": self.nosaukums,
            "autors": self.autors,
            "cena": self.cena,
            "pieejamas": self.pieejamas,
            "izsniegtas": self.izsniegtas
        }

# Darbs ar grāmatu sarakstu 
class Library:
    def __init__(self):
        self.books = self.load_books()

    def load_books(self):
        """Nolasa grāmatu datus no JSON faila"""

        try:
            with open(dati, "r", encoding="utf-8") as file:
                data = json.load(file)
                return data
        except (FileNotFoundError, json.JSONDecodeError): # fails nav atrasts vai invalid saturs
            return []

    def save_books(self):
        """Saglabā grāmatu datus JSON failā"""

        with open(dati, "w", encoding="utf-8") as file:
            json.dump(self.books, file, ensure_ascii=False, indent=4) # atbalsta latviešu simbolus

    def add_or_update_book(self):
        """Atjaunina veco vai pievieno jaunu grāmatu"""
        
        nosaukums = input("Nosaukums: ").strip()
        autors = input("Autors: ").strip()

        try:
            cena = float(input("Cena: "))
            pieejamas = int(input("Pieejamais eksemplāru skaits: "))
        except ValueError:
            print("Kļūda! Cena un pieejamais grāmatu skaits jāievada kā skaitļi")
            return

        if cena < 0 or pieejamas < 0:
            print("Kļūda! Vērtības nevar būt negatīvas")
            return

        # pārbauda, vai grāmata jau eksistē
        for book in self.books:
            if book["nosaukums"].lower() == nosaukums.lower():
                print("Grāmata jau pastāv - dati tiek atjaunināti")
                book["autors"] = autors
                book["cena"] = cena
                book["pieejamas"] = pieejamas
                self.save_books()
                return

        # ja neeksistē - pievieno jaunu
        new_book = Book(nosaukums, autors, cena, pieejamas)
        self.books.append(new_book.convert()) # pārvērš objektu Book par vārdnīcu un pievieno to sarakstā
        self.save_books()
        print("Grāmata veiksmīgi pievienota")

    def show_all_books(self):
        """Visu grāmatu saraksta apskate"""

        if not self.books:
            print("Nav grāmatu")
            return

        print("\n--- Visas pieejamās grāmatas ---")
        for book in self.books:
            print("-----------------------------")
            print(f"Nosaukums: {book['nosaukums']}")
            print(f"Autors: {book['autors']}")
            print(f"Cena: {book['cena']} EUR")
            print(f"Pieejamas: {book['pieejamas']}")
            print(f"Izsniegtas: {book['izsniegtas']}")
            print("-----------------------------")

    def top_5_popular(self):
        """Top 5 visvairāk izsniegtās grāmatas"""

        print("\n--- Top 5 visvairāk izsniegtās grāmatas ---")
        sorted_books = sorted(self.books, key=lambda x: x["izsniegtas"], reverse=True) # sakārto grāmatas pēc mainīgā "izsniegtas"

        for book in sorted_books[:5]:
            print(book["nosaukums"], "-", book["izsniegtas"])

    def top_5_expensive(self):
        """Top 5 dārgākās grāmatas"""

        print("\n--- Top 5 dārgākās grāmatas ---")
        sorted_books = sorted(self.books, key=lambda x: x["cena"], reverse=True) # sakārto grāmatas pēc mainīgā "cena"

        for book in sorted_books[:5]:
            print(book["nosaukums"], "-", book["cena"], "EUR")
