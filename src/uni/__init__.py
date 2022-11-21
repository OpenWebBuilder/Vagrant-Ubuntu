import pathlib
import os
import platform
import subprocess

class Uni:
    def __init__(self):
        self.vagrant_home = f"{pathlib.Path.home()}/.uni/hyperion/vagrant"
        self.machine_dir = f"{self.vagrant_home}/machine"

        self.init()
    def init(self):
        os.makedirs(self.machine_dir, exist_ok=True)

    def get_machine_dir(self):
        return self.machine_dir

    def get_vagrant_home(self):
        return self.vagrant_home

    def open_dir(self, dir):
        if platform.system() == "Windows":
            os.startfile(dir)
        elif platform.system() == "Darwin":
            subprocess.Popen(["open", dir])
        else:
            subprocess.Popen(["xdg-open", dir])

    def open_vagrant(self):
        self.open_dir(self.vagrant_home)

    def open_machine(self):
        self.open_dir(self.machine_dir)
