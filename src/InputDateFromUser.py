# Author: Techdenovo

import datetime


def obtaindate():
    date_input = input("Type Date dd/mm/yyyy: ")
    print(date_input)
    d = datetime.datetime.strptime(date_input, '%d/%m/%Y').date()
    print(d)


obtaindate()
