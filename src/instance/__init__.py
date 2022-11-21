import vagrant

import template
import vagrantfile

class Instance:
    def __init__(self, vagrantfile):
        self.vagrantfile = vagrantfile

    def start_instance(vagrantfile):
        vf = vagrantfile

    def connect(self):
        return vagrant.Vagrant(root=f"{self.vagrantfile.location}")

    def make_vagrantfile(self):
        v = self.connect()
        v.init(box_name=template.UbuntuLTS.box)

    def tryit(self):
        name = v.status()[0][0]
        state = v.status()[0][1]
        provider = v.status()[0][2]
        print(v.status())
        # v.up()
