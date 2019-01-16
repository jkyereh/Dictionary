#Import library
import json

#Load the json data as python dictionary
#Try typing "type(data)" in terminal after executing first two lines of this snippet
data = json.load(open("dictionary.json"))

#Function for retrivnig definition
def retrive_definition(word):
    #Remove the case-sensitivity from the program
    word = word.lower()

    
    #Check for non existing words
    #elif to make sure word with capitals are captured and to capture acronyms too
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    else:
        return("Oooops, I have no idea what that is..... Sorry bro")

#Input from user
word_user = input("Enter a word: ")

#Retrive the definition using function and print the result
print(retrive_definition(word_user))

