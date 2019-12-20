#Minh Vu
#Hangman Game
#10/22/2018

from graphics import *
import random

#This function will 
def readfile(aFile):

    infile = open(aFile, 'r')

    line = infile.readline()

    aList = []

    while line != '':

        line = line.rstrip('\n')
        aList.append(line)
        line = infile.readline()

    word = random.choice(aList)

    return word

def display(win, aList):

    stick1 = Line(Point(225, 300), Point(325, 300))
    stick1.draw(win)
        
    stick2 = Line(Point(275, 300), Point(275, 100))
    stick2.draw(win)

    stick3 = Line(Point(275, 100), Point(200, 100))
    stick3.draw(win)

    rope = Line(Point(200, 100), Point(200, 130))
    rope.draw(win)

    text1 = Text(Point(150, 350), 'Enter a letter:')
    text1.setSize(15)
    text1.draw(win)

    text2 = Text(Point(90, 370), 'Letters Available: ')
    text2.draw(win)
    text2.setSize(9)

    for i in range(len(aList)):

        space = Line(Point(120+i*22, 400), Point(132+i*22, 400))
        space.draw(win)


    button = Rectangle(Point(300, 340), Point(350, 360))
    button.setFill('pink')
    button.draw(win)

    label = Text(Point(325, 350), 'CLICK HERE')
    label.setSize(7)
    label.draw(win)

    return button
#this function make the user click into the button or else will trap in a loop
def clicked(win, button):

    clickPoint = win.getMouse()

    x1 = button.getP1().getX()
    y1 = button.getP1().getY()
    #extract the point of the button
    x2 = button.getP2().getX()
    y2 = button.getP2().getY()
    x = clickPoint.getX() # extract X and Y coords
    y = clickPoint.getY()
    
    while not (x1 < x and x2 > x and y1 < y and y2 > y):
        print('trap in loop')
        clickPoint = win.getMouse()
        x = clickPoint.getX() # extract X and Y coord
        y = clickPoint.getY()
    print('About to return True')

    

    
    
        
'''this function will put a new item at the right position, then we can have the needed list
this function serve in the alphabet funtion to create available letter
this function also serve to create a list of correct guessed letter to compare with
the original letter'''
def replaced(aList, pos, letter):

    aList[pos] = letter

#this function helps delete the guessed letter(actually replace it with '')
def alphabet(letter, alphabet):

    pos = -1
    for item in alphabet:

        pos += 1
        if letter == item:

            replaced(alphabet, pos, ' ')

    return alphabet
            
def play(win, orgList, button):

    num = len(orgList)

    print('This word has ', num, 'letters')

    entry = Entry(Point(250, 350), 10)
    entry.draw(win)

    #newList is a list of letters that the user guessed correctly
    newList = []

    #newList at first is a list with a number of '', the same number as the original list
    for i in range(len(orgList)):

        newList.append('')

    
    count = 0#this variable counts the time user guessed wrong

    letter = ''#this variable is the letter the user guessed each time
    alpha_list = Text(Point(135, 370), '')#Draw a list of available letters for the user
    alpha_list.draw(win)

    #this graphic_list create a list to later undraw the old list of available letters
    graphic_list = [alpha_list]

    wordList = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

    
    while count < 6 and newList != orgList:#to end the loop the user will guess wrong 6 times or have the same list of letters as the word

        #this loop undraw each letter in the letters available
        for obj in graphic_list:
            obj.undraw()

        #wordList is a list of available letters after each time the user guessed
        wordList = alphabet(letter, wordList)

        k = -1

        #this loop draw a vailable letters
        for item in wordList:

            k += 1

            alpha_list = Text(Point(135 + k * 10, 370), item)
            alpha_list.setSize(9)
            alpha_list.draw(win)

            graphic_list.append(alpha_list)
        
        
        clicked(win, button)#function to make user click into the button
        letter =  entry.getText()#get the letter from the entry box
        print('you guess', letter)

        if letter in orgList:

            print('this is right')
            
            pos = -1

            #this loop helps put the letter at the right position in the word
            for item in orgList:

                pos += 1

                if letter == item:

                    print('Correct')
                    print('this letter is at position', pos)
                    text = Text(Point(126 + pos * 22, 390), letter)
                    text.draw(win)
                    text.setSize(12)

                    replaced(newList, pos, letter)

        elif letter not in orgList:

            print('wrong')

            count += 1

            print('lost', count, 'chance')

            if count == 1:

                head = Circle(Point(200, 150), 20)
                head.draw(win)

            elif count == 2:

                body = Line(Point(200, 170), Point(200, 240))
                body.draw(win)
                
            elif count == 3:

                leftArm = Line(Point(200, 180), Point(180, 210))
                leftArm.draw(win)

            elif count == 4:

                rightArm = Line(Point(200, 180), Point(220, 210))
                rightArm.draw(win)

            elif count == 5:

                leftLeg = Line(Point(200, 240), Point(180, 295))
                leftLeg.draw(win)



    if count == 6:#the condition to lose
        
        rightLeg = Line(Point(200, 240), Point(220, 295))
        rightLeg.draw(win)
        print('lose')

        rectangle  = Rectangle(Point(350,430),Point(150,530))
        rectangle.setFill("light grey")
        rectangle.draw(win)
        
        #display the message 'YOU LOSE'
        message = Text(Point(250, 480,), "YOU DIE")
        message.setFill("Black")
        message.setSize(15)
        message.draw(win)

        #draw the answer when you lose the game
        pos = -1
        for item in orgList:

                pos += 1
                text = Text(Point(126 + pos * 22, 390), item)
                text.draw(win)
                text.setSize(12)

    elif newList == orgList:#the condition to win

        print('win')

        rectangle  = Rectangle(Point(350,430),Point(150,530))
        rectangle.setFill("light yellow")
        rectangle.draw(win)

        #display the message 'YOU WIN'
        message = Text(Point(250,480), "YOU LIVE")
        message.setFill("Black")
        message.setSize(15)
        message.draw(win)

                
        
        




def main():

    windowWidth = 500
    windowHeight = 600
    win = GraphWin('Hangman', windowWidth, windowHeight)
    win.setBackground('light sky blue')

    word = readfile('puzzles.txt')
    print(word)

    wordList = list(word)

    button = display(win, wordList)

    print(wordList)

    play(win, wordList, button)

    win.getMouse()
    win.close()


main()
