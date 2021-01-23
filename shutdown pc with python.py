# # import os
# # os.system("shutdown /s /t 30") 
import pyttsx3
import speech_recognition as sr
import os
class shoutdownpc :
    def speak(self,text) :
        self.text =text
        engine= pyttsx3.init()
        engine.say(text) 
        engine.runAndWait()
    def recognize(self) :
        r = sr.Recognizer() #intalising the speech recognizer
        mic = sr.Microphone() #intalising the microphone class
        try : 
            with mic as source :  #making the default microphone as source for sound
                print("listening....")
                voice = r.listen(source) #listening whatever comes from the source i.e microphone
                print("Recognizing")
                message = r.recognize_google(voice) #calling google API to recognize the voice and convert to text.Free version of google recognize upto 30 sec only,and ther is limit of 50 requests fro a day,if it exceddssa it throws a request error
                # timeout is used as argument in listen function,it mean howe much time to wait until the speaking starts 
                print(message)
                return message
        except :
            self.speak("Error occured, while listening, please check your interenet connection, and try again") 
            exit() 
    def shutdown(self) :
        self.speak("Do you want to shutdown the PC Sir")
        opinion = self.recognize()
        if opinion in ['yes','s'] :
            self.speak("Got it Sir, shutdowning the Pc, for you")
            self.speak("Thank you Sir,Have a nice day")
            os.system("shutdown /s /t 30")
        else :
            self.speak("Ok Sir,I obey your opinion")    
user = shoutdownpc()
user.shutdown()      
