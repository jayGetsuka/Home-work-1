#sumstd = []
score_std = []
round = int(input("จำนวนนักศึกษา: "))
print("ตัวอย่างการใช้งานโปรแกรมลงคะแนน เช่น 18,20,28   ห้ามเว้นวรรค ห้ามใส่เป็นตัวหนังสือ ห้ามใส่เกิน3ตัว ใส่คอมม่าคั้นตลอด")
for i in range(round):
    print("คนที่", i +1)
    score = list(eval(input("การสอบครั้งที่1,ครั้งที่2,ครั้งที่3: ")))
    #sumstd.append(sum(score))
    if i == 0:
        score_std.append([score[0]])
        score_std.append([score[1]])
        score_std.append([score[2]])
    else:
        score_std[0].append(score[0])
        score_std[1].append(score[1])
        score_std[2].append(score[2])
print()
n = 1
for i in range(len(score_std[0])):
    print("คนที่",n, "ได้คะแนน: ",(score_std[0][i] + score_std[1][i] +score_std[2][i]))
    n += 1
print()
for i in range(len(score_std)):
    print("การสอบครั้งที่", i+ 1)
    print("คะแนนเฉลี่ย: {:.2f}".format(sum(score_std[i]) / len(score_std[i])))
    print("คะแนนสูงสุด: ", max(score_std[i]))
    print("คะแนนต่ำสุด: ", min(score_std[i]))
