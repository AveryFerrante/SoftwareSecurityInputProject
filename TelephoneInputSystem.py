import unicodedata


# Used to normalize inputs and make them caseless for comparison
def normalizeCaseless(text):
    return unicodedata.normalize("NFKD", text.casefold())

def printMenu():
    print("Please enter a valid option <ADD, DEL, LIST>:")




# Start of program logic here
# Check file / begin read lines
# DO WE HAVE TO DO IT THE EXACT WAY THE PAPER SAYS??
while True:
    printMenu()
    userInput = normalizeCaseless(input())
    print(userInput)

    if userInput == normalizeCaseless("ADD"):
        # User wants to add a phone number
        pass

    elif userInput == normalizeCaseless("DEL"):
        # User wants to delete a phone number
        pass

    elif userInput == normalizeCaseless("LIST"):
        # List all current entries
        pass

    elif userInput == normalizeCaseless("QUIT") or userInput == normalizeCaseless("Q"):
        break;

    else:
        print("Option not recognized")
