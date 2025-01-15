import turtle
import pandas

def get_mouse_click_coor(x, y, text_str):
    print(x, y)
    text.penup()
    text.goto(x, y)
    text.pendown()
    text.write(text_str, align="center", font=("Arial", 12, "normal"))

screen = turtle.Screen()
screen.title("US States")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
text = turtle.Turtle()
text.hideturtle()

data = pandas.read_csv("50_states.csv")
answer_state = ""

while answer_state != "Exit":
    answer_state = screen.textinput(title="Guess a state", prompt="Guess a state on the map: ")
    for state in data.state:
        if state == answer_state:
            get_mouse_click_coor(int(data[data.state == answer_state].x), int(data[data.state == answer_state].y), state)

turtle.exitonclick()
