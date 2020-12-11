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
            
def infixToPostfix(infixexpr):
    prec = {}
    prec["^"] = 4
    prec["*"] = 3
    prec["/"] = 3
    prec["+"] = 2
    prec["-"] = 2
    prec["("] = 1
    opStack = ArrayStack()
    postfixList = []
    tokenList = infixexpr.split()

    for token in tokenList:
        if token in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" or token in "0123456789":
            postfixList.append(token)
        elif token == '(':
            opStack.push(token)
        elif token == ')':
            topToken = opStack.pop()
            while topToken != '(':
                postfixList.append(topToken)
                topToken = opStack.pop()
        else:
            while (not opStack.isEmpty()) and \
                (prec[opStack.peek()] >= prec[token]):
                postfixList.append(opStack.pop())
            opStack.push(token)

    while not opStack.isEmpty():
        postfixList.append(opStack.pop())
    return " ".join(postfixList)

print(infixToPostfix("A - ( B / ( C - D ) * E + F ) ^ G"))

