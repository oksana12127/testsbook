import fire


class Calculator(object):

    def sum(self, a):

        sum = a + 2
        return print(sum)

if __name__ == '__main__':
    fire.Fire(Calculator)
