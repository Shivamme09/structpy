from structpy import stack

stk = stack()
stk.push(8)
stk.push(12)
stk.push(15)

def test_str():
	assert(str(stk)=="[8, 12, 15]")

def test_pop():
	assert(stk.pop()==15)

def test_gettop():
	assert(stk.gettop()==12)

def test_length():
	assert(len(stk)==2)

def test_pop_again():
	assert(stk.pop()==12)