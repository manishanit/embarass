import urllib
def read_text():
    quotes = open("C:\Python27\oops\movie_quotes.txt")
    contents_of_file = quotes.read()
    #print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)


def check_profanity(text_to_check):
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
    output = connection.read()
    #print(output)
    if "true" in output:
        print("Profinity Alert")
    elif "false" in output:
        print("This document has no curse words")
    else:
        print("Could not scan the document properly")
    connection.close()
read_text()
