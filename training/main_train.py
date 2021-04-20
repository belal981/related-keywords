"""

Inspired by NETL Repositry: https://github.com/sb1992/NETL-Automatic-Topic-Labelling-


-e  The extract parameter which will call Wiki-Extractor to process our XML dump file.
-ng It gets directory of sub bdirectories which contains tokenised documents and following similar directory
    structure  gets documnts which contains wikipedia titles.
-wv Trains word2vec model.
"""

import os
import argparse
parser = argparse.ArgumentParser()


# Parameters for extract.py
wiki_extractor_path = "support_packages/WikiExtractor.py" # Give the Path to WikiExtractor.py file after you download it.
input_dump = "dump/dumpfile" # The path to your Wikipedia XML dump.
size ="500M"             # Size of each individual file extracted (you can vary file sizes)
template ="no-templates" # Does not allow WikiExtractor to use any pre installed templates (avoid changing it till you are sure)
output_processed_directory = "processed_documents/docs"   # output directory whre you want documents extracted from dump (path for the directory)

parser.add_argument("-e", "--extract", help="extract wikidump into documents using WikiExtractor",
                    action="store_true")


#parameters for create_ngrams.py
# The file which has list of valid n-grams. word2vec phrase list can be obtained from drive
word2vec_phrase_file = "additional_files/word2vec_phrases_list_tokenized.txt" 
input_dir_ngrams = "processed_documents/docs_tokenised" # The directory which has tokensied documents. Already created above in tokenisation
output_dir_ngrams = "processed_documents/docs_ngram" # This is where output will be stored. Will be created in the script.

parser.add_argument("-ng","--ngrams", help ="Run the ngrams file and generate token file with ngrams  (upto 4 gram phrases in it) ", action ="store_true")


#parameters for word2vectrin.py
epochs_word2vec =15 #Ideal number of epochs for word2vecmodel. If you want the model to be trained quicker reduce the epochs.
input_dir_word2vec ="processed_documents/docs_ngram" # This is the directory where you have all tokenized wikipedia files. The script takes all files in the directory for training.
output_dir_word2vec = "trained_models/word2vec" #name of directory in which you want to save trained word2vec. This directory will be created as part of script.

parser.add_argument("-wv", "--word2vectrain", help = "train the word2vec model", action ="store_true")


args = parser.parse_args()

if args.extract:  
    query1 = "python extract.py "+wiki_extractor_path+" "+input_dump +" "+size+" "+template+" " +output_processed_directory
    print (query1)
    os.system(query1)

if args.ngrams:
   query2 = "python create_ngrams.py "+word2vec_phrase_file+" "+input_dir_ngrams +" "+output_dir_ngrams
   print (query2)
   os.system(query2)

if args.word2vectrain:
    query3 = "python word2vectrain.py "+str(epochs_word2vec) +" "+input_dir_word2vec+" "+output_dir_word2vec
    print (query3)
    os.system(query3)
