import shutil
import os

fileName = input("Enter the name of the file: ")
file = open(fileName)
fileLines = file.readlines()
searchedWord = input("Enter the word you want to search: ")
searched_word = searchedWord.lower()
count  = 0
found = False

for lines in fileLines:
    words=lines.split()
    for word in words:
        word = word.lower()
        if(word == searched_word):
            found=True
            count+=1
    
if(found == True):
    print(searchedWord,'is found',count,'times in the file')

else:
    print(searchedWord,"is not present in the file")