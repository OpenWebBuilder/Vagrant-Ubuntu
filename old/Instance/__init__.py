from oldVagrantfile import Vagrantfile

class Instance():
    def __init__(self, vagrant_file):
        self.foo = "bar"
        self.vagrant = vagrant_file

    def set_vagrant(self, obj):
        print('In my_method method of MyClass')
        print("Location:", obj.location)
        print("Box:", obj.box)

    def get_foo(self):
        print(self.foo)
        print(self.vagrant)

        # print(self.vagrant.location)