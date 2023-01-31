"""
CMPS 2200  Recitation 1
"""

### the only imports needed are here
import tabulate
import time
###

def linear_search(mylist, key):
	""" done. """
	for i,v in enumerate(mylist):
		if v == key:
			return i
	return -1

def test_linear_search():
	""" done. """
	assert linear_search([1,2,3,4,5], 5) == 4
	assert linear_search([1,2,3,4,5], 1) == 0
	assert linear_search([1,2,3,4,5], 6) == -1

def binary_search(mylist, key):
	""" done. """
	return _binary_search(mylist, key, 0, len(mylist)-1)

def _binary_search(mylist, key, left, right):
  if (right >= left):
    middle = (left + right) // 2
    if key == mylist[middle]:
      return middle
    if key < mylist[middle]:
      return _binary_search(mylist, key, left, middle - 1)
    if key > mylist[middle]:
      return _binary_search(mylist, key, middle + 1, right)
  else:
    return -1

def test_binary_search():
  assert binary_search([1,2,3,4,5], 5) == 4
  assert binary_search([1,2,3,4,5], 1) == 0
  assert binary_search([1,2,3,4,5], 6) == -1
  assert binary_search([1,2,3,4,5], 2) == 1
  assert binary_search([1,2,3,4,5], 4) == 3


def time_search(search_fn, mylist, key):
  start = time.time()
  search_fn(mylist, key)
  end = time.time()
  runtime = end - start
  runtime *= 1000
  return runtime

def compare_search(sizes=[1e1, 1e2, 1e3, 1e4, 1e5, 1e6, 1e7]):
  linearTimes = []
  for i in list(range(len(sizes))):
    searchList = list(range(int(sizes[i])))
    time = time_search(linear_search, searchList, -1)
    linearTimes.append(time)

  binaryTimes = []
  for i in list(range(len(sizes))):
    searchList = list(range(int(sizes[i])))
    time = time_search(binary_search, searchList, -1)
    binaryTimes.append(time)

  finalList = list(zip(sizes, linearTimes, binaryTimes))
  
  return finalList

def print_results(results):
	""" done """
	print(tabulate.tabulate(results,
							headers=['n', 'linear', 'binary'],
							floatfmt=".3f",
							tablefmt="github"))

def test_compare_search():
	res = compare_search(sizes=[10, 100])
	print(res)
	assert res[0][0] == 10
	assert res[1][0] == 100
	assert res[0][1] < 1
	assert res[1][1] < 1


print_results(compare_search())
