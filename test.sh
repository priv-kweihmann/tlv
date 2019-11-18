#! /bin/sh
export PATH=$(pwd)/bin:${PATH}
export TESTPATH=$(pwd)/tests
for _test in $(pwd)/tests/*; do
    /bin/sh ${_test} || true
done