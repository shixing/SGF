# -*- coding: utf-8 -*-

import sys
from bllipparser import RerankingParser

class Parser:

	def __init__(self,parse_model='WSJ+Gigaword-v2'):
		#self.rrp = RerankingParser.fetch_and_load(parse_model, verbose=True)
		self.rrp = RerankingParser.from_unified_model_dir("/home/nlg-05/xingshi/workspace/tools/BLLIP/WSJ+Gigaword-v2/")
	def bllip_parser(self,st):
		try:
			tree =  self.rrp.simple_parse(st)
		except:
			tree = ""
		
		return tree

escape_dict = {"&quot;":'"',
	       "&apos;":"'",
	       "&#91;":"[",
	       "&#93;":"]",
	       "&amp;":"&",
	       "&#124;":'|',
	       "&gt;":">",
	       "&lt;":"<",
	       '“':'"',
	       '”':'"',
	       "‘":"'",
	       "’":"'"
	       }


def ptb_tokenize(words):
	new_words = []
	start = True
	for word in words:
		if word in escape_dict:
			word = escape_dict[word]
		if "&apos;" in word:
			word = word.replace("&apos;","'")

		if word == "\"":
			if start:
				new_words.append("``")
				start = False
			else:
				new_words.append("''")
				start = True
		elif word == "'t":
			if len(new_words) > 0 and new_words[-1].endswith('n') and len(new_words[-1])>1:
				new_words[-1] = new_words[-1][:-1]
				new_words.append("n't")
			else:
				new_words.append("'t")
		else:
			new_words.append(word)
	return new_words

if __name__ == "__main__":
	parser = Parser()
	fo = open(sys.argv[2],'w')
	with open(sys.argv[1]) as fin:
		i = 0
		for line in fin:
			print i 
			if line == "\n":
				fo.write("\n")
			else:
				words = ptb_tokenize(line.split())
				fo.write(parser.bllip_parser(words)+"\n")
			i += 1
			if i % 100 == 0:
				fo.flush()
	fo.close()
