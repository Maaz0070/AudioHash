from django.shortcuts import render
from django.urls import reverse

import math
import requests
import speech_recognition as sr
import pyttsx3
from timeit import default_timer as timer

wordCounts = 0
wordCount = 0
HashTable = [[]]

mostIndex = []
#functions for hashing-chainign:
# Function to display hashtable
 

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

#Helps to get ASCII equivalent
def toASC(res):
    for i in res:
        key = 0
        for j in i:
            key += ord(j)
    return key
  
  
# Hashing Function to return 
# key for every value.
def Hashing(res, Hashtable):
    key = 0
    for i in res:
        key += ord(i)
    return key #% len(Hashtable)
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
    hash_key = keyvalue #% len(Hashtable)
    Hashtable[hash_key].append(value)

def insertM(Hashtable,keyvalue, value):
    A = .68
    hashLength = len(Hashtable)
    hash_key = keyvalue * A
    hash_key = hash_key % 1
    hash_key = hash_key * hashLength
    
    
    hash_key = math.floor(hash_key)
    print(Hashtable[hash_key])
   
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
    res = 0
    index = Hashing(word, Hashtable)
    index = index % len(Hashtable)
    print("holo: " + str(index))
    print("holo: " + str(len(Hashtable[index])))
    
    for i in range(len(Hashtable[index])):
        if(Hashtable[index][i] == word):
            res += 1

    return res

def searchOccurenceH(word, Hashtable):
    res = 0
    asc = toASC(word)
    index = HashingH(asc, Hashtable)

    print("index: " + str(index))
    if(Hashtable[index] == ' '):
        return 0
    else:
        for i in range(len(Hashtable[index])):
            if i == ' ':
                res += 1
    print("HashingH wordCount: " + str(res+1))
    return res + 1



# Create your views here.
def index(request):
    global HashTable

    if request.method == "POST":

            fileName = request.POST["myfile"]
            print(fileName)

            r = sr.Recognizer()

            with sr.AudioFile('/Users/mymac/Downloads/' + fileName ) as source:
                audio = r.listen(source)
                try:
                    text = r.recognize_google(audio)
                    print("Working on...")
                except:
                    print("Sorry.. run again...")

            res = text.split()

            # Creating Hashtable as 
            # a nested list.
            HashTable = [[] for _ in range(len(res)+1489)]
            start1 = timer()
            for i in res:
                key = Hashing(i, HashTable)
                if(i != "but" and i != "always" and i != "how" and i != "not" and i != "you" and i != "be" and i != "which" and i != "they're" and i != "do" and i != "as" and i != "of" and i != "right" and i != "we" and i != "is" and i != "to" and i != "that" and i != "like" and i != "than" and i != "were" and i != "sure" and i != "very" and i != "and" and i != "the" and i != "them" and i != "did" and i != "actually"):
                    insert(HashTable, key, i)
            end1 = timer()
            display_hash(HashTable)

            HashTableH = [' '] * len(res)
            HashTableM = [' '] * len(res)
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
            print("Timer for ASCII hashing function:", end1 - start1)
            print("Timer for Division hashing function: ", end2 - start2)
            print("Timer for Multiplication hashing function:", end3 - start3)
            

            return render(request, "audiohash/main.html", {
                "text": text,
                "hash": HashTable,
                "wordCount": wordCount,
                "HashTableH": HashTableH,
                "HashTableM": HashTableM,
                "wordCounts": wordCounts
            })

    else:
        return render(request, "audiohash/main.html")

def search(request):
    global HashTable
    if request.method == "POST":
        query = request.POST["search"]
        res = searchOccurence(query, HashTable)
        print("res: " + str(res))
        return render(request, "audiohash/result.html", {
                "searchCount": res
            })
    else:
        return render(request, "audiohash/result.html")

    

    
