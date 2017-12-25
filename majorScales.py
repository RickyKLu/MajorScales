#! python3 
# majorScales.py - program that asks user for the name of a major scale and 
#   the solfege  name of the note (i.e. Do, Re, Mi...) and returns that 
#   corresponding note in the scale

# list of notes in scale
chromScale = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'] 
# list of solfege 
#solfege = ['Do', 'Re', 'Mi', 'Fa', 'So', 'La', 'Ti'] 
solfege = {'Do':0, 'Re':2, 'Mi':4, 'Fa':5, 'So':7, 'La':9, 'Ti':11} 

# ask user for major scale
while True:
    maj_Scale = input("What major scale?\n  >> ")
    if maj_Scale not in chromScale:
        print ("Invalid input. Try again.\n")
    else:
        break

# ask user for solfege 
while True:
    sol = input("What solfege?\n >> ")
    if sol not in solfege:
        print ("Invalid input. Try again.\n")
    else:
        break

# take slice starting with the index to create new scale
indexScale = chromScale.index(maj_Scale)
indexSol = solfege[sol]
#print("Solfege index is {}".format(indexSol))

newScale = chromScale[indexScale:] + chromScale[:indexScale]
print("New scale is:\n {}\n".format(newScale))

newNote = newScale[indexSol]
print("The corresponding note is: {}\n".format(newNote))

