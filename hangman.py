# hangman.py

# Name:Gia
# Collaborators:
from graphics import *
from time import sleep
win = GraphWin("hangman", 400, 500)
win.setBackground("lightcyan")
#Scaffold code here
def scaffold():
    bottom_line = Line(Point(100, 300), Point(300,300))
    up_line = Line(Point(200,300), Point(200,100))
    top_line = Line(Point(200,100), Point(275,100))
    hang_line = Line(Point(275, 100), Point(275,150))
    bottom_line.draw(win)
    up_line.draw(win)
    top_line.draw(win)
    hang_line.draw(win)
scaffold()
#Head code here
def head():
    head = Circle(Point(275, 170), 20)
    head.draw(win)

#Torso code here
def torso():
    body = Line(Point(275, 190), Point(275, 246))
    body.draw(win)

#Left Leg code here
def left_leg():
    left_leg = Line(Point(275, 245), Point(255, 285))
    left_leg.draw(win)

#Right Leg code here
def right_leg():
    right_leg = Line(Point(275,245), Point(295, 285))
    right_leg.draw(win)

#Left Arm code here
def left_arm():
    left_arm = Line(Point(275,218), Point(250,218))
    left_arm.draw(win)

#Right Arm code here
def right_arm():
    right_arm = Line(Point(275,218), Point(300, 218))
    right_arm.draw(win)
#intro
request_name1 = Text(Point(150, 50),"What is player one's name?")
request_name1.draw(win)
name_enter_1 = Entry(Point(150, 350), 20)
name_enter_1.draw(win)
key = win.checkKey()
while key != 'Return':
    key = win.checkKey()
name_1 = name_enter_1.getText()
request_name1.undraw()
name_enter_1.undraw()
display_name_1 = Text(Point(150,50),"Hello " + name_1)
display_name_1.draw(win)
time.sleep(.5)
display_name_1.undraw()
request_name2 = Text(Point(150, 50),"What is player two's name?")
request_name2.draw(win)
name_enter_2 = Entry(Point(150, 350), 20)
name_enter_2.draw(win)
key = win.checkKey()
while key != 'Return':
    key = win.checkKey()
name_2 = name_enter_2.getText()
request_name2.undraw()
name_enter_2.undraw()
display_name_2 = Text(Point(150,50),"Hello " + name_2)
display_name_2.draw(win)
time.sleep(.5)
display_name_2.undraw()

request_word = Text(Point(150, 50),name_1 + " input a word")
request_word.draw(win)
word_enter = Entry(Point(150, 350), 20)
word_enter.draw(win)
key = win.checkKey()
while key != 'Return':
    key = win.checkKey()
word_choice = word_enter.getText()
request_word.undraw()
word_enter.undraw()

display_guess = Text(Point(70, 75), "wrong guesses")
display_guess.draw(win)
letter_guess = []
b = 0
def guessing():
    global b
    request_guess = Text(Point(150, 50), name_2 + " please guess a letter",)
    request_guess.draw(win)
    guess_enter = Entry(Point(150, 350), 20)
    guess_enter.draw(win)
    key = win.checkKey()
    while key != 'Return':
        key = win.checkKey()
    guess = guess_enter.getText()
    request_guess.undraw()
    guess_enter.undraw()
    
    global letter_guess
    if guess in letter_guess:
        repeat_guess = Text(Point(150,50), "That was already guessed")
        repeat_guess.draw(win)
        time.sleep(.5)
        repeat_guess.undraw()

        guessing()
    if len(guess)!= 1 or guess == range(10000000):
        bad_guess = Text(Point(150,50), "That is not a valid guess")
        bad_guess.draw(win)
        time.sleep(.5)
        bad_guess.undraw()
##        print "Too many letters"
        guessing()
    letter_guess += guess
        
z_display = Text(Point(200,400), "")
z_display.draw(win)

def display(letter_guess, word_choice):
    z = ""
    for letter in word_choice:
        if letter in letter_guess:
            z += letter
        if letter not in letter_guess:
            z += " _ "
    z_display.setText(z)

