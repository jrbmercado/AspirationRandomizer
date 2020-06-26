# Sims Aspiration Randomizer
# Created by Justin Mercado
# Completed 6/26/20
# To generate exe from python file, pyinstaller --onefile -w AspirationGenerator.py

import tkinter as tk
import random

# Create Window
root = tk.Tk()
root.title("Sims 4 Aspiration Randomizer")

# Define State Variables for Checkboxes
animalVar1 = tk.IntVar()
athleticVar1 = tk.IntVar()
creativityVar1 = tk.IntVar()
creativityVar2 = tk.IntVar()
creativityVar3 = tk.IntVar()
creativityVar4 = tk.IntVar()
creativityVar5 = tk.IntVar()
devianceVar1 = tk.IntVar()
devianceVar2 = tk.IntVar()
familyVar1 = tk.IntVar()
familyVar2 = tk.IntVar()
familyVar3 = tk.IntVar()
familyVar4 = tk.IntVar()
foodVar1 = tk.IntVar()
foodVar2 = tk.IntVar()
fortuneVar1 = tk.IntVar()
fortuneVar2 = tk.IntVar()
knowledgeVar1 = tk.IntVar()
knowledgeVar2 = tk.IntVar()
knowledgeVar3 = tk.IntVar()
knowledgeVar4 = tk.IntVar()
knowledgeVar5 = tk.IntVar()
knowledgeVar6 = tk.IntVar()
knowledgeVar7 = tk.IntVar()
locationVar1 = tk.IntVar()
locationVar2 = tk.IntVar()
locationVar3 = tk.IntVar()
loveVar1 = tk.IntVar()
loveVar2 = tk.IntVar()
natureVar1 = tk.IntVar()
natureVar2 = tk.IntVar()
natureVar3 = tk.IntVar()
natureVar4 = tk.IntVar()
natureVar5 = tk.IntVar()
natureVar6 = tk.IntVar()
natureVar7 = tk.IntVar()
popularityVar1 = tk.IntVar()
popularityVar2 = tk.IntVar()
popularityVar3 = tk.IntVar()
popularityVar4 = tk.IntVar()
popularityVar5 = tk.IntVar()
popularityVar6 = tk.IntVar()

# Create Generation Variables
generatedAspiration = tk.StringVar()
generatedAspiration.set("")


# Prints state of checkboxes for debugging purposes
def debugCheckboxes():
    print("Animal " + str(animalVar1.get()))
    print("Athletic " + str(athleticVar1.get()))
    print("Creativity " + str(creativityVar1.get()))
    print("Creativity " + str(creativityVar2.get()))
    print("Creativity " + str(creativityVar3.get()))
    print("Creativity " + str(creativityVar4.get()))
    print("Creativity " + str(creativityVar5.get()))
    print("Deviance " + str(devianceVar1.get()))
    print("Deviance " + str(devianceVar2.get()))
    print("Family " + str(familyVar1.get()))
    print("Family " + str(familyVar2.get()))
    print("Family " + str(familyVar3.get()))
    print("Family " + str(familyVar4.get()))
    print("Food " + str(foodVar1.get()))
    print("Food " + str(foodVar2.get()))
    print("Fortune " + str(fortuneVar1.get()))
    print("Fortune " + str(fortuneVar2.get()))
    print("Knowledge " + str(knowledgeVar1.get()))
    print("Knowledge " + str(knowledgeVar2.get()))
    print("Knowledge " + str(knowledgeVar3.get()))
    print("Knowledge " + str(knowledgeVar4.get()))
    print("Knowledge " + str(knowledgeVar5.get()))
    print("Knowledge " + str(knowledgeVar6.get()))
    print("Knowledge " + str(knowledgeVar7.get()))
    print("Location " + str(locationVar1.get()))
    print("Location " + str(locationVar2.get()))
    print("Location " + str(locationVar3.get()))
    print("Love " + str(loveVar1.get()))
    print("Love " + str(loveVar2.get()))
    print("Nature " + str(natureVar1.get()))
    print("Nature " + str(natureVar2.get()))
    print("Nature " + str(natureVar3.get()))
    print("Nature " + str(natureVar4.get()))
    print("Nature " + str(natureVar5.get()))
    print("Nature " + str(natureVar6.get()))
    print("Nature " + str(natureVar7.get()))
    print("Popularity " + str(popularityVar1.get()))
    print("Popularity " + str(popularityVar2.get()))
    print("Popularity " + str(popularityVar3.get()))
    print("Popularity " + str(popularityVar4.get()))
    print("Popularity " + str(popularityVar5.get()))
    print("Popularity " + str(popularityVar6.get()))


