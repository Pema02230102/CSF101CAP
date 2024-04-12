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
#Total Score: 49801
#################################################################################################################################

def read_input(f_path):
#Here I defined a function named read_input_file that takes a single argument "f_path", which is the path to the input file.
    
    game_rounds = [] 
    #To store the data reads from input file, game_rounds" initializes an empty list. 

    with open(f_path, 'r') as file:
    #This opens the file specified by f_path in read mode "r" and
    #at the sametime it ensures that the file is properly closed after its suit finishes.

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
#Defines a function named calculate_score that takes a single argument game_rounds, which is a list of tuples containing 
#sign and condition data, in order to calculate the total score based on the game_rounds played. 
    scoring_rule = {
    ("A", "X"): 3,
    ("A", "Y"): 4,          #
    ("A", "Z"): 8,
    ("B", "X"): 1,
    ("B", "Y"): 5,
    ("B", "Z"): 9,
    ("C", "X"): 2,
    ("C", "Y"): 6,
    ("C", "Z"): 7
    }
    # The dictionary above maps the score for the different combination.
    score = 0
    #Initializes a variable score to keep track of the total score

     
    for sign, condition in game_rounds:
        # Calculate total score for all rounds using for loop to iterate
        sign_score = scoring_rule.get((sign, condition), 0)
        # Get the score for the current combination from the mapping
        score += sign_score      
        # Add the score to the total up.
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
