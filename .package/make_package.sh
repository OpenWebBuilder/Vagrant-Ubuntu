# folder for PyPi
mkdir -p vagrant_ai
# copy
cp -r ../src/python/* vagrant_ai/
# Hardlink
ln ../readme.md vagrant_ai/README.md
ln ../license vagrant_ai/LICENSE
