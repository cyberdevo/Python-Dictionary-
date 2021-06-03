import  speech_recognition  as  sr


r2 = sr.Recognizer()
# r3 = sr.Recognizer()
 
with  sr.Microphone()  as  source:
    print('[ search youtube]')
    print('Speak Now.......')
    
    with  sr.Microphone() as source:
        audio = r2.listen(source)
        try:
            get = r2.recognize_google(audio)
            print('Your query')
            print(get)
        except  sr.UnknownValueError:
            print('error')
        except  sr.RequestError  as e:
            print('failed'.format(e))
 
