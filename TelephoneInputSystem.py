import unicodedata, re, os


def clearScreen():
	os.system('cls' if os.name == 'nt' else 'clear')

# Used to normalize inputs and make them caseless for comparison
def normalizeCaseless(text):
    return unicodedata.normalize("NFKD", text.casefold())

def printMenu():
    print("Please enter a valid option <ADD, DEL, LIST>:")

def getNameInput(nameType):
	if nameType is "middle":
		print("Please enter " + nameType + " name (leave blank if necessary): ")
	else:
		print("Please enter " + nameType + " name: ")
	return normalizeCaseless(input())
	
def getValidName(nameType):
	clearScreen()
	while True:
		name = getNameInput(nameType)
		# Middle name is not necessary, not all cultures use them
		if not name and nameType is "middle":
			return None
		pattern = re.compile("^([a-z]+[.\-']?)+$")
		if pattern.match(name):
			return name
		else:
			print("That was not a valid " + nameType + " name")
			
def getValidPhoneNumber():
	clearScreen()
	print("******************************")
	print("*        Phone Number        *")
	print("******************************")
	while True:
		print("Please enter the phone number: ")
		number = input()
		usPhoneNoParenthesis = re.compile("^1?[2-9]\d{2}([.\-\s])?\d{3}\\1?\d{4}$")
		usPhoneParenthesis = re.compile("^1?\\([2-9]\d{2}\\)([.\-\s])?\d{3}\\1\d{4}$")
		if usPhoneNoParenthesis.match(number) or usPhoneParenthesis.match(number):
			# Get all the keys from the dictionary and remove any non-numeric digit so I can compare
			keyList = [re.sub("[^0-9]", "", key) for key in phoneBook]
			tempNumb = re.sub("[^0-9]", "", number)
			if tempNumb in keyList:
				print("\nAn entry already exists for this number.")
			else:
				return number
		else:
			print("\nThat is not a valid US phone number")
		


# Start of program logic here
# Check file / begin read lines

# Dictionary key is the phone number, this should be unique
phoneBook = {}
while True:
    printMenu()
    userInput = normalizeCaseless(input())

    if userInput == normalizeCaseless("ADD"):
        # User wants to add a phone number
        firstName = getValidName("first")
        middleName = getValidName("middle")
        lastName = getValidName("last")
        number = getValidPhoneNumber()
        phoneBook[number] = (firstName, middleName, lastName)
        print(phoneBook)
        

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
