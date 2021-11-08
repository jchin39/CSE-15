from logic import TruthTable

truth = 'tautology'
exp = (input('Enter Expression: '))
table = TruthTable([exp])
table.display()
tt = table.table
vals = []
for i in range(len(tt)):
    vals.append(tt[i][len(tt[0])-1][0])
for i in vals:
    if i == 0:
        truth = 'contradiction'
        for i in vals:
            if i == 1:
                truth = 'contingency'
                break
print(truth)