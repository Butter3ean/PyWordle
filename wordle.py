import enchant
import pandas as pd
import random
import tkinter as tk

checker = enchant.Dict('en_US')
df = pd.read_csv('5_letter_words.csv')
words = df['word'].tolist()

def entryValid(word):
    if len(word) != 5:
        return False
    return checker.check(word)
        
def getWord():
   return word_entry.get()
   
def wordle():
    userGuess = word_entry.get()
    if entryValid(userGuess):
        if userGuess.lower == word:
            print("Correct!")
        else:
            for i, label in zip(userGuess, char_labels):
                if i in word and userGuess.index(i) == word.index(i):
                    print(f'\u001b[32m{i}\u001b[0m', end="")
                    # Color Green
                    label.config(text = i, bg='green')
                elif i in word and userGuess.index(i) != word.index(i):
                    print(f'\u001b[33m{i}\u001b[0m', end="")
                    # Color Yellow
                    label.config(text = i, bg='yellow')
                else:
                    print(f'\u001b[31m{i}\u001b[0m', end="")
                    # Color red
                    label.config(text = i, bg='red')
    else:
        print("Invalid Entry")

window = tk.Tk()
window.rowconfigure([0, 1, 2], minsize=50)
window.columnconfigure([0, 1, 2, 3, 4], minsize=50)

char_labels = []
char1 = tk.Label(text='')
char_labels.append(char1)

char2 = tk.Label(text='')
char_labels.append(char2)

char3 = tk.Label(text='')
char_labels.append(char3)

char4 = tk.Label(text='')
char_labels.append(char4)

char5 = tk.Label(text='')
char_labels.append(char5)

count = 0
for labels in char_labels:
    labels.grid(row=0, column=count)
    count += 1

label = tk.Label(text="Please Enter a Five Letter Word")
word_entry = tk.StringVar()
userEntry = tk.Entry(width=50, textvariable=word_entry)
submitBtn = tk.Button(text='Submit', command=wordle)
label.grid(row=1, column=2)
userEntry.grid(row=2, column=2)
submitBtn.grid(row=3, column=2)

word = random.choice(words)

print(word)

window.mainloop()




