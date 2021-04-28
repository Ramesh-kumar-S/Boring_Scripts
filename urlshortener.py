import pyshorteners
def urlshorten(url):
    s=pyshorteners.Shortener()
    return s.tinyurl.short(url)

link=input("Enter the URL ")
print(urlshorten(link))
    

