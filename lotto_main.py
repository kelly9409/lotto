from lotto_utils import *

while True:
    try : 
        count = int(input("몇 게임을 원해 (1~10)? : "))
        if 1<= count <=10 :    
            break
        print('1~10 사이의 숫자를 입력하세요.')
    except ValueError:
        print('숫자를 입력하세요.')

games = make_games(count)

print('\n\n### 로또 번호 생성기 ###\n')
for i in range(count) :
    print(f'게임 {i+1} : {to_text(games[i])}')

print()