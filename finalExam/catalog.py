from book import Book
from bookItem import BookItem

import json


class Catalog(Book):
    def __init__(self):
        self.books = []
        self.bookItems = []
        self.index = {}

    def checkAvailability(self, input: str=None):
        """
        제목 또는 저자 이름으로 제공되는 책을 화면에 모두 출력 할 것
        :param input: 책의 제목이나 저자이름
        :return: 없음
        """
        if input == None:
            print("No Book Found")

        if self.isSearchedBook(input):
            for value in self.bookItems:
                if value.title == input:
                    print(f'{value.title} 존재합니다.')

        if self.isSearchedAuthor(input):
            for value in self.bookItems:
               if value[0].username == input:
                   print(f'{value[0].username} 존재합니다.')


    def addBook(self, author, country, imageLink, language, link, pages, title, year):


        """
        books리스트에 Book클래스로 추가하고 bookset.json에 추가로 저장할것
        :param author:
        :param country:
        :param imageLink:
        :param language:
        :param link:
        :param pages:
        :param title:
        :param year:
        :return:
        """
        self.books.append(Book(author, country, imageLink, language, link, pages, title, year))
        json_data = []
        obj = {"author": author, "country": country, "imageLink": imageLink, "language": language, "link": link,
               "pages": pages, "title": title, "year": year}

        with open('bookset.json') as f:
            json_data = json.load(f)
        json_data.append(obj)

        with open('bookset.json', 'w') as f:
            json.dump(json_data, f)
        print(f'성공적으로 책제목: {obj["title"]}을 저장하였습니다.')

    def addBookItem(self, author, country, imageLink, language, link, pages, title, year):
        """
        새로운 책을 bookItems리스트에 넣는변수
        :param author:
        :param country:
        :param imageLink:
        :param language:
        :param link:
        :param pages:
        :param title:
        :param year:
        :return:
        """
        self.bookItems.append(BookItem(author, country, imageLink, language, link, pages, title, year))

    def initBooks(self):
        """
        books.json파일을 parsing 하여 해당 값들을 books
        :return: x
        """
        with open("bookset.json") as f:
            json_data = json.load(f)

            for _, v in enumerate(json_data):
                self.books.append(Book(v["author"], v["country"], v["imageLink"], v["language"], v["link"],
                                       v["pages"], v["title"], v["year"]))
                self.bookItems.append(BookItem(v["author"], v["country"], v["imageLink"], v["language"],
                                               v["link"], v["pages"], v["title"], v["year"]))
        f.close()