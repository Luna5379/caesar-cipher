import string

initialPosition = 0
shiftedPosition = 0
lettersLower = string.ascii_lowercase
lettersUpper = string.ascii_uppercase
numbers = string.digits
symbols = string.punctuation
possibleCharacters = lettersLower + lettersUpper + numbers + symbols

def decrypt():
  shiftedPosition = (initialPosition - key)%len(possibleCharacters)
  return shiftedPosition

print("Welcome! This program will crack the Caesar cipher and figure out any secret message that was encrypted with the Caesar cipher. Type in your encrypted message and this program will print all of the key possibilities of your message below. \n\nYour message can only include the following characters: " + possibleCharacters + "\n\n")
initialMessage = input("What is your encrypted message? ")
input("\nPress enter to generate all of the key possibilities for your encrypted message.\n")

for key in range(len(possibleCharacters)):
  shiftedMessage = ""
  for character in initialMessage:
      if character in possibleCharacters:
        initialPosition = possibleCharacters.find(character)
        shiftedPosition = decrypt()

        shiftedMessage = shiftedMessage + possibleCharacters[shiftedPosition]

      else: 
        shiftedMessage = shiftedMessage + character

  print(shiftedMessage)

print("\nNow scroll through all of the key possibilities above and find the readable plaintext message.")
