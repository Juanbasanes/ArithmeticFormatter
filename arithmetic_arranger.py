import re

def arithmetic_arranger(problems, solve = False):

#arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])

#arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)

  # Check lenght of problems is <= 5  
  if(len(problems) > 5):
    return "Error: Too many problems."
  
  # Variables
  first = ""
  second = ""
  lines = ""
  sumx = ""
  string = ""

  # Loop
  for problem in problems:

    # Check operator (+/-) and int
      if(re.search("[^\s0-9.+-]", problem)):
        if(re.search("[/]", problem) or re.search("[*]", problem)):
          return "Error: Operator must be '+' or '-'."
        return "Error: Numbers must only contain digits."
  
      firstNumber = problem.split(" ")[0]
      operator = problem.split(" ")[1]
      secondNumber = problem.split(" ")[2]
  
    # Check if lenght of each number < 5 digits
      if(len(firstNumber) >= 5 or len(secondNumber) >= 5):
        return "Error: Numbers cannot be more than four digits."
  
    # Calculation (+/-)  
      sum = ""  
      if(operator == "+"):
        sum = str(int(firstNumber) + int(secondNumber))
      elif(operator == "-"):
        sum = str(int(firstNumber) - int(secondNumber))
  
      length = max(len(firstNumber), len(secondNumber)) + 2
      top = str(firstNumber).rjust(length)
      bottom = operator + str(secondNumber).rjust(length - 1)
      line = ""
      res = str(sum).rjust(length)
      for s in range(length):
        line += "-"
  
      if problem != problems[-1]:
        first += top + '    '
        second += bottom + '    '
        lines += line + '    '
        sumx += res + '    '
      else:
        first += top
        second += bottom
        lines += line
        sumx += res

  if solve:
    string = first + "\n" + second + "\n" + lines + "\n" + sumx
  else:
    string = first + "\n" + second + "\n" + lines
  return string

  