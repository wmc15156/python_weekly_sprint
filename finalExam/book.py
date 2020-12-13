from author import Author

import json


class Book():
    def __init__(self, author, country, imageLink, language, link, pages, title, year):
        self.author = []
        self.author.append(Author(author))
        self.country = country
        self.imageLink = imageLink
        self.language = language
        self.link = link
        self.pages = pages
        self.title = title
        self.year = year

    def getTitle(self) -> str:
        """
        책의 제목을 반환한다.
        :return: 책의 제목
        """
        return self.title

    def isSearchedBook(self, titleLookup: str) -> bool:
        """
        입력의로 받은 titleLookup이 book.json이 있는지 판별 후 true/false반환
        :param titleLookup: 찾을 책의 제목
        :return: true, false반환
        """

        is_true = False
        with open("bookset.json") as f:
            json_data = json.load(f)

            for _, value in enumerate(json_data):
                if titleLookup == value['title']:
                    is_true = True

        return is_true

    def isSearchedAuthor(self, input: str) -> bool:
        """
        저자리스트 내의 이름이 책 항목 중 하나와 일치하면 True, False반환
        :param input: 작가이름
        :return: 존재여부 true , false 반환
        """

        is_true = False

        with open("bookset.json") as f:
            json_data = json.load(f)
            for _, value in enumerate(json_data):
                if value["author"] == input:
                    is_true = True

        return is_true
