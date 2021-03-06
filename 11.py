class ArrayStack(object):
#Constructor to create a stack
    def __init__(self, limit=10):
        self.stk = [] # Create an empty stack
        self.limit = limit

    #Return True if the stack is empty
    def isEmpty(self):
        return len(self.stk) <= 0

    #Return True if the stack is full
    def isFull(self):
       return len(self.stk) >= self.limit

    #Add item to the top of the stack
    def push(self, item):
        if self.isFull(): #Check if the stack is full
           print ('Stack Overflow!')
        else:
            self.stk.append(item)
            print ('Stack after Push', self.stk)
    #Remove and return item from the top of the stack
    def pop(self):
        if self.isEmpty(): #Check if the stack is empty
           print ('Stack Underflow!')
           return 0
        else:
           return self.stk.pop()

    #Return (but do not remove) item at the top of the stack
    def peek(self):
        if self.isEmpty():
           print ('Stack Underflow!')
           return 0
        else:
           return self.stk[-1]

    #Return the number of items in the stack
    def size(self):
       return len(self.stk)
            
def postfixEval(postfixExpr):
    operandStack = ArrayStack()
    tokenList = postfixExpr.split()

    for token in tokenList:
        if token in "0123456789":
           operandStack.push(int(token))
        else:
           operand2 = operandStack.pop()
           operand1 = operandStack.pop()
           result = calMath(token, operand1, operand2)
           operandStack.push(result)
    return operandStack.pop()

def calMath(op, op1, op2):
    if op == "*":
        return op1 * op2
    elif op == "/":
        return op1 / op2
    elif op == "+":
        return op1 + op2
    else:
        return op1 - op2

print(postfixEval("20 5 3 - / 5 *"))