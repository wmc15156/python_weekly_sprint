from catalog import Catalog
from loanAdministrator import LoanAdministration
from customer import Customer

import pickle


class PublicLibrary():
    def __init__(self):
        self.catalog = Catalog()
        self.catalog.initBooks()
        self.loanAdministration = LoanAdministration(self.catalog)
        self.loanAdministration.initCustomers()
        print(self)

    def makeBackup(self, namefile: str):
        """
        파일명을 입력받으면 PublicLibrary 객체를 저장
        pickle을 이용
        :param namefile: 저장할 파일 이름
        :return:x
        """
        with open(namefile, 'wb') as f:
            pickle.dump(self, f, pickle.HIGHEST_PROTOCOL)

    def restoreBackup(self, name: str):
        """
        입력 파라미터를 pickle로 불러오는 기능
        :param name: 불러올 파일 이름
        :return:
        """

        with open(name, 'rb') as f:
            data = pickle.load(f)
            print(data)


if __name__ == "__main__":
    print("도서관 초기화...")
    library = PublicLibrary()
    print("공공도서관 시스템 입니다.!")

    print("첫번째 고객 'Valentin' 불러오기")
    customer = library.loanAdministration.customers[3]  # customer.csv 내의 4번째 고객 참고
    print("The Book Of Job 책 찾기!")
    library.catalog.isSearchedBook("The Book Of Job")
    print("'The Book Of Job'을 빌릴 수 있는지 확인합니다.")
    library.catalog.checkAvailability("The Book Of Job")
    print("책 제목은 모르고 ISBN '2'를 검색하여 빌릴 수 있는지 확인합니다. ")
    library.catalog.checkAvailability("2")

    # 9번째 책을 빌리고자 합니다.
    the_book_of_job = library.catalog.bookItems[8]
    print("Valentin이 지금까지 빌린 책을 살펴 보겠습니다.")
    library.loanAdministration.borrowBook(customer, the_book_of_job)

    customer.getBorrowedBooks()

    library.catalog.checkAvailability("The Book Of Job")

    # 1번째 book items리스트에서 책 가져오기
    things_fall_apart = library.catalog.bookItems[1]
    library.loanAdministration.borrowBook(customer, things_fall_apart)
    # 'Things Fall Apart'
    library.catalog.checkAvailability("Things Fall Apart")
    # 'The End Of Times'
    library.catalog.checkAvailability("The End Of Times")
    print("책 넣기")
    library.catalog.addBook("Hamza Fethi", "Netherlands", "images/times-end.jpg", "Dutch",
                            "https://en.wikipedia.org/wiki/Fairy_Tales_Told_for_Children._First_Collection.\n", 433,
                            "The End Of Times", 1750)
    library.catalog.addBookItem("Hamza Fethi", "Netherlands", "images/times-end.jpg", "Dutch",
                                "https://en.wikipedia.org/wiki/Fairy_Tales_Told_for_Children._First_Collection.\n", 433,
                                "The End Of Times", 1750)
    # 책 찾아보기
    library.catalog.checkAvailability("The End Of Times")

    # Customer 등록
    # "'Gary Veulen'을 새로운 고객으로 등록
    new_customer = Customer("male", "Dutch", "Gary", "Veulen", "Palisanderstraat 43", "3031 CG", "Rotterdam",
                            "garyveulen1998@gmail.com", "GaryVeulen", "06-84211309")
    library.loanAdministration.addCustomer(new_customer)

    # 책 'The Book Of Job'이 빌린 상태인지 확인
    library.catalog.checkAvailability("The Book Of Job")

    # 7번째 BookItems가져와서 빌려보기
    the_book_of_job_second = library.catalog.bookItems[7]
    library.loanAdministration.borrowBook(new_customer, the_book_of_job_second)
    library.catalog.checkAvailability("The Book Of Job")

    # 백업
    library.makeBackup("backup_first")

