import turtle
t=turtle.Turtle()
t.shape("turtle")

while True:
    s=turtle.textinput("","도형을 입력하시오:")
    if s=="사각형":
        s=turtle.textinput("","가로:")
        w=int(s)
        s = turtle.textinput("","세로: ")
        h=int(s)
        t.forward(w)
        t.left(90)
        t.forward(h)
        t.left(90)
        t.forward(w)
        t.left(90)
        t.forward(h)
        break
    if s=="원":
        s=turtle.textinput("","반지름:")
        w=int(s)
        t.circle(w)
        break
    if s=="삼각형":
        s=turtle.textinput("","한변의 길이:")
        w=int(s)
        t.forward(w)
        t.left(120)
        t.forward(w)
        t.left(120)
        t.forward(w)
        break
    else:
        print("삼각형, 삼각형, 원중에 하나를 입력하시오.")
        continue
