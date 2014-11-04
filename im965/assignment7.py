#Israel Malkin, im965
#assignment 7

import numpy as np


def q1():
  '''question #1 module'''
  a=np.arange(1,16).reshape(3,5).T
  b=a[[1,3],:]
  c=a[:,[1]]
  d=a[1:,:3]
  e=a[(a>2) & (a<12)]


  print ""  
  print "Question #1"
  print "input"
  print a
  print "a"
  print b
  print "b"
  print c
  print "c"
  print d
  print "d"
  print e
  print ""

#################################

def q2():
  '''question #2 module'''
  f=np.arange(25).reshape(5,5)
  g=np.array([1., 5, 10, 15, 20]).reshape(5,1)
  h=f/g
 
  print ""
  print "Question #2"
  print "input"
  print f
  print "divisor"
  print g
  print "output"
  print h
   


#################################

def q3():
  '''question #3 module'''
  i=np.random.uniform(size=(10,3))
  ii=i[np.arange(10),np.abs(i-0.5).argmax(1)]

  print ""
  print "Question #3"
  print "random array"
  print i
  print "output"
  print ii
  print ""


#################################

def q4():
  '''question #4 module'''
  #grids
  pixel=1000.0
  x=np.arange(-2,1,3.0/pixel)
  y=np.arange(-1.5,1.5,3.0/pixel)
  xs,ys=np.meshgrid(x,y)

  #intialize
  mask=np.empty((pixel,pixel))
  mask[:,:]=1
  max_N=50
  bound=50
  c=xs+(1j*ys)
  z=c

  for t in np.arange(max_N):
    z= z**2 + c
    mask=mask*(z<bound)

  import matplotlib.pyplot as plt
  plt.imshow(mask, extent=[-2, 1, -1.5, 1.5])
  plt.gray()
  plt.savefig('mandelbrot.png')
  print ""
  print "Question #4"
  print "mandelbrot.png has been saved to local directory"
  print ""

#### Answer questions
q1()
q2()
q3()
q4()





