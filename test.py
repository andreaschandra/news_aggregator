import re

string = 'Intip Latihan Bebe Rexha untuk Malam Puncak HUT SCTV ke-27⁠⁠⁠⁠'
titleen = string.encode('utf-8')

title = re.sub(r'\\x[a-z0-9]{2}', '', str(titleen))

print(title)