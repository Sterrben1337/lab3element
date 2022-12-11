from enum import Enum
from typing import List
import math


class Account(Enum):
    usd = 'USD'
    eur = 'EUR'
    rub = 'RUB'
    kzt = 'KZT'

class BankAccount:
    def __init__(self, name, surname, account=Account.kzt, balance=0):
        self.name = name
        self.surname = surname
        self.account = account
        self.balance = balance

    def get_balance(self):
        print(f'Your balance: {round(self.balance, 2)} {self.account.value}')

    def money_conversion(self, amount, currency):
        current_wallet_type = self.account.value
        if current_wallet_type == 'KZT':
            if currency == 'KZT':
                return amount
            elif currency == 'RUB':
                return amount * 7.57
            elif currency == 'USD':
                return amount * 472.24
            elif currency == 'EUR':
                return amount * 498.42
        elif current_wallet_type == 'RUB':
            if currency == 'KZT':
                return amount * 0.13
            elif currency == 'RUB':
                return amount
            elif currency == 'USD':
                return amount * 62.38
            elif currency == 'EUR':
                return amount * 65.84
        elif current_wallet_type == 'EUR':
            if currency == 'KZT':
                return amount * 0.002
            elif currency == 'RUB':
                return amount * 0.015
            elif currency == 'USD':
                return amount * 0.95
            elif currency == 'EUR':
                return amount
        elif current_wallet_type == 'USD':
            if currency == 'KZT':
                return amount * 0.0021
            elif currency == 'RUB':
                return amount * 0.016
            elif currency == 'USD':
                return amount
            elif currency == 'EUR':
                return amount * 1.05

    def get_account(self):
        print(f'Account: {self.name} {self.surname} - {self.account.value}')

    def add_to_bank_account(self, amount, currency):
        self.balance += self.money_conversion(amount, currency)
        print(f'Account {self.name} {self.surname} has been replenished by the  {amount} {currency}')
        self.get_balance()

    def subtract_from_bank_account(self, amount, currency):
        self.balance -= self.money_conversion(amount, currency)
        print(f'You have withdrawn money from an ATM in the amount of {amount} {currency}')
        self.get_balance()

    def set_balance(self, currency):
        current_balance = self.balance
        current_wallet_type = self.account.value
        if current_wallet_type == 'KZT':
            if currency == 'KZT':
                return current_balance
            elif currency == 'RUB':
                return current_balance / 7.63
            elif currency == 'USD':
                return current_balance / 473.25
            elif currency == 'EUR':
                return current_balance / 497.76
        elif current_wallet_type == 'RUB':
            if currency == 'KZT':
                return current_balance / 0.13
            elif currency == 'RUB':
                return current_balance
            elif currency == 'USD':
                return current_balance / 62
            elif currency == 'EUR':
                return current_balance / 65.21
        elif current_wallet_type == 'EUR':
            if currency == 'KZT':
                return current_balance / 0.002
            elif currency == 'RUB':
                return current_balance / 0.015
            elif currency == 'USD':
                return current_balance / 0.95
            elif currency == 'EUR':
                return current_balance
        elif current_wallet_type == 'USD':
            if currency == 'KZT':
                return current_balance / 0.0021
            elif currency == 'RUB':
                return current_balance / 0.016
            elif currency == 'USD':
                return current_balance
            elif currency == 'EUR':
                return current_balance / 1.05

    def set_account(self, currency):
        self.balance = self.set_balance(currency)
        for a in Account:
            if a.value == currency:
                self.account = a
        print(f'\nAccount {self.name} {self.surname} was changed!')
        print(f'Account {self.name} {self.surname} - {self.account.value}')
        self.get_balance()

    def __del__(self):
        print(f'Account {self.name} {self.surname} was removed!')


users: List[BankAccount] = []


def choose_user():
    print()
    print('Choose account')
    name = input('name: ')
    surname = input('surname: ')
    current_user = BankAccount('user', 'user')
    wallet_type = Account

    for user in users:
        if user.name == name and user.surname == surname:
            current_user = user
            break
    else:
        print('\nUser not found!')
        return

    while True:
        print("\n1. Replenish the balance")
        print("2. Withdraw money")
        print("3. Change currency")
        print("4. Balance")
        print("5. Log out")
        action = int(input("Choose action: "))
        match action:
            case 1:
                amount = int(input("\nAmount: "))
                currency = input("Currency: ")
                current_user.add_to_bank_account(amount, currency)
            case 2:
                amount = int(input("Amount: "))
                currency = input("Currency: ")
                current_user.subtract_from_bank_account(amount, currency)
            case 3:
                print(f'Your current account {current_user.account.value}')
                currency = input('Currency: KZT, USD, RUB, EUR: ')
                current_user.set_account(currency)
            case 4:
                print()
                current_user.get_balance()
            case 5:
                print()
                main()


def create_user():
    name = input('name: ')
    surname = input('surname: ')
    new_user = BankAccount(name, surname)
    users.append(new_user)
    choose_user()


def main():
    print("Choose action")
    print("1. Create account")
    print("2. Choose account")
    print("3. Log out")
    action = int(input())
    if action == 1:
        create_user()
    elif action == 2:
        choose_user()
    elif action == 3:
        print('Not choosed acoount!')


if __name__ == '__main__':
    main()



