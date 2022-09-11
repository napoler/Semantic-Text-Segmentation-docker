# coding: utf-8
from gensim.models import KeyedVectors
from gensim.scripts.glove2word2vec import glove2word2vec

# !wget https://nlp.stanford.edu/data/glove.6B.zip
# !unzip glove.6B.zip
# Convert
# input_file = './glove.6B.50d.txt'
input_file = './glove.6B.100d.txt'
output_file = 'gensim_glove.6B.txt'
out_fname="./glove.6B.bin"

def save_model(input_file,output_file,out_fname):
    """
    The save_model function saves the model in a format that can be used by the
    load_model function. The save_model function takes three arguments: input_file,
    output_file, and out_fname. Input file is the name of a GloVe model file to be
    converted into Word2Vec format. Output file is where we want to save our new Word2Vec
    format of our converted GloVe model. Out fname is what we want to call our saved output.

    :param input_file: Used to Specify the path of the file that contains the glove model.
    :param output_file: Used to Specify the path of the converted file.
    :param out_fname: Used to Specify the name of the output file.
    :return: The model that is saved in the output_file.

    :doc-author: Tredlent
    """

    glove2word2vec(input_file, output_file)
    model = KeyedVectors.load_word2vec_format(output_file, binary=False)
    model.save_word2vec_format(fname=out_fname,binary=True)