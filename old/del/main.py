import Instance
import uni
from oldVagrantfile import Vagrantfile
from Instance import Instance

def testit():
    unios = uni.Uni()
    unios.open_machine()

if __name__ == '__main__':
    # vfile = new_instance()
    # print(vfile.get_location())
    # inst.get_info()
    # print(inst.foo)
    # print("Hello")

    v_file = Vagrantfile()

    # new_in = Instance(v_file)
    # new_in.get_foo()
