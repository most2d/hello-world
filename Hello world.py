print("Hello World")
inp = input("Type something...")
print(inp)

class abc:
  def __init__(self,x=1,y=2):
    xcood=x; ycood=y;
    
  def __str__(self):
    return "X=%g Y=%g" % (self.x,self.y)
    
  def __add__(self,others):
    #self.x+=self.y
    v = self
    v.x+=others.x
    v.y+=others.y
    return v
    
class pqr(abc):
  t = (1000,200,300)
  list1 = ["a1","b2","c4"]
  
m = abc(); m.x = 4; m.y = 5
n = abc(); n.x = 6; n.y = 7
print m + n

z=pqr()
print zip(z.list1,z.t)

w=dict()
w[(100,200)]="ll"
w[(200,300)]="ee"
w[(300,400)]="ff"
w[(400,500)]="tt"
#print w.sorted()
print w

#fp=open("c:\gnotdata\3x2024.txt")