x=0
y=0
p1_score = 0
p2_score = 0
word_choice_var = list(word_choice)
t=0
#code for scores
score_p1 = Text(Point(100,450), name_1 + "'s score:")
score_p1.draw(win)
score_p2 = Text(Point(200,450), name_2 + "'s score:")
score_p2.draw(win)
number_score_1 = Text(Point(100, 475), str(p1_score))
number_score_1.draw(win)
number_score_2 = Text(Point(200, 475), str(p2_score))
number_score_2.draw(win)
display_letter_guess = Text(Point (30,100 + b), "")
display_letter_guess.draw(win)
head = Circle(Point(275, 170), 20)
body = Line(Point(275, 190), Point(275, 246))
right_leg = Line(Point(275,245), Point(295, 285))
left_leg = Line(Point(275, 245), Point(255, 285))
right_arm = Line(Point(275,218), Point(300, 218))
left_arm = Line(Point(275,218), Point(250,218))
def game_over():
    global x
    global y
    global letter_guess
    global word_choice
    global word_choice_var
    global p1_score
    global p2_score
    global b
    global t
    guessing()
    display(letter_guess, word_choice)
    for letter in letter_guess[-1]:
        if letter in word_choice:
            x += 0
        if letter not in word_choice:
            x += 1
            a = display_letter_guess.getText() + letter
            display_letter_guess.setText(a)
            b += 15
            if x == 1:
                x1 = Text(Point(200,50),"Oh no! Only 5 more guesses remaining")
                x1.draw(win)
                head.draw(win)
                time.sleep(.5)
                x1.undraw()
            if x == 2:
                x2 = Text(Point(200,50), "Keep going! Only 4 more guesses remaining")
                x2.draw(win)
                body.draw(win)
                time.sleep(.5)
                x2.undraw()
            if x == 3:
                x3 = Text(Point(200,50),"Nope, try again! Only 3 more guesses remaining")
                x3.draw(win)
                right_leg.draw(win)
                time.sleep(.5)
                x3.undraw()
            if x == 4:
                x4 = Text(Point(200,50),"Keep trying! Only 2 more guesses reaming")
                x4.draw(win)
                left_leg.draw(win)
                time.sleep(.5)
                x4.undraw()
            if x == 5:
                x5 = Text(Point(200,50),"Whoops that's incorrect! Only 1 more guess reaming")
                x5.draw(win)
                right_arm.draw(win)
                time.sleep(.5)
                x5.undraw()
    if x == 6:
        x6 = Text(Point(200,50),"Oops there are no more guesses")
        x6.draw(win)
        left_arm.draw(win)
        time.sleep(.5)
        x6.undraw()
        game_over_1 = True
        time_1_game_over = Text(Point(200,50), "Game over." + name_1 + "wins!" )
        time_1_game_over.draw(win)
        time.sleep(.5)
        time_1_game_over.undraw()
        p1_score += 1
        number_score_1.setText(p1_score)
        display_guess.undraw()
        display_letter_guess.undraw()
        head.undraw()
        body.undraw()
        right_arm.undraw()
        left_arm.undraw()
        right_leg.undraw()
        left_leg.undraw()
        return game_over_1
    game_over_1 = True
    for word in word_choice:
        if word not in letter_guess:
            game_over_1 = False
            return game_over_1
    if game_over_1 == True:
        time_2_game_over = Text(Point(200,50), "Game over." + name_2 + "wins!")
        time_2_game_over.draw(win)
        time.sleep(.5)
        time_2_game_over.undraw()
        p2_score += 1
        number_score_2.setText(p2_score)
        display_guess.undraw()
        display_letter_guess.undraw()
        head.undraw()
        body.undraw()
        right_arm.undraw()
        left_arm.undraw()
        right_leg.undraw()
        left_leg.undraw()
        return game_over_1
while game_over() == False:
    pass

request_play_again = Text(Point(200,50), "Do you want to play agian? For yes type y for no type n")
request_play_again.draw(win)
play_again_enter = Entry(Point(150,350), 20)
play_again_enter.draw(win)
key= win.checkKey()
while key != 'Return':
    key= win.checkKey()
play_again = play_again_enter.getText()
request_play_again.undraw()
play_again_enter.undraw()

while play_again == "y":

    request_word = Text(Point(150, 50),name_1 + " input a word")
    request_word.draw(win)
    word_enter = Entry(Point(150, 350), 20)
    word_enter.draw(win)
    key = win.checkKey()
    while key != 'Return':
        key = win.checkKey()
    word_choice = word_enter.getText()
    request_word.undraw()
    word_enter.undraw()
    display_guess = Text(Point(70, 75), "wrong guesses")
    display_guess.draw(win)
    display_letter_guess = Text(Point (30,100 + b), "")
    display_letter_guess.draw(win)
    letter_guess = []
    x=0
    y=0
    while game_over()==False:
        pass
    
    request_play_again = Text(Point(200,50), "Do you want to play agian? For yes type y for no type n")
    request_play_again.draw(win)
    play_again_enter = Entry(Point(150,350), 20)
    play_again_enter.draw(win)
    key= win.checkKey()
    while key != 'Return':
        key= win.checkKey()
    play_again = play_again_enter.getText()
    request_play_again.undraw()
    play_again_enter.undraw()
end = Text(Point(200,50), "Thanks for playing")
end.draw(win)
time.sleep(.5)
win.close()

