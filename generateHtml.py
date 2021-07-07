with open("text.txt", "r") as f:
    text = f.read()

print(text)

with open("index.html", "a") as f:
    f.write(text + "\n")