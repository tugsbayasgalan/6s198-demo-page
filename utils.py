import numpy

from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Flatten
from keras.layers import Dropout
from keras.layers import LSTM
from keras.utils import np_utils


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

def generate_lyrics(input_seed, genre):

    seq_length = 100 # can be changed later

    model = Sequential()
    model.add(LSTM(256, input_shape=(seq_length, 1), return_sequences=True))
    model.add(Dropout(0.2))
    model.add(Flatten())
    model.add(Dense(55, activation='softmax'))
    model.compile(loss='categorical_crossentropy', optimizer='adam')

    weights = numpy.load("jank_weights.npy")
    print "Weights:", weights


    #process the user input
    input_pattern = []
    for char in input_seed:
        if char not in char_to_int:
            continue
        else:
            input_pattern.append(char_to_int[char])

    while len(input_pattern) < seq_length:
        input_pattern.append(char_to_int['a'])

    print ("Seed:")
    print ("\"", ''.join([int_to_char[value] for value in input_pattern]), "\"")
    # generate characters

    final_result = ""
    for i in range(1000):
        x = numpy.reshape(input_pattern, (1, len(input_pattern), 1))
        x = x / float(n_vocab)
        prediction = model.predict(x, verbose=0)
        index = numpy.argmax(prediction)
        result = int_to_char[index]
        seq_in = [int_to_char[value] for value in input_pattern]
        final_result += result
        input_pattern.append(index)
        input_pattern = input_pattern[1:len(input_pattern)]
    print ("\nDone.")
    return final_result
