def calculate(operation, number1, number2):
  if operation.lower() == 'a':
    result = number1 + number2
  if operation.lower() == 'm':
    result = number1 * number2
  if operation.lower() == "d":
      result = number1 / number2
  return result