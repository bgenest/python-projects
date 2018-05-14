
alphabet = "abcdefghijklmnopqrstuvwxyz"

key = 3

message = input ("Please enter a message: ")
newMessage = ''
newMessage1= ''


for character in message:
    if character in alphabet:
        position = alphabet.index(character)
        newPosition = (position + key) % 26
        newCharacter = alphabet[newPosition]
        #print('Encrypted character is:' , newCharacter)
        newMessage += newCharacter
    else:
        newMessage += character
print('Your encrypted message is:', newMessage)

for character in message:
    if character in alphabet:
        position = alphabet.index(character)
        newPosition1 = (position - key) % 26
        newCharacter1 = alphabet[newPosition1]
        # print('Encrypted character is:' , newCharacter)
        newMessage1 += newCharacter1
    else:
        newMessage1 += character

print('Your deencrypted message is' , newMessage1)