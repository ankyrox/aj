
def sumProblem(x, y):
    sum = x + y
    sentence = 'The sum of {} and {} is {}.'.format(x, y, sum)
    print(sentence)


def main():
    sumProblem(2, 3)
    sumProblem(1234567890, 9876543210)
    a = int(input("enter an integer: ".title()))
    b = int(input("enter another integer: ".title()))
    sumProblem(a, b)

main()    
