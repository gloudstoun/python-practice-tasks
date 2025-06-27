class Book:

    def __init__(self, title, author, isbn):
        '''
        Наш конструктор. Инициализируем атрибуты экземпляра
        и добавляем атрибут для проверки доступности книги.
        '''
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True

    def display_book_info(self):
        '''
        Вывожу информацию о книге и проверяю ее доступность
        '''
        status = "Да" if self.is_available else "Нет"
        print(f"Название: {self.title}, Автор: {self.author}, ISBN: {self.isbn}. Доступна: {status}")

class Library:

    def __init__(self, name):
        '''
        Конструктор второго класса, инициализирует атрибут экземпляра(имя библиотеки) и список объектов(книг)
        '''
        self.name = name
        self.books = [] # Список для хранения объектов Book

    def add_book(self, book_object):
        '''
        Добавляю объект класса Book в инициализированный список объектов класса Library
        '''
        self.books.append(book_object) # Добавляю элемент в конец списка self.books

        print(f"Книга '{book_object.title}' добавлена в библиотеку '{self.name}'.")

    def list_all_books(self):
        """
        Выводит список всех книг в библиотеке.
        """
        print(f"\n--- Книги в библиотеке '{self.name}': ---")
        if not self.books:
            print("В библиотеке пока нет книг.")
        else:
            for book in self.books:
                book.display_book_info()

    def borrow_book(self, isbn_to_borrow):
        for book in self.books:
            if book.isbn == isbn_to_borrow:
                if book.is_available:
                    book.is_available = False
                    print(f"Книга '{book.title}' успешно выдана.")
                    return True  
                else:
                    print(f"Книга '{book.title}' сейчас недоступна.")
                    return False
        print(f"Книга с ISBN {isbn_to_borrow} не найдена в библиотеке.")
        return False
    
    def return_book(self, isbn_to_return):
        for book in self.books:
            if book.isbn == isbn_to_return:
                if not book.is_available:
                    book.is_available = True
                    print(f"Книга '{book.title}' успешно возвращена.")
                    return True
                else:
                    print(f"Книга '{book.title}' уже доступна в библиотеке.")
                    return False
        print(f"Книга с ISBN {isbn_to_return} не найдена в библиотеке.")
        return False
    
    def search_book(self, query): # query (строка - это может быть часть названия или имя автора).
        found_books = []
        for book in self.books:
            if query.lower() in book.title.lower() or query.lower() in book.author.lower():
                found_books.append(book)
        if found_books: # Нужно пройтись по каждой найденной книге и вывести ее информацию
            print( "\n--- Найденные книги: ---")
            for found_book in found_books:  # Новый цикл по найденным книгам
                found_book.display_book_info() # Вызываем display_book_info для каждой из них
            return found_books
        else:
            print(f"Книги по запросу '{query}' не найдены.")
            return []

#ДОБАВЛЕНИЕ ОБЪЕКТОВ
            
book1 = Book("Война и мир", "Лев Толстой", "978-5389088656")
book2 = Book("Мастер и Маргарита", "Михаил Булгаков", "978-5699708764")
book3 = Book("Преступление и наказание", "Федор Достоевский", "978-5171120251")
my_library = Library("Центральная городская библиотека")

my_library.add_book(book1)
my_library.add_book(book2)
my_library.add_book(book3)

#ПРОВЕРКИ РАБОТЫ МЕТОДОВ

print("\n--- Пробуем взять доступную книгу ---")
is_borrow_successful = my_library.borrow_book("978-5389088656")
if is_borrow_successful:
    print("Внешний код: Операция borrow_book завершилась УСПЕШНО.")
else:
    print("Внешний код: Операция borrow_book завершилась НЕУДАЧНО.")

print("\n--- Пробуем взять ту же книгу снова (недоступна) ---")
is_borrow_successful_again = my_library.borrow_book("978-5389088656")
if is_borrow_successful_again:
    print("Внешний код: Операция borrow_book завершилась УСПЕШНО.")
else:
    print("Внешний код: Операция borrow_book завершилась НЕУДАЧНО.")

print("\n--- Пробуем взять несуществующую книгу ---")
is_borrow_successful_nonexistent = my_library.borrow_book("НЕ-СУЩЕСТВУЮЩИЙ-ISBN")
if is_borrow_successful_nonexistent:
    print("Внешний код: Операция borrow_book завершилась УСПЕШНО.")
else:
    print("Внешний код: Операция borrow_book завершилась НЕУДАЧНО.")

print("\n--- Пробуем вернуть осутствующую книгу ---")
is_return_book_successful = my_library.return_book("978-5389088656")

print("\n--- Пробуем вернуть книгу в наличии  ---")
is_return_book_successful_again = my_library.return_book("978-5389088656")

print("\n--- Пробуем найти книги по запросу 'мир' ---")
my_library.search_book("мир")

print("\n--- Пробуем найти книги по запросу 'достоевский' ---")
my_library.search_book("достоевский")

print("\n--- Пробуем найти книги по запросу 'несуществующий' ---")
my_library.search_book("несуществующий")

my_library.list_all_books() # Должно вывести информацию о book1, book2 и book3