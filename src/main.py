from uni import Uni
from vagrantfile import Vagrantfile

Uni.init()

print(Uni())

vm1 = Vagrantfile()

vm1.make_vagrantfile()