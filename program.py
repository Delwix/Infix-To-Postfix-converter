import re


dic = {'(':1,'+':2,'-':2,'*':3,'/':3,'^':4}


def postfix(formula):
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
        
    print(out)
    return(out)


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
    postfix(s)
    return
    
if __name__== '__main__':
    main()