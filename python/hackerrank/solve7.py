def verify_if_is_factor(array, integer):
    factors = [value for value in array if integer % value == 0]
    if len(factors) == len(array):
      return True
    
    return False

def verify_if_integer_is_factor(array, integer):
    factors = [value for value in array if value % integer == 0]
    
    if len(factors) == len(array):
      return True
    return False
  
verify_if_is_factor([2,4])
