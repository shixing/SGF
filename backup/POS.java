import java.io.BufferedReader;
import java.io.FileReader;
import java.util.List;

import edu.stanford.nlp.ling.Sentence;
import edu.stanford.nlp.ling.TaggedWord;
import edu.stanford.nlp.ling.HasWord;
import edu.stanford.nlp.tagger.maxent.MaxentTagger;
import edu.stanford.nlp.process.DocumentPreprocessor;


public class POS {

	public static void main(String[] args) throws Exception{
		// TODO Auto-generated method stub
		if (args.length != 3) {
		      System.err.println("usage: java TaggerDemo modelFile fileToTag maxlength");
		      return;
		    }
		    MaxentTagger tagger = new MaxentTagger(args[0]);
		    int maxLength = Integer.parseInt(args[2]);
		    BufferedReader r = new BufferedReader(new FileReader(args[1]));
		    DocumentPreprocessor documentPreprocessor = new DocumentPreprocessor(r);
		    for (List<HasWord> sentence : documentPreprocessor) {
		      if (sentence.size() > maxLength) {continue;}
		      try{
		    	  List<TaggedWord> tSentence = tagger.tagSentence(sentence);
		    	  System.out.println(Sentence.listToString(tSentence, false));
		      }catch (Exception e) {
		    	  
		      }
		    }
	}

}
