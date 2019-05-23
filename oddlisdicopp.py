 
# try an oop approach
# each object has a name like ke
# and list of strings descrining its qualities

class Oword:
    
    def __init__(self,name,atlist):
        self.name=name
        self.atlist= atlist
        self.dc = 0
        self.diflist = []
        
    def diff_from(self,otherWord):
        for item in self.atlist:
            if item not in otherWord.atlist:
                print('a {} is different from {} because it is {}'.format(self.name, otherWord.name, item)) 
                self.dc+=1
                self.diflist.append(item)
        for oitem in otherWord.atlist: # catces absence of attribute meaning it check for symmetric difference
            if oitem not in self.atlist:
                print('a {} is different from {} because it is not {}'.format(self.name, otherWord.name, oitem))
                self.dc+=1
                self.diflist.append('not '+oitem)
            
        
      



dog = Oword('dog',['small','a mammal'])   # name and  and list with adjs or article + noun
cat = Oword('cat',['small','a mammal'])
turtle = Oword('turtle',['small'])
elephant = Oword('elephant',['big', 'a mammal'])

oddlist= [dog,cat,turtle,elephant]

human = Oword('human',['smart','a mammal'])   # name and  and list with adjs or article + noun
dolphin = Oword('dolphin',['a mammal','living in water','smart'])
shark = Oword('shark',['living in water'])
whale = Oword('whale',['big', 'a mammal', 'living in water','smart'])

oddlist2= [human,dolphin,shark,whale]







#print(set(dog.atlist).difference(set(cat.atlist),set(turtle.atlist),set(elephant.atlist)))

#print(set(dog.atlist).difference(set(turtle.atlist)))
#print(set(turtle.atlist).difference(set(dog.atlist)))
#
#print(set(turtle.atlist).symmetric_difference(set(dog.atlist)))
#print(set(dog.atlist).symmetric_difference(set(turtle.atlist)))


dog.diff_from(turtle)
dog.diff_from(elephant)
dog.diff_from(cat)
turtle.diff_from(dog)
turtle.diff_from(cat)
turtle.diff_from(elephant)
cat.diff_from(turtle)
cat.diff_from(dog)
cat.diff_from(elephant)
elephant.diff_from(cat)
elephant.diff_from(turtle)
elephant.diff_from(dog)

print(dog.name,dog.dc)
print(cat.name,cat.dc)
print(turtle.name,turtle.dc)
print(elephant.name,elephant.dc)

print(dog.name,dog.diflist)
print(cat.name,cat.diflist)
print(turtle.name,turtle.diflist)
print(elephant.name,elephant.diflist)
## we can fid the odd one out reason by  using the most frequent apperance in diff list

difcountdict ={item.name : item.dc for item in oddlist}  #dictionary comprhension
    
difcountlist =[(item.dc , item.name) for item in oddlist]  #list of tuples
difcountlist2 =[item.dc for item in oddlist]   #list of ints

print(difcountlist)
print(difcountdict)
difcountlist.sort()
print(difcountlist)
print(difcountlist2)
difcountlist2.sort()
print(difcountlist2)

print(max(difcountlist2))
print(min(difcountlist2))

if max(difcountlist2) > min(difcountlist2):
    print("there is an odd one out")
    
for item in oddlist:
    if item.dc > min(difcountlist2):
        print(item.name+' is an odd one out')





###### gets the differences for od list 2######


for anim in oddlist2:
    for oanim in oddlist2:
        anim.diff_from(oanim)


        
        
difcountdict ={item.name : item.dc for item in oddlist2}  #dictionary comprhension
    
difcountlist =[(item.dc , item.name) for item in oddlist2]  #list of tuples
difcountlist2 =[item.dc for item in oddlist2]   #list of ints

print(difcountlist)
print(difcountdict)
difcountlist.sort()
print(difcountlist)
print(difcountlist2)
difcountlist2.sort()
print(difcountlist2)

print(max(difcountlist2))
print(min(difcountlist2))

if max(difcountlist2) > min(difcountlist2):     ## if dif cout list is greater than min of that list you can call it odd one out
    print("there is an odd one out")

oddOneOut = []    
for item in oddlist2:
    if item.dc > min(difcountlist2):
        print(item.name+' is an odd one out')
        oddOneOut.append(item)
        
       
for oddone in oddOneOut:
    
    for item in set(oddone.diflist):
        if oddone.diflist.count(item) >=3:
            print("{} is the odd one out because it is {}".format(oddone.name,item))
    
 
    






