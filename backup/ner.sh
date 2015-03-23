#!/bin/sh
scriptdir=`dirname $0`

java -Xmx2048m -cp "$scriptdir/stanford-ner.jar:." NER $scriptdir/classifiers/english.all.7class.distsim.crf.ser.gz $1 50 >$2
