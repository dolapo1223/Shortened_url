import pyshorteners

link = input("Enter the url: ")

url_short = pyshorteners.Shortener()

x = url_short.tinyurl.short(link)

print(x)