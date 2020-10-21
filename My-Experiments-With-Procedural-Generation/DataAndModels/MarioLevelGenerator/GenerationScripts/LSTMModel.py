# -*- coding: utf-8 -*-

import numpy as np
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import Dropout
from keras.layers import Activation
from keras.layers import LSTM
from keras.callbacks import ModelCheckpoint
from keras.utils import np_utils
import random
import sys

filename = "mario-1-1_t.csv"
generatedLevelFile = "GenLev1.txt"
raw_text = open(filename, 'r', encoding='utf-8').read()
raw_text = raw_text.lower()

print(len(raw_text))

chars=sorted(list(set(raw_text)))
words = set(open(filename).read().lower().split())
print(len(words))
print(len(chars))

char_indices=dict((c,i) for i,c in enumerate(chars))
indices_char=dict((i,c) for i,c in enumerate(chars))

word_indices = dict((c, i) for i, c in enumerate(words))
indices_word = dict((i, c) for i, c in enumerate(words))

sentences = []
next_words = []
wordlist=raw_text.lower().split()
for i in range(0, len(wordlist) - 40, 3):
    sentences.append(wordlist[i: i + 40])
    next_words.append(wordlist[i + 40])

x_train = np.zeros((len(sentences), 40, len(words)), dtype=np.bool)
y_train = np.zeros((len(sentences), len(words)), dtype=np.bool)
for i, sentence in enumerate(sentences):
    for t, word in enumerate(sentence):
        x_train[i, t, word_indices[word]] = 1
    y_train[i, word_indices[next_words[i]]] = 1
    
regressor=Sequential()

regressor.add(LSTM(units=512,return_sequences=True,input_shape=(40,len(words))))
regressor.add(Dropout(0.2))

regressor.add(LSTM(units=512,return_sequences=True))
regressor.add(Dropout(0.2))

regressor.add(LSTM(units=512,return_sequences=True))
regressor.add(Dropout(0.2))

regressor.add(LSTM(units=512))
regressor.add(Dropout(0.2))

regressor.add(Dense(len(words)))
regressor.add(Activation('softmax'))

regressor.compile(optimizer='rmsprop',loss='categorical_crossentropy')

def sample(preds, temperature=1.0):
    preds = np.asarray(preds).astype('float64')
    preds = np.log(preds) / temperature
    exp_preds = np.exp(preds)
    preds = exp_preds / np.sum(exp_preds)
    probas = np.random.multinomial(1, preds, 1)
    return np.argmax(probas)

for cycle in range(1,50):
    print()
    print('*'*50)
    print('Iteration->',cycle)
    regressor.fit(x_train,y_train,epochs=2,batch_size=64)
    
    start_index = random.randint(0, len(wordlist) - 40 - 1)
    predictedLevelText = open(generatedLevelFile, "w+")
    for diversity in [1.0, 1.1]:
        print()
        print('#'*25)
        print('Diversity:', diversity)
        generated = ''
        sentence = wordlist[start_index: start_index + 40]
        generated += ' '.join(sentence)
        print('-'*15)
        print('Generating with seed: "' , sentence , '"')
        print()
        sys.stdout.write(generated)
        print()

        for i in range(1024):
            x = np.zeros((1, 40, len(words)))
            for t, word in enumerate(sentence):
                x[0, t, word_indices[word]] = 1.

            preds = regressor.predict(x, verbose=0)[0]
            next_index = sample(preds, diversity)
            next_word = indices_word[next_index]
            generated += next_word
            predictedLevelText.write(next_word+"\n")
            del sentence[0]
            sentence.append(next_word)
            sys.stdout.write(' ')
            sys.stdout.write(next_word)
            sys.stdout.flush()
        print()


