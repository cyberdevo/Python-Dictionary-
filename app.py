import json
import  speech_recognition  as  sr
from difflib import get_close_matches
import tkinter as tk
word = ""
data = json.load(open("data.json"))

def translate(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data: 
        return data[w.upper()]
    elif len(get_close_matches(w,data.keys()))>0:
        li = get_close_matches(w,data.keys(), n = 4, cutoff=0.6)
        print("Suggestions ")
        for i in range(len(li)):
            print("Press " ,i, "For this Keyword " , li[i] )
      
        take_in = int(input("Press Keyword please...: "))
        if take_in == 0:
            return(data[li[0]])
        elif take_in == 1:
            return(data[li[1]])
        elif take_in == 2:
            return(data[li[2]])
        elif take_in == 3:
            return(data[li[3]])
        else:
            return("Invalid Input . Please Check Again")
    else:
        return"The word does'nt exist. Please Double check it."


check = int(input("Press 1 to Translate a world by Keyboard... Press 2 to translate a word with youe voice:" ))

# if check > 0:
#     print("Positive number")
# elif check == 0:
    # print("Zero")

if check == 1:
    print("1st Condition: 1") 
    word = input("Enter word for finding its meaning....: ")

elif check == 2 :
    r2 = sr.Recognizer()
    r3 = sr.Recognizer()
    
    with  sr.Microphone()  as  source:
        
        print('Speak Now.......')
        
        with  sr.Microphone()  as source:
            
            audio = r2.listen(source)
            
            try:
                word = r2.recognize_google(audio)
                print('Your query')
                print(word)
            except  sr.UnknownValueError:
                print('error')
            except  sr.RequestError  as e:
                print('failed'.format(e))
            


output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)

print("Stay Connected for more Information")


