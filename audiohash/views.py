from django.shortcuts import render
from django.urls import reverse


import requests
import speech_recognition as sr
import pyttsx3

# Create your views here.
def index(request):

    r = sr.Recognizer()

    with sr.AudioFile('/Users/mymac/Downloads/lexclip.wav') as source:
        audio = r.listen(source)
        try:
            text = r.recognize_google(audio)
            print("Working on...")
            print(text)
        except:
            print("Sorry.. run again...")

    HashTable = [[] for _ in range(10)]

    def Hashing(keyValue):
        return ord(keyValue) # % len(HashTable)

    def insert(Hashtable, keyValue, value):
        hash_key = Hashing(keyValue)
        Hashtable[hash_key].append(value)

    def display_hash(hashTable):
        for i in range(len(hashTable)):
            print(i, end = " ")
            
            for j in hashTable[i]:
                print("-->", end = " ")
                print(j, end = " ")
                
            print()

    res = text.split()
    key = 0

    for i in res:
        key += 1
        insert(HashTable, i, key)
    
    display_hash(HashTable)
        

    return render(request, "audiohash/main.html", {
        "text": text,
        "hash": HashTable
    })
