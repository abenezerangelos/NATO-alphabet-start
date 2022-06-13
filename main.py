student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    if row.student== "Angela":
        print(row.score)


# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}


{"A": "Alfa", "B": "Bravo"}
Nato=pandas.read_csv("nato_phonetic_alphabet.csv")
df = pandas.DataFrame(Nato)
Nato_dict={v[df.columns[0]]:v[df.columns[1]] for k,v in df.iterrows()}
print(Nato_dict)







name=input("What is your name?").upper()
output=[Nato_dict[letter] for letter in name]
print(output)
