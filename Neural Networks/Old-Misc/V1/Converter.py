f=open('example.txt','r')
dataset=f.readlines()
matrix=[[]]
#print(dataset)
f.close()

count=0
for data in dataset:
    if data=='\n':
        matrix.append([])
        count=count+1
    else:
        matrix[count].append(data)

#print(matrix[1])
for mat in matrix:
    for j in range(len(mat)):
        edit=list(mat[j])
        #print(edit)

        editremove=[]
        for i in range(len(edit)-1):
            #print(i)
            if edit[i]==edit[i+1] and type(edit[i])!=int:
                editremove.append(edit[i])

        for remove in editremove:
            edit.remove(remove)

        print(edit)