# Checks the state of all check boxes then randomly selects from ones active, updates label with result
def generate():
    # debugCheckboxes()

    # Aspiration Random Generator
    # Check state of all checkboxes and update list of possibilities
    listOfPossibleAspirations = []
    if animalVar1.get() == 1:
        listOfPossibleAspirations.append("Friend of the Animals")
    if athleticVar1.get() == 1:
        listOfPossibleAspirations.append("Bodybuilding")
    if creativityVar1.get() == 1:
        listOfPossibleAspirations.append("Painter Extraordinaire")
    if creativityVar2.get() == 1:
        listOfPossibleAspirations.append("Musical Genius")
    if creativityVar3.get() == 1:
        listOfPossibleAspirations.append("Bestselling Author")
    if creativityVar4.get() == 1:
        listOfPossibleAspirations.append("Master Actor")
    if creativityVar5.get() == 1:
        listOfPossibleAspirations.append("Master Maker")
    if devianceVar1.get() == 1:
        listOfPossibleAspirations.append("Public Enemy")
    if devianceVar2.get() == 1:
        listOfPossibleAspirations.append("Chief of Mischief")
    if familyVar1.get() == 1:
        listOfPossibleAspirations.append("Successful Lineage")
    if familyVar2.get() == 1:
        listOfPossibleAspirations.append("Big Happy Family")
    if familyVar3.get() == 1:
        listOfPossibleAspirations.append("Super Parent")
    if familyVar4.get() == 1:
        listOfPossibleAspirations.append("Vampire Family")
    if foodVar1.get() == 1:
        listOfPossibleAspirations.append("Master Chief")
    if foodVar2.get() == 1:
        listOfPossibleAspirations.append("Master Mixologist")
    if fortuneVar1.get() == 1:
        listOfPossibleAspirations.append("Fabulous Wealthy")
    if fortuneVar2.get() == 1:
        listOfPossibleAspirations.append("Mansion Baron")
    if knowledgeVar1.get() == 1:
        listOfPossibleAspirations.append("Renaissance Sim")
    if knowledgeVar2.get() == 1:
        listOfPossibleAspirations.append("Nerd Brain")
    if knowledgeVar3.get() == 1:
        listOfPossibleAspirations.append("Computer Whiz")
    if knowledgeVar4.get() == 1:
        listOfPossibleAspirations.append("Academic")
    if knowledgeVar5.get() == 1:
        listOfPossibleAspirations.append("Spellcraft & Sorcery")
    if knowledgeVar6.get() == 1:
        listOfPossibleAspirations.append("Master Vampire")
    if knowledgeVar7.get() == 1:
        listOfPossibleAspirations.append("Archeology Scholar")
    if locationVar1.get() == 1:
        listOfPossibleAspirations.append("Beach Life")
    if locationVar2.get() == 1:
        listOfPossibleAspirations.append("City Native")
    if locationVar3.get() == 1:
        listOfPossibleAspirations.append("StrangerVille Mystery")
    if loveVar1.get() == 1:
        listOfPossibleAspirations.append("Serial Romantic")
    if loveVar2.get() == 1:
        listOfPossibleAspirations.append("Soulmater")
    if natureVar1.get() == 1:
        listOfPossibleAspirations.append("Eco Innovator")
    if natureVar2.get() == 1:
        listOfPossibleAspirations.append("Freelance Botanist")
    if natureVar3.get() == 1:
        listOfPossibleAspirations.append("The Curator")
    if natureVar4.get() == 1:
        listOfPossibleAspirations.append("Angling Ace")
    if natureVar5.get() == 1:
        listOfPossibleAspirations.append("Purveyor of Potions")
    if natureVar6.get() == 1:
        listOfPossibleAspirations.append("Outdoor Enthusiast")
    if natureVar7.get() == 1:
        listOfPossibleAspirations.append("Jungle Explorer")
    if popularityVar1.get() == 1:
        listOfPossibleAspirations.append("Joke Star")
    if popularityVar2.get() == 1:
        listOfPossibleAspirations.append("Party Animal")
    if popularityVar3.get() == 1:
        listOfPossibleAspirations.append("Friend of the World")
    if popularityVar4.get() == 1:
        listOfPossibleAspirations.append("Leader of the Pack")
    if popularityVar5.get() == 1:
        listOfPossibleAspirations.append("Good Vampire")
    if popularityVar6.get() == 1:
        listOfPossibleAspirations.append("World-Famous Celebrity")

    # Randomly select from list of possible aspirations
    if len(listOfPossibleAspirations) == 0:
        pass
    else:
        global generatedAspiration
        pick = random.randint(0, len(listOfPossibleAspirations) - 1)
        generatedAspiration.set(str(listOfPossibleAspirations[pick]))


