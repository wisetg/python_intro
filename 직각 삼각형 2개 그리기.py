def calculate_left (m):
        for i in range(1,m+1):
                result = print('*'*i)
        return result

def calculate_right (m):
        for i in range(1,m+1):
                result = print(' '*(m-i),'*'*i)
        return result

n=int(input('삼각형의 크기를 입력하시오: '))
left=calculate_left(n)
right=calculate_right(n)
