#! python3 
# majorScales.py - program that asks user for the name of a major scale and 
#   the solfege  name of the note (i.e. Do, Re, Mi...) and returns that 
#   corresponding note in the scale

# list of notes in scale
chromScale = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'] 
# list of solfege 
#solfege = ['Do', 'Re', 'Mi', 'Fa', 'So', 'La', 'Ti'] 
solfege = {'Do':0, 'Re':2, 'Mi':4, 'Fa':5, 'So':7, 'La':9, 'Ti':11} 

def note ( majScale, sol):
    #error checking 
    if majScale not in chromScale:
        return 1

    if sol not in solfege:
        return 1

    indexScale = chromScale.index(majScale)
    indexSol = solfege[sol]

    # take slice starting with the index to create new scale
    newScale = chromScale[indexScale:] + chromScale[:indexScale]
    #print("New scale is:\n {}\n".format(newScale))

    newNote = newScale[indexSol]
    print("The corresponding note is: {}".format(newNote))
# testing below
note('C', 'Do') #   C
note("C", "Re") #   D
note("C", "Mi") #   E
note("D", "Mi") #   F#
note("A#", "Fa") #  D#
