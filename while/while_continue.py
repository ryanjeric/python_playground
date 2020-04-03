spam = 0
while spam < 5:
    spam = spam + 1
    if spam == 3:
        continue # jump to while
    print('spam is ' + str(spam))