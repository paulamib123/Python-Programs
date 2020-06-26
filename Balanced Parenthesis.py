def splitparenthesis(txt):
    ans = []
    new = ""
    count1 = 0
    count2 = 0
    for i in range(len(txt)):
        if txt[i] == '(':
            count1 += 1
            new += txt[i]
        elif txt[i] == ')':
            count2 += 1
            new += txt[i]
        if count1 == count2:
            ans.append(new)
            count1 = 0
            count2 = 0
            new = ""
    return ans
