from pyfiglet import Figlet
import sys
import random

figlet = Figlet()

if len(sys.argv) == 1:
    hasOneArg = True
elif len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "-f"):
    hasOneArg = False
else:
    print("Invalid Usage")
    sys.exit()


text = input("Input: ")

if hasOneArg == True:
    font = random.choice(figlet.getFonts())
    figlet.setFont(font= font)
else:
    try:
        figlet.setFont(font= sys.argv[2])
    except:
        print("Invalid Usage")
        sys.exit()

print(figlet.renderText(text))
