from random import *
import string


class Password():
    def __init__(self, length, num, special, capital):
        self.length = length
        self.num = num
        self.special = special
        self.capital = capital
        self.normal = length - num - special - capital

    def gen_password(self):
        ls_num = []
        ls_special = []
        ls_capital = []
        ls_normal = []
        for i in range(self.num):
            ls_num.append(str(randint(0,9)))
        for i in range(self.special):
            ls_special.append(choice(['!', '@', '#', '$', '%', '^', '&', '*']))
        for i in range(self.capital):
            ls_capital.append(choice(string.ascii_uppercase))
        for i in range(self.normal):
            ls_normal.append(choice(string.ascii_letters))
        
        sequence = ls_num + ls_special + ls_special + ls_capital + ls_normal
        shuffle(sequence)
        password = ''
        for each in sequence:
            password += each

        return password


def main():
    length = int(input('length required: '))
    num = int(input('numbers required: '))
    special = int(input('special charecters required: '))
    capital = int(input('capitals required: '))
    
    new_params = Password(length, num, special, capital)
    password = new_params.gen_password()
    print('\n%s\nrandomly generated password: %s\n%s' %('-'*(31+new_params.length), password, '-'*(31+new_params.length)))


main()