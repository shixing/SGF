#!/bin/sh
#
# usage: ./stanford-postagger.sh model textFile
#  e.g., ./stanford-postagger.sh models/english-left3words-distsim.tagger sample-input.txt

scriptdir=`dirname $0`

java -mx2048m -cp "$scriptdir/stanford-postagger.jar:" edu.stanford.nlp.tagger.maxent.MaxentTagger -model $scriptdir/models/english-bidirectional-distsim.tagger -textFile $1 >$2
