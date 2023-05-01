import curses as cr

screen = cr.initscr()
screen_h,screen_w=screen.getmaxyx()
cr.curs_set(0)
win=cr.newwin(screen_h,screen_w,0,0)
win.timeout(1000000)
win.keypad(1)
arr=[1,2,3,4,5,6,7,8,9]
move=[]
num_t=1
count = 0

b1=0
b2=0
b3=0
for i in range(4):
  win.hline(1,2+b1,cr.ACS_SBSB,1)
  b1+=4
  win.hline(3,2+b2,cr.ACS_SBSB,1)
  b2+=4
  win.hline(5,2+b3,cr.ACS_SBSB,1)
  b3+=4
#win.hline(1,6)
c1=0
c2=0
c3=0
for i in range(3):
  win.addstr(1,4+c1,str(i+1),cr.A_BOLD)
  c1+=4
for i in range(3,6):
  win.addstr(3,4+c2,str(i+1),cr.A_BOLD)
  c2+=4  
for i in range(6,9):
  win.addstr(5,4+c3,str(i+1),cr.A_BOLD)
  c3+=4  
while True:  
  key=(win.getkey(10,5))
  #win.addstr(15,9,f"key{key}")
  a = int(key)
   

 
  
  #print(len(str(a)))
  #print(type(a))

  #a=int(input("rr"))
  
  
  
  def is_valid(a):
    
    val_x=True
    while val_x:
      if a  not in move:
        move.append(a)
        
        val_x=False
      else:
        print('not valid move,please return')
        key=(win.getkey(10,5))
        a=int(key)
      
      
    
  
  def get_cor(a):
    if a in [1,2,3]:
      r=a
      return (1,r*4)
    if a in [4,5,6]:
      r=a%4 +1
      return (3,r*4)
    if a in [7,8,9]:
      r=a%6
      return (5,r*4)  
    
  def turn():
    t1=num_t%2
    if t1 ==0:

      return True
    else:
      return False
  
  
 
  is_valid(a)
  #get_cor(a)
  
 
  x1,y1=get_cor(a)
  
  if turn():
    win.addstr(x1,y1,"o",cr.A_BOLD)
    arr[a-1]="o"
  else:
    win.addstr(x1,y1,"x",cr.A_BOLD)
    arr[a-1]="x"

  num_t +=1
  count+=1
  winner=0
  #print(arr[0:4])
  if count :
    if arr[0]==arr[1]==arr[2]:
      win.addstr(15,15,"Game Over",cr.A_BOLD)
      winner=1
    if arr[3]==arr[4]==arr[5]:
      win.addstr(15,15,"Game Over",cr.A_BOLD) 
      winner=1
    if arr[6]==arr[7]==arr[8]:
      win.addstr(15,15,"Game Over",cr.A_BOLD) 
      winner=1
    if turn() and winner:
      win.addstr(18,14,"X Player win",cr.A_BOLD)
    elif turn()==False  and winner:
      win.addstr(18,14,"O Player win",cr.A_BOLD)
      
  win.refresh()
'''
  if a in [1,2,3]:
    if a==1:
      win.addstr(1,4,"x",cr.A_BOLD)

#win.addstr(1,8,"2",cr.A_BOLD)
#win.addstr(1,12,"3",cr.A_BOLD)


#win.hline(5,10,cr.ACS_S1,8)
  

#win.addch()
#win.addstr(0, 0, "Current mode: Typing mode",cr.A_REVERSE)
win.refresh()



state=1
arr=[1,2,3,4,5,6,7,8,9]
move=[]

while state:
  
  x=int(input('x player j'))
  val_x=True
  while val_x:
    if x  not in move:
      move.append(x)
      arr[x]="x"
      val_x=False
    else:
      print('not valid move,please return')
      x=int(input('x player'))
  
      
    o=int(input('o player'))
    val_o=1
    while val_o:
      if o  not in move: 
        move.append(o)
        arr[o]="o"
        val_o=0
      else:
        print('not valid move,please return')
        o=int(input())
''' 

