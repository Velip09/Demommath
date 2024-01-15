#Function to Calculate the Least Common Multiple (LCM) of three numbers

def lcm(a, b, c):
 
  max_num = max(a, b, c)  #  # Find the maximum of the three numbers
  lcm = max_num   # Initialize lcm with the maximum number
  while True:
    if lcm % a == 0 and lcm % b == 0 and lcm % c == 0: # Check if lcm is divisible by all three numbers
      break           # Break the loop if lcm is found  
    lcm += max_num    # Increment lcm by the maximum number to continue checking

  return lcm