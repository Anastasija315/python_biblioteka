from book_manager import add_or_update_book, show_all_books, top_5_popular, top_5_expensive

def main():
    while True:
        print("\n *** Laipni lūgti digitālajā bibliotēkā! ***")
        print("Ievadiet skaitli no 1 līdz 5, lai izvēlēties darbību:")
        print("1 - Pievienot vai atjaunināt grāmatu")
        print("2 - Apskatīt visas grāmatas")
        print("3 - Aizņemt vai atgriezt grāmatu")
        print("4 - Meklēt grāmatu")
        print("5 - Apskatīt Top 5 sarakstus")
        print("6 - Iziet no sistēmas")

        izvele = input("Jūsu izvēle: ")

        if izvele == "1":
            add_or_update_book()
        elif izvele == "2":
            show_all_books()
        elif izvele == "3":
            pass
        elif izvele == "4":
            pass
        elif izvele == "5":
            pass
        elif izvele == "6":
            print("Uz redzēšanos!")
            break
        else:
            print("Kļūda! Ievadiet skaitli no 1 līdz 6")

if __name__ == "__main__":
    main()
