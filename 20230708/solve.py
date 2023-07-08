# We know that 1 + 4 = 5 and in this puzzle, it's the only line that is mathematically correct.
# Let's declare the variables for that
line1_solution = 5
line2_solution = 12
line3_solution = 21

def solve_line(a,b):
    return (a * b) + a

print("Below are the three lines that are given in the challenge. For each line there's a piece of code. Below this, I'll try to put it all in a loop.")
print("")
print("--------------------------------------------------------------------------------")
print("")

a = 1
b = 4
outcome = solve_line(a,b)
print("Line 1 is: " + str(a) + " + " + str(b) + " = " + str(outcome))


a = 2
b = 5
outcome = solve_line(a,b)
print("Line 2 is: " + str(a) + " + " + str(b) + " = " + str(outcome))

a = 3
b = 6
outcome = solve_line(a,b)

print("Line 3 is: " + str(a) + " + " + str(b) + " = " + str(outcome))
print("")
print("--------------------------------------------------------------------------------")
print("")
print("The first integer (left of the + sign) correspnds with the line number.")
print("We'll call that variable 'line_no' from now on")
print("The second number will be called 'second_no' from this point on.")
print("We know that the second number increases by 1 for every line.")
print("If we put that in a loop, we should be able to print all lines with the corresponding solutions.")
print("")
print("--------------------------------------------------------------------------------")
print("")
line_no = 1
second_no = 4
goal_no = 11

for x in range(line_no, goal_no):
    # print("The value of variable 'line_no' = " + str(line_no) + " and the value of variable 'second_no' is " + str(second_no) + ".")
    result = solve_line(line_no,second_no)
    print(str(line_no) + " + " + str(second_no) + " = " + str(result))
    line_no += 1
    second_no += 1

