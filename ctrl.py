# ch 7.7.2 ctrl.py

class Control:
  
  def __init__(self, view):
    self.view = view
    self.connectSignals()

  def calculate(self): # ^, % 연산 기능 제거거
    try:  
      num1 = float(self.view.le1.text())
      num2 = float(self.view.le2.text())
      operator = self.view.cb.currentText()   

      if operator == '+': 
        return f'{num1} + {num2} = {self.sum(num1, num2)}'
      elif operator == '-': 
        return f'{num1} - {num2} = {self.sub(num1, num2)}'
      elif operator == '*': 
        return f'{num1} * {num2} = {self.mul(num1, num2)}'
      elif operator == '/': 
        return f'{num1} - {num2} = {self.div(num1, num2)}'
      # elif operator == '^': 
      #   return f'{num1} ^ {num2} = {self.pow(num1, num2)}'
      # elif operator == '%': # '%'를 입력했을 때 mod 연산 결과를 출력하도록 추가
      #   return f'{num1} % {num2} = {self.mod(num1, num2)}'
      else:
        return "Calculation Error"
    except:
      return "Calculation Error"

  def connectSignals(self): # btn1을 클릭하면 calculate 결과가 화면에 표시되도록 수정 
    self.view.btn1.clicked.connect(lambda: \
                                   self.view.setDisplay(self.calculate()))
    self.view.btn2.clicked.connect(self.view.clearMessage)

  def sum(self, a, b):  
    return a + b
  
  def sub(self, a, b): 
    return a - b
  
  def mul(self, a, b): 
    return a * b
  
  def div(self, a, b): # div 함수 수정
    try:
      if b==0:
        raise Exception("Divisor Error")
    except Exception as e:
      return e
  
    return a / b
  
  def pow(self, a, b): # 예외 처리를 사용하도록 수정정
    try:
      if a==0:
        raise Exception("Base Error")
    except Exception as e:
      return e

    return pow(a, b)
  
  def mod(self, a, b):  # 나눗센 연산의 나머지를 리턴하는 함수 추가
    try:
      if b==0:
        raise Exception("Divisor Error")
    except Exception as e:
        return e
    
    return a%b
