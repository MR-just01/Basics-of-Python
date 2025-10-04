history_file = "history.txt"  

def show_history():
    file = open(history_file , 'r')
    lines = file.readlines()
    if len(lines) == 0 :
        print("no history found!!")
    else:
        for line in reversed(lines):
            print(line.strip())
    file.close()

def clear_history():
    file = open(history_file , 'w')
    file.close()
    print("History is cleaned")

def save_to_history(equation , result):
    file  = open(history_file , 'a')
    file.write(equation + '=' + str(result)+ "\n")
    file.close()


def calculator(user_input):
    for op in ['+', '-', '*', '/']:
        if op in user_input:
            num1, num2 = user_input.split(op)
            num1 = float(num1.strip())
            num2 = float(num2.strip())
            operator = op
            break
    else:
        print("Invalid input. Use +, -, *, /")
        return

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 == 0:
            print("Invalid! You cannot divide by zero.")
            return
        result = num1 / num2

    print("Result:", result)
    save_to_history(user_input, result)
    

def main():
    print("-----------SIMPLE CALCULATOR-------------")
    while(True):
      user_input = input("enter the calculation (+,-,*,/) or command(history , clean , or exit  = )")
      if user_input == "exit":
          print("goodbye :)")
          break
      
      elif user_input == "history":
          show_history()
      elif user_input == "clean":
          clear_history()
      else:
          calculator(user_input)
        
main()
      
