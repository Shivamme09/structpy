from structpy import queue

que = queue()
que.enque(4)
que.enque(6)
que.enque(10)

def test_str():
	assert(str(que)=="[4, 6, 10]")

def test_deque():
	assert(que.deque()==4)

def test_getfront():
	assert(que.getfront()==6)

def test_getlast():
	assert(que.getlast()==10)

def test_length():
	assert(len(que)==2)