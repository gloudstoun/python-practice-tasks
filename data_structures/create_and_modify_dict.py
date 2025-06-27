def create_and_modify_dict():
    phone_book = {"Анна": "123-4567", "Борис": "987-6543", "Виктор": "555-1212"}
    phone_book["Анна"] = "111-2233"
    phone_book["Галина"] = "777-8899"
    del phone_book["Борис"]
    
    print(phone_book)
    return phone_book["Виктор"]

final_book_state = create_and_modify_dict()
print(f"\nНомер Виктора из функции: {final_book_state}")