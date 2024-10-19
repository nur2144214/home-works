class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        self.read = False

    def mark_as_read(self):
        self.read = True

    def mark_as_unread(self):
        self.read = False

    def __str__(self):
        status = "Прочитана" if self.read else "Не прочитана"
        return f"'{self.title}' от {self.author} ({self.year}) - {status}"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def list_books(self):
        for book in self.books:
            print(book)

    def find_by_title(self, title):
        found_books = [book for book in self.books if book.title.lower() == title.lower()]
        return found_books

    def find_by_author(self, author):
        found_books = [book for book in self.books if book.author.lower() == author.lower()]
        return found_books

    def mark_book_as_read(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                book.mark_as_read()
                return f"Книга '{title}' отмечена как прочитанная."
        return f"Книга '{title}' не найдена."

    def remove_book(self, title):
        self.books = [book for book in self.books if book.title.lower() != title.lower()]

    def filter_books(self, read_status):
        return [book for book in self.books if book.read == read_status]

    def sort_books_by_year(self):
        self.books.sort(key=lambda book: book.year)



def commands():
    library = Library()

    while True:
        try:
            print("\nДобро пожаловать в библиотеку!")
            print("1. Добавить книгу")
            print("2. Просмотреть список книг")
            print("3. Найти книгу по названию")
            print("4. Найти книгу по автору")
            print("5. Отметить книгу как прочитанную")
            print("6. Удалить книгу")
            print("7. Фильтрация книг по статусу")
            print("8. Сортировка книг по году публикации")
            print("9. Выход")

            choice = input("Выберите действие: ")

            if choice == '1':
                title = input("Введите название книги: ")
                author = input("Введите автора книги: ")
                year = int(input("Введите год публикации книги: "))
                book = Book(title, author, year)
                library.add_book(book)
                print(f"Книга '{title}' добавлена в библиотеку.")

            elif choice == '2':
                library.list_books()

            elif choice == '3':
                title = input("Введите название книги: ")
                found_books = library.find_by_title(title)
                if found_books:
                    for book in found_books:
                        print(book)
                else:
                    print("Книга не найдена.")

            elif choice == '4':
                author = input("Введите автора книги: ")
                found_books = library.find_by_author(author)
                if found_books:
                    for book in found_books:
                        print(book)
                else:
                    print("Книги не найдены.")

            elif choice == '5':
                title = input("Введите название книги: ")
                result = library.mark_book_as_read(title)
                print(result)

            elif choice == '6':
                title = input("Введите название книги: ")
                library.remove_book(title)
                print(f"Книга '{title}' удалена из библиотеки.")

            elif choice == '7':
                status = input("Показать только прочитанные книги? (да/нет): ").lower() == 'да'
                filtered_books = library.filter_books(status)
                for book in filtered_books:
                    print(book)

            elif choice == '8':
                library.sort_books_by_year()
                print("Книги отсортированы по году публикации.")
                library.list_books()

            elif choice == '9':
                print("Выход из программы. До свидания!")
                break

            else:
                print("Неверный выбор. Пожалуйста, выберите снова.")

        except Exception as e:
            print(f"Произошла ошибка: {e}")



commands()

