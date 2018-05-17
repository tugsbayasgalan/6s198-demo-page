import numpy
import h5py
import sys
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Flatten
from keras.layers import Dropout
from keras.layers import LSTM
from keras.utils import np_utils
from keras.callbacks import ModelCheckpoint
from keras import backend as K
K.tensorflow_backend._get_available_gpus()


filename = "country_lyrics_all.txt"
raw_text = open(filename).read()
raw_text = raw_text.lower()
# create mapping of unique chars to integers, and a reverse mapping
chars = sorted(list(set(raw_text)))
char_to_int = dict((c, i) for i, c in enumerate(chars))
int_to_char = dict((i, c) for i, c in enumerate(chars))
# summarize the loaded data
n_chars = len(raw_text)
n_vocab = len(chars)
print ("Total Characters: ", n_chars)
print ("Total Vocab: ", n_vocab)


seq_length = 50 # can be changed later
dataX = []
dataY = []

for i in range(0, n_chars - seq_length, 1):
     seq_in = raw_text[i: i + seq_length]
     seq_out = raw_text[i + seq_length]
     dataX.append([char_to_int[char] for char in seq_in])
     dataY.append(char_to_int[seq_out])

     if i % 1000000 == 0:
         print('here')

n_patterns = len(dataX)
# print ("Total Patterns: ", len(dataX))
X = numpy.reshape(dataX, (n_patterns, seq_length, 1))

X = X / float(n_vocab)

y = np_utils.to_categorical(dataY)
numpy.save("dataX_v2.npy", X)
numpy.save("dataY_v2.npy", y)
