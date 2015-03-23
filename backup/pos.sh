#!/bin/sh
#
# usage: bash pos.sh input_file outputFile 
#  e.g., ./stanford-postagger.sh models/english-left3words-distsim.tagger sample-input.txt

scriptdir=`dirname $0`

java -mx2048m -cp $scriptdir/stanford-postagger.jar:$scriptdir POS $scriptdir/models/english-bidirectional-distsim.tagger $1 50 >$2
