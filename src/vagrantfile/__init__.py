import os.path

import template
import uni

# Specify Vagrantfile location #43
# https://github.com/pycontribs/python-vagrant/issues/43

default_name = "ubuntu-LTS-server"
default_box = "generic/ubuntu2204"


class Vagrantfile:
    """
    Create a Vagrantfile
    """
    help = False
    def __init__(self, name=default_name, box=default_box, max_instances=5, create_another=False, help=False):
        """
        :type max_instances: number
        """
        self.help = help
        self.uni = uni.Uni()
        self.name = name
        self.box = box
        self.location = f"{self.uni.get_machine_dir()}/{self.name}"
        self.max_instances = max_instances
        self.create_another = create_another

        if self.help:
            Vagrantfile.help = True
        # init new instance
        # self.new_instance()

    def exists(self, try_location):
        return os.path.isdir(try_location)

    def new_instance(self):
        suffix = 0
        try_location = self.location
        max_instances = False

        while self.exists(try_location):
            if ( (suffix <= self.max_instances - 2) and self.create_another):
                try_location = f"{self.uni.get_vagrant_home()}/{self.name}{suffix}"
                self.location = try_location
                suffix += 1
            else:
                max_instances = True
                break

        if max_instances:
            self.help_max_instances_reached()
            return -1
        else:
            os.makedirs(self.location, exist_ok=True)
            self.help_made_new_instance(suffix)
            return 0

    def help_made_new_instance(self, suffix):
        if Vagrantfile.help:
            if suffix > 0:
                this = suffix - 1
                print(f"Making new instance: {self.name}{this}")
            else:
                print(f"Making new instance: {self.name}")

    def help_max_instances_reached(self):
        if Vagrantfile.help:
            print(f"Max instances of '{self.name}' on this node, can't create any more. Delete an existing one, or Edit '.uni/config/vagrant.yml' to increase.")

    def get_location(self):
        return self.location

    def make_vagrantfile(self, tmpl=template.UbuntuLTS):
        print(self.location)
        print(tmpl)
