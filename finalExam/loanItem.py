from bookItem import BookItem


class LoanItem(BookItem):
    def __init__(self, author, country, imageLink, language, link, pages, title, year):
        super().__init__(author, country, imageLink, language, link, pages, title, year)