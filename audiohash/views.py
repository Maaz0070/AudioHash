from django.shortcuts import render
from django.urls import reverse


import requests
import speech_recognition as sr
import pyttsx3

#functions for hashing-chainign:
# Function to display hashtable
def display_hash(hashTable):
      
    for i in range(len(hashTable)):
        print(i, end = " ")
          
        for j in hashTable[i]:
            print("-->", end = " ")
            print(j, end = " ")
              
        print()
  
  
# Hashing Function to return 
# key for every value.
def Hashing(keyvalue, Hashtable):
    return keyvalue % len(Hashtable)
  
  
# Insert Function to add
# values to the hash table
def insert(Hashtable, keyvalue, value):
    hash_key = Hashing(keyvalue, Hashtable)
    Hashtable[hash_key].append(value)

# Create your views here.
def index(request):

    r = sr.Recognizer()

    with sr.AudioFile('/Users/kenny/Movies/Movavi_Library/Snot.wav') as source:
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print("Working on...")
            print(text)
        except:
            print("Sorry.. run again...")

    res = text.split()

    # Creating Hashtable as 
    # a nested list.
    HashTable = [[] for _ in range(len(res))]

    for i in res:
        key = 0
        for j in i:
            key += ord(j)
        insert(HashTable, key, i)
    
    display_hash(HashTable)
        

    return render(request, "audiohash/main.html", {
        "text": text,
        "hash": HashTable
    })
