import os
import platform
import subprocess

import template
import uni
import vagrant


class Vagrantfile:
    def __init__(self, name=template.UbuntuLTS.name, tmpl=template.UbuntuLTS):
        if name != tmpl.name:
            self.name = name
        else:
            self.name = tmpl.name
        self.box = tmpl.box
        self.path = f"{uni.Uni.instance_dir}/{self.name}"
        self.vagrantfile = f"{self.path}/Vagrantfile"

        uni.Uni.init()

    def make_dir(self):
        os.makedirs(self.path, exist_ok=True)

    def make_vagrantfile(self):
        self.make_dir()
        v = vagrant.Vagrant(root=self.path)
        if not os.path.isfile(self.vagrantfile):
            v.init(self.box)

    def open_dir(self):
        self.make_dir()

        if platform.system() == "Windows":
            os.startfile(self.path)
        elif platform.system() == "Darwin":
            subprocess.Popen(["open", self.path])
        else:
            subprocess.Popen(["xdg-open", self.path])

    def __str__(self):
        return f"{self.name}, {self.box}, {self.path}"
