def creating(expresion):
    output = []
    stack = []
    priority = {"^":3, "*":2, "/":2, "+":1, "-":1}
    for elem in expresion:
        if elem.isdigit():
            output.append(elem)
        elif elem in priority:
            while len(stack) > 0 and stack[-1] != '(' and priority[stack[-1]] >= priority[elem]:
                output.append(stack.pop())
            stack.append(elem) 
        elif elem == '(':
            stack.append(elem)
        elif elem == ')':
            for stk in stack:
                if stk == '(':
                    while len(stack) > 0 and stack[-1] != '(':
                        output.append(stack.pop())
                    stack.pop()
    while len(stack) > 0:
        if stack[-1] != '(':
            output.append(stack.pop())
        else:
            stack.pop() 
    return output


def calculating(output):
    stack=[]
    for elem in output:
        if elem not in ["^","*","/","+","-"]:
            stack.append(elem)
        else:
            b = float(stack.pop()) 
            a = float(stack.pop())
            match (elem):
                case "+":                    # Якщо значення op + то виконується даний випадок
                    stack.append(a + b)
                case "-":                    # Якщо значення op - то виконується даний випадок
                    stack.append(a - b)
                case "*":                    # Якщо значення op * то виконується даний випадок
                    stack.append(a * b)
                case "/":                    # Якщо значення op / то виконується даний випадок
                    try:               
                        stack.append(a / b)
                    except ZeroDivisionError:
                        return("Неможливо ділити на 0")
                case "^":                    # Якщо значення op ** то виконується даний випадок                
                    stack.append(a ** b)
    return stack[0]


def main():
    expresion = input("Введіть вираз: ").replace(' ', '')
    output=creating(expresion)
    print(f"Вираз у ЗПН :{output} ")
    print(f"Результат: {calculating(output)}")

main()