from vagrantfile import Vagrantfile
from template import UbuntuLTS

def test_vagrant():
    name = "wordpress"
    vm1 = Vagrantfile(name)
    vm1.open_dir()

def test_template():
    print(UbuntuLTS.name)
    print(UbuntuLTS.box)
