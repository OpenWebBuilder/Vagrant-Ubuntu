
def new_instance():
    multiple = False #True
    help = False

    vf = Vagrantfile("wordpress", max_instances=3, create_another=multiple, help=help)
    vf.new_instance()
    return vf
