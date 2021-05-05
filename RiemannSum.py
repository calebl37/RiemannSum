#name:safe_to_integer
#purpose: converts user input to number
#inputs: string
#returns: integer
def safe_to_integer(number, default =1):
  try:
    return int(number)
  except (ValueError, TypeError):
    return default

#name: f
#purpose: calculates f(x) which is a quadratic
#inputs: 4 integers, the valu of x and the coefficients for the quadratic
#returns: integer
def f(x,coeff1,coeff2,coeff3):
  return coeff1*x*x+coeff2*x+coeff3

#name: LHS
#purpose: calculates the left hand sum for a given number of rectangles
#inputs: 3 integers: lower bound, upper bound, deltaX
#returns: none
def LHS(start,end,width): #start is lower bound (a), end is lower bound (b) and width is deltaX
  global A
  global B
  global C
  global n
  area = 0 #area starts at zero
  if start > end: #negative integration
    lower = 1
    upper = n+1
  else: #positive integration
    lower = 0
    upper = n
  for i in range(lower,upper): #ex: for positive integration, if there are 10 rectangles, i would be 0, 1, 2...9) for negative integration, if there are 10 rectangles, i would be 1, 2, 3...10
    currentX = start + i*width #due to the i, currentX would be a, a+deltaX, a+2deltaX, ...b-deltaX)
    one_rectangle = f(currentX,A,B,C)*width #f(currentX,A,B,C) is the height, area is height * width)
    area += one_rectangle #summation of the areas of each rectangle
  #print("LH"+str(n) + " = " + str(area))
  return area

#name: RHS
#purpose: calculates the right hand sum for a given number of rectangles
#inputs: 3 integers: lower bound, upper bound, deltaX
#returns: none
def RHS(start,end,width): #start is lower bound (a), end is lower bound (b) and width is deltaX
  global A
  global B
  global C
  global n
  area = 0 #area starts at zero
  if start > end: #negative integration
    lower = 1
    upper = n+1
  else: #positive integration
    lower = 0
    upper = n
  for i in range(lower,upper): #ex: for positive integration, if there are 10 rectangles, i would be 0, 1, 2...9) for negative integration, if there are 10 rectangles, i would be 1, 2, 3...10
    currentX = end - i*width #due to the i, currentX would be b, b-deltaX, b-2deltaX, ... a+deltaX)
    one_rectangle = f(currentX,A,B,C)*width #f(currentX,A,B,C) is the height, area is height * width
    area += one_rectangle #summation of the areas of each rectangle
  #print("RH"+str(n) + " = " + str(area))
  return area

#name: M
#purpose: calculates the midpoint sum for a given number of rectangles
#inputs: 3 integers: lower bound, upper bound, deltaX
#returns: none
def M(start,end,width):
  global A
  global B
  global C
  global n
  area = 0 #area starts at zero
  for i in range(0,n): #ex: if there are 10 rectangles, i would be 0, 1, 2...9)
    x1 = start + i*width #point 1 (a, a+deltaX, a+2deltaX,...b-deltaX)
    x2 = start + (i+1)*width #point 2, which is deltaX away from point 1 (a+deltaX, a+2deltaX,... b-deltaX, b)
    avg = (x1 + x2)/2 #midpoint of point 1 and point 2
    one_rectangle = f(avg,A,B,C)*width #f(avg,A,B,C) is the height, area is height * width
    area += one_rectangle #summation of the areas of each rectangle
  return area
  #print("M"+str(n) + " = " + str(area)) 


#name: T
#purpose: calculates the trapezoid sum for a given number of rectangles
#inputs: 3 integers: lower bound, upper bound, deltaX
#returns: none
def T(start,end,width):
  global A
  global B
  global C
  global n
  area = 0 #area starts at zero
  for i in range(0,n): #ex: if there are 10 rectangles, i would be 0, 1, 2...9)
    x1 = start + i*width #point 1 (a, a+deltaX, a+2deltaX,...b-deltaX)
    x2 = start + (i+1)*width #point 2, which is deltaX away from point 1 (a+deltaX, a+2deltaX,... b-deltaX, b)
    base1 = f(x1,A,B,C) #base 1 of the trapezoid
    base2 = f(x2,A,B,C) #base 2 of the trapezoid
    one_trapezoid = ((base1+base2)/2)*width #area of a trapezoid formula
    area += one_trapezoid #summation of the areas of each rectangle
  #print("T"+str(n) + " = " + str(area))
  return area
##########################################################
#MAIN
game_over = False
while not game_over:
  print("Calculate the area under the curve of a quadratic using a Riemann Sum!")
  print("A quadratic has the form Ax^2 + Bx + C")
  A = safe_to_integer(input("What is A?--->")) #gets the x^2 term
  B = safe_to_integer(input("What is B?--->")) #gets the x term
  C = safe_to_integer(input("What is C?--->")) #gets the constant
  print("Your equation is " + str(A)+ "x^2+" + str(B) + "x+"+ str(C)) #prints the quadratic
  a = safe_to_integer(input("Enter lower bound: ")) #gets the a value (minumum of integration)
  b = safe_to_integer(input("Enter upper bound: ")) #gets the b value (maximum of integration)
  n = safe_to_integer(input("How many rectangles in the Riemann Sum?--->")) #gets the n value
  deltaX = (b-a)/n #formula for n rectangles with equal width over [a,b] 
  print("\nDelta x: " + str(deltaX)) 
  print("\nProcessing...")
  print("\nLH" + str(n) + ": " + str(LHS(a,b,deltaX))) #uses the users' input to calulate all Riemann Sums
  print("\nRH" + str(n) + ": " + str(RHS(a,b,deltaX)))
  print("\nM" + str(n) + ": " + str(M(a,b,deltaX)))
  print("\nT" + str(n) + ": " + str(T(a,b,deltaX)))
  avg_L_R = (LHS(a,b,deltaX)+RHS(a,b,deltaX))/2 #the mean of LHS and RHS
  print("\nThe average of LH" + str(n) + " and RH" + str(n) + " is " + str(avg_L_R) + ". This should be equal to the trapezoid sum.")
  print("\n\n\n\n\n")
  