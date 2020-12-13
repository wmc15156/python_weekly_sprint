from person import Person

class Author(Person):
    def __init__(self, givenName, surName='N/A', gender='N/A', nameSet='N/A', adress='N/A', zipCode='N/A', city='N/A',
                 email='N/A', userName='N/A', phoneNumber='N/A'):
        super().__init__(gender, nameSet, givenName, surName, adress, zipCode, city, email, userName, phoneNumber)

    def getFullName(self) -> str:
        return f'{self.givenName} {self.surName}'
