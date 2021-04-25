from faker import Faker
import random
from randomize import Randomize
from generate import Generate


fake = Faker(['es_ES'])


class BankAccount:
    def __init__(self):
        self.rut = Generate.rut()
        self.first_name = fake.first_name()
        self.second_name = random.choice([fake.first_name(), ''])
        self.last_name = fake.last_name()
        self.second_surname = random.choice([fake.last_name(), ''])
        self.bank_name = Generate.bank_name()
        self.bank_account_type = Generate.account_type()
        self.mail = fake.email()
        self.bank_account_number = Generate.account_number(
            self.bank_account_type, self.rut)

    @property
    def full_name(self) -> str:
        full_name = self.first_name + ' '
        full_name += self.second_name + ' ' if self.second_name else ''
        full_name += self.last_name
        full_name += self.second_surname + ' ' if self.second_surname else ''
        return full_name

    def randomize_bank_account(self) -> str:
        data = []
        data.append(Randomize.rut(self.rut))
        data.append(Randomize.account_number(self.bank_account_number))
        data.append(Randomize.name(self.first_name, self.second_name,
                    self.last_name, self.second_surname, self.full_name))
        data.append(fake.text())
        data += Randomize.bank(self.bank_name, self.bank_account_type)
        random.shuffle(data)
        return ''.join(data)

    def __str__(self):
        return """rut: {}, name: {}, bank_name: {}, bank_account_type: {}, mail: {}, bank_account_number: {}""".format(
            self.rut,
            self.full_name,
            self.bank_name,
            self.bank_account_type,
            self.mail,
            self.bank_account_number
        )


if __name__ == '__main__':
    bank_account = BankAccount()
    print(bank_account)
    print(bank_account.randomize_bank_account())
