"""
2分探索法で年齢を当てるプログラム
> N M age
> age

"""

mnage = list(map(int, input().split()))
m = mnage[0]
n = mnage[1]
age = mnage[2]


def binary_search(n, m, age):
    """
    binary search

    Args:
        n (int): lowest number
        m (int): highest number
        age (int): aim number

    Return: age

    """

    counter = 0
    while True:
        guess_number = int((m + n) / 2)
        counter += 1

        if age == guess_number:
            break
        elif guess_number < age:
            n = guess_number
        else:
            m = guess_number
    return counter


print(binary_search(m, n, age))
