count = {'짜장': 3, '짬뽕': 2, '볶음밥': 1, '탕수육': 4}
print(list(count.items()))
print(sorted(count.items()))                 # 기준 없음
items = sorted(count.items(), key=lambda x: x[1], reverse=True)
print(items)
for menu, c in items[:2]:                    # 앞의 2개만
    print(menu, c)
 
def second(x):          # lambda x: x[1] 과 같은 함수
    return x[1]


print(second(('짜장', 3)))                                  # 3

a = sorted(count.items(), key=second, reverse=True)        # 일반 함수
b = sorted(count.items(), key=lambda x: x[1], reverse=True)  # 람다
print(a)
print(b)