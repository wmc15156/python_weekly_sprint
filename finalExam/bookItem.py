from book import Book


class BookItem(Book):
    bookItemIsbn = 0

    @staticmethod
    def generateISBN() -> int:
        """
        bookItemIsbn을 1을 올려주고 반환한다.
        :return: 책고유 번호
        """
        BookItem.bookItemIsbn += 1
        return BookItem.bookItemIsbn

    def __init__(self, author, country, imageLink, language, link, pages, title, year):
        super().__init__(author, country, imageLink, language, link, pages, title, year)
        self.ISBN = BookItem.generateISBN()

    def isSearchedISBN(self, isbn: int) -> bool:
        """
        입력된 isbn이 클래스의 ISBN과 같으면 True 아니면 False를 반환
        :param isbn: 책고유번호
        :return: 고유번호 일치여부 반환
        """
        is_isbn: bool = False
        if isbn == self.ISBN:
            is_isbn = True
        return is_isbn