def checkAll():
    animal1CheckButton.select()
    athletic1CheckButton.select()
    creativity1CheckButton.select()
    creativity2CheckButton.select()
    creativity3CheckButton.select()
    creativity4CheckButton.select()
    creativity5CheckButton.select()
    deviance1CheckButton.select()
    deviance2CheckButton.select()
    family1CheckButton.select()
    family2CheckButton.select()
    family3CheckButton.select()
    family4CheckButton.select()
    food1CheckButton.select()
    food2CheckButton.select()
    fortune1CheckButton.select()
    fortune2CheckButton.select()
    knowledge1CheckButton.select()
    knowledge2CheckButton.select()
    knowledge3CheckButton.select()
    knowledge4CheckButton.select()
    knowledge5CheckButton.select()
    knowledge6CheckButton.select()
    knowledge7CheckButton.select()
    location1CheckButton.select()
    location2CheckButton.select()
    location3CheckButton.select()
    love1CheckButton.select()
    love2CheckButton.select()
    nature1CheckButton.select()
    nature2CheckButton.select()
    nature3CheckButton.select()
    nature4CheckButton.select()
    nature5CheckButton.select()
    nature6CheckButton.select()
    nature7CheckButton.select()
    popularity1CheckButton.select()
    popularity2CheckButton.select()
    popularity3CheckButton.select()
    popularity4CheckButton.select()
    popularity5CheckButton.select()
    popularity6CheckButton.select()


def uncheckAll():
    animal1CheckButton.deselect()
    athletic1CheckButton.deselect()
    creativity1CheckButton.deselect()
    creativity2CheckButton.deselect()
    creativity3CheckButton.deselect()
    creativity4CheckButton.deselect()
    creativity5CheckButton.deselect()
    deviance1CheckButton.deselect()
    deviance2CheckButton.deselect()
    family1CheckButton.deselect()
    family2CheckButton.deselect()
    family3CheckButton.deselect()
    family4CheckButton.deselect()
    food1CheckButton.deselect()
    food2CheckButton.deselect()
    fortune1CheckButton.deselect()
    fortune2CheckButton.deselect()
    knowledge1CheckButton.deselect()
    knowledge2CheckButton.deselect()
    knowledge3CheckButton.deselect()
    knowledge4CheckButton.deselect()
    knowledge5CheckButton.deselect()
    knowledge6CheckButton.deselect()
    knowledge7CheckButton.deselect()
    location1CheckButton.deselect()
    location2CheckButton.deselect()
    location3CheckButton.deselect()
    love1CheckButton.deselect()
    love2CheckButton.deselect()
    nature1CheckButton.deselect()
    nature2CheckButton.deselect()
    nature3CheckButton.deselect()
    nature4CheckButton.deselect()
    nature5CheckButton.deselect()
    nature6CheckButton.deselect()
    nature7CheckButton.deselect()
    popularity1CheckButton.deselect()
    popularity2CheckButton.deselect()
    popularity3CheckButton.deselect()
    popularity4CheckButton.deselect()
    popularity5CheckButton.deselect()
    popularity6CheckButton.deselect()


