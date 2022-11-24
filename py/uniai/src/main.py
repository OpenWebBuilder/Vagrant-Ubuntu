from vagrant import template


def print_hi(word):
    print(word)


if __name__ == '__main__':
    print_hi('PyCharm')
    se = template.UbuntuLTS()
    de = template.UbuntuDesktop()

    print(se)
    print(de)