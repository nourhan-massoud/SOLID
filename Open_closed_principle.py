# Open Closed Principle states that “Software entities (classes, modules, functions, etc.) 
# should be open for extension but closed for modification.”

# wrong with this behavior is when we need to add new clinet like google 
# we will modifie code not add extension to it !
# this behavior break SOLID(open closed principle).
from bs4 import BeautifulSoup
from urllib.request import urlopen
from abc import ABC ,abstractmethod

class StorageLocker():
    def authenticate(self,client):
        if client == "aws":
            # some code to authenticate with aws .
        elif client == "azure":
            # some code to authenticate with azure .

        return client

    def upload_file(self,filename):
        if client == "aws":
            # some code to uplaod file with aws .
        elif client == "azure":
            # some code to uplaod file with azure .

        return client

# lets start again with new behavior 

class Auth(ABC):
    @abstractmethod
    def authenticate(self):
        pass


class Uploader():  
    @abstractmethod
    def upload_file(self):
        pass  

# Or azure/google class .
class AWS(Auth,Uploader):  
    def authenticate(self):
        # some code to auth with aws .
        return auth_client
        
    def upload_file(self): 
        # some code to upload file with aws . 
        return status_code 

# --------------------------------------------------------------------------------------------------
# Another example to explain this point
# example of the method that counts words in a text after extracting it in a local file:

def count_word_occurrences(word, localfile):
    content = return open(localfile, "r").read()
    counter = 0
        for e in content.split():
            if word.lower() == e.lower():
                counter += 1
        return counter

# But what if we wanted to extract content from other source, 
# like for example a url ? 
# If we worked with the above function, to implement new functionality, 
# we would need to modify the existing function which would go against the Open/Closed Principle.

# The better way of organizing the code would be the following:
# and use SOLID(open closed principle) correctly .

# red file only
def read_localfile(file):
    '''Read file only'''
    return open(file, "r").read()

# count words only
def count_word_occurrences(word, content):
    '''Count number of word occurrences in a file'''
    counter = 0
    for e in content.split():
        if word.lower() == e.lower():
            counter += 1
    return counter

# add new method to extract words from url without any modify
def get_text_from_url(url):
    '''Extract html as string from given url'''
    page = urlopen(url).read()
    soup = BeautifulSoup(page)
    text = soup.get_text()
    return text

# Next we would just call the already existing function count_word_occurrences() 
# with the content extracted using get_text_from_url() function :

content = get_text_from_url('https://en.wikipedia.org/wiki/Main_Page')
count_word_occurrences('and', content)

# So we added new functionality to the code without needing to modify the existing code.
# So we extension (add new method) but closed for modification (not done any edits on old code) .