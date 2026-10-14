states_in_india = ("Delhi", "Uttar pradesh", "Haryana", "Punjab", "Goa", "Gujrat")
print("Display some states in india is here : ", states_in_india)

temp = list(states_in_india)
temp.append("J&K")
temp.pop(2)
temp[1] = "Kerela"
states_in_india = tuple(temp)
print(states_in_india)
