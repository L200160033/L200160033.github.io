from urllib.parse import urlparse   ##URLs
from urllib.parse import urljoin    ##PATH
from urllib.parse import parse_qs   ##QUERY STRINGS
from urllib.parse import quote      ##URL ENCODING
from urllib.parse import urlencode  ##URL ENCODING
from urllib.parse import urlunparse ##URL ENCODING

def start():
    print ("===============================")
    print ("        Nama Sub Bab           ")
    print ("===============================")
    print ("[1] URLs")
    print ("[2] Paths and relative URLs")
    print ("[3] Query Strings")
    print ("[4] URL encoding")

    pilih = input("Pilih : ")

    if pilih == '1':
        urls()
    if pilih == '2':
        path()
    if pilih == '3':
        query()
    if pilih == '4':
        urlen()
    else:
        print ("MAAF PERMINTAAN TIDAK SESUAI")
        start()
        
def urls():
    result = urlparse('http://www.python.org/dev/peps')
    print ("===============================")
    print ("             URLs              ")
    print ("===============================")
    print ("[1] Result")
    print ("[2] Result.netloc")
    print ("[3] Result.path")
    print ("[4] urlparse('http://www.python.org:8080/')")
    print ("[0] Home")

    pilih = input("Pilih : ")

    if pilih == '1':
        print (result)
        urls()
    if pilih == '2':
        print (result.netloc)
        urls()
    if pilih == '3':
        print (result.path)
        urls()
    if pilih == '4':
        print (urlparse('http://www.python.org:8080/'))
        urls()
    if pilih == '0':
        start()
    else:
        print ("MAAF PERMINTAAN TIDAK SESUAI")
        urls()

def path():
    print ("==============================")
    print ("   PATHS AND RELATIVE URLs    ")
    print ("==============================")
    print ("[1] urlparse('http://www.python.org/')")
    print ("[2] urlparse('../images/tux.png')")
    print ("[3] urljoin('http://www.debian.org', 'intro/about')")
    print ("[4] urljoin('http://www.debian.org/intro/', 'about')")
    print ("[5] urljoin('http://www.debian.org/intro', 'about')")
    print ("[6] urljoin('http://www.debian.org/intro/about', '/News')")
    print ("[7] urljoin('http://www.debian.org/intro/about/', '../News')")
    print ("[8] urljoin('http://www.debian.org/intro/about/', '../../News')")
    print ("[9] urljoin('http://www.debian.org/intro/about', '../News')")
    print ("[10] urljoin('http://www.debian.org/about', 'http://www.python.org')")
    print ("[0] Back")

    pilih = input("Pilih : ")

    if pilih == '1':
        print (urlparse('http://www.python.org/'))
        path()
    if pilih == '2':
        print (urlparse('../images/tux.png'))
        path()
    if pilih == '3':
        print (urljoin('http://www.debian.org', 'intro/about'))
        path()
    if pilih == '4':
        print (urljoin('http://www.debian.org/intro/', 'about'))
        path()
    if pilih == '5':
        print (urljoin('http://www.debian.org/intro', 'about'))
        path()
    if pilih == '6':
        print (urljoin('http://www.debian.org/intro/about', '/News'))
        path()
    if pilih == '7':
        print (urljoin('http://www.debian.org/intro/about/', '../News'))
        path()
    if pilih == '8':
        print (urljoin('http://www.debian.org/intro/about/', '../../News'))
        path()
    if pilih == '9':
        print (urljoin('http://www.debian.org/intro/about', '../News'))
        path()
    if pilih == '10':
        print (urljoin('http://www.debian.org/about', 'http://www.python.org'))
        path()
    if pilih == '0':
        start()
    else:
        print ("MAAF PERMINTAAN TIDAK SESUAI")
        path()
        
    
def query():
    print ("==============================")
    print ("         QUERY STRINGS        ")
    print ("==============================")
    print ("[1] urlparse('http://docs.python.org/3/search.html?q=urlparse&area=default')")
    print ("[2] parse_qs(result.query)")
    print ("[3] parse_qs(result.query)")
    print ("[0] Back")

    pilih = input("pilih: ")

    if pilih == '1':
        print(urlparse('http://docs.python.org/3/search.html?q=urlparse&area=default'))
        query()
    if pilih  == '2':
        result = urlparse('http://docs.python.org/3/search.html?q=urlparse&area=default')
        print(parse_qs(result.query))
        query()
    if pilih == '3':
        result = urlparse('http://docs.python.org/3/search.html?q=urlparse&q=urljoin')
        print(parse_qs(result.query))
        query()
    if pilih == '0':
        start()
    else:
        print ("MAAF PERMINTAAN TIDAK SESUAI")
        query()

def urlen():
    print ("==============================")
    print ("         URL ENCODING         ")
    print ("==============================")
    print ("[1] quote('A duck?')")
    print ("[2] query_enc")
    print ("[3] urlunparse(('http', netloc, path_enc, '', query_enc, ''))")
    print ("[4] quote(path)")
    print ("[5] quote(path)")
    print ("[0] Back")

    pilih = input("Pilih : ")

    path = 'pypi'
    path_enc = quote(path)
    query_dict = {':action': 'search', 'term': 'Are you quite sure this is a cheese shop?'}
    query_enc = urlencode(query_dict)
    netloc = 'pypi.python.org'
        
    if pilih == '1':
        print(quote('A duck?'))
        urlen()
    if pilih == '2':
        print (query_enc)
        urlen()
    if pilih == '3':  
        print (urlunparse(('http', netloc, path_enc, '', query_enc, '')))
        urlen()
    if pilih == '4':
        path = '/images/users/+Zoot+/'
        print (quote(path))
        urlen()
    if pilih == '5':
        username = '+Zoot/Dingo+'
        path = 'images/users/{}'.format(username)
        print (quote(path))
        urlen()
    if pilih == '0':
        start()
    else:
        print ("MAAF PERMINTAAN TIDAK SESUAI")
        urlen()

start()
                  




