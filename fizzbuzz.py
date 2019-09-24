from functools import partial


def is_multiple_of(base, num):
    return num % base == 0


multiple_of_three = partial(is_multiple_of, 3)
multiple_of_five = partial(is_multiple_of, 5)


def robot(pos):
    say = str(pos)
    if multiple_of_three(pos) and multiple_of_five(pos):
        say = 'fizzbuzz'
    elif multiple_of_three(pos):
        say = 'fizz'
    elif multiple_of_five(pos):
        say = 'buzz'

    return say


if __name__ == '__main__':
    assert robot(1) == '1'
    assert robot(2) == '2'
    assert robot(4) == '4'

    assert robot(3) == 'fizz'
    assert robot(6) == 'fizz'
    assert robot(9) == 'fizz'

    assert robot(5) == 'buzz'
    assert robot(10) == 'buzz'
    assert robot(20) == 'buzz'

    assert robot(15) == 'fizzbuzz'
    assert robot(30) == 'fizzbuzz'
    assert robot(45) == 'fizzbuzz'
