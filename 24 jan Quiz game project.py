#QUIZ GAME PROJECT
file_name = "high_score.txt"
score=0
high_score = 0
#load high_score
def load_high_score():
    global high_score
    try:
        file= open(file_name,"r")                   # open the file in read mode
        high_score = int(file.read())
        file.close()
    except :
        pass

#save high score

def save_high_score():
    file = open(file_name,"w")                   # open the file in write mode  
    file.write(str(high_score))
    file.close()
def play_quiz():
    global score
    questions = ["What is the output of (2+3)?","which datatype stores True/False","Which key word is used to fetch global variable in the function?"]
    answers = ["5","Bool","Global"]
    for i in range(len(questions)):
        print("\nQ.",questions[i])  
        user_input = input("Enter your answer: ")
        if user_input.lower() == answers[i].lower():
            score+=1
            print("Correct")
        else:
            print("Incorrect")
    print("Your final score is:",score)
    
def main():
    global high_score
    load_high_score()
    name = input("ENter your name: ")
    print("Welcome""to the quiz",name,"!!")
    play_quiz()
    print("**You have completed the quiz**")
    if score>high_score:
        high_score = score
        save_high_score()
        print("Congratulations!! You have set a new high score")
    else:
        print("Thank you for playing")
main()        