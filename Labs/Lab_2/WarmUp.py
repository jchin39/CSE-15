from logic import TruthTable

table1 = TruthTable(['a', 'b'], ['a and -b'])
table1.display()

table2 = TruthTable(['a', 'b', 'c'], ['a and b','a and b or -c'])
table2.display()