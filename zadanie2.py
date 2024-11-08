def calculate_rpn(expression):
  """
  Вычисляет выражение в обратной польской нотации (RPN).

  Args:
    expression: Строка, представляющая выражение в RPN.

  Returns:
    Результат вычисления выражения.
  """

  stack = []
  operators = {"+": lambda x, y: x + y,
                "-": lambda x, y: x - y,
                "*": lambda x, y: x * y,
                "/": lambda x, y: x / y}

  for token in expression.split():
    if token in operators:
      operand2 = stack.pop()
      operand1 = stack.pop()
      result = operators[token](operand1, operand2)
      stack.append(result)
    else:
      stack.append(float(token))

  return stack.pop()
