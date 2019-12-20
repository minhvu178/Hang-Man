#create graphics
from graphics import *

windowWidth = 500
windowHeight = 600
win = GraphWin('Hangman', windowWidth, windowHeight)

#Draw hang man

entry = Entry(Point(250, 350), 10)
entry.draw(win)

stick1 = Line(Point(225, 300), Point(325, 300))
stick1.draw(win)
    
stick2 = Line(Point(275, 300), Point(275, 100))
stick2.draw(win)

stick3 = Line(Point(275, 100), Point(200, 100))
stick3.draw(win)

rope = Line(Point(200, 100), Point(200, 130))
rope.draw(win)

head = Circle(Point(200, 150), 20)
head.draw(win)

body = Line(Point(200, 170), Point(200, 240))
body.draw(win)

leftArm = Line(Point(200, 180), Point(180, 210))
leftArm.draw(win)

rightArm = Line(Point(200, 180), Point(220, 210))
rightArm.draw(win)

leftLeg = Line(Point(200, 240), Point(180, 295))
leftLeg.draw(win)

rightLeg = Line(Point(200, 240), Point(220, 295))
rightLeg.draw(win)

text1 = Text(Point(150, 350), 'Enter a letter')
text1.draw(win)

button = Rectangle(Point(300, 360), Point(350, 340))
button.draw(win)

text2 = Text(Point(90, 370), 'Letters Available: ')
text2.draw(win)
text2.setSize(9)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

i = -1

for item in alphabet:

    i += 1

    text = Text(Point(135 + i * 10, 370), item)
    text.draw(win)
    text.setSize(9)


alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', ' ', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

i = -1
some = []

for item in alphabet:

    i += 1

    text = Text(Point(135 + i * 10, 370), item)
    text.draw(win)
    text.setSize(9)

    some.append(text)

for obj in some:

    t



            