# Results Frame
resultsFrame = tk.Frame(root)
resultsFrame.grid(row=0, column=0, columnspan=5)

resultLabel = tk.Label(resultsFrame, text="Results", bg="#32a8a2", padx=340, pady=2)
resultLabel.grid(row=0, column=0, columnspan=5)

aspirationResultLabel = tk.Label(resultsFrame, text="Aspiration: ", padx=45, pady=2)
aspirationResultLabel.grid(row=1, column=0)

aspirationResultText = tk.Label(resultsFrame, textvariable=generatedAspiration, padx=45, pady=2)
aspirationResultText.grid(row=1, column=1)

generateButton = tk.Button(resultsFrame, text="Generate", bg="#19d13e", padx=50, pady=2, command=generate)
generateButton.grid(row=1, column=4)

checkAllButton = tk.Button(resultsFrame, text="Check All", bg="#d6d6d6", padx=36, pady=2, command=checkAll)
checkAllButton.grid(row=1, column=2)

uncheckAllButton = tk.Button(resultsFrame, text="Uncheck All", bg="#d6d6d6", padx=30, pady=2, command=uncheckAll)
uncheckAllButton.grid(row=2, column=2)

# Aspiration Selection Frame
aspirationFrame = tk.Frame(root)
aspirationFrame.grid(row=1, column=0, columnspan=5)

aspirationLabel = tk.Label(aspirationFrame, text="Aspirations", bg="#32a8a2", padx=329, pady=2)
aspirationLabel.grid(row=0, column=0, columnspan=5)

# Animal
animalLabel = tk.Label(aspirationFrame, text="Animal", bg="#3295a8", padx=45, pady=2)
animalLabel.grid(row=1, column=0)

animal1CheckButton = tk.Checkbutton(aspirationFrame, text="Friend of the Animals", variable=animalVar1)
animal1CheckButton.grid(row=2, column=0)
animal1CheckButton.select()

# Athletic
athleticLabel = tk.Label(aspirationFrame, text="Athletic", bg="#3295a8", padx=45, pady=2)
athleticLabel.grid(row=1, column=1)

athletic1CheckButton = tk.Checkbutton(aspirationFrame, text="Bodybuilding", variable=athleticVar1)
athletic1CheckButton.grid(row=2, column=1)
athletic1CheckButton.select()

# Creativity
creativityLabel = tk.Label(aspirationFrame, text="Creativity", bg="#3295a8", padx=45, pady=2)
creativityLabel.grid(row=1, column=2)

creativity1CheckButton = tk.Checkbutton(aspirationFrame, text="Painter Extraordinaire", variable=creativityVar1)
creativity1CheckButton.grid(row=2, column=2)
creativity1CheckButton.select()

creativity2CheckButton = tk.Checkbutton(aspirationFrame, text="Musical Genius", variable=creativityVar2)
creativity2CheckButton.grid(row=3, column=2)
creativity2CheckButton.select()

creativity3CheckButton = tk.Checkbutton(aspirationFrame, text="Bestselling Author", variable=creativityVar3)
creativity3CheckButton.grid(row=4, column=2)
creativity3CheckButton.select()

creativity4CheckButton = tk.Checkbutton(aspirationFrame, text="Master Actor", variable=creativityVar4)
creativity4CheckButton.grid(row=5, column=2)
creativity4CheckButton.select()

creativity5CheckButton = tk.Checkbutton(aspirationFrame, text="Master Maker", variable=creativityVar5)
creativity5CheckButton.grid(row=6, column=2)
creativity5CheckButton.select()

# Deviance
devianceLabel = tk.Label(aspirationFrame, text="Deviance", bg="#3295a8", padx=35, pady=2)
devianceLabel.grid(row=1, column=3)

deviance1CheckButton = tk.Checkbutton(aspirationFrame, text="Public Enemy", variable=devianceVar1)
deviance1CheckButton.grid(row=2, column=3)
deviance1CheckButton.select()

deviance2CheckButton = tk.Checkbutton(aspirationFrame, text="Chief of Mischief", variable=devianceVar2)
deviance2CheckButton.grid(row=3, column=3)
deviance2CheckButton.select()

