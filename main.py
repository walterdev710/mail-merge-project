#for each name in invited_names.txt

with open("./input/names/invited_names.txt", mode="r") as names:
    name_list = names.readlines() #it returns list
    
with open("./input/letters/starting_letter.txt") as letter:
    example_letter = letter.read()
    for name in name_list:
        stripped_names = name.strip("\n")
        ready_letter = example_letter.replace("[name]", stripped_names)
        with open(f"./output/readyToSend/letter_for_{stripped_names}.docx", mode="w") as completed_letters:
            completed_letters.write(ready_letter)

    
# for name in range(len(name_list)):
#     stripped_names = name_list[name].strip("\n")
#     replaced_names = example_letter.replace("[name]", stripped_names )
#     with open(f"./output/readyToSend/mail_for_{stripped_names}.docx", mode="w") as ready_letters:
#         ready_letters.write(replaced_names)