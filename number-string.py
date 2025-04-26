#數字運算
x=3+6
#小數除法
x=3/6
#整數除法
x=7/6
#2的3次方
x=2**3
print(x)
#取餘數
x=2%3
print(x)
x=5
x+=1 # x=x+1 #將變數中的數字+1
print(x)

#字串運算
s="Hell\"o" # \ 跳脫
print(s)

s="Hello"+"World"
s="Hello" "World" #同樣達到自串串接的結果
print(s) 

s="Hello\nWorld" #換行
print(s)
s="""Hello
World""" #一樣達到換行的效果
print(s)

s="Hello"*3+"World"
print(s)

#字串會對內部的字元編號(索引), 從0開始算起
s="Hello"
print(s[0])
print(s[1:4]) #包含開頭編號 但不包含結尾編號
print(s[1:]) #取開頭不給結尾 包含開頭後面所有的內容
print(s[:4]) #不包含結尾的前面所有內容