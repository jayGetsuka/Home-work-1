def Process(list_num, num):
    total = []
    for i in list_num:
        if i > num:
            total.append(i)
        else:
            pass
    return total

number = int(input("ค่า K : "))
list_num = list(eval(input("ชุดข้อมูลจำนวนเต็ม: ")))
data = Process(list_num, number)
print("ค่าที่มากกว่าค่า: ",number)
print("ได้แก่")
for i in data:
    print(i, end=" ")
