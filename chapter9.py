# challenge 1
content = None
with open("info.txt","r") as f:
    content = f.read()
    print(content)

# challenge 2
with open("info.txt", "w") as c:
    new_text = input("text to add to file: \n")
    c.write(f"{content}\n\n{new_text}")

# challenge 3
import csv
movies = [["Top Gun", "Risky Business", "Minority Report"], ["Titanic","The Revenant", "Inception"],
           ["Training Day", "Man On Fire", "Flight"]]
with open("test.csv", "w", newline="") as f:
    w = csv.writer(f, delimiter=",")
    for movie in movies:
        w.writerow(movie)