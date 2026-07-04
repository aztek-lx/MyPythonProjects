import random
print("Note form creator: Please don't be offended by the prompts in this program! They are intende to be fun only!\n")

print("=== THE PROFESSOR'S GATEKEEPER ===")
print("Stop right there. You want to see the Professor?")
print("I am his assistant. You must pass my test first.")
print("If you fail, you must leave. There are no second chances in life!")
print() 

#Q1
answer = input("Question 1: What do we call action words in English?\n").strip()

if answer.lower() == "verbs":
    print("Correct. But that was wayy too easy. Do not even thing of getting happy yet.")
else:
    print("Wrong! That is a terrible start. You are not looking smart at alll.")  
print()


#Q2
target_length = random.randint(6, 9)

print("Question 2: Give me a word that has EXACTLY", target_length, "letters.")
answer = input("Type your word here:\n").strip()

if len(answer) == target_length:
    print("Let me count... Yes, it has", target_length, "letters. You got lucky.")
else:
    print("Wrong! You cannot even count!")
    print("I wanted", target_length, "letters, but you gave me", len(answer), ".")
print()


#Q3
answer = input("Question 3: Type a sentence that has the word 'please' inside it:\n").strip()


if "please" in answer.lower():
    print("Oh, you are begging me? Fine, I will let you pass this one.")
    print("But you'll only get one freebie from me!")
else:
    print("No! You did not to say 'please'. You have no manners.")
    print("Show some respect for your betters.")
    print("people these days have no idea what it takes to...")
print()


#Q4
answer = input("Question 4: Type the word 'NO' using only CAPITAL letters:\n").strip()

if answer.isupper() and answer == "NO":
    print("Okay, stop shouting at me OR ELSE. Next question.")
elif answer == "NO":
    print("You typed the word, but you used lowercase letters. That is a whisper!")
else:
    print("Wrong word completely! Pay attention.")
    print("How do you manage to fail that? All you had to do was type TWO letters!!! Just two!!")
print()


#Q5
print("Question 5: Say something nice to me.")
answer = input("Your sentence MUST end with the words 'wise assistant.'\n").strip()

if answer.lower().endswith('wise assistant.'):
    print("Hmph. You called me the 'wise assistant.' That is correct.")
else:
    print("Wrong! You did not end the sentence correctly.")
    print("You must respect my title!")
print()   


#Q6
print("Final Choice: Pick a time slot to see the Professor next Monday:")
print("A. Morning", "B. Afternoon", "C. Evening", sep='\t')

choice = input("Select A, B, or C:\n").strip()

if choice.upper() == 'A':
    print("Slot A chosen. The Professor is very sleepy in the morning.")
elif choice.upper() == 'B':
    print("Slot B chosen. The Professor is very hungry in the afternoon.")
elif choice.upper() == 'C':
    print("Slot C chosen. The Professor is very tired in the evening.")
else:
    print("That was not even a choice! You ruined the test.")

#Q7
print("Question 7: I think you are a spy. Prove you are not a robot.")
answer = input("Type a word that has at least three 'z' letters in it:\n").strip()

z_count = answer.lower().count('z')

if z_count >= 3:
    print("Fine. You usd", z_count, "z's. Only a weird human or a broken robot would type that.")
else:
    print("I caught you! Your word only had", z_count, "z's. You are a terrible spy.")
    print("Your master must be dissapointed in your existance")
print()


# --- TASK 8: Use .replace() to modify a string ---
print("Question 8: Let us play a game. Give me a word that starts with the letter 'p'.")
answer = input("Type your 'p' word here:\n").strip()

# Replace the letter 'p' with the word 'BANANA'
funny_word = answer.lower().replace('p', 'BANANA')

if answer.lower().startswith('p'):
    print("I do not like that word. I changed it to:", funny_word)
    print("Now it sounds much better.")
else:
    print("That does not even start with a 'p'! You cannot follow simple rules.")
print()