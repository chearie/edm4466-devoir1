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
# jolieListe = [code1, code2]
# print(jolieListe)
grandeListe = list(range(20000,30151))
# print(grandeListe)
# print(grandeListe)
n = 0
for articles in grandeListe:
    n += 1
    print(n,url1+str(articles))
print(grandeListe)
print(len(grandeListe))