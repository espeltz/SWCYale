mylist=[1,2,5]

mydict={'xin':12, 'yfloat':12., 'mylist':mylist}


def func3(*args,**kwargs) :
	keys = kwargs.keys()
	keys.sort()
	print keys		


func3('xin'=12, 'yfloat'=12., 'mylist'=mylist)

