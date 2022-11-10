class library:

    def __int__(self, name, author, publishing, genre):
        self.__name = name
        self.__author = author
        self.__publishing = publishing
        self.__genre = genre


    def __str__(self):
        return f"книги: {self.__name}\n" \
               f"автор: {self.__author}\n" \
               f"издательство: {self.__publishing}\n" \
               f"жанр: {self.__genre}\n" \



name = str(input("Введите название вашей книги: "))

author = str(input("Введите автора вашей книги: "))

publishing = str(input("Введите издательство: "))

genre = str(input("Введите жанр: "))


book1 = library(name, author, publishing, genre)
