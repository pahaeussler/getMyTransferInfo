import random
from faker import Faker
from rut_chile import rut_chile
from constants import RUT_MESSAGES, NAMES_OPTIONS, ACCOUNT_NUMBER_MESSAGES, BANK_OPTIONS, BANK_NAME_MESSAGES, ACCOUNT_TYPES_MESSAGES, ACCOUNT_TYPES_CARACTERS, BOOLEANS, END_LINE


class Randomize:
    @staticmethod
    def message(array: list, value: str) -> str:
        message = random.choice(array)
        if message:
            message += random.choice([': ', ' '])
        message += value
        message += Randomize.end_line()
        return message

    @staticmethod
    def end_line() -> str:
        return random.choice(END_LINE)

    @staticmethod
    def bank(bank_name, bank_account_type) -> list:
        data = []
        option = random.choice(BANK_OPTIONS)
        if option == 'name-type':
            data.append(
                f'{bank_account_type}: {bank_name} {Randomize.end_line()}')
            return data
        data.append(Randomize.message(BANK_NAME_MESSAGES, bank_name))
        data.append(Randomize.message(
            ACCOUNT_TYPES_MESSAGES, bank_account_type))
        return data

    @staticmethod
    def account_number(account_number: str) -> str:
        caracter = random.choice(ACCOUNT_TYPES_CARACTERS)
        i = 0
        while caracter and i < 3:
            pos = random.randint(0, len(account_number))
            account_number = f'{account_number[:pos]} {caracter} {account_number[pos:]}'
            caracter = random.choice(ACCOUNT_TYPES_CARACTERS)
            i += 1
        return Randomize.message(ACCOUNT_NUMBER_MESSAGES, account_number)

    @staticmethod
    def rut(rut: str) -> str:
        rut = rut_chile.format_rut(
            rut, with_dots=random.choice(BOOLEANS))
        return Randomize.message(RUT_MESSAGES, rut)

    @staticmethod
    def name(first_name: str, second_name: str, last_name: str, second_surname: str, full_name: str) -> str:
        option = random.choice(NAMES_OPTIONS)
        if option == 'name/lastname':
            message = Randomize.message(
                ['', 'nombre'], f'{first_name} {second_name}')
            message += Randomize.message(['', 'apellido'],
                                         f'{last_name} {second_surname}')
            return message
        return Randomize.message(['', 'nombre'], full_name)


if __name__ == '__main__':
    pass
