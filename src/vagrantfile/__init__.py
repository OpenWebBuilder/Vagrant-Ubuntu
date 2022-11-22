import template
import uni
import vagrant


class Vagrantfile:
    def __init__(self, tmpl=template.UbuntuLTS):
        self.name = tmpl.name
        self.box = tmpl.box
        self.path = f"{uni.Uni.instance_dir}/{self.name}"

    def make_vagrantfile(self):
        v = vagrant.Vagrant()
        v.init(self.box)


    def __str__(self):
        return f"{self.name}, {self.box}, {self.path}"