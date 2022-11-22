
class UbuntuLTS:
    default_box = "generic/ubuntu2204"
    box = default_box
    def __init__(self, box=default_box):
        # overwrite default box
        UbuntuLTS.box = box
