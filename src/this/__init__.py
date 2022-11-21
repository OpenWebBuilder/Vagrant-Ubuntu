import vagrant
import vagrantfile

def startServer():
    v = vagrant.Vagrant(root=f"{vagrantfile.server}")

    name = v.status()[0][0]
    state = v.status()[0][1]
    provider = v.status()[0][2]
    print(v.status())
    # v.up()
