import pandas
from turtle import Screen,Turtle
import time

import pandas
screen=Screen()
turtle=Turtle()
screen.title("us States Game")
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

time.sleep(0.1)
completed_states=[]
remaining_states=[]
game_on=True
score=0
count=0
while game_on:
    count+=1
    answer_state=screen.textinput(title=f"Guess the State Score={score}/{count}",prompt="what is ur another state")

    guess=answer_state.title()
    data=pandas.read_csv("/home/kambalapallysirivennela/PycharmProjects/Us States Game/50_states.csv")
    all_states=data["state"].to_list()


    if  guess in all_states:
        completed_states.append(guess)
        score+=1
        row = data[data["state"] == guess]
        x = row.x.item()
        y = row.y.item()
        turtle.hideturtle()
        turtle.penup()
        turtle.goto(x,y)
        turtle.write(f"{guess}",align="center",font=("arial",10,"normal"))
    #print(completed_states)
    if answer_state == "exit":
            #game_on = False
            remaining_states=[state  for state in all_states if state not in completed_states]

            print(remaining_states)
            game_on = False
            data=pandas.DataFrame(remaining_states)
            data.to_csv("learn.csv")
    print(f"Score:{score}/{count}")
screen.mainloop()
'''student_dict={
    "name":["alex","siri","lara"],
    "score":[34,48,59]
}
student_data=pandas.DataFrame(student_dict)
print(student_data)
#for (key,value) in student_data.items() :
    #print(key,value)
for (index,row) in student_data.iterrows():
    print(row['name'])'''




