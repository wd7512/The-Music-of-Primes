def reverse(word):
    rev=[]
    for i in range(len(word)):
        rev.append(word[len(word)-1-i])
    return ''.join(rev)
f=open('Reverse.txt','r')
text=f.readlines()
f.close()
for line in text:
    
