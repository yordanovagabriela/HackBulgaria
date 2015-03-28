def p_score(n):
    if str(n) == str(n)[::-1]:
        return(1)
    else:
        return 1+p_score(n+int(str(n)[::-1]))
print(p_score(198))
