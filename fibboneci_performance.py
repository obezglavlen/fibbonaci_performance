import time


def fibonacci_stndrd(n):
	if n == 0:
		return 0
	if n == 1:
		return 1
	return fibonacci_stndrd(n - 1) + fibonacci_stndrd(n - 2)


def fibonacci_memoize(n, computed = {0: 0, 1: 1}):
	if n not in computed:
		computed[n] = fibonacci_memoize(n-1, computed) + fibonacci_memoize(n-2, computed)
	return computed[n]


def fibonacci2(n):
	a, b = 0, 1

	if n in [0, 1]:
		return n

	for i in range(n):
		a, b = b, a + b

	return b


def timer(func):
	def wrapper(*argc, **kwargc):
		start_time = time.perf_counter()
		value = func(*argc, **kwargc)
		end_time = time.perf_counter()
		work_time = end_time - start_time
		print(f'{func.__name__} end in {work_time:.6f} secs.')
		return value
	return wrapper


# ~90s
@timer
def fib_std():
	for i in range (10, 50, 10):
		fibonacci_stndrd(i)


# ~0.01s
@timer
def fib_mem():
	for i in range (10000):
		fibonacci_memoize(i)


# ~10s
@timer
def fib2():
	for i in range (10000):
		fibonacci2(i)


# fib_std();
fib_mem()
# fib2()