def are_happy(s):
    if len(s)<2:
        return s[1]==s[0] and s[1] != '_'
    if s.count('_') == 0:
        for i in range (1, len(s) - 1):
            if s[i] != s[i + 1] and s[i] != s[i-1]:
                return False
        return True
    s = s.replace("_","")
    bugcounts = {}
    for bug in s:
        bugcounts.setdefault(bug,0)
        bugcounts[bug]=bugcounts[bug] + 1
    counts = list(bugcounts.values())
    return counts.count(1) == 0

bugs = 'abadds_ff_edskkkskkkk'

print(are_happy(bugs))