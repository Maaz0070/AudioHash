from django.shortcuts import render
from django.urls import reverse

import math
import requests
import speech_recognition as sr
import pyttsx3
from timeit import default_timer as timer

wordCounts = 0
mostIndex = []
#functions for hashing-chainign:
# Function to display hashtable
def mostOccurASCII(hashTable):
    currMax = 0
    
def mostOccur(hashTable):
    global mostIndex
    currMax = 0
    for i in range(len(hashTable)):
        j = hashTable[i] 
        if(j != None):
            for x in range(0,len(j)):
                 space = 0
                 if j[x] == ' ':
                     space += 1
                 if space >= currMax and not mostIndex:
                     currMax = space
                     mostIndex.append(i)
                 elif space == currMax and len(mostIndex) > 0:
                     currMax = space
                     mostIndex.append(i)
                 elif space > currMax and len(mostIndex) > 0:
                     currMax = space
                     mostIndex.clear()
                     mostIndex.append(i)
                     
                 
    
    for i in range (len(mostIndex)):
        print(hashTable[mostIndex[i]])
def display_hash(hashTable):
      
    for i in range(len(hashTable)):
        print(i, end = " ")
        j = hashTable[i]
        if j == None:
            print(" ")
        if j != None:
            print("-->", end = " ")
            print(j, end = " ")
              
        print()
  
  
# Hashing Function to return 
# key for every value.
def Hashing(res, Hashtable):
    key = 0
    for i in res:
        key += ord(i)
    return key % len(Hashtable)
    #return keyvalue % len(Hashtable)

def HashingH(keyvalue, Hashtable):
    return keyvalue % len(Hashtable)

def HashingM(keyvalue,Hashtable):
    A = .68
    hashLength = len(Hashtable)
    hash_key = keyvalue * A
    hash_key = hash_key % 1
    hash_key = hash_key * hashLength
    hash_key = math.floor(hash_key)
    return hash_key
  
  
# Insert Function to add
# values to the hash table
def insert(Hashtable, keyvalue, value):
    hash_key = keyvalue % len(Hashtable)
    Hashtable[hash_key].append(value)
def insertM(Hashtable,keyvalue, value):
   
    hash_key = HashingM(keyvalue,Hashtable)
    flag = False
    
    if Hashtable[hash_key] == " ":
        print("no collision")
        Hashtable[hash_key] = value
        flag = True
    elif Hashtable[hash_key] == value and flag == False:
        Hashtable[hash_key] = Hashtable[hash_key] + " " + value
    else:
        while(Hashtable[hash_key] != " "):
            hash_key += 1
            if hash_key >= len(Hashtable):
                hash_key = 0
            if Hashtable[hash_key] == value and flag == False:
                Hashtable[hash_key] = Hashtable[hash_key] + " " + value
        if flag == True:
            Hashtable[hash_key] = value
   
def insertH(Hashtable, keyvalue, value):
    global wordCounts

    hash_key = HashingH(keyvalue, Hashtable)

    print(Hashtable[hash_key])
    flag = False
    if len(value) > 0:
        wordCounts += 1
    if Hashtable[hash_key] == " ":
        print("no collision")
        Hashtable[hash_key] = value
        flag = True
    elif Hashtable[hash_key] == value and flag == False:
        Hashtable[hash_key] = Hashtable[hash_key] + " " + value
    else:
        while(Hashtable[hash_key] != " "):
            hash_key += 1
            if hash_key >= len(Hashtable):
                hash_key = 0
            if Hashtable[hash_key] == value and flag == False:
                Hashtable[hash_key] = Hashtable[hash_key] + " " + value
        if flag == True:
            Hashtable[hash_key] = value


def searchOccurence(word, Hashtable):
    index = Hashing(word, Hashtable)
    index = index % len(Hashtable)
    print("holo: " + str(index))
    return len(Hashtable[index])



# Create your views here.
def index(request):
    


        r = sr.Recognizer()

        with sr.AudioFile('/Users/kenny/Movies/Movavi_Library/Podcast.wav' ) as source:
            audio = r.listen(source)
            try:
                text = r.recognize_google(audio)
                print("Working on...")
            except:
                print("Sorry.. run again...")

        res = text.split()

        # Creating Hashtable as 
        # a nested list.
        HashTable = [[] for _ in range(len(res))]
        start1 = timer()
        for i in res:
            key = Hashing(i, HashTable)
            if(i != "but" and i != "always" and i != "how" and i != "not" and i != "you" and i != "be" and i != "which" and i != "they're" and i != "do" and i != "as" and i != "of" and i != "right" and i != "we" and i != "is" and i != "to" and i != "that" and i != "like" and i != "than" and i != "were" and i != "sure" and i != "very" and i != "and" and i != "the" and i != "them" and i != "did" and i != "actually"):
                insert(HashTable, key, i)
        end1 = timer()
        wordCount = searchOccurence("autopilot", HashTable)
        display_hash(HashTable)

        HashTableH = [" "] * len(res)
        HashTableM = [" "] * len(res)
        start2 = timer()
        for i in res:
            key = 0
            for j in i:
                key += ord(j)
            insertH(HashTableH, key, i)
        end2 = timer()
        start3 = timer()
        for i in res:
            key = 0
            for j in i:
                key += ord(j)
            insertM(HashTableM, key, i)
        end3 = timer()
        print ("The word count is ", wordCounts)
        display_hash(HashTableH)
        display_hash(HashTableM)
        mostOccur(HashTableH)
        print("Timer for ASCII hashing function:", end1 - start1)
        print("Timer for Division hashing function: ", end2 - start2)
        print("Timer for Multiplication hashing function:", end3 - start3)
        


        

        return render(request, "audiohash/main.html", {
            "text": text,
            "hash": HashTable,
            "wordCount": wordCounts,
            "HashTableH": HashTableH,
            "HashTableM": HashTableM,
            "wordCounts": wordCounts
        })
    
