votes = ['짜장', '짬뽕', '짜장', '볶음밥', '짜장', '짬뽕']
 
count = {}
for menu in ['짜장', '짬뽕', '볶음밥']:
    count[menu] = 0           # ① 0으로 준비
for v in votes:
    count[v] += 1             # ② 나올 때마다 +1
 
print(count)
print(count['짜장'], sum(count.values()))