from typing import Optional

from Bank_Users.models import User
from Bank_Users.repositories import UserRepository

class ServiceUser:
    userRepo: UserRepository

    def __init__(self, user: UserRepository):
        self.userRepo = user

    def createUser(self, name: str, surname: str, password: str) -> None:
        if len(name) < 3 or len(surname) < 3 or len(password) < 3:
            print('The all data must be more than 3 characters')
            return
        self.userRepo.createUser(name, surname, password)

    def getUser(self, name: str, surname: str, password: str) -> Optional[User]:
        if len(name) < 3 or len(surname) < 3 or len(password) < 3:
            print('The all data must be more than 3 characters')
            return
        return self.userRepo.getUser(name, surname, password)

    def sendBankAccount(self, name: str, surname: str, sender: User, money: int) -> None:
        if len(name) < 3 or len(surname) < 3:
            print('The all data must be more than 3 characters')
            return
        self.userRepo.sendBankAccount(name, surname, sender, money)