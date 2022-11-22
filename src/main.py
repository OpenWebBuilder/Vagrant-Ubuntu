from vagrantfile import Vagrantfile


def default():
    vm1 = Vagrantfile()
    vm1.open_dir()
    vm1.make_vagrantfile()


def named():
    vm1 = Vagrantfile("foobar")
    vm1.open_dir()
    vm1.make_vagrantfile()


named()
