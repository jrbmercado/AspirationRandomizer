# Sims Aspiration Randomizer
# Created by Justin Mercado
# 6/25/20
# To generate exe from python file, pyinstaller --onefile -w AspirationGenerator.py

import tkinter as tk
import random

fields = ["Friend of the Animals", "Bodybuilder", "The Positivity Challenge",
          "Painter Extraordinaire", "Musical Genius", "Bestselling Author",
          "Master Actor/Master Actress", "Master Maker", "Public Enemy", "Chief of Mischief",
          "Successful Lineage", "Big Happy Family", "Vampire Family", "Super Parent", "Master Chef",
          "Master Mixologist", "Fabulously Wealthy", "Mansion Baron", "Renaissance Sim", "Nerd Brain",
          "Computer Whiz", "Master Vampire", "Archaeology Scholar", "Spellcraft & Sorcery", "Academic",
          "Serial Romantic", "Soulmate", "City Native", "StrangerVille Mystery", "Beach Life", "Freelance Botanist",
          "The Curator", "Angling Ace", "Outdoor Enthusiast", "Jungle Explorer", "Purveyor of Potions",
          "Eco Innovator", "Joke Star", "Party Animal", "Friend of the World", "Leader of the Pack",
          "Good Vampire", "World-Famous Celebrity"]

root = tk.Tk()
root.title("Sims 4 Aspiration Randomizer")

display = tk.Entry(root, width=40, borderwidth=5)
display.grid(row=0, column=1)


def randomPick():
    display.delete(0, tk.END)
    pick = random.randint(0, len(fields)-1)
    display.insert(0, str(fields[pick]))


randomButton = tk.Button(root, text="Generate", padx=50, pady=20, command=randomPick)
randomButton.grid(row=1, column=1)

root.mainloop()