import json

def act():
    y = open('promptmodule.json')
    data = json.load(y)
    act = []
    for i in data["gpt_prompt"]:
        act.append(i["act"])   
    y.close()
    return act

def prompt(val):
    y = open('promptmodule.json')
    data = json.load(y)
    for i in data["gpt_prompt"]:
        if val == i["act"]:
            match = i["full_prompt"]
            return match
        return "None"
    y.close()

def pick_option(options):
    user_input = ''
    input_message = "Pick an promt option:\n"
    for index, item in enumerate(options):
        input_message += f'{index+1}) {item}\n'
    input_message += 'Your choice: '
    while user_input not in map(str, range(1, len(options) + 1)):
        user_input = input(input_message)
    
    return options[int(user_input) - 1]


options = act()
prompt_act = pick_option(options)
user_task = input('Type the prompt to send to the OpenAI API: ')
file_name = input('Type the name of the file with extension: ')
final_prompt = prompt(prompt_act) + " " + user_task


