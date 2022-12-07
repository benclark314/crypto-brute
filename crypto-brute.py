#import math
import time
import math
import itertools
#from itertools import permutations
#from unittest import result
##########################################
#Function Definitions:
##########################################

def get_all_strings_by_regular_moduli_in_range_inclusive(ciphertext, lower, upper):
    allresults = []
    for x in range(lower, upper + 1):
        array = compute_array(ciphertext, x)
        stringsarray = compute_strings_array(array)
        allresults.extend(stringsarray)
    return allresults

def compute_strings_array(array):
    permsarrayindices = []
    permsarray = []
    results = []

    for x in range(0, len(array)):
        permsarrayindices.append(x)
        
    permsarray = list(itertools.permutations(permsarrayindices))
    #print(permsarray)
    for y in range(0, len(permsarray)):
        count = 0
        flag = True
        result_string = ""
        string_bound_exceeded = 0
        while(flag):
            perms_index = count % len(permsarray[y])
            string_index = math.ceil((count + 1) / (len(permsarray[y])))
            main_index = permsarray[y][perms_index]
            # print("array: ")
            # print(array)
            # print("\n main_index: ")
            # print(str(main_index))
            # print("\n string_index: ")
            # print(str(string_index))
            if(len(array[main_index]) > string_index - 1):
                result_string = result_string + array[main_index][string_index - 1]
            else:
                string_bound_exceeded = string_bound_exceeded + 1
            count = count + 1
            if(string_bound_exceeded == len(array)):
                results.append(result_string)
                flag = False
    return results
    #print(results)

#prints several arrays, each one index further up the input string. EG: abcdefghi -> [a, d, g], [b, e, h], [c, f, i]
def compute_array(inputstring, numberOfArrays):
    completedSubstrings = []
    for w in range(0, numberOfArrays + 1):
        completedSubstrings.append("")
    for x in range(0, len(inputstring)):
        index = x % (numberOfArrays + 1)
        completedSubstrings[index] = completedSubstrings[index] + ciphertext[x]
    #print(completedSubstrings)
    return completedSubstrings

def compute_skip(inputstring, skipNumber):
    completedNumbers = []
    resultstring = ""
    for x in range(0, len(inputstring)):
        index = skipNumber*x % len(inputstring)

        if (index not in completedNumbers and index <= len(inputstring)):
            completedNumbers.append(index)
        else:
            while (index in completedNumbers and index <= len(inputstring)):
                index = index + 1

            completedNumbers.append(index)
        if(index < len(inputstring)):
            resultstring = resultstring + inputstring[index]
    return resultstring

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

#SKIP BY REGULAR MODULI:
english_words = load_words()
f = open("ciphertext.txt", "r")
ciphertext = f.read()
f = open("results.txt", "a")
summary = []
f.write("Original String: " + ciphertext + "\n")
stngs = get_all_strings_by_regular_moduli_in_range_inclusive(ciphertext, 6, 8)
for stng in stngs:
    f.write("String: " + stng + "\n")
    words = find_sub_words(english_words, stng)
    wordcount = len(words)
    f.write("\t Had " + str(wordcount) + " words.\n")
    for y in range(0, wordcount):
        f.write("\t" + words[y] + "\n")
    summary.append(str(wordcount) + " English words " + "are found in string " + stng + "\n")
summary.sort()
for z in summary:
    f.write(z)
endtime = time.perf_counter()
f.write("runtime was " + str(endtime - starttime) + " seconds.")
f.close()


