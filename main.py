import turtle
import pandas
from drawstates import DrawStates

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
data = pandas.read_csv("50_states.csv")
draw_states = DrawStates()
game_is_on = True
n = 0
all_states = data.state.to_list()
guessed_states = []
output_list = []

# def get_mouse_click_coor(x, y):
#   print(x, y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()


while game_is_on:

    answer_state = screen.textinput(title=f"{n}/50 Guess the State",
                                    prompt="What's another state's name?").title()

    if answer_state in all_states:
        answer_member = data[data["state"] == answer_state]
        guessed_states.append(answer_state)
        print(answer_member)

        x_cor = int(answer_member.x.iloc[0])
        y_cor = int(answer_member.y.iloc[0])

        print(x_cor)
        print(y_cor)
        draw_states.write_location(answer_state, x_cor, y_cor)
        n += 1
    if answer_state == "Close":
        missing_state = [state for state in all_states if state not in guessed_states]
        # for state in all_states:
        #     if state not in guessed_states:
        #         missing_state.append(state)
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("states_to_learn.csv")
        game_is_on = False
    elif n == 50:
        game_is_on = False
