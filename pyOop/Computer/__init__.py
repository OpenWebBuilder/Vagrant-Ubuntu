class Computer:
    foo = "bar"

    def __init__(self):
        self.ram = 1024
        self.hd = "128 GB"

    def get_foo(self):
        return Computer.foo
