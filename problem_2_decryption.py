#JASMIN ERICKA A. CELEBRE
#PROBLEM 2 DECRYPTION
import pyfiglet 
#ask user for the encrypted text then save it
encr_text = input("What is the encrypted text? ")
#initialize empty decrypted Jtext
decr_text= ""
#check every character
for i in range(len(encr_text)):
#if * change a
    if encr_text[i] == "*":
        decr_text +="a"
#if & change e
    elif encr_text[i] == "&":
        decr_text +="e"
#if # change i
    elif encr_text[i] == "#":
        decr_text +="i"
#if + change o
    elif encr_text[i] == "+":
        decr_text +="o"
#if ! change u
    elif encr_text[i] == "!":
        decr_text +="u"
    else:
        decr_text +=encr_text[i]
#print output
print ("=*"*80)
print (pyfiglet.figlet_format(decr_text, font="smkeyboard", justify="center"))
print ("=*"*80)