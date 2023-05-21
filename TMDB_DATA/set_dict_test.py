dict1={'name':'wefff', 'pk':'rrr33'}
dict2={'name':'wefff1', 'pk':'rrr331'}
dict3={'name':'wefff2', 'pk':'rrr332'}
dict4={'name':'wefff3', 'pk':'rrr333'}
dict5={'name':'wefff4', 'pk':'rrr334'}
a=list()
# a.append(dict1)
a.append(dict2)
a.append(dict3)
a.append(dict4)
a.append(dict5)
if dict1 in a:
    pass
else :
    a.append(dict1)
# a=set()
# a.add(dict1)
# a.add(dict2)
# a.add(dict3)
# a.add(dict4)
# a.add(dict5)
print(a)
