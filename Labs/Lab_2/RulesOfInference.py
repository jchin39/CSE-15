from logic import TruthTable

print('Modus Poncus')
tablePoncus = TruthTable(['p', 'q'], ['p -> q','(p -> q) and p', '((p -> q) and p) -> q'])
tablePoncus.display()

print ('Modus Tollens')
tableTollens = TruthTable(['p', 'q'], ['-p', 'p -> q', '-q and (p -> q)', '(-q and (p -> q)) -> -p'])
tableTollens.display()

print ('Hypothetical Syllogism')
tableHypo = TruthTable(['p', 'q', 'r'], ['p -> q', 'q -> r', 'p -> r', '(p -> q) and (q -> r)', '((p -> q) and (q -> r)) -> (p -> r)'])
tableHypo.display()

print ('Disjunctive Syllogism')
tableDisj = TruthTable(['p', 'q'], ['-p', 'p or q', '((p or q) and -p)', '((p or q) and -p) -> q'])
tableDisj.display()

print ('Addition')
tableAddition = TruthTable(['p', 'q'], ['p or q', 'p -> (p or q)'])
tableAddition.display()

print ('Simplification')
tableSimplification = TruthTable(['p', 'q'], ['p and q', '(p and q) -> p'])
tableSimplification.display()

print('Conjunction')
tableConjunction = TruthTable(['p', 'q'], ['((p) and (q))', '(p and q)', '((p) and (q)) -> (p and q)'])
tableConjunction.display()

print('Resolution')
tableResolution = TruthTable(['p', 'q', 'r'], ['-p','-p or r', 'p or q', 'q or r', '((p or q) and (-p or r))', '((p or q) and (-p or r)) -> (q or r)'])
tableResolution.display()

print('number 5')
table5 = TruthTable(['p1','p2','p3','q'],['p1 -> q', 'p2 -> q', 'p3 -> q', 'p1 and p2 and p3 -> q', '(p1 -> q) and (p2 -> q) and (p3 -> q)', '((p1 and p2 and p3) -> q) <-> ((p1 -> q) and (p2 -> q) and (p3 -> q))'])
table5.display()
table5.latex()

table5_1 = TruthTable([''],[ '(p1 -> q) and (p2 -> q) and (p3 -> q)', '((p1 and p2 and p3) -> q) <-> ((p1 -> q) and (p2 -> q) and (p3 -> q))'])
table5_1.latex()