# import fire


class Calculator(object):

    def sum(self, a):
        print(a)
        sum = a + 2
        return print(sum)

    def minus(self, a):
        print(a)
        minus = a - 2
        return print(minus)



if __name__ == '__main__':
    calculator = Calculator()
    calculator.sum(10)
    calculator.minus(10)

# fire.Fire(sum)


