__author__ = 'leilu'

#Question 1
from numpy import *
#generate a new matrix as required
def GenerateNew():
    ls=[]
    for i in range(5):
        new=filter((lambda x: x%5==(i+1)%5), range(1,16))
        ls.append(new)
        new_matrix=asarray(ls)
    print new_matrix

#displays 2nd and 4th rows
    new=new_matrix[[1,3]]
    print new
#displays second column
    thirdColumn=new_matrix[:,1]
    print thirdColumn
#displays the rectangle required
    newrectangle=new_matrix[1:4, 0:3]
    print newrectangle
#displays the elements between 3 and 11
    desired=[]
    ls=new_matrix.ravel()
    for i in range(len(ls)):
        if ls[i]<=11 and ls[i]>=3:
            desired.append(ls[i])
    print desired


