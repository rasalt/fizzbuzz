#!/usr/bin/python
# Version 2 of fizz buzz
import sys

#rint "The name of this script is {}".format(sys.argv[0])
#print "User supplied {} arguments at run time".format(len(sys.argv))

#for arg in sys.argv[1:]:
#  print arg
# Check if the second argument exists and if so check if its valid

if (len(sys.argv) > 1):
  input=sys.argv[1]
else:
  input=raw_input("Please enter an upper limit ")

# Check if the input is valid
validinput=False
while not validinput:
  try:
    upperlimit=int(input)
    validinput=True
  except:
    print "ERROR: Please input a valid value > 1"
    input=raw_input("Enter ")
    
for i in range(1,upperlimit+1):
  if ((i%3==0) and (i%5==0)):
    print "fizz buzz"
  elif i%3==0:
    print "fizz"
  elif i%5==0:
    print "buzz"
  else:
    print i
    
    