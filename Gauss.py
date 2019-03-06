# I swear those were necessary
positive_answers = ["yes", "y", "aye", "ofc", "yes pls", "yeah"]
negative_answers = ["no", "n", "no pls", "nah"]

# That's used to fill the initial system to be transformed and solved, returns the complete system
def ask_for_input():
    print("Enter the size of the system:")
    size = int(input())
    data = []
    for i in range(0, size):
        temp_array = []
        for j in range(0, size+1):
            print("Enter the value for the position:" + str(i) + "," + str(j))
            value = float(input())
            temp_array.append(value)
        data.append(temp_array)
    return data

# Creates a triangular system from the starter system, returns the triangular system as output
def gauss_cannon(system):
    system_lenght = len(system)

    for i in range(0, system_lenght):
        maximum_element = abs(system[i][i])
        maximum_row = i

        for k in range(i+1, system_lenght):
            if abs(system[k][i]) > maximum_element:
                maximum_element = abs(system[k][i])
                maximum_row = k

        for k in range(i, system_lenght+1):
            tmp = system[maximum_row][k]
            system[maximum_row][k] = system[i][k]
            system[i][k] = tmp

        try:
            for k in range(i+1, system_lenght):
                c = -system[k][i]/system[i][i]
                for j in range(i, system_lenght+1):
                    if i == j:
                        system[k][j] = 0
                    else:
                        system[k][j] += c * system[i][j]
        except Exception as e:
            pass

    if round(system[system_lenght-1][system_lenght-1], 5) == 0 and round(system[system_lenght-1][system_lenght], 5) != 0:
        print("\nThe triangular system is:")
        print(system)
        print("There's no solution for that system")
        return []

    if round(system[system_lenght-1][system_lenght-1], 5) == 0 and round(system[system_lenght-1][system_lenght], 5) == 0:
        print("\nThe triangular system is:")
        print(system)
        print("There's infinite solutions for that system")
        return []

    print("\nThe triangular system is:")
    print(system)
    return system

# Asks the user politely if it wants the system solved or not
def solver(system):
    print("\nDo you also want me to solve the triangular system?")
    answer = input()
    if answer.lower() in positive_answers:
    	solve_triangular_system(system)
    elif answer.lower() in negative_answers:
    	print("All right, have a nice day!")
    else:
    	print("Sorry, I didn't undertand. You can answer with Y/N")
    	solver(system)

# Solves the triangular sys, returning the results into a beautiful array
def solve_triangular_system(trianguar_system):
    solution = [0 for i in range(len(trianguar_system))]
    for i in range(len(trianguar_system)-1, -1, -1):
        solution[i] = trianguar_system[i][len(trianguar_system)]/trianguar_system[i][i]
        for k in range(i-1, -1, -1):
            trianguar_system[k][len(trianguar_system)] -= trianguar_system[k][i] * solution[i]
    print("The solution to the triangular system is:")
    print(solution)

# This is the "main"
system = ask_for_input()
triangular_system = gauss_cannon(system)
if (triangular_system != []):
    solver(triangular_system)

end = input()