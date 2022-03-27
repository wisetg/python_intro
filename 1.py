imoney1000=int(input("투입한 1000원 : "))
imoney500=int(input("투입한 500원 : "))
imoney100=int(input("투입한 100원 : "))
imoney=imoney1000*1000+imoney500*500+imoney100*100
print("투입한 금액 : ",imoney)
money500=int(input("구입할 500원 상품 갯수 : "))
money300=int(input("구입할 300원 상품 갯수 : "))
money=money500*500+money300*300
print("총가격 : ",money)
rmoney=imoney-money
print("거스름돈 : ",rmoney)
rmoney1000=rmoney//1000
rmoney1=rmoney-rmoney1000*1000
print("반환 할 1000원의 개수 : ",rmoney1000)
rmoney500=rmoney1//500
rmoney2=rmoney1-rmoney500*500
print("반환 할 500원의 개수 : ",rmoney500)
rmoney100=rmoney2//100
print("반환 할 100원의 개수 : ",rmoney100)

