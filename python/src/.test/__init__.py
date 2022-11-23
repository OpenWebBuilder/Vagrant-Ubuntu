from vagrantfile import Vagrantfile

name = "foobar"

def default():
    vm1 = Vagrantfile()
    vm1.open_dir()
    vm1.make_vagrantfile()


def named():
    # init
    vm1 = Vagrantfile(name)
    vm1.open_dir()
    vm1.make_vagrantfile()

    # wrapper
    vm1.up()
    vm1.halt()

    # native
    vm1.vagrant.destroy()


named()
