import re

def isInt(t):
    return t.isdigit()

def isFloat(t):
    try:
        float(t)
        return True
    except:
        return False

def isChar(t):
    if t[0] != '\'' or t[1] != '\'':
        return False
    elif not t[1].isalpha():
        return False
    return True

def isString(t):
    if t[0] != '"' or t[-1] != '"':
        return False
    return True

def isIndentifier(t):
    if not t[0].isalpha() and t[0] != '_':
        return False

    for i in t:
        if not i.isalpha() and not isInt(i) and i != '_':
            return False

    return True

keywords = ['float', 'int', 'return', 'auto', 'case', 'break', 'char', 'do', 'while', 'for']
operators = ['+', '-', '*', '/', '%', '=', '<', '>', '==', '<=', '>=', '!=']

def tokenize(pr):
    tokens = []
    for lexeme in pr:
        end_statment = False

        if lexeme[-1] == ';':
            end_statment = True
            lexeme = lexeme[:-1]

        if lexeme in keywords:
            tokens.append(('keyword', lexeme))

        elif lexeme in operators:
            tokens.append(('operator', lexeme))

        elif isInt(lexeme):
            tokens.append(('literal-integer', lexeme))

        elif isFloat(lexeme):
            tokens.append(('literal-float', lexeme))

        elif isString(lexeme):
            tokens.append(('literal-string', lexeme))

        elif isChar(lexeme):
            tokens.append(('literal-char', lexeme))

        elif isIndentifier(lexeme):
            tokens.append(('identifier', lexeme))

        elif lexeme == '{':
            tokens.append(('block-start', lexeme))

        elif lexeme == '}':
            tokens.append(('block-close', lexeme))

        if end_statment:
            tokens.append(('END-STATEMENT'))


f = open("program.c", "r");
x = f.read().split()
tokens = tokenize(x)

for token in tokens:
    print(token)

print(x)
