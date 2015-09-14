# - Convert this while-loop to a function that you can call, and replace 6 in the test (i < 6) with a variable.
# - Use this function to rewrite the script to try different numbers.
# - Add another variable to the function arguments that you can pass in that lets you change the + 1 on line 8 so you can change how much it increments by.
# - Rewrite the script again to use this function to see what effect that has.

# i = 0
# numbers = []

# while i < 6:
#     print "At the top i is %d" % i
#     numbers.append(i)

#     i = i + 1
#     print "Numbers now: ", numbers
#     print "At the bottom i is %d" % i


# print "The numbers: "

# for num in numbers:
#     print num

def loop(maximum, increment):
  i = 0
  numbers = []

  while i < maximum:
    print "At the top i is %d" % i
    numbers.append(i)

    i += increment
    print "Numbers now: ", numbers
    print "At the bottom i is %d" % i

  print "The numbers: "

  for num in numbers:
    print num

loop(6, 1)