# module to open url
import urllib


#for i in range(5):
# list of words to look for
#words = ['word', 'word1', 'word2']
words = ["Currently, this is a snippet of what I have",'greg','sparkapp1','sparkapp2',"sparkapp3","sparkapp4"]

# website to open and read
site = urllib.urlopen('https://stackoverflow.com/questions/8204373/checking-if-certain-words-are-on-a-web-page-using-python').read()

#print(site)

for word in words:
    if word in site:
       		print("FOUND: " + word)
       		print("")
    else:
       		print(word + ": not found")
       		print("")