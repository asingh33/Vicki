import speech_recognition as sr
import os

r = sr.Recognizer()
retStr = ""
exitphrase = "exit"
voice = "Zarvox"
song = "Mood aashiqana he, subah ghar jaana he, tune kaysa jaadoo he kiya. Tu kheech meri photo Tu kheech meri photo Tu kheech meri photo Piya"
with sr.Microphone() as source:
    r.adjust_for_ambient_noise(source, duration=1)
    print(r.energy_threshold)
    r.energy_threshold += 350
    print(r.energy_threshold)
    while True:
        print("Say something!")
        
        try:
            audio = r.listen(source, timeout=10)
            #os.system('say -v Bruce "hmm" &')
            print("....")
            phrase = r.recognize_google(audio, language="en-GB")
            
            #if the phrase contains a 'exit' word
            if phrase.find(exitphrase) >= 0:
                os.system("say -v " + voice + " \" Bye Bye\"")
                break
            #if phrase.find('stop') >= 0:
            #    os.killpg(os.getpgid(pro.pid), signal.SIGTERM)
            
            # Voice changer logic
            if phrase.find('Wiki') >= 0:
                voice = 'Vicki'
            elif phrase.find('Bruce') >= 0:
                voice = 'Bruce'
            elif phrase.find('Samantha') >= 0:
                voice = 'Samantha'
            elif phrase.find('Fred') >= 0:
                voice = "\"Cellos\""
            
            
            if phrase.find('hey') >= 0:
                phrase = 'Hello Abhishek!'
            if phrase.find('how are you doing') >= 0:
                phrase = 'I am doing good, thanks for asking'
            if phrase.find('song') >= 0:
                phrase = song
            if phrase.find('are you there') >= 0:
                phrase = 'Hey Abhishek, I am here'
            if phrase.find('who is this') >= 0:
                phrase = 'This is ' + voice
            
            print phrase
            retStr = "say -v " + voice + " \"" + phrase + "\""
            
        except sr.UnknownValueError as err:
            print err
        else:
        
            #print retStr
            os.system(retStr)

            
