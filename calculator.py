def calculate(query):
	query = query.lower()
	idx1 = query.find('будет')
	idx2 = query.find('вычисли')
	idx = max(idx1, idx2)
	expr = ' '.join(query[idx:].split()[1:])
	expr = expr if expr[-1] != '?' else expr[:-1]
	expr = expr.replace('^', '**')
	print(eval(expr))
	
	
if __name__ == "__main__":
	calculate(input())