a = 4-1
b = 2-1


dp = {}

def helper(p1, p2, s1, s2):

    # root case, plus one for p1 or plus one for p2, or reached a seen state before
    if s1 >=21:
        return (1,0)
    if s2 >= 21:
        return (0,1)
    if (p1, p2, s1, s2) in dp:
        return dp[(p1, p2, s1, s2)]
    
    ans = (0,0)

    for d1 in [1,2,3]:
        for d2 in [1,2,3]:
            for d3 in [1,2,3]:
                new_p1 = (p1+d1+d2+d3) % 10
                new_s1 = s1 + new_p1 + 1

                # reverse order, no move count, p1 is now p2, p2 is now p1 after p1 take turn
                x1, y1 = helper(p2, new_p1, s2, new_s1)
                ans = (ans[0]+y1, ans[1]+x1)
    dp[(p1, p2, s1, s2)] = ans
    return ans

print(max(helper(a, b, 0, 0)))