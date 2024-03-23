def check(n):
    if n==0:
        return True
    else:
        return False
    

def p(n,m):
    if m==0:
        return 1
    return n*p(n,m-1)
p()
