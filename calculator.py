import re



def do_operation(a,op,b):
    if op == "+":
        return a+b
    if op == "-":
        return a-b

def read_line_and_split():
    line=input("enter your equation,")
    print (line,"=")
    # a,op,b = line.split()
    _, a, op, b, _ = re.split('(\d+)', line)
    return int(a),op,int(b)

X, operator, Y = read_line_and_split()
#print("X is", X)
#print("operator is", operator)
#print("Y is", Y)

answer =do_operation(X, operator, Y)
print (answer)