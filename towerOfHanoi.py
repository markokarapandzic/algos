def pm(start, end):
  print(start, " -> ", end)

def hanoi(n, start, end):
  if n == 1:
    pm(start, end)
  else:
    other = 6 - (start + end)
    hanoi(n - 1, start, other)
    pm(start, end)
    hanoi(n - 1, other, end)

# hanoi(3, 1, 3)

# Base CaseL n = 1, znaci vracamo 1
# f(n - 1) = Recimo ako je n = 5 onda moramo 5 + 4 + 3!
# f(n) = Onda ako n = 5 Moramo 5 + 4!
def factorial(n):
  if n == 1:
    return 1
  else:
    return n * factorial(n - 1)

# print(factorial(5))

# Base Case: ako je n = 1, onda vracamo 1
# f(n - 1) case: Ako nam je n = 5, onda za moramo da za 4 dobijemo 3
# f(n) case: Ako nam je n = 5, onda moramo nazad da dobijemo 5(jer je 5 elem po redu)
def fibo(n):
  if n == 1:
    return 1
  if n == 2:
    return 2
  else:
    return fibo(n - 1) + fibo(n - 2)

# print(fibo(5))

# Base case: n == 1 proverimo da li je x, ako jeste vratimo x, ako nije vratimo None
# f(n - 1) case: Izbacili smo prvu polovinu, onda gledamo samo desnu ili levu, uzimamo pola i idemo dalje
# f(n) case: Gledam sta je vise a sta manje i izbacujemo polovinu, ako je mid == x onda vratimo x
def binSearch(arr, n, x):
  if n == 1:
    if arr[0] == x:
      print(str(arr[0]))
    else:
      print("Element is not in the array")
  else:
    mid = n // 2

    if arr[mid] == x:
      print(str(arr[mid]))
    elif (x > arr[mid]):
      binSearch(arr[mid:], len(arr[mid:]), x)
    else:
      binSearch(arr[:mid], len(arr[:mid]), x)

test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
binSearch(test_list, len(test_list), 1)

