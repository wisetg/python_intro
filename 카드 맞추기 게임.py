import random     #렌덤 정의

sh=['S','C','H','D']    #sh리스트
num=['A', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'J', 'Q', 'K']     #num리스트
players=['csm', 'yhm', 'zgm']     #players리스트

csm=2000     #철수 소지금
yhm=2000     #철수 소지금
zgm=2000     #철수 소지금
n=0     #회차



def player_turn():     #참가자 순서 함수
    global csm, yhm, zgm     #전역변수 불러오기
    print("=== 플레이어 : 철수 (", csm, ") ===\n")     #철수의 소지금 출력
    csm=game_play(csm)     #철수의 소지금
    print("=== 플레이어 : 영희 (", yhm, ") ===\n")     #영희의 소지금 출력
    yhm=game_play(yhm)     #영희의 소지금
    print("=== 플레이어 : 짱구 (", zgm, ") ===\n")     #짱구의 소지금 출력
    zgm=game_play(zgm)     #짱구의 소지금
    return csm, yhm, zgm     #소지금 리턴


def game_play(player_money):     #소지금 배팅
    while True:     #반복문
        com_shape1=random.choice(sh)     #컴퓨터 모양1 고르기
        com_num1=random.choice(num)     #컴퓨터 숫자1 고르기
        com_shape2=random.choice(sh)     #컴퓨터 모양2 고르기
        com_num2=random.choice(num)     #컴퓨터 숫자2 고르기
        bet_money=int(input("배팅 금액 :"))     #배팅금액 입력받기
        game_money=bet_money-player_money     #배팅금액-소지금액
        if (game_money>0):     #소지금액 배팅금액 보다 적을 때
            print("자신의 금액 내에서 배팅해주세요")     #배팅 다시하기 출력
            continue     #다시 반복
        else:     #그외의 상황일때
            pmm=game(game_money, bet_money, player_money)     #최종 소지금
            return pmm     #최종 소지금 반환
        
def game(game_money, bet_money, player_money):     #게임 함수
    while True:     #반복문
        pl_num1=input("1번째 카드의 숫자 선택 :")     #1번째 카드 숫자 입력
        if (pl_num1 in num):     #1번째 카드가 num리스트에 있을 때
            break     #탈출
        else:     #그외
            print("A 부터 K내에서 선택해 주세요.")     #A부터 K에서 선택하게 출력
            continue     #계속
    while True:     #반복문
        pl_shape1=input("1번째 카드의 문양 선택, ♠(S)♣(C)♥(H)◆(D) :")     #카드의 모양선택
        if (pl_shape1 in sh):  #sh에서 모양을 선택했을 때
            break     #탈출
        else:     #그외
            print("♠(S)♣(C)♥(H)◆(D) 에서 선택해 주세요.")     #다시 선택 요청
            continue     #계속
    print("\n")     #줄 띄기
    while True:     #반복문
        pl_num2=input("2번째 카드의 숫자 선택 :")     #2번째 카드 숫자 입력
        if (pl_num2 in num):     #2번째 카드가 num리스트에 있을 때
            break     #탈출
        else:     #그외
            print("A 부터 K내에서 선택해 주세요.")     #다시 선택하게 출력
            continue     #계속
    while True:     #반복문
        pl_shape2=input("2번째 카드의 문양 선택, ♠(S)♣(C)♥(H)◆(D) :")     #카드의 모양선택
        if (pl_shape2 in sh):     #sh에서 모양을 선택했을 때
            break     #탈출
        else:     #그외
            print("♠(S)♣(C)♥(H)◆(D) 에서 선택해 주세요.")     #다시 선택 요청
            continue     #계속
    print("\n")     #줄 띄기
    print("선택한 카드 : ", pl_num1, pl_shape1, pl_num2, pl_shape2,"\n")     #선택한 카드 출력
    pm=betting(pl_num1, com_num1, pl_shape1, com_shape1, pl_num2, com_num2, pl_shape2, com_shape2, player_money, bet_money)     #다른 함수에서 값 불러오기
    return pm     #반환


