
#simple quiz game

print("Welcome to Quiz game")

name = input('What is your Name? \n')
print('Welcome', name)

print("----------------------------------------------")
ready = input("Are you ready for an Amazing Quiz? \n").lower()
if ready == 'yes':
    print("Lets go !")
else:
    print('Such a loser! LOL')

score = 0

print("----------------------------------------------")
question1 = input('Q1. What is the 5th planet in our solar system? ').lower()
if question1 == "jupiter":
    print('Hurray! Correct answer',)
    score = score++1

else:
    print('Such a loser! Wrong answer')


print("----------------------------------------------")
question2 = input('Q2. Largest mammal on planet earth: ').lower()
if question2 == "blue whale":
    print('Hurray! Correct answer',)
    score = score++1

else:
    print('Such a loser! Wrong answer')

print("----------------------------------------------")

question3 = input('Q3. Molecular formula of water: ').lower()
if question3 == "h20":
    print('Hurray! Correct answer',)
    score = score++1

else:
    print('Such a loser! Wrong answer')

print("----------------------------------------------")

question4 = input('Q4. Who invented Computer? ').lower()
if question4 == "charles babbage":
    print('Hurray! Correct answer',)
    score = score++1

else:
    print('Such a loser! Wrong answer')

print("----------------------------------------------")

question5 = input('Q5. 100 KM is __ M : ').lower()
if question5 == "10000":
    print('Hurray! Correct answer',)
    score = score++1

else:
    print('Such a loser! Wrong answer')

print("----------------------------------------------")

print('You have successfully completed the quiz \n You scored', score,  'marks')
