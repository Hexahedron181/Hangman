import random
import linecache
import turtle

t = turtle.Turtle()
t.hideturtle()
t.speed(0)

def head():
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.circle(20)

def body():
    t.penup()
    t.goto(0, 0)
    t.pendown()
    t.setheading(270)
    t.fd(50)

def leg1():
    t.penup()
    t.goto(0, -50)
    t.pendown()
    t.setheading(315)
    t.fd(30)

def leg2():
    t.penup()
    t.goto(0, -50)
    t.pendown()
    t.setheading(225)
    t.fd(30)

def arm1():
    t.penup()
    t.goto(0, -25)
    t.pendown()
    t.setheading(180)
    t.fd(25)

def arm2():
    t.penup()
    t.goto(0, -25)
    t.pendown()
    t.setheading(0)
    t.fd(25)

def rope():
    t.penup()
    t.goto(0, 40)
    t.setheading(90)
    t.pendown()
    t.fd(20)

def top():
    t.penup()
    t.goto(0, 60)
    t.setheading(180)
    t.pendown()
    t.fd(70)

def side():
    t.penup()
    t.goto(-70, 60)
    t.setheading(270)
    t.pendown()
    t.fd(150)

def floor():
    t.penup()
    t.goto(-90, -90)
    t.setheading(0)
    t.pendown()
    t.fd(170)

def triangle():
    t.penup()
    t.goto(-40, 60)
    t.pendown()
    t.goto(-70, 30)

def words():

    Num = 0
    for i in range(0, len(letters)):
        print("{0:2}".format(letters[Num]),end=" ")
        Num = Num + 1
    print("\n")
    
print("\n\n==== WELCOME TO HANGMAN ===\n\n")

List = ["side", "top", "triangle", "rope", "floor", "head", "body", "leg1", "leg2", "arm1", "arm2"]
letters = []
Alpha = []
Num = random.randint(0, 300)
Word = linecache.getline("HMwords.txt", Num)

x = 0
for i in range(0, len(Word) - 1):
    Alpha.append(Word[x])
    x = x + 1

for i in range(0, len(Word) - 1):
    letters.append("_")

input("Press any button to start: ")
print("\n\nYour word is:\n")
Win = 0
hangman = 0
while Win == 0:
    
    print("\n")
    words()
    userInput = input("Letter: ")
    Num = 0
    check = 0
    points = 0
    for i in range(0, len(letters)):
        if userInput == Alpha[Num]:
            letters[Num] = userInput
            Alpha[Num] = "-"
            points = points + 1
        Num = Num + 1
    if points == 0:
        eval(List[hangman] + "()")
        if hangman == len(List) - 1:
            Win = 1
            print("YOU LOSE!")
            break
        hangman = hangman + 1
    Num = 0
    while check == 0:
        if letters[Num] != "_":
            Num = Num + 1
        else:
            check = 1
        if Num == len(letters):
            check = 1
            print("\n")
            words()
            print("\nWELL DONE YOU GUESSED THE WORD!!")
            Win = 1

    





