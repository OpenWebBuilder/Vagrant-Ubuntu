import vagrant

import template
# import oldVagrantfile


class VMInstance:
    def __init__(self, foo="bar"):
        self.foo = foo
        print("Try it now")

       new_instance(self)

    def new_instance(self):
        print("Help me")
        # vf = oldVagrantfile.oldVagrantfile("wordpress", max_instances=3, create_another=False, help=help)
        # print(vf.location)
        # print(vf)
        # self.oldVagrantfile = vfile
        # self.location = vfile.location

    # def get_info(self):
        # print(self.oldVagrantfile)
        # print(self.oldVagrantfile.box)
        # print(f"Make Instance: {self.oldVagrantfile.location}")
        # print("Before")
        # print(self.location)
        # print("After")

    def default_init(self):
        pass

    def start_instance(vagrantfile):
        vf = vagrantfile

    # def connect(self):
    #     return vagrant.Vagrant(root=f"{self.oldVagrantfile.location}")

    # def make_vagrantfile(self):
    #     v = self.connect()
    #     v.init(box_name=template.UbuntuLTS.box)

    def get_status(self):
        # name = self.vm.status()[0][0]
        # state = self.vm.status()[0][1]
        # provider = self.vm.status()[0][2]
        # print(self.vm.status)
        pass
