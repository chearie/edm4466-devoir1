### BONJOUR ARIANE, ICI JEAN-HUGUES ROY
### TOUS MES COMMENTAIRES SERONT EN MAJUSCULES ET PRÉCÉDÉS DE 3 # (HASHTAGS)

# 2020 Ariane Chevrier
# coding: utf-8
url = "https://montrealcampus.ca?p=30145"
# print(url)
# print(url.find("="))
# print(url[url.find("=")+1:])
chiffre = url.find("=")
url1 = (url[:url.find("=")+1])
# print(url1)
code = (url[url.find("=")+1:])
# print(code)
code1 = code.replace(code,"20000")
# print(code1)
code2 = code.replace(code,"30150")
# # print(code2)
# jolieListe = [code1, code2] ### HAHA! JOLI NOM DE VARIABLE!
# print(jolieListe)
# grandeListe = list(range(20000,30151))
# print(grandeListe)

### TOUT LE CODE QUI PRÉCÈDE EST EXCELLENT.
### IL NE TE PERMET PAS DE RÉPONDRE À LA QUESTION,
### MAIS IL ILLUSTRE QUAND MÊME QUE TU AS TENTÉ D'APPLIQUER
### CE QU'ON A VU EN CLASSE :)

n = 0
# for articles in grandeListe:
#     n += 1
#     print(n,url1+str(articles))
# print(grandeListe)
urlFinaux = []
for articles in range(20000,30151) :
    n += 1
    print(n, url1+str(articles))
    urlFinaux.append(url1+str(articles))

print(urlFinaux)
print(len(urlFinaux))

### SUPER! ÇA FONCTIONNE!