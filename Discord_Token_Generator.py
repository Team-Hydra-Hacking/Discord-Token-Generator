#---------------------------------------------Discord Token Generator---(Developed By Dasher#1111)----------------------------------------#
import random
import string 
import os
import pyfiglet
from os import system, name
from colorama import Fore, Back, Style


print(Fore.MAGENTA)
name = pyfiglet.figlet_format("Discord Token Generator") 
print(name)
print("Developed By ＤＡＳＨＥＲ#1111")

print("NOTE! 1 token loop = 5 Tokens of different types. ")
N = input("How many tokens loop?: ")
count = 0
current_path = os.path.dirname(os.path.realpath(__file__))
while(int(count)<int(N)):
    firstGen = random.choice(string.ascii_letters).upper()+random.choice(string.ascii_letters).upper()+random.choice(string.ascii_letters)+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(21))+"."+ random.choice(string.ascii_letters).upper()+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5))+"."+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(27))
    secondGen = "MT"+random.choice(string.ascii_letters)+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(21))+"."+random.choice(string.ascii_letters).upper()+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5))+"."+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(27))
    thirdGen = "NT"+random.choice(string.ascii_letters)+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(21))+"."+random.choice(string.ascii_letters).upper()+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5))+"."+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(27))
    fourthGen = "MD"+random.choice(string.ascii_letters)+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(21))+"."+random.choice(string.ascii_letters).upper()+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5))+"."+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(27))
    fifthGen = "MT"+random.choice(string.ascii_letters)+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(21))+"."+random.choice(string.ascii_letters).upper()+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(5))+"."+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(27))
    f= open(current_path+"/"+str("Generated Tokens")+str("")+".txt","a")
    f.write(firstGen+"\n"+secondGen+"\n"+thirdGen+"\n"+fourthGen+"\n"+fifthGen+"\n")
    print(firstGen)
    print(secondGen)
    print(thirdGen)
    print(fourthGen)
    print(fifthGen)
    count+=1