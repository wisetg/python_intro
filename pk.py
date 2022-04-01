import random
hom=0
awa=0

while True:
    options=["좌","중","우"]
    user_choice = input("\n어디를 수비하시겠어요?(좌, 중, 우) : ")
    computer_choice = random.choice(options)
    if computer_choice == user_choice:
        print("수비에 성공하셨습니다. 당신:", hom, "cpt:", awa)
    else:
        awa=awa+1
        print("페널티 킥이 성공하였습니다. 당신:", hom, "cpt:", awa)
    
    user_choice = input("어디를 공격하시겠어요?(좌, 중, 우) : ")
    computer_choice = random.choice(options)
    if computer_choice != user_choice:
        hom=hom+1
        print("공격에 성공하셨습니다. 당신:", hom, "cpt:", awa)
    else:
        print("공격에 실패하였습니다. 당신:", hom, "cpt:", awa)
    if hom>=5 and hom>awa:
        print("\n\n당신이 이겼습니다!!!")
        break
    if awa>=5 and awa>hom:
        print("\n\n당신은 젔습니다. 더 연습하세요!!!")
        break
