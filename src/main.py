import uni
from vagrantfile import *
from instance import *


def print_hi(name):
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def new_instance():
    multiple = False #True

    vf = Vagrantfile("wordpress", max_instances=3, create_another=multiple, help=True)
    vf.new_instance()
    print(Vagrantfile.help)

    return vf


if __name__ == '__main__':
    print_hi('PyCharm')
    vf = new_instance()

    print(vf.get_location())

    uni = uni.Uni()
    print(uni.machine_dir)
    # uni.open_vagrant()
    uni.open_machine()

    # vm = instance.Instance(vf)