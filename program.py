import re
import operator

dic = {'(':1,'+':2,'-':2,'*':3,'/':3,'^':4}
ops = {
    '+' : operator.add,
    '-' : operator.sub,
    '*' : operator.mul,
    '/' : operator.truediv,
    '^' : operator.pow,
}


def convert(formula):  #Convert Infix to Postfix
    out = ""
    stack = []
    for i in formula:
        if i == ')':
            while True:
                last = stack.pop()
                if last == '(':
                    break
                out += last
                    
        elif re.match(r'[\^\(\+\-\*/]',i):
            if stack == [] or i=='(' or dic[i] > dic[stack[-1]]:
                stack.append(i)
                continue
            else:
                while stack and dic[stack[-1]] >= dic[i]:
                    last = stack.pop()
                    out += last
                stack.append(i)
                continue
        else:
            out += i
    while stack:
        out += stack.pop()
        
    print("Postfix :",out)
    return(out)



def evaluate(pfx):
    stack = []
    for i in pfx:
        if re.match(r'[\^\+\-\*/]',i):
            a = stack.pop()
            b = stack.pop()
            res = ops[i](b,a)
            stack.append(res)
        else:
            stack.append(int(i))
    return(stack[0])
    
    
def preprocess(s):
    s = s.replace(" ","")
    x = re.findall(r'[^a-zA-Z0-9\^\(\+\-\*/\)]',s)
    if x:
        print('Incorrect characters:', x)
        exit()
    #To Add later: check if the formula is correct (parentheses etc)
    return s
    
 
"""
Some valid test cases:
    A = "a*(a+b)*b^2"
    B = "(((A+B)*C)-((D-E)*(F+G)))"
    C = "4-2/2"
    D = "A+B*C+D"
    E = "3*(x+1)-2/2"
"""
   
def main():
    s = input()
    s = preprocess(s)
    out = convert(s)
    if re.search(r'[^0-9\^\+\-\*/]',out):
        print("Can't evaluate")
        return(1)
    print("evaluation =",evaluate(out))
    return(0)
    
if __name__== '__main__':
    main()