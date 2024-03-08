# challenge 1
li = ["The Walking Dead", "Entourage", "The Sopranos", "The Vampire Diaries"]
for i in li:
    print(i)

# challenge 2
for i in range(25, 51):
    print(i)

# challenge 3
for i in range(len(li)):
    print(i)
    print(li[i])

# challenge 4
while True:
    print("press q to quit")
    numbers = [6,13,68]
    guess = input("Guess a number: ")
    if guess == "q":
        break
    if int(guess) in numbers:
        print("You guessed one of the numbers!")
        break

# challenge 5
list1 = [8,19,148,4]
list2 = [9,1,33,83]
for x in list1:
    for y in list2:
        print(x*y)