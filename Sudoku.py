import sys
import numpy as np
validity = list()
t=[[0,0,0,2,6,0,7,0,1],
   [6,8,0,0,7,0,0,9,0],
   [1,9,0,0,0,4,5,0,0],
   [8,2,0,1,0,0,0,4,0],
   [0,0,4,6,0,2,9,0,0],
   [0,5,0,0,0,3,0,2,8],
   [0,0,9,3,0,0,0,7,4],
   [0,4,0,0,5,0,0,3,6],
   [7,0,3,0,1,8,0,0,0]]
"""t=[[0,0,0,0,0,0,0,0,2],
   [0,0,0,0,0,0,9,4,0],
   [0,0,3,0,0,0,0,0,5],
   [0,9,2,3,0,5,0,7,4],
   [8,4,0,0,0,0,0,0,0],
   [0,6,7,0,9,8,0,0,0],
   [0,0,0,7,0,6,0,0,0],
   [0,0,0,9,0,0,0,2,0],
   [4,0,8,5,0,0,3,6,0]]"""
su_grid = np.array(t).reshape(9,9)
ec = list()
grid=list()
grid.append(su_grid[0:3,0:3])
grid.append(su_grid[0:3,3:6])
grid.append(su_grid[0:3,6:9])
grid.append(su_grid[3:6,0:3])
grid.append(su_grid[3:6,3:6])
grid.append(su_grid[3:6,6:9])
grid.append(su_grid[6:9,0:3])
grid.append(su_grid[6:9,3:6])
grid.append(su_grid[6:9,6:9])
count=0
g = list()
for i in range(0,9):
    for j in range(0,9):
        if(su_grid[i,j]==0):
            ec.append(i)
            ec.append(j)
            if(i < 3 and j < 3):
                g.append(0)
            elif(i < 3 and j in range(3,6)):
                g.append(1)
            elif(i < 3 and j in range(6,9)):
                g.append(2)
            elif(i in range(3,6) and j < 3):
                g.append(3)
            elif(i in range(3,6) and j in range(3,6)):
                g.append(4)
            elif(i in range(3,6) and j in range(6,9)):
                g.append(5)
            elif(i in range(6,9) and j < 3):
                g.append(6)
            elif(i in range(6,9) and j in range(3,6)):
                g.append(7)
            elif(i in range(6,9) and j in range(6,9)):
                g.append(8)
            count+=1
emp_cell = np.matrix(ec).reshape(count,2)
emp_cell=emp_cell.tolist()
validity = [0] * count
listi=list()
def get_i_j_no():
    listi = list()
    j=0
    for i in range(0,count):
        if emp_cell[i][j] == 4:
            listi.append(emp_cell[i][1])
def return_prev_em_cell(i,j):
	e = emp_cell.index([i,j])
	return emp_cell[e-1]
def row_check(num,i,j):
    b = True
    for k in range(0,9):
        if(num == su_grid[i][k]):
            return False
    if b==True:
        return True
def column_check(num,i,j):
    b = True
    for k in range(0,9):
        if(num == su_grid[k][j]):
            return False
    if b == True:
        return True
def grid_check(num,i,j):
    indn = emp_cell.index([i,j])
    ind = g[indn]
    a = True
    
    if num in grid[ind]:
        a = False
    return a
"""def k_greater_1(k,i,j):
    a = False
    for num in range(k,9):
        if(row_check(num,i,j) and column_check(num,i,j) and grid_check(num,i,j)):
            su_grid[i][j] = num
            a = True
   if a == False:
        exception_check(i,j)"""
def exception_check(i,j):
        c = False
        x,y = return_prev_em_cell(i,j)
        get_i_j_no()
        for k in listi:
            if validity[emp_cell.index([i,k])]>1:
                c = True
                break
        if c == True: 
            if Placing_Number(1,x,y) == False:
                exception_check(x,y)
        else:
            if su_grid[x][y]+1<10:
                if Placing_Number(su_grid[x][y]+1,x,y) == False:
                    exception_check(x,y)
            else:
                if Placing_Number(1,x,y) == False:
                    exception_check(x,y)
        Placing_Number(1,i,j)
def Placing_Number(k,i,j):
    a = False
    inde = 0
    for num in range(k,10):
        if(row_check(num,i,j) and column_check(num,i,j) and grid_check(num,i,j)):
            inde = emp_cell.index([i,j])
            validity[inde] += 1
            su_grid[i][j] = num
            a = True
            return True
    if (a == False):
        return False
def Solve_Sudoku(i,j):
    if Placing_Number(1,i,j):
        return True
    else:
        exception_check(i,j)
if __name__ == '__main__': 
    sys.setrecursionlimit(10**6) 
    for i,j in emp_cell:
        Solve_Sudoku(i,j)
        """  if su_grid[i][j] == 0:
            Solve_Sudoku(i,j)"""
    for i in range(0,9):
        print()
        for j in range(0,9):
            print(su_grid[i][j],end=" ")