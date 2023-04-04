def wins(mat,flag):
    if(mat[0][0]==mat[0][1]==mat[0][2] or mat[1][0]==mat[1][1]==mat[1][2] or mat[2][0]==mat[2][1]==mat[2][2] or mat[0][0]==mat[1][0]==mat[2][0] or mat[0][1]==mat[1][1]==mat[2][1] or mat[0][2]==mat[1][2]==mat[2][2] or mat[0][0]==mat[1][1]==mat[2][2] or mat[0][2]==mat[1][1]==mat[2][0]):
        print("winner declared ...match over")
        return 1
    elif(flag==9):
        print("match tied")  
        return 1  
mat=[["","",""],["","",""],["","",""]]
print("welcome to tictactoe")
flag=1
l=[]
l1=[]
for i in range(8):
    if(flag%2!=0):
        print("its x chance")
        a=input("Enter the index with space where you want to insert:")
        l=list(map(int,a.split()))
        mat[l[0]][l[1]]='x'
    elif(flag%2==0):
        print("its o's chance")
        b=input("Enter the index with space where you want to insert:")
        l1=list(map(int,b.split()))
        mat[l1[0]][l1[1]]='o'   
    flag=flag+1   
    print(mat)
    if(flag==5 or flag>5):
       b= wins(mat,flag)
       if(b==1):
           break


    

    

