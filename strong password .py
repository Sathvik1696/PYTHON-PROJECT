'''
#1.Generate random password
#2.Check Password strength
#3.count character used in password
#4.gives a strength score using math
#5.saves the result in a file using os
'''

import math
import random
import os
import re
from collections import Counter

password=random.choice(["Sathvik@9696","Ram@916","Seth@12387"])         #randomly choose a password
  
pattern=r"^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*@).{8,}$"               #regex pattern used for checking the choosen password
if re.search(pattern,password):       
    passwordstrength="Strong"                                         # for checking the password strength
else:
    passwordstrength="Weak"

Character_count=Counter(password)                                     #character count(to count how many characters are there)
character_length = len(password)                             
strength_score=math.ceil(character_length/2)                          # strength score 

if not os.path.exists("password_reports"):                            #checks does file exist or not
    os.mkdir("password_reports")                                      #make file 
file_path=os.path.join("password_reports","password_report.txt")   

file = open(file_path,"w")                                            #write the file path which created
file.write(f"Generated Password:{password}")                  
file.write(f"Password Strength:{passwordstrength}")
file.write(f"Character Count:{character_length}")
file.write(f"Strength Score:{strength_score}")
file.write("Character Count:\n")

for ch,count in Character_count.items():
    file.write(f"{ch} : {count}\n")                                   #write each charactr and its count together
    
file.close()

print(password)                                       #prints password
print(passwordstrength)                               #prints password strength
print(Character_count)                                #prints countof characters
print(strength_score)                                 #prints strength score of password

print(file_path)                                      #prints file path
