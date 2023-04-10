import sys
import operator
import time
import pgzrun
import pygame
import pgzero.clock




WIDTH=1280 #Setting up dimensions for window size, question, time, and answers.

HEIGHT=720

main_box = Rect(0, 0, 820, 240) 
timer_box = Rect(0, 0, 240, 240)
answer_box1 = Rect(0, 0, 495, 165)
answer_box2 = Rect(0, 0, 495, 165)
answer_box3 = Rect(0, 0, 495, 165)
answer_box4 = Rect(0, 0, 495, 165)

main_box.move_ip(50, 40) #placing question, time, and answer
timer_box.move_ip (990, 40)
answer_box1.move_ip(50,358)
answer_box2.move_ip(735,358)
answer_box3.move_ip(50,538)
answer_box4.move_ip(735,538)

answer_boxes = [answer_box1, answer_box2, answer_box3, answer_box4] #used to list answer


score=0 #number of questions successfully answered

time_left = 10 #Time remaining

# All Questions
q1= ["Who wrote the Declaration of Independence?",
     "George Washington", "Thomas Jefferson", "Benjamin Franklin", "Alexander Hamilton", 2]

q2= ["Which pharaoh was buried in the Great Pyramid?",
     "Sneferu", "Khafre", "Khufu", "Djedefre", 3]

q3= ["Which Civil War General led the March to the Sea?",
     "Ulysses S. Grant", "George B. McClellan", "George G. Meade", "William Tecumseh Sherman", 4]

q4= ["Carl Benz created which of these vehicles?",
     "Train", "Automobile", "Airplane", "Tank", 2]

q5= ["Joan of Arc fought for which country?",
     "England", "Ireland", "France", "Germany", 3]

q6= ["The body of which Soviet Leader is on display in Red Square?",
     "Vladimir Lenin", "Joseph Stalin", "Nikita Khrushchev", "Mikhail Gorbachev", 1]

q7= ["Who was the first man on the Moon?",
     "Buzz Aldrin", "Gus Grissom", "Gene Cernan", "Neil Armstrong", 4]

q8= ["Who discovered that Jupiter had moons?",
     "Tycho Brahe", "Galileo Galilei", "Nicolaus Copernicus", "Johannes Kepler", 2]

q9= ["William the Conqueror is known for conquering which country?",
     "England", "Spain", "France", "Germany", 1]

q10= ["What home appliance is James M. Spanger best known for inventing?",
     "Air Conditioner", "Dishwasher", "Electric Vacuum Cleaner", "Electric Stove", 3]



questions = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10] #Listing Questions

question =questions.pop(0)

def draw():
    screen.fill ("black")  #add elements to screen
    screen.draw.filled_rect (main_box, "light sea green")
    screen.draw.filled_rect (timer_box, "light sea green")
    for box in answer_boxes:
        screen.draw.filled_rect (box, "hot pink")
    screen.draw.textbox (str(time_left), timer_box, color=("black")) #Add Text
    screen.draw.textbox(question[0], main_box, color=("black"))
    
    index =1 # Adds text to each answer box
    for box in answer_boxes:
        screen.draw.textbox(question [index], box, color=("black"))
        index=index+1

def game_over(): #Displays score when game ends and blanks out questions
    global question, time_left
    message="Game over. you got %s questions correct" %str(score)
    question = [message, "-", "-", "-", "-",5]
    time_left = 0

def correct_answer(): #Add point and move to next screen when answer is correct.
    global question, score, time_left
    
    score= score+1
    if questions: 
        question=questions.pop(0)
        time_left=10
    else:
        print("End of questions")
        game_over()

def on_mouse_down(pos): # accept clicks and determine if the correct box has been clicked.
    index=1
    for box in answer_boxes:
        if box.collidepoint(pos):
            print ("Clicked on answer"+str(index))
            if index == question [5]:
                print("You got it correct!")
                correct_answer()
            else:  #Goes to game over screen if answer is incorrect.
                game_over()
        index=index+1

def update_time_left(): #count down time
    global time_left
    if time_left:
        time_left=time_left-1
    else: # Game ends if time expires
        game_over()

def on_key_up(key): #Adds hint and skip functionality
    global score
    if key==keys.H: # Provides answer if "H" is pressed
        print ("The correct answer is box number %s" % question[5])
    
    if key==keys.SPACE: # Skips question and deducts point if S is pressed.
        score=score-1
        correct_answer()
    
clock.schedule_interval(update_time_left, 1.0) #updates clock

pgzrun.go()