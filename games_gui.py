# games_gui.py
# Program to catalog and select games.

from graphics import *

def main():

    win = GraphWin("Games Catalog", 400, 300)
    win.setCoords(0.0, 0.0, 3.0, 4.0)

    # Draw the interface
    Text(Point(.6,3), "Would you like to catalog?:").draw(win)
    input = Entry(Point(2,3), 25)
    input.setText("")
    input.draw(win)
    output = Text(Point(2,1), "")
    output.draw(win)

    # Quit after click
    win.getMouse()
    win.close()

main()
