# Magic 8 Ball for fortune-telling or seeking advice
# https://www.w3resource.com/projects/python/python-projects-5.php
import random

answers = ['It is certain', 'It is decidedly so', 'Without a doubt', 'Yes – definitely', 'You may rely on it',
           'As I see it, yes', 'Most likely', 'Outlook good', 'Yes Signs point to yes', 'Reply hazy', 'try again',
           'Ask again later', 'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again',
           'Dont count on it', 'My reply is no', 'My sources say no', 'Outlook not so good', 'Very doubtful']

print('What is your name?')
name = input()
print('Hello ' + name)


def Magic8Ball():
    print('Ask me a question.')
    input()
    print(answers[random.randint(0, len(answers) - 1)])
    print('I hope that helped!')
    Replay()


def Replay():
    print('Do you have another question? [Y/N] ')
    reply = input()
    if reply == 'Y':
        Magic8Ball()
    elif reply == 'N':
        exit()
    else:
        print('I apologies, I did not catch that. Please repeat.')
        Replay()


Magic8Ball()