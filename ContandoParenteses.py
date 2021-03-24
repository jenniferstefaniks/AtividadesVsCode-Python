def parenteses(string):
    var1 = string.count('(')
    var2 = string.count(')')
    if var1 == var2:
        return print('Parenteses se fecham')
    else:
        return print('Os parenteses não se fecham')
    
string = '((())))'
parenteses(string)
    
    