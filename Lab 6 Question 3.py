#Question No: 3
def even(n):
    for i in range(2, n):
        if i%2 == 0 or i%3 == 0:
            print(i, end=', ')
even(36)