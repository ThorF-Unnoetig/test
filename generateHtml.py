with open("text.txt", "r") as f:
    text = f.read()

print(text)

html = "<h1>Hallo neue Seite</h1>\n<p>Just a test to get used to the pages and actions enviroment.</p>"
import os
path = "output/"
os.mkdir(path)
with open(path + "index.html", "a") as f:
    f.write(html + "\n" + text + "\n")