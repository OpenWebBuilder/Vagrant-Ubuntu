dependencies(){
  # Build dependencies
  pdm add python-vagrant
}

development_install(){
  # Editable install
  pip3 install -e .
}

pdm init
#dependencies
pdm install
development_install
