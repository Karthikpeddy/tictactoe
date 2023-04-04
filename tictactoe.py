def sum(a,b,c):
    return a+b+c
def printboard(xstate,ostate):
    zero="x" if xstate[0] else ("o" if ostate[0] else "0")
    one="x" if xstate[1] else ("o" if ostate[1] else "1")
    two="x" if xstate[2] else ("o" if ostate[2] else "2")
    three="x" if xstate[3] else ("o" if ostate[3] else "3")
    four="x" if xstate[4] else ("o" if ostate[4] else "4")
    five="x" if xstate[5] else ("o" if ostate[5] else "5")
    six="x" if xstate[6] else ("o" if ostate[6] else "6")
    seven="x" if xstate[7] else ("o" if ostate[7] else "7")
    eight="x" if xstate[8] else ("o" if ostate[8] else "8")
    print(zero +f"|" + one + f"|" + two)
    print("-|-|-")
    print(three +f"|" + four + f"|" + five)
    print("-|-|-")
    print(six +f"|" + seven + f"|" + eight)
def checkwins(xstate,ostate):
    wins=[[0,1,2],[3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for win in wins:
        if(sum(xstate[win[0]],xstate[win[1]],xstate[win[2]])==3):
            return 1
        elif(sum(ostate[win[0]],ostate[win[1]],ostate[win[2]])==3):
            return 0
        else:
            return -1
          
print("welcome to tictactoe")
xstate=[0,0,0,0,0,0,0,0,0]
ostate=[0,0,0,0,0,0,0,0,0]
ttt=[0,0,0,0,0,0,0,0,0]
turn=1
count=0
while(True):
    printboard(xstate,ostate)
    if(turn%2!=0):
        print("its X chance")
        xin=int(input("please enter the number where you want to insert:"))
        if(xstate[xin]==1):
            print("its already has been inserted")
        else:
            xstate[xin]=1
            ttt[xin]=1
            print("the block which is selected by you is filled")    
    elif(turn%2==0):
        print("its O chance")
        oin=int(input("please enter the number where you want to insert:"))
        if(ostate[oin]==1):
            print("its already has been inserted")
        else:
            ostate[oin]=1
            ttt[oin]=1
            print("the block which is selected by you is filled")  
    count=count+1
    turn=turn+1
    print(turn)
    print(count)
    print(xstate)
    print(ostate)
    checking=checkwins(xstate,ostate)
    print("checking is :",checking)
    if(count==4 or count>4):
        if(checking==1):
            print("x wins the match")
            break
        elif(checking==0):
            print("o wins the match")
            break
    elif(count==8):
        print("its a tie")
        break
    





