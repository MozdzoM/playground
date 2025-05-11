import turtle
import pandas

from writer import Writer


writer = Writer()
screen = turtle.Screen()
screen.title("US States Game")
image = "./blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

df = pandas.read_csv("./50_states.csv")
all_states = df.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/{len(all_states)} States Correct",
                                    prompt="What's another state's name?").title()

    if answer_state == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("./missing_states.csv")
        break
    elif answer_state in all_states and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        state_info = df[df.state == answer_state]
        writer.write_state(answer_state, state_info.x.item(), state_info.y.item())

screen.exitonclick()
