name=['shaha', 'shoha','ali']
number=[904284968, 331233313, 904669074]
newname=input()
newnumber=input()
if newname.lower() in name or newnumber in number:
    print('exsist')
else:
    name.append(newname.lower())
    number.append(newnumber)
    print(name)
    print(newnumber)
