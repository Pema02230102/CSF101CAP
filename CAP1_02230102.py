#################################################################################################################################
#Pema Tshering
#1ECE
#02230102
#################################################################################################################################
#REFERENCES
#https://www.dataquest.io/blog/read-file-python/#:~:text=Python%20provides%20a%20built%2Din,we%20can%20manipulate%20its%20content
#https://www.mathplanet.com/education/programming/repeating-code/lists#!/exercise/exercises/
#https://chat.openai.com/c/c9055288-d0fb-4edf-854e-a8e1660cf648
#################################################################################################################################

#SOLUTION
#Total Score: 49903
#################################################################################################################################

def read_input(f_path):
#Here I defined a function named read_input_file that takes a single argument "f_path", which is the path to the input file.
    
    game_rounds = [] 
    #To store the data reads from input file, game_rounds" initializes an empty list. 

    with open(f_path, 'r') as file:
    #This opens the file specified by f_path in read mode "r" and
    #At the sametime it ensures that the file is properly closed after its suit finishes, even if an exception is raised during the execution.

        for line in file:
        # It iterates over each line in the opened file.
            
            sign, condition = line.strip().split()
            #This Splits each line into two parts based on whitespace,
            #Removes any leading/trailing whitespace using strip() and 
            #Assigns the two parts to variables sign and condition.

            game_rounds.append((sign, condition))
            #Appends a tuple (sign, condition) to the game_rounds list for each line in the file.
    
    return game_rounds #Returns the list of tuples containing the shape and outcome for each round.

def calculate_score(game_rounds):
#Defines a function named calculate_score that takes a single argument game_rounds, which is a list of tuples containing sign and condition data,
#in order to calculate the total score based on the game_rounds played. 

    
    
    
    score = 0
    #Initializes a variable score to keep track of the total score.

    for sign, condition in game_rounds:
    #Iterates over each tuple (shape, outcome) in the rounds list.

        if sign == "A":
            sign_score = 1
        elif sign == "B":
            sign_score = 2         
        elif sign == "C":
            sign_score = 3
                                   #Inside the loop, it assigns scores based on the sign and conditions values. 
                                   #The sign scores are assigned based on the sign letters A, B, and C, 
                                   #while condition scores are assigned based on the condition letters X, Y, and Z.
                                   #These scores are then added to the score variable.
        if condition == "X":
            condition_score = 0
        elif condition == "Y":
            condition_score = 3
        elif condition == "Z":
            condition_score = 6

        score += sign_score + condition_score

    return score #Returns the total score calculated based on the rounds played.



f_path = "input_2_cap1.txt" 
#It defines the f_path variable to point to the input file.

game_rounds = read_input(f_path) 
#Here it calls the read_input_file() function with the f_path argument to read the input data and
#store it in the game_rounds variable.

total_score = calculate_score(game_rounds) 
#Calls the calculate_score() function with the game_rounds data as input to calculate the total score.

print("Total Score:", total_score)
#Finally prints the total score calculated.
