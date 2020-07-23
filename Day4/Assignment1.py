text="What we think we became; we are Python programmers"
count=text.count('we')
addstep=0
newText=0
check=0
flag =1
while flag:
    findText=text.find('we')
    newText=newText+findText+addstep
    print(newText)
    text=text[findText+1:]
    addstep+=1
    check+=1
    if count==check:
        flag =0
