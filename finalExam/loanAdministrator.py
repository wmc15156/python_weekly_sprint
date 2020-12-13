from customer import Customer
from loanItem import LoanItem

import csv

class LoanAdministration():
    def __init__(self, catalog):
        self.loanItems = []
        self.customers = []
        self.catalog = catalog

    def addCustomer(self, customer):

        """
        입력받은 Customer Class를 self.customers에 저장하고
        해당  정보를 customer.csv파일에 추가
        :param customer: Customer class
        :return:
        """
        # Customer("male", "Dutch", "Gary", "Veulen", "Palisanderstraat 43", "3031 CG", "Rotterdam", "garyveulen1998@gmail.com", "GaryVeulen", "06-84211309")

        self.customers.append(Customer(customer.gender, customer.nameSet, customer.givenName, customer.surName,
                                       customer.adress, customer.zipCode, customer.city, customer.email,
                                       customer.userName, customer.phoneNumber))

        f = open("customers.csv", "a", newline="")

        wr = csv.writer(f)
        wr.writerow([customer.id, customer.gender, customer.nameSet, customer.givenName, customer.surName,
                     customer.adress, customer.zipCode, customer.city, customer.email, customer.userName,
                     customer.phoneNumber])
        f.close()

    def borrowBook(self, customer, bookitem):
        # pass
        # the_book_of_job = library.catalog.bookItems[8]
        # library.loanAdministration.borrowBook(customer, the_book_of_job)
        # self.catalog.bookItems
        # customer = library.loanAdministration.customers[3]
        """
        입력 파라미터로 들어온 bookitem을 멤버변수 catalog내의 햔재 책 항목리스트인
        bookitems내의 bookitem을 지우고 멤버변수 customers를 입력 파라미터 customer를 찾은
        뒤에 LoanItem으로 바꾸어 다시 cutomers의 addBook을 이용하여 넣기

        :param customer: Customer class
        :param bookitem: BookItem Class
        :return: 반환없음
        """
        for value in self.catalog.bookItems:
            if value.title == bookitem.title:
                self.catalog.bookItems.remove(value)

        for v in self.customers:
            if v.email == customer.email:

                self.catalog.addBook(bookitem.author[0].getFullName(), bookitem.country, bookitem.imageLink, bookitem.language,
                                     bookitem.link, bookitem.pages, bookitem.title, bookitem.year)

                self.loanItems.append(LoanItem(bookitem.author[0].getFullName(), bookitem.country, bookitem.imageLink, bookitem.language, bookitem.link,
                         bookitem.pages, bookitem.title, bookitem.year))

        print(f"고객{customer.userName}는 {bookitem.title}을 빌렸습니다.")

    def initCustomers(self):
        """
        customers 배열에 고객정보 넣기
        :return:
        """
        count = 0
        f = open('customers.csv', 'r')
        rdr = csv.reader(f)

        for _, value in enumerate(rdr):
            count += 1

            self.customers.append(
                Customer(value[1], value[2], value[3], value[4], value[5], value[6], value[7], value[8], value[9], value[10]))
        f.close()

        print(f'총 {count}명의 고객들을 읽었습니다.')