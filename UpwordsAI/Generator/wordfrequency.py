# -*- coding: utf-8 -*-
"""
Created on Thu Nov 17 20:31:24 2016

@author: Parth Bhatt
"""
import dictionary, math

class Wordfrequency:
    
    FILENAME = "Generator/wordfreq.txt"
    DICTIONARY = "Generator/upwords_usage.txt"
    
    
    def __init__(self):
        
        self.count = {}
        self.load()
        self.dict = dictionary.Dictionary(Wordfrequency.DICTIONARY)
    
    def load(self):
        try:
            freqFile = open(Wordfrequency.FILENAME, 'r')
            
            for line in freqFile:
                tokens = line.split()
                assert len(tokens) == 2
                word = tokens[0]
                freq = int(tokens[1])
                
                self.count[word] = freq
        except IOError as e:
            pass
    
    def save(self):
        
        freqFile = open(Wordfrequency.FILENAME, 'w')
        
        for word in self.count.keys():
            freqFile.write(word+" "+str(self.count[word])+"\n")
    
    def wordPlayed(self, word):
        if self.count.has_key(word):
            self.count[word] += 1
        else:
            self.count[word] = 1
    
    def displayStats(self):
        
        totalPlayed = 0
        playedOnlyOnce = 0
        longest = 0
        longestWord = 0
        numberSevenLetters = 0
        threeLetters = {}
        fourLetters = {}
        fiveLetters = {}
        wordsWithQ = {}
        wordsWithX = {}
        wordsWithZ = {}
        wordsWithJ = {}
        wordsWithK = {}
        wordsWithY = {}
        wordsWithV = {}
        wordsWithF = {}
        wordsWithW = {}
        wordsWithC = {}
        for word in self.count.keys():
            totalPlayed += self.count[word]
            if len(word) > longest:
                longest = len(word)
                longestWord = word
            if len(word) >= 7:
                numberSevenLetters += 1
            if self.count[word] == 1:
                playedOnlyOnce += 1
            if len(word) == 3:
                threeLetters[word] = self.count[word]
            elif len(word) == 4:
                fourLetters[word] = self.count[word]
            elif len(word) == 5:
                fiveLetters[word] = self.count[word]
            
            if 'Q' in word:
                wordsWithQ[word] = self.count[word]
            if 'Z' in word:
                wordsWithZ[word] = self.count[word]
            if 'J' in word:
                wordsWithJ[word] = self.count[word]
            if 'X' in word:
                wordsWithX[word] = self.count[word]
            if 'K' in word:
                wordsWithK[word] = self.count[word]
            if 'Y' in word:
                wordsWithY[word] = self.count[word]
            if 'V' in word:
                wordsWithV[word] = self.count[word]
            if 'F' in word:
                wordsWithF[word] = self.count[word]
            if 'W' in word:
                wordsWithW[word] = self.count[word]
            if 'C' in word:
                wordsWithC[word] = self.count[word]
            
            
        print("Unique words = " + str(len(self.count.keys())))
        print("Words played = " + str(totalPlayed))
        print("Words played only once = " + str(playedOnlyOnce))
        print("Longest word played: " + longestWord)
        print("Number of words at least seven letters long: " + str(numberSevenLetters))
        
        print("Top 500 Most Frequent Words: ")
        i = 1
        for w in sorted(self.count, key = self.count.get, reverse = True):
            self.printFreq(i, w, self.count[w])
            i += 1
            if i > 500:
                break
        print("")
        
        print("Top 10 Most Frequent 3-Letter Words: ")
        i = 1
        