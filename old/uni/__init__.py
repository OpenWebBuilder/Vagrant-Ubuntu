
import platform
import subprocess


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
