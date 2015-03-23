import edu.stanford.nlp.ie.AbstractSequenceClassifier;
import edu.stanford.nlp.ie.crf.*;
import edu.stanford.nlp.io.IOUtils;
import edu.stanford.nlp.ling.CoreLabel;
import edu.stanford.nlp.ling.CoreAnnotations;
import edu.stanford.nlp.sequences.DocumentReaderAndWriter;
import edu.stanford.nlp.util.Triple;

import java.io.BufferedReader;
import java.io.FileReader;
import java.util.List;

import java.util.List;

public class NER {
    public static void main(String[] args) throws Exception {
		// TODO Auto-generated method stub
		if (args.length != 3) {
		      System.err.println("usage: java NER modelFile fileToTag maxlength");
		      return;
		    }
		
		String serializedClassifier = args[0];//"/Users/xingshi/Workspace/tools/stanford-ner/classifiers/english.all.7class.distsim.crf.ser.gz";
	    AbstractSequenceClassifier<CoreLabel> classifier = CRFClassifier.getClassifier(serializedClassifier);
	    int maxLength = Integer.parseInt(args[2]);
	    BufferedReader r = new BufferedReader(new FileReader(args[1]));
	    
	    String sentence = null;
	    while ((sentence = r.readLine())!=null){

	    	if (sentence.split(" ").length > maxLength)
		    {
			System.out.println();
			continue;
		    }
	    	try{
		    String nerstr = classifier.classifyToString(sentence,"slashTags",true);
		    if (nerstr.split(" ").length == sentence.split(" ").length)
			System.out.println(nerstr);
		    else
			System.out.println();
	    	} catch (Exception e){
		    System.out.println();
		}
	    }

	}

       

}
