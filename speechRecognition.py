import speech_recognition as sr

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.6  
        audio = r.listen(source)
    
    try:
        print("Recognizing....")
        query = r.recognize_google(audio,language='en-in')
        print(f"user said: {query}\n")
        
    except Exception as e:
        print("Say that again Please....")
        return "None"
    return query
    
if __name__=='__main__':
    takeCommand()