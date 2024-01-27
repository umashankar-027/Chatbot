import pyttsx3
m=pyttsx3.init()
print("com:How are you?")
m.say("com:How are you?")
m.runAndWait()
a=input('you: ')
if a in['I am fine','I am doing good','good','not bad']:
    print('com: That is good what did you had for break fast')
    m.say('That is good what did you had for break fast')
    b=input('you: ')
    print('com: Is it was yummy?')
    m.say('Is it was yummy?')
    c = input('you: ')
    if c in ['yes', 'I like it']:
        print('com: Wow great')
        m.say('Wow great')
    if c in ['no', 'I dont like it']:
        print('com: But it is good to eat')
        m.say('But it is good to eat')