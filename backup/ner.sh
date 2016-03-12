#!/usr/bin/env bash
#
# Runs the English POS Tagger, suppose the sentence is already tokenized, sentence is seperated by newline

if [ ! $# -ge 1 ]; then
  echo Usage: `basename $0` 'file(s)'
  echo
  exit
fi

scriptdir=`dirname $0`

java -mx2048m -cp "$scriptdir/*:" edu.stanford.nlp.ie.crf.CRFClassifier -loadClassifier $scriptdir/classifiers/english.all.7class.distsim.crf.ser.gz -tokenizerFactory edu.stanford.nlp.process.WhitespaceTokenizer -tokenizerOptions "tokenizeNLs=false" -textFile $1 > $2


