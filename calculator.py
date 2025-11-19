def add(a, b):
  return a + b
def square(a):
  """Return the square number"""
  return a ** 2
def percentage(value, percent):
    """Calculate percentage of a value"""
    return (value * percent) / 100
# Updated from the Github web interfaces
if __name__ == "__main__":
  print("Calculator Loaded!")
  print(f"5 + 3 = {add(5, 3)}")
  print(f"5 squared = {square(5)}")
