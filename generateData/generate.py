import random
from faker import Faker
from rut_chile import rut_chile
from constants import RUT_LOWER_RANGE, RUT_UPPER_RANGE, ACCOUNT_NUMBER_LOWER_RANGE, ACCOUNT_NUMBER_UPPER_RANGE, BANK_NAMES, ACCOUNT_TYPES, BOOLEANS


class Generate:
    @staticmethod
    def rut(with_dots=False) -> str:
        rut_number = str(random.randint(RUT_LOWER_RANGE, RUT_UPPER_RANGE))
        verificatior_digit = rut_chile.get_verification_digit(rut_number)
        return rut_chile.format_rut('{}{}'.format(rut_number, verificatior_digit), with_dots=with_dots)

    @staticmethod
    def account_number(account_type: str, rut: str) -> str:
        if account_type == 'Cuenta rut':
            display = random.choice(BOOLEANS)
            if display:
                return rut[:-2]
            else:
                return ''
        return str(random.randint(ACCOUNT_NUMBER_LOWER_RANGE, ACCOUNT_NUMBER_UPPER_RANGE))

    @staticmethod
    def bank_name() -> str:
        return random.choice(BANK_NAMES)

    @staticmethod
    def account_type() -> str:
        return random.choice(ACCOUNT_TYPES)
