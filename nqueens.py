
n=int(input("\nEnter no. of Queens : "))
a=[[0 for x in range(n)] for y in range(n)]
b={}

def isColSafe(row,col):
    	while(row>=0):
        	if (a[row][col]==1):
            		return 0
        	row=row-1
    	return 1

def isLDiagonal(row,col):
	while(row>=0 and col>=0):
        	if(a[row][col]==1):
            		return 0
        	row=row-1
        	col=col-1
	return 1

 
def isRDiagonal(row,col):
	while(row>=0 and col<n):
		if(a[row][col]==1):
			return 0
		row=row-1
		col=col+1
	return 1

'''def isRowSafe(row,col):
	while(col<n):
		if(a[row][col]==1):
			return 1
		col=col+1
	return 1'''


def isSafe(row,col):
    	if(isColSafe(row,col)== 0):
        	return 0
    	if(isLDiagonal(row,col)==0):
        	return 0
    	if(isRDiagonal(row,col)==0):
        	return 0
    	return 1


def checkBoard(r,c):
    	if(r>=n):
        	return
    	p=0
    	while(c<n):
        	p = isSafe(r,c)
        	if(p==1):
            		a[r][c] = 1
            		b.update({r:c})
            		break
        	c=c+1
    	if(p==1):
        	checkBoard(r+1,0) 
    	else:
        	a[r-1][b.get(r-1)]=0
        	checkBoard(r-1,int(b.get(r-1))+1)	#Backtrack
 
checkBoard(0,0)
print("\n")
for i in range(n):
	for j in range(n):
		print(a[i][j],end="     ")
	print("\n")




'''
Output:

guest-ydS0jW@112C-07:~/Desktop$ python3 nqueens.py

Enter no. of Queens : 8


1     0     0     0     0     0     0     0     

0     0     0     0     1     0     0     0     

0     0     0     0     0     0     0     1     

0     0     0     0     0     1     0     0     

0     0     1     0     0     0     0     0     

0     0     0     0     0     0     1     0     

0     1     0     0     0     0     0     0     

0     0     0     1     0     0     0     0     

  

'''



