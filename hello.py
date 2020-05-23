from datetime import datetime

now = datetime.now()

today = now.strftime('%A')

answer = False
counter = 1
answers = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

while answer == False:

    day = str(input('What day is it? '))


    if day != today and day in answers:
        print('Sorry, today is not', day)
        counter = counter +1
    else:
        print('Correct, today is', day)
        answer = True

print('You guessed', counter, 'times')





