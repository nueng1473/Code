def books(book, amount):

    if book > 3 and amount > 500:
        amount_pay = amount - amount * 0.1
        print('You have to pay %d bath'%amount_pay)
    else:
        print('You have to pay %d bath'%amount)

book = int(input('Enter book : '))
amount = int(input('enter amount : '))
books(book, amount)