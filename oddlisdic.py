odddict={'dog':['is small','is mammal'],'cat':['is small','is mammal'],'turtle':['is small'],'elephant':['is big', 'is mammal']}

print(odddict)


def oddout(dict):
    for key, value in dict.items():
        for okey, oval in dict.items():
            if value == oval and key!=okey:
                print(key, okey,value)
 
def oddout2(dict):
    for key, value in dict.items():
        for okey, oval in dict.items():
            for item in value:
                if item not in oval and key != okey:
                    print('a {} is different from {} because it {}'.format(key, okey, item)) 
                         
                                 
#for key, value in odddict.items():
 #   print(key,'::')
#    for item in value:
 #       print(item)
        
oddout2(odddict)   

# try an oop approach
# each object has a name like ke
# and list of strings descrining its qualities

class Oword:
    
    def __init__(self,name,atlist):
        self.name=name
        self.atlist=atlist
        
    def diff_from(self,otherWord):
        for item in self.atlist:
            if item not in otherWord.atlist:
                print('a {} is different from {} because it {}'.format(self.name, otherWord.name, item)) 
        for oitem in otherWord.atlist: # catces absence of attribute
            if oitem not in self.atlist:
                print('a {} is different from {} because it not {}'.format(self.name, otherWord.name, oitem)) 
        
      
word1 = Oword('bat',['is mammal','is small','flies'])

word2= Oword('bird',['is small','flies'])

print(word1,word1.name)
print(word2,word2.name)

word1.diff_from(word2)
word2.diff_from(word1)# dosent catch when list is differnt length





