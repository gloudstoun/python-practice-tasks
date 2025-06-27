import abc
import datetime

class Book(abc.ABC):
    def __init__(self, title, author, isbn, publication_year, initial_rating_value): # publication_year (год издания, целое число), initial_rating_value (начальное значение рейтинга)
        self.publication_year = publication_year
        self.title = title
        self._rating = Rating(initial_rating_value)
        self.author = author
        self.isbn = isbn
        self.is_available = True

    @property
    def rating(self):
        return self._rating
    
    @rating.setter
    def rating(self, new_rating_value):
        self._rating.value = new_rating_value

    @property
    def title(self):
        #print(f"--- Вызван ГЕТТЕР для Title: {self.author}")
        return self._title
    
    @title.setter
    def title(self, new_title):
        #print(f"--- Вызван СЕТТЕР для Title: {new_title}")
        if not new_title or not isinstance(new_title, str) or new_title.strip() == "":
            raise ValueError("Название книги не может быть пустым или состоять только из пробелов.")
        self._title = new_title

    @property
    def publication_year(self):
        #print(f"--- Вызван ГЕТТЕР для PublicationYear: {self.author}")
        return self._publication_year
    
    @publication_year.setter
    def publication_year(self, year):
        current_year = datetime.date.today().year
        #print(f"--- Вызван СЕТТЕР для Publication Year: {year}")
        if not isinstance(year, int):
            raise ValueError("Год издания должен быть целым числом.")
        if not (1000 <= year <= current_year + 5): 
            raise ValueError(f"Год издания должен быть в диапазоне от 1000 до {current_year + 5}.")
        self._publication_year = year

    def __gt__(self, other):
        if self.publication_year > other.publication_year:
            return True

    def borrow(self):
        if self.is_available:
            self.is_available = False
            print(f"Книга '{self.title}' взята.")
        else:
            print(f"Книга '{self.title}' уже выдана.")

    def return_book(self):
        if not self.is_available:
            self.is_available = True
            print(f"Книга '{self.title}' успешно возвращена.")
        else:
            print(f"Книга '{self.title}' уже на месте.")

    @abc.abstractmethod
    def display_info(self):
        pass

    def to_dict(self):
        return {
            'title': self.title, # Используем свойство title
            'author': self.author,
            'isbn': self.isbn,
            'publication_year': self.publication_year, # Используем свойство publication_year
            'is_available': self.is_available, # Это обычный атрибут, его можно брать напрямую
            'rating': self.rating.to_dict() # Вызываем to_dict у объекта Rating, полученного через свойство rating
        } 

class Magazine(Book):
    def __init__(self, title, author, isbn, issue_number, publication_year, initial_rating_value): # issue_number (номер выпуска, целое число)
        super().__init__(title, author, isbn, publication_year, initial_rating_value)
        self.issue_number = issue_number

    def display_info(self):
        status = "Да" if self.is_available else "Нет"
        print(f"Название: '{self.title}', Автор: {self.author}, ISBN: {self.isbn}, год выпуска: {self.publication_year}, номер выпуска журнала: {self.issue_number}. Доступна: {status}")
        self.rating.display_rating()

    def to_dict(self):
        book_data = super().to_dict() # Получаем словарь от родительского класса Book
        book_data['issue_number'] = self.issue_number # Добавляем специфичный для Magazine атрибут
        book_data['type'] = 'Magazine' # Добавляем тип для корректной загрузки
        return book_data
    
    @classmethod
    def from_dict(cls, data):
        # Метод класса для создания объекта Magazine из словаря
        return cls(data['title'], data['author'], data['isbn'], data['issue_number'], 
                   data['publication_year'], data['rating']['value'])

