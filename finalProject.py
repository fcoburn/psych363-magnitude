# Import required libraries
from psychopy import visual,core, clock, event
import random as rd
import csv
import os

# Setup the window
win = visual.Window(size = [1000, 1000], color = 'grey', fullscr = True)


# Create an empty array to store results
results = []

# Asking for participant's ID
id_prompt = visual.TextStim(win,
                                     text = "Enter ID: ",
                                     pos = [0, 0])
id_prompt.size = 0.05
id_input = visual.TextBox2(win,
                                         text = "",
                                         size = 1,
                                         pos = [0.6, 0])
# Getting input
while True:
    id_prompt.draw()
    id_input.draw()
    win.flip()
    
    keys = event.getKeys()
    if 'return' in keys:
        break
    elif 'backspace' in keys:
        id_input.text = id_input.text[:-1]
    elif len(keys) > 0 and keys[0] != 'escape':
        id_input.text += keys[0]
PID = id_input.text

# Getting participant's gender
genderChoice = visual.RatingScale(
    win, choices=['Male', 'Female','Non-binary'],
    markerStart=0.5, singleClick=True)
while genderChoice.noResponse:
    genderChoice.draw()
    win.flip()
PG = genderChoice.getRating()

# Display prompt for looking at fixation spot
prompt = visual.TextStim(win,
                         text = "By continuing in this study, you acknowledge you are giving your consent to participating and allowing the researchers to use your data.\nAn ethics review has taken place, and it has been determined there is a low risk of any harm or adverse reactions to the contents of this experiment.\nIn the event that you no longer wish to participate you can decline at any point without any consequences.\nPlease press 'N' to continue!")
prompt.draw()
win.flip()  
event.waitKeys(keyList = ['n'])
prompt.text = "A line with its length specified will appear shortly after the introduction.\nPress 'N' to continue!"
prompt.draw()
win.flip()  
event.waitKeys(keyList = ['n'])
prompt.text = "Lines with different length will appear after the first line appears.\nPress 'N' to continue!"
prompt.draw()
win.flip()
event.waitKeys(keyList = ['n'])
prompt.text = "Your task is to estimate the length of the lines based on the first line's length!\nPress 'N' to continue!"
prompt.draw()
win.flip()
event.waitKeys(keyList = ['n'])


# Create and display the first line
first_line = visual.Line(win,
                         start = [-0.5, 0],
                         end = [0.5, 0],
                         lineWidth = 10)
first_line_length = visual.TextStim(win,
                                    text = "Length: 100",
                                    pos = [0, -0.25])
first_line_length.size = 0.05
first_line.draw()
first_line_length.draw()
win.flip()
core.wait(5)

# Create and display the second line and ask for estimation
second_true_length = 50
second_line = visual.Line(win,
                          start = [-0.5, 0],
                          end = [0, 0],
                          lineWidth = 10)
second_line_prompt = visual.TextStim(win,
                                     text = "Length: ",
                                     pos = [0, -0.25])
second_line_prompt.size = 0.05
second_line_estimation = visual.TextBox2(win,
                                         text = "",
                                         size = 1,
                                         pos = [0.56, -0.25])
# Getting input
while True:
    second_line.draw()
    second_line_prompt.draw()
    second_line_estimation.draw()
    win.flip()
    
    keys = event.getKeys()
    if 'return' in keys:
        break
    elif 'backspace' in keys:
        second_line_estimation.text = second_line_estimation.text[:-1]
    elif len(keys) > 0 and keys[0] != 'escape':
        second_line_estimation.text += keys[0]

# Log the estimation
results.append([PID, PG, second_true_length, second_line_estimation.text])
 

# Create and display the third line and ask for estimation
third_true_length = 120
third_line = visual.Line(win,
                          start = [-0.5, 0],
                          end = [0.7, 0],
                          lineWidth = 10)
third_line_prompt = visual.TextStim(win,
                                     text = "Length: ",
                                     pos = [0, -0.25])
third_line_prompt.size = 0.05
third_line_estimation = visual.TextBox2(win,
                                         text = "",
                                         size = 1,
                                         pos = [0.56, -0.25])
# Getting input
while True:
    third_line.draw()
    third_line_prompt.draw()
    third_line_estimation.draw()
    win.flip()
    
    keys = event.getKeys()
    if 'return' in keys:
        break
    elif 'backspace' in keys:
        third_line_estimation.text = third_line_estimation.text[:-1]
    elif len(keys) > 0 and keys[0] != 'escape':
        third_line_estimation.text += keys[0]
# Log the estimation
results.append([PID, PG, third_true_length, third_line_estimation.text])

# Create and display the fourth line and ask for estimation
fourth_true_length = 10
fourth_line = visual.Line(win,
                          start = [0, 0],
                          end = [0.1, 0],
                          lineWidth = 10)
fourth_line_prompt = visual.TextStim(win,
                                     text = "Length: ",
                                     pos = [0, -0.25])
fourth_line_prompt.size = 0.05
fourth_line_estimation = visual.TextBox2(win,
                                         text = "",
                                         size = 1,
                                         pos = [0.56, -0.25])
# Getting input
while True:
    fourth_line.draw()
    fourth_line_prompt.draw()
    fourth_line_estimation.draw()
    win.flip()
    
    keys = event.getKeys()
    if 'return' in keys:
        break
    elif 'backspace' in keys:
        fourth_line_estimation.text = fourth_line_estimation.text[:-1]
    elif len(keys) > 0 and keys[0] != 'escape':
        fourth_line_estimation.text += keys[0]
# Log the estimation
results.append([PID, PG, fourth_true_length, fourth_line_estimation.text])
 
 
# Create and display the fifth line and ask for estimation
fifth_true_length = 100
fifth_line = visual.Line(win,
                          start = [-0.3, 0],
                          end = [0.7, 0],
                          lineWidth = 10)
fifth_line_prompt = visual.TextStim(win,
                                     text = "Length: ",
                                     pos = [0, -0.25])
fifth_line_prompt.size = 0.05
fifth_line_estimation = visual.TextBox2(win,
                                         text = "",
                                         size = 1,
                                         pos = [0.56, -0.25])
# Getting input
while True:
    fifth_line.draw()
    fifth_line_prompt.draw()
    fifth_line_estimation.draw()
    win.flip()
    
    keys = event.getKeys()
    if 'return' in keys:
        break
    elif 'backspace' in keys:
        fifth_line_estimation.text = fifth_line_estimation.text[:-1]
    elif len(keys) > 0 and keys[0] != 'escape':
        fifth_line_estimation.text += keys[0]
# Log the estimation
results.append([PID, PG, fifth_true_length, fifth_line_estimation.text])
 

# Get the directory and write results to a csv file
script_dir = os.path.dirname(os.path.abspath(__file__))
output_file_path = os.path.join(script_dir, str(PID)+"results.csv")
with open(output_file_path, 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(['PID','Gender','Length','Estimations'])
    for result in results:
        writer.writerow(result)
