#!/usr/bin/env bash
#
# Runs the English POS Tagger, suppose the sentence is not tokenized, sentence is seperated by newline

if [ ! $# -ge 1 ]; then
  echo Usage: `basename $0` 'file(s)'
  echo
  exit
fi

scriptdir=`dirname $0`



java -mx2048m -cp "$scriptdir/*:" edu.stanford.nlp.tagger.maxent.MaxentTagger -model $scriptdir/models/english-bidirectional-distsim.tagger \
 -tokenizerOptions americanize=false -outputFormat tsv -sentenceDelimiter newline -textFile  $1 > $2