class AudioBook(Book):
    def __init__(self, title, author, isbn, duration_minutes, publication_year, initial_rating_value): # duration_minutes (продолжительность в минутах, целое число)
        super().__init__(title, author, isbn, publication_year, initial_rating_value)
        self.duration_minutes = duration_minutes

    def display_info(self):
        status = "Да" if self.is_available else "Нет"
        print(f"Название: '{self.title}', Автор: {self.author}, ISBN: {self.isbn}, год выпуска: {self.publication_year}, продолжительность аудиокниги составляет {self.duration_minutes} мин. Доступна: {status}")
        self.rating.display_rating()

    def to_dict(self):
        book_data = super().to_dict() # Получаем словарь от родительского класса Book
        book_data['duration_minutes'] = self.duration_minutes # Добавляем специфичный для AudioBook атрибут
        book_data['type'] = 'AudioBook' # Добавляем тип для корректной загрузки
        return book_data
    
    @classmethod
    def from_dict(cls, data):
        # Метод класса для создания объекта AudioBook из словаря
        return cls(data['title'], data['author'], data['isbn'], data['duration_minutes'], 
                   data['publication_year'], data['rating']['value'])

class Rating:
    def __init__(self, initial_value ): # атрибут initial_value (целое число, это наш рейтинг)
        self.value = initial_value 

    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, new_rating_value):
        if not isinstance(new_rating_value, int): 
            raise ValueError("Рейтинг должен быть целым числом.")
        if not (1 <= new_rating_value <= 5): 
            raise ValueError("Рейтинг должен быть в диапазоне от 1 до 5.")
        self._value = new_rating_value
    
    def display_rating(self):
        print(f"Рейтинг: {self.value}/5")

    def to_dict(self):
        return {'value': self.value}

class Library:
    def __init__(self, name):
        self.books = []
        self.name = name

    def add_book(self, book_object):
        for book in self.books:
            if book.isbn == book_object.isbn:
                print(f"Книга '{book_object.title}' с ISBN '{book_object.isbn}' уже есть в наличии в {self.name}.")
                return
        self.books.append(book_object)
        print(f"Книга '{book_object.title}' с ISBN '{book_object.isbn}' успешно добавлена в {self.name}.")

    def remove_book(self, isbn_to_remove):
        found_book = None
        for book in self.books:
            if book.isbn == isbn_to_remove:
                found_book = book
                break
        if found_book:
            self.books.remove(found_book)
            print(f"Книга '{found_book.title}' с ISBN '{isbn_to_remove}' изъята из наличия в {self.name}.")
        else:
            print(f"Книга с ISBN '{isbn_to_remove}' не найдена в библиотеке {self.name}.")

    def find_book(self, query):
        found_books = []
        for book in self.books:
            if query.lower() in book.title.lower() or query.lower() in book.author.lower() or query in book.isbn:
                found_books.append(book)
        
        if found_books:
            print(f"\n--- Найденные книги по запросу '{query}' в {self.name}: ---")
            for found_book in found_books:
                found_book.display_info()
            return found_books
        else:
            print(f"Книги по запросу '{query}' в {self.name} не найдены.")
            return []

    def display_all_books(self):
        print(f"\n--- Список книг в библеотеке {self.name}: ---")
        if not self.books:
            print(f"В библиотеке {self.name} пока нет книг.")
        else:
            for book in self.books:
                book.display_info()

    def save_to_file(self, filename):
        pass

#ПРОВЕРКИ РАБОТЫ МЕТОДОВ
my_library = Library("Городская библиотека")
magazine1 = None 
audio_book1 = None

try:
    magazine1 = Magazine("Осенний журнал", "Вива", "678-5386732656", 5, 2025, 4) 
except ValueError as e:
    print(f"Ошибка при создании журнала: {e}")

try:
    audio_book1 = AudioBook("Анна Каренина", "Лев Толстой", "978-5389154656", 60, 1995, 3)
except ValueError as e:
    print(f"Ошибка при создании аудиокниги: {e}")

if magazine1:
    try:
        my_library.add_book(magazine1)
    except Exception as e: 
        print(f"Ошибка при добавлении журнала в библиотеку: {e}")

if audio_book1:
    try:
        my_library.add_book(audio_book1)
    except Exception as e:
        print(f"Ошибка при добавлении аудиокниги в библиотеку: {e}")

my_library.display_all_books()

