from book_manager import Library

def main():
    library = Library() 

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
            library.add_or_update_book()
        elif izvele == "2":
            library.show_all_books()
        elif izvele == "3":
            pass
        elif izvele == "4":
            pass
        elif izvele == "5":
            print("\n1 - Top 5 visvairāk izsniegtās grāmatas")
            print("2 - Top 5 dārgākās grāmatas")
            izvele2 = input("Izvēle: ")

            if izvele2 == "1":
                library.top_5_popular()
            elif izvele2 == "2":
                library.top_5_expensive()
            else:
                print("Kļūda! Ievadiet skaitli no 1 līdz 2")


        elif izvele == "6":
            print("Uz redzēšanos!")
            break
        else:
            print("Kļūda! Ievadiet skaitli no 1 līdz 6")

if __name__ == "__main__":
    main()
