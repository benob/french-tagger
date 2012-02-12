#!/bin/bash

if [ ! -f ftb6_1.conll09 ]
then
    echo "ERROR: put 'ftb6_1.conll09' in this directory"
    exit 1
fi

dir=`dirname $0`
python=`which pypy 2>/dev/null || which python2 2>/dev/null || which python`

cat ftb6_1.conll09 \
    | cut -f2,5 \
    | $python $dir/add-morpho-features.py \
    | $python $dir/add-contextual-features.py \
    | $python $dir/add-lefff-features.py $dir/lefff-word-tag.txt \
    > ftb6_$i.conll09.crfsuite

crfsuite learn -a l2sgd -p feature.minfreq=2 -m ftb6.model ftb6_1.conll09.crfsuite

