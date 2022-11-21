import this
from vagrantfile import *

def print_hi(name):
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def newInstance():
    v1 = Vagrantfile("wordpress", max_instances=3, create_another=False)
    v1.new_instance()
    print(v1.get_location())


if __name__ == '__main__':
    print_hi('PyCharm')
    newInstance()
    # this.startServer()

    u = uni.Uni()
    u.open_vagrant()