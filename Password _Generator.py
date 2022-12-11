import random


class Generate_pass:
    pass_Length = 0
    chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()+<>?,./1234567890'
    password = ''

    def __init__(self, pass_Length) -> None:
        self.pass_Length = pass_Length

    def generate(self) -> str:
        for char in range(self.pass_Length):
            self.password += char
        return self.password
