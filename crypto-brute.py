#import math
import time
##########################################
#Function Definitions:
##########################################
from unittest import result

def get_res(ciphertext, indexArray):
    result = ""
    for x in range(0, len(ciphertext)):
        index = indexArray.index(x)
        result = result + ciphertext[index]
    return result    

def get_skip_indices(inputstring, skipNumber):
    completedNumbers = []
    resultIndices = []
    for x in range(0, len(inputstring)):
        index = skipNumber*x % len(inputstring)

        if (index not in completedNumbers and index <= len(inputstring)):
            completedNumbers.append(index)
        else:
            while (index in completedNumbers and index <= len(inputstring)):
                index = index + 1

            completedNumbers.append(index)
        if(index < len(inputstring)):
            resultIndices.append(index)
    return resultIndices

def find_sub_words(english_words, ciphertext):
    containedWords = []
    for x in range(0, len(ciphertext)):
        for y in range(1, len(ciphertext) - x):
            if (ciphertext[x:y] in english_words):
                containedWords.append(ciphertext[x:y])
    return containedWords

def load_words():
    #can also use words_alpha.txt
    with open('scrabble_dictionary.txt') as word_file:
        valid_words = set(word_file.read().split())
    return valid_words

##########################################
#Program Script:
##########################################
#if __name__ == '__main__':
starttime = time.perf_counter()




#Attempt to reverse, essentially rotate the index mapping by 90 degrees clockwise.
#Attempted to accomplish this by using arrays of indices, and then mapping ciphertext to index of index in that array.
#.......didn't work!


english_words = load_words()
f = open("ciphertext.txt", "r")
ciphertext = f.read()
f = open("results.txt", "a")
summary = []
f.write("Original String: " + ciphertext + "\n")
for w in range(0, len(ciphertext)):
    if (w != 0):
        #Shift the ciphertext over one to the right, bringing rightmost element to front:
        ciphertext = ciphertext[-1] + ciphertext[0: len(ciphertext) - 1]
    for x in range(1, len(ciphertext)):
        reso = get_skip_indices(ciphertext, x)
        res = get_res(ciphertext, reso)


        # ssef = ""
        # for ind in range(0, len(reso)):
        #     ssef = ssef + ", " + str(reso[ind])
        # f.write("Index array " + ssef + "\n")


        f.write("Inverse shift by " + str(w) + " and skip by " + str(x) + " results in: " + res + "\n")
        words = find_sub_words(english_words, res)
        wordcount = len(words)
        f.write("\tTransform resulted in " + str(wordcount) + " words.\n")
        for y in range(0, wordcount):
            f.write("\t" + words[y] + "\n")
        summary.append(str(wordcount) + " English words " + "are found with Shift by " + str(w) + " and skip by " + str(x) + "\n")
summary.sort()
for z in summary:
    f.write(z)
endtime = time.perf_counter()
f.write("runtime was " + str(endtime - starttime) + " seconds.")
f.close()