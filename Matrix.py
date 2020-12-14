import numpy as np

def swap(a, i, j):
  temp = np.copy(a[i, 0:])
  a[i, 0:] = a[j, 0:]
  a[j, 0:] = temp
print("Example input : 1,2,3,4")
row1 = list(eval(input("Row 1: ")))
row2 = list(eval(input("Row 2: ")))
row3 = list(eval(input("Row 3: ")))
a = np.array([row1, row2, row3], float)
swap(a, 0, 2)
print(a)
nr = len(a)
nc = len(a[0, 0:])
for i in range(0,nr):
  if a[i,i] == 0:
   j = i +1
   while j < nr:
     if a[j, i] == 0:
       j += 1
     else:
       break
   print("Swap row", i, " & row ", j, "\n")
   swap(a,i, j )
  d = a[i, i ]
  a[i, 0:] = a[i, 0:] / d
  print("Devide row ", i , "By", d, "\n")
  print(a)

  #reduce row
  for j in range(0, nr):
    if i != j:
      dd =  a[j,i]
      a[j, 0:] = a[j, 0:] - a[i, 0:] *dd
      print("reduce row ", j, "-", dd, "+R", i, "->R", j, "\n")
  print(a)