#!/bin/bash

dir=`dirname $0`
python=`which pypy 2>/dev/null || which python2 2>/dev/null || which python`
export PYTHONIOENCODING="utf8"

cat | $python $dir/segment-and-tokenize.py > /tmp/$$.words

cat /tmp/$$.words \
    | $python $dir/add-morpho-features.py \
    | $python $dir/add-contextual-features.py \
    | $python $dir/add-lefff-features.py $dir/lefff-word-tag.txt \
    | crfsuite tag -m $dir/ftb6.model \
    | paste -d" " /tmp/$$.words -

rm /tmp/$$.words
