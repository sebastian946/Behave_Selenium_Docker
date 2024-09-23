from faker import Faker


class GenerateData:
    def __init__(self):
        self.faker = Faker()

    def generateFirstName(self):
        return self.faker.first_name()

    def generateLastName(self):
        return self.faker.last_name()

    def generateEmail(self):
        return self.faker.email()

    def generatePhone(self):
        return self.faker.phone_number()

    def generatePassword(self):
        return self.faker.password(9,True,True,True,True)

    def generateCompany(self):
        return self.faker.company()

    def generateCity(self):
        return self.faker.city()

    def generateAddress(self):
        return self.faker.address()

    def generatePostalCode(self):
        return self.faker.old_postal_code()

    def generateText(self):
        return "Comment generate"