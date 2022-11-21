import pathlib
import os
import platform
import subprocess

class Uni:
    def __init__(self):
        self.vagrant_home = f"{pathlib.Path.home()}/.uni/hyperion/vagrant"
        self.machines = f"{self.vagrant_home}/machine"

        os.makedirs(self.vagrant_home, exist_ok=True)

    def get_machine_dir(self):
        return self.machines

    def open_vagrant(self):
        if platform.system() == "Windows":
            os.startfile(self.vagrant_home)
        elif platform.system() == "Darwin":
            subprocess.Popen(["open", self.vagrant_home])
        else:
            subprocess.Popen(["xdg-open", self.vagrant_home])