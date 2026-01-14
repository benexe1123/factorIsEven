# Function which determines if a number is even or odd, using factors (2)
def isEven(num):
  if num==0:                                                              # num==0 is an even number.
    print("0 is even.")
  else:                                                                     # For positive and negative numbers
    factors = findFactors(num)                                              # Compute all positive factors of num
    if 2 in factors:                                                        # If 2 is a factor of num, num is even
      print(f"{num} is even.")
    else:                                                                   # Otherwise num is odd
      print(f"{num} is odd.")
  
# Returns a list of positive factors of a positive number
def findFactors(num):
  arr = []                                                                  # Array of factors
  for i in range(1, abs(num)+1):                                            # Iterate through every i from 1 to abs(num)+1
    if (num%i==0):                                                          # If the number is divisible by i
      arr.append(i)                                                         # Then append it to the shared factor list
  return arr                                                                # Returns the list of factors

# Main function: Loop of prompt for numbers, displays even/odd
def main():
  cont = True                                                               # Continue flag
  while cont == True:                                                       # While continue flag
    num = input("Enter an integer value or type 'exit': ")                  # User input
    if num == "exit":                                                       # If exit code
      cont = False
    else:                                                                   # Otherwise, compute even or odd
      isEven(int(num))

main()  