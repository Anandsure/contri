import os
import time as t
import random as rand
import subprocess
while True:
    t.sleep(8)
    print('starting')
    f= open("topush.txt","w+")
    ch = rand.randint(0,9)
    f.write(str(ch))
    subprocess.call(["git", "add" , "."])
    subprocess.call(["git","commit","-m",'''"test push"'''])
    subprocess.call(["git" , "push"])
    print('pushed')