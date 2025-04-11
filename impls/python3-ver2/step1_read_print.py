def READ(arg):
    return arg

def EVAL(arg):
    return arg

def PRINT(arg):
    return arg

def rep(arg):
    return PRINT(EVAL(READ(arg)))

# MAIN LOOP
try:
    while True:
        print("user> ", end="")
        arg = input()
        repResult = rep(arg)
        print(repResult)
except (KeyboardInterrupt, EOFError):
    exit()