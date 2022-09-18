#!/bin/sh
pip3 install --user twine
./build.sh
twine upload dist/*