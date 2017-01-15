import chardet
text=input("随便输入字符").encode()
print(chardet.detect(text))
