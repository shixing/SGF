#!/bin/sh
scriptdir=`dirname $0`

java -Xmx2048m -cp "$scriptdir/stanford-ner.jar:" edu.stanford.nlp.ie.crf.CRFClassifier -loadClassifier $scriptdir/classifiers/english.all.7class.distsim.crf.ser.gz -textFile $1 >$2
