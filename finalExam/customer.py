from person import Person
from book import Book


class Customer(Person):
    personId = 0

    @staticmethod
    def generateIdentification():
        """
        :return: personId를 1증가 시키고 반환
        """
        Customer.personId += 1
        return Customer.personId

    def __init__(self, gender, nameSet, givenName, surName, adress, zipCode, city, email, userName, phoneNumber, books=[]):

        super().__init__(gender, nameSet, givenName, surName, adress, zipCode, city, email, userName, phoneNumber)
        self.id = Customer.generateIdentification()
        self.books = books

    def getName(self):
        """
        고객이름 반환
        :return: 고객이름
        """
        return self.givenName

    def getBorrowedBooks(self):
        """
        책 반환을 출력
        :return:
        """

        customer_name = self.getName()
        print(f"유저 {customer_name}의 반환목록은 다음과 같습니다.")
        for i, v in enumerate(self.books):
            print(v["title"])

    def addBook(self, book):
        """
        책의 정보를 추가합니다.
        :param book: 책의 정보
        :return:
        """
        self.books.append(Book(book[0], book[1], book[2], book[3], book[4], book[5], book[6], book[7]))