# Family
familyLabel = tk.Label(aspirationFrame, text="Family", bg="#3295a8", padx=40, pady=2)
familyLabel.grid(row=1, column=4)

family1CheckButton = tk.Checkbutton(aspirationFrame, text="Successful Lineage", variable=familyVar1)
family1CheckButton.grid(row=2, column=4)
family1CheckButton.select()

family2CheckButton = tk.Checkbutton(aspirationFrame, text="Big Happy Family", variable=familyVar2)
family2CheckButton.grid(row=3, column=4)
family2CheckButton.select()

family3CheckButton = tk.Checkbutton(aspirationFrame, text="Super Parent", variable=familyVar3)
family3CheckButton.grid(row=4, column=4)
family3CheckButton.select()

family4CheckButton = tk.Checkbutton(aspirationFrame, text="Vampire Family", variable=familyVar4)
family4CheckButton.grid(row=5, column=4)
family4CheckButton.select()

# Food
foodLabel = tk.Label(aspirationFrame, text="Food", bg="#3295a8", padx=45, pady=2)
foodLabel.grid(row=7, column=0)

food1CheckButton = tk.Checkbutton(aspirationFrame, text="Master Chief", variable=foodVar1)
food1CheckButton.grid(row=8, column=0)
food1CheckButton.select()

food2CheckButton = tk.Checkbutton(aspirationFrame, text="Master Mixologist", variable=foodVar2)
food2CheckButton.grid(row=9, column=0)
food2CheckButton.select()

# Fortune
fortuneLabel = tk.Label(aspirationFrame, text="Fortune", bg="#3295a8", padx=45, pady=2)
fortuneLabel.grid(row=7, column=1)

fortune1CheckButton = tk.Checkbutton(aspirationFrame, text="Fabulous Wealthy", variable=fortuneVar1)
fortune1CheckButton.grid(row=8, column=1)
fortune1CheckButton.select()

fortune2CheckButton = tk.Checkbutton(aspirationFrame, text="Mansion Baron", variable=fortuneVar2)
fortune2CheckButton.grid(row=9, column=1)
fortune2CheckButton.select()

# Knowledge
knowledgeLabel = tk.Label(aspirationFrame, text="Knowledge", bg="#3295a8", padx=35, pady=2)
knowledgeLabel.grid(row=7, column=2)

knowledge1CheckButton = tk.Checkbutton(aspirationFrame, text="Renaissance Sim", variable=knowledgeVar1)
knowledge1CheckButton.grid(row=8, column=2)
knowledge1CheckButton.select()

knowledge2CheckButton = tk.Checkbutton(aspirationFrame, text="Nerd Brain", variable=knowledgeVar2)
knowledge2CheckButton.grid(row=9, column=2)
knowledge2CheckButton.select()

knowledge3CheckButton = tk.Checkbutton(aspirationFrame, text="Computer Whiz", variable=knowledgeVar3)
knowledge3CheckButton.grid(row=10, column=2)
knowledge3CheckButton.select()

knowledge4CheckButton = tk.Checkbutton(aspirationFrame, text="Academic", variable=knowledgeVar4)
knowledge4CheckButton.grid(row=11, column=2)
knowledge4CheckButton.select()

knowledge5CheckButton = tk.Checkbutton(aspirationFrame, text="Spellcraft & Sorcery", variable=knowledgeVar5)
knowledge5CheckButton.grid(row=12, column=2)
knowledge5CheckButton.select()

knowledge6CheckButton = tk.Checkbutton(aspirationFrame, text="Master Vampire", variable=knowledgeVar6)
knowledge6CheckButton.grid(row=13, column=2)
knowledge6CheckButton.select()

knowledge7CheckButton = tk.Checkbutton(aspirationFrame, text="Archeology Scholar", variable=knowledgeVar7)
knowledge7CheckButton.grid(row=14, column=2)
knowledge7CheckButton.select()

# Location
locationLabel = tk.Label(aspirationFrame, text="Location", bg="#3295a8", padx=45, pady=2)
locationLabel.grid(row=7, column=3)

