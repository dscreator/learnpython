def factorial( n ):
  if n == 0: # base case
    return 1
  else:
      recurse = factorial(n-1)
      result = n * recurse
      return result

print ("enter a number ")
c = input()
print (factorial(int(c)))

