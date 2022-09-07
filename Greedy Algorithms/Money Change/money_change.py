# python3


def money_change(money):
    assert 0 <= money <= 10 ** 3
    n = money//10
    money = money % 10
    n = n + money // 5
    money = money % 5
    n = n + money
    return n



if __name__ == '__main__':
    input_money = int(input())
    print(money_change(input_money))
