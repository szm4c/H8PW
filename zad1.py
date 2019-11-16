
def repleace_pattern(t,s,r):
    assert len(t) > 0
    assert len(s) > 0
    assert len(r) > 0
    assert len(t) >= len(s)
    n = len(t)
    m = len(s)
    k = len(r)
    idx = -1
    for i in range(0, n):
        if t[i] == s[0]:
            pattern = True
            for j in range(1,m):
                if t[i+j] != s[j]:
                    pattern = False
                    break
            if(pattern):
                idx=i
                break
    result = t
    print(idx)
    if(idx!=-1):
        result = [*t[0:idx],*r,*t[idx+m:n]]
    return result





print (repleace_pattern([1,2,3,1,2,3,4],[1,2,3,4],[9,0]))





