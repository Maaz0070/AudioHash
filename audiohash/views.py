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
HashTableH = [[]]
HashTableM = [[]]

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

def HashingH(res, Hashtable):
    keyvalue = 0
    for i in res:
        keyvalue += ord(i)
    return keyvalue % len(Hashtable)

def HashingM(res,Hashtable):
    key = 0
    for i in res:
        key += ord(i)
    A = .68
    hashLength = len(Hashtable)
    hash_key = key * A
    hash_key = hash_key % 1
    hash_key = hash_key * hashLength
    hash_key = math.floor(hash_key)
    return hash_key
  
  
# Insert Function to add
# values to the hash table
def insert(Hashtable, keyvalue, value):
    hash_key = keyvalue #% len(Hashtable)
    Hashtable[hash_key].append(value)

def insertM(Hashtable,key, value):
    global wordCount
    flag = False
    hash_key = key % len(Hashtable)
    if Hashtable[hash_key] == []:
        print("no collision")
        Hashtable[hash_key].append(value)
    elif Hashtable[hash_key][0] == value:
        Hashtable[hash_key].append(value)
    else:
        flag = True
        while(Hashtable[hash_key] != []):
            hash_key += 1
            if(hash_key >= len(Hashtable)):
                hash_key = 0
            if(Hashtable[hash_key]!= []):
                if(Hashtable[hash_key][0] == value):
                    Hashtable[hash_key].append(value)
                    flag = False
        if flag == True:
            Hashtable[hash_key].append(value)
   
def insertH(Hashtable, keyvalue, value):
   global wordCount
   hash_key = keyvalue % len(Hashtable)
   if Hashtable[hash_key] == []:
        print("no collision")
        Hashtable[hash_key].append(value)
   elif Hashtable[hash_key][0] == value:
        Hashtable[hash_key].append(value)
   else:
        flag = True
        while(Hashtable[hash_key] != []):
            hash_key += 1
            if(hash_key >= len(Hashtable)):
                hash_key = 0
            if(Hashtable[hash_key]!= []):
                if(Hashtable[hash_key][0] == value):
                    Hashtable[hash_key].append(value)
                    flag = False
        if flag == True:
            Hashtable[hash_key].append(value)


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
    index = HashingH(word, Hashtable)
    print("holoH: " + str(index))
    print("holoH: " + str(len(Hashtable[index])))
    
    for i in range(len(Hashtable[index])):
        if(Hashtable[index][i] == word):
            res += 1

    return res

def searchOccurenceM(word, Hashtable):
    res = 0
    index = HashingM(word, Hashtable)
    print("holoM: " + str(index))
    print("holoM: " + str(len(Hashtable[index])))
    
    for i in range(len(Hashtable[index])):
        if(Hashtable[index][i] == word):
            res += 1

    return res



# Create your views here.
def index(request):
    global HashTable
    global HashTableH
    global HashTableM

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
                insert(HashTable, key, i)
            end1 = timer()
            display_hash(HashTable)

            HashTableH = [[] for _ in range(len(res))]
            HashTableM = [[] for _ in range(len(res))]
            start2 = timer()
            for i in res:
                key = HashingH(i,HashTable)
                insertH(HashTableH,key,i)
            end2 = timer()
            start3 = timer()
            for i in res:
                key = HashingM(i,HashTable)
                print(key, " ", i)
                insertM(HashTableM,key,i)
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
    global HashTableH
    global HashTableM
    if request.method == "POST":
        query = request.POST["search"]
        res = searchOccurence(query, HashTable)
        # resH = searchOccurenceH(query, HashTableH)
        # resM = searchOccurenceM(query, HashTableM)
        print("res: " + str(res))
        return render(request, "audiohash/result.html", {
                "searchCount": res
                # "searchCountH": resH,
                # "searchCountM": resM
            })
    else:
        return render(request, "audiohash/result.html")

    

    
