import urllib
import urllib.request

try:
    site = urllib.request.urlopen('http//www.youtube.com')
except:
    print(f'Deu ERRO {}')
else:
    print('Tudo ok')