def betting(pl_num1, com_num1, pl_shape1, com_shape1, pl_num2, com_num2, pl_shape2, com_shape2, player_money, bet_money):     #배팅 함수
    if (pl_num1==com_num1 and pl_shape1==com_shape1 and pl_num2==com_num2 and pl_shape2==com_shape2):     #2 카드가 같을 때
        player_money= player_money-bet_money+bet_money*10     #10배 배당
        return player_money     #반환
    elif (pl_num1==com_num2 and pl_shape1==com_shape2 and pl_num2==com_num1 and pl_shape2==com_shape1):     #2 카드가 같을 때
        player_money= player_money-bet_money+bet_money*10     #10배 배당
        return player_money     #반환
    elif (pl_num1==com_num1 and pl_num2==com_num2):     #2 숫자가 같을 때
        player_money= player_money-bet_money+bet_money*8     #8배 배당
        return player_money     #반환
    elif (pl_num2==com_num1 and pl_num1==com_num2):     #2 숫자가 같을 때
        player_money= player_money-bet_money+bet_money*8     #8배 배당
        return player_money     #반환
    elif (pl_num1==com_num1 and pl_shape1==com_shape1):     #1 카드만 같을 때
        player_money= player_money-bet_money+bet_money*5     #5베 배딩
        return player_money     #반환
    elif(pl_num2==com_num2 and pl_shape2==com_shape2):     #1 카드만 같을 때
        player_money= player_money-bet_money+bet_money*5     #5배 배당
        return player_money     #반환
    elif(pl_num1==com_num2 and pl_shape1==com_shape2):     #1 카드만 같을 때
        player_money= player_money-bet_money+bet_money*5     #5배 배당
        return player_money     #반환
    elif(pl_num2==com_num1 and pl_shape2==com_shape1):     #1 카드만 같을 때
        player_money= player_money-bet_money+bet_money*5     #5배 배당
        return player_money     #반환
    elif (pl_num1==com_num1 or pl_num2==com_num2 or pl_num1==com_num2 or pl_num2==com_num1):     #1 숫자만 같을 때
        player_money= player_money-bet_money+bet_money*3     #3배 배당
        return player_money     #반환
    else:     #그외
        player_money= player_money-bet_money     #배당금 없음
        return player_money     #반환
        

def result():     #결과 함수
    global csm, yhm, zgm     #전역변수 불러오기
    if (csm>=yhm and csm>=zgm and yhm>=zgm):     #철수, 영희 짱구 순서일 때
        print("순위   이름   소지금 \n================\n 1    철수   ",csm,"\n 2    영희   ",yhm,"\n 3    짱구   ",zgm)
    elif (csm>=yhm and csm>=zgm and zgm>=yhm):     #철수, 짱구, 영희 순서일 때
        print("순위   이름   소지금 \n================\n 1    철수   ",csm,"\n 2    짱구   ",zgm,"\n 3    영희   ",yhm)
    elif (yhm>=csm and yhm>=zgm and csm>=zgm):     #영희, 철수, 짱구 순서일 때
        print("순위   이름   소지금 \n================\n 1    영희   ",yhm,"\n 2    철수   ",csm,"\n 3    짱구   ",zgm)
    elif (yhm>=csm and yhm>=zgm and zgm>=csm):     #영희, 짱구, 철수 순서일 때
        print("순위   이름   소지금 \n================\n 1    영희   ",yhm,"\n 2    짱구   ",zgm,"\n 3    철수   ",csm)
    elif (zgm>=csm and zgm>=yhm and csm>=yhm):     #짱구, 철수, 영희 순서일 때
        print("순위   이름   소지금 \n================\n 1    짱구   ",zgm,"\n 2    철수   ",csm,"\n 3    영희   ",yhm)
    else:     #그외
        print("순위   이름   소지금 \n================\n 1    짱구   ",zgm,"\n 2    영희   ",yhm,"\n 3    철수   ",csm)
    
    

for n in [1, 2, 3, 4, 5]:     #5번 반복
    print("\n============================\n\n")     #보기좋게 삽입
    print("<", n, "라운드> \n")     #라운드 번호
    while True:
        com_shape1=random.choice(sh)     #컴퓨터 모양1 고르기
        com_num1=random.choice(num)     #컴퓨터 숫자1 고르기
        com_shape2=random.choice(sh)     #컴퓨터 모양2 고르기
        com_num2=random.choice(num)     #컴퓨터 숫자2 고르기
        if (com_shape1==com_shape2 and com_num1==com_num2):     #컴퓨터의 두가지 숫자가 같을 때
            continue     #계속
        else:     #그외
            break     #탈출
    player_turn()     #참가자 순서 함수 불러오기
    print("=== 카드오픈 : ", com_num1,com_shape1, com_num2,com_shape2, "===\n")     #컴퓨터 카드 오픈
    result()     #결과 함수
