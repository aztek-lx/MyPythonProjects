#Note: I have made use of concepts I learn't in my school as well, such as .lower.
import time
#Welcoming
print('|    ELECTRICITY BOT    |')
print()

print('EEEEE', 'L    ', 'EEEEE', 'CCCCC', 'TTTTT', 'RRRR ', 'IIIII', 'CCCCC', 'IIIII', 'TTTTT', 'Y   Y')
print('E    ', 'L    ', 'E    ', 'C    ', '  T  ', 'R   R', '  I  ', 'C    ', '  I  ', '  T  ', ' Y Y ')
print('EEEE ', 'L    ', 'EEEE ', 'C    ', '  T  ', 'RRRR ', '  I  ', 'C    ', '  I  ', '  T  ', '  Y  ')
print('E    ', 'L    ', 'E    ', 'C    ', '  T  ', 'R  R ', '  I  ', 'C    ', '  I  ', '  T  ', '  Y  ')
print('EEEEE', 'LLLLL', 'EEEEE', 'CCCCC', '  T  ', 'R   R', 'IIIII', 'CCCCC', 'IIIII', '  T  ', '  Y  ')


#Inputing user name
print()
name = input('What is your name? ')
name_long = 'Hello ' + name + "!"
print() 
for i in range(len(name_long)+1):
    print(name_long[0:i+1:1], end='\r')
    time.sleep(0.1)
print(name_long)

print("Today we\'ll talk about electricity.")
print()


#Quiz
answer = input('Do you use electricity every day? (yes/no) ')
print()

if answer.lower() == 'yes' or answer.lower() == "y":
    print('Correct! Most you do use electricity every day. In fact, you\'re using it right now!')
else:
    print('You might use it more than you think!')
time.sleep(3)

print()
time.sleep(1)
print("⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡⚡")
print()
print('W   W', 'EEEEE', 'L    ', 'CCCCC', ' OOO ', 'M   M', 'EEEEE', sep='|')
print('W   W', 'E    ', 'L    ', 'C    ', 'O   O', 'MM MM', 'E    ', sep='|')
print('W W W', 'EEEE ', 'L    ', 'C    ', 'O   O', 'M M M', 'EEEE ', sep='|')
print('WW WW', 'E    ', 'L    ', 'C    ', 'O   O', 'M   M', 'E    ', sep='|')
print('W   W', 'EEEEE', 'LLLLL', 'CCCCC', ' OOO ', 'M   M', 'EEEEE', sep='|')
print()
time.sleep(1)
print('To the ELECTRICAL quiz!')

#Q1
print()
print('------------------------------------------------------------------------------------------')
print()
for i in range(len("Question 1")):
    print("Question 1"[0:i+1:1], end='\r')
    time.sleep(0.1)
print()

print('What powers a light bulb?')
print('1. Electricity')
print('2. Water')
print('3. Sand')
print()

choice = input('Enter your answer: 1, 2, or 3: ')

if choice == '1':
    for i in range(len('Great job! A light bulb uses electricity.')):
        print('Great job! A light bulb uses electricity.'[0:i+1:1], end='\r')
        time.sleep(0.1)
    print()
else:
    for i in range(len('Not quite. The answer is Electricity.')):
        print('Not quite. The answer is Electricity.'[0:i+1:1], end='\r')
        time.sleep(0.1)
    print()
#Q2
print()
for i in range(len("Question 2")):
    print("Question 2"[0:i+1:1], end='\r')
    time.sleep(0.1)
print()

print('Which of these uses electricity?')
print('1. Pencil')
print('2. Refrigerator')
print('3. Book')

choice = input('Enter 1, 2, or 3: ')

if choice == '2':
    for i in range(len('Great job! A refrigerator uses electricity.')):
        print('Great job! A refrigerator uses electricity.'[0:i+1:1], end='\r')
        time.sleep(0.1)
    print()
else:
    for i in range(len('You were')):
        print('You were'[0:i+1:1], end='\r')
        time.sleep(0.1)
    print()
    print()
    time.sleep(1)
    print('W   W', 'RRRR ', ' OOO ', 'N   N', 'GGGGG', sep=' | ')
    print('W   W', 'R   R', 'O   O', 'NN  N', 'G    ', sep=' | ')
    print('W W W', 'RRRR ', 'O   O', 'N N N', 'G GGG', sep=' | ')
    print('WW WW', 'R  R ', 'O   O', 'N  NN', 'G   G', sep=' | ')
    print('W   W', 'R   R', ' OOO ', 'N   N', 'GGGGG', sep=' | ')
    

#Post quiz
time.sleep(3)
print()
print("That's all for now,", name)

time.sleep(1)
print()
print('BBBBB ', 'Y   Y', 'EEEEE')
print('B   B ', ' Y Y ', 'E')
print('BBBBB ', '  Y  ', 'EEEE')
print('B   B ', '  Y  ', 'E')
print('BBBBB ', '  Y  ', 'EEEEE')

print()
print('Thanks for chatting about electricity')