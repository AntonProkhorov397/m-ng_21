import random
koloda = [6,7,8,9,2,3,4,11] * 4
random.shuffle(koloda)
count = 0
a = input("Хочешь сыграть в 21 очко? y/n  ")
if a == "y":
    while True:
        vibor = input("Берешь карту? y/n   ")
        if vibor == "y":
            current = koloda.pop()
            print("Тебе попалась карта достоинством %d" %current)
            count += current
            if count >21:
                print("Неудачник, ты проиграл))))))")
                break
            elif count == 21:
                print("Ты победил, какая жалость((((")
                break
            else:
                print("У тебя %d очков." %count)
        elif vibor == "n":
            print("У тебя %d очков." %count)
            break
        elif a == "n":
            break
        else:
            break
    print("Надеюсь, что больше тебя не увижу")