location1CheckButton = tk.Checkbutton(aspirationFrame, text="Beach Life", variable=locationVar1)
location1CheckButton.grid(row=8, column=3)
location1CheckButton.select()

location2CheckButton = tk.Checkbutton(aspirationFrame, text="City Native", variable=locationVar2)
location2CheckButton.grid(row=9, column=3)
location2CheckButton.select()

location3CheckButton = tk.Checkbutton(aspirationFrame, text="StrangerVille Mystery", variable=locationVar3)
location3CheckButton.grid(row=10, column=3)
location3CheckButton.select()

# Love
loveLabel = tk.Label(aspirationFrame, text="Love", bg="#3295a8", padx=45, pady=2)
loveLabel.grid(row=7, column=4)

love1CheckButton = tk.Checkbutton(aspirationFrame, text="Serial Romantic", variable=loveVar1)
love1CheckButton.grid(row=8, column=4)
love1CheckButton.select()

love2CheckButton = tk.Checkbutton(aspirationFrame, text="Soulmater", variable=loveVar2)
love2CheckButton.grid(row=9, column=4)
love2CheckButton.select()

# Nature
natureLabel = tk.Label(aspirationFrame, text="Nature", bg="#3295a8", padx=45, pady=2)
natureLabel.grid(row=15, column=0)

nature1CheckButton = tk.Checkbutton(aspirationFrame, text="Eco Innovator", variable=natureVar1)
nature1CheckButton.grid(row=16, column=0)
nature1CheckButton.select()

nature2CheckButton = tk.Checkbutton(aspirationFrame, text="Freelance Botanist", variable=natureVar2)
nature2CheckButton.grid(row=17, column=0)
nature2CheckButton.select()

nature3CheckButton = tk.Checkbutton(aspirationFrame, text="The Curator", variable=natureVar3)
nature3CheckButton.grid(row=18, column=0)
nature3CheckButton.select()

nature4CheckButton = tk.Checkbutton(aspirationFrame, text="Angling Ace", variable=natureVar4)
nature4CheckButton.grid(row=19, column=0)
nature4CheckButton.select()

nature5CheckButton = tk.Checkbutton(aspirationFrame, text="Purveyor of Potions", variable=natureVar5)
nature5CheckButton.grid(row=20, column=0)
nature5CheckButton.select()

nature6CheckButton = tk.Checkbutton(aspirationFrame, text="Outdoor Enthusiast", variable=natureVar6)
nature6CheckButton.grid(row=21, column=0)
nature6CheckButton.select()

nature7CheckButton = tk.Checkbutton(aspirationFrame, text="Jungle Explorer", variable=natureVar7)
nature7CheckButton.grid(row=22, column=0)
nature7CheckButton.select()

# Popularity
popularityLabel = tk.Label(aspirationFrame, text="Popularity", bg="#3295a8", padx=45, pady=2)
popularityLabel.grid(row=15, column=1)

popularity1CheckButton = tk.Checkbutton(aspirationFrame, text="Joke Star", variable=popularityVar1)
popularity1CheckButton.grid(row=16, column=1)
popularity1CheckButton.select()

popularity2CheckButton = tk.Checkbutton(aspirationFrame, text="Party Animal", variable=popularityVar2)
popularity2CheckButton.grid(row=17, column=1)
popularity2CheckButton.select()

popularity3CheckButton = tk.Checkbutton(aspirationFrame, text="Friend of the World", variable=popularityVar3)
popularity3CheckButton.grid(row=18, column=1)
popularity3CheckButton.select()

popularity4CheckButton = tk.Checkbutton(aspirationFrame, text="Leader of the Pack", variable=popularityVar4)
popularity4CheckButton.grid(row=19, column=1)
popularity4CheckButton.select()

popularity5CheckButton = tk.Checkbutton(aspirationFrame, text="Good Vampire", variable=popularityVar5)
popularity5CheckButton.grid(row=20, column=1)
popularity5CheckButton.select()

popularity6CheckButton = tk.Checkbutton(aspirationFrame, text="World-Famous Celebrity", variable=popularityVar6)
popularity6CheckButton.grid(row=21, column=1)
popularity6CheckButton.select()

root.mainloop()
