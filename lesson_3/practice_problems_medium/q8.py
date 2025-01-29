def rps(fist1, fist2):
    if fist1 == "rock":
        return "paper" if fist2 == "paper" else "rock"
    elif fist1 == "paper":
        return "scissors" if fist2 == "scissors" else "paper"
    else:
        return "rock" if fist2 == "rock" else "scissors"
    
# What does the following code output?

print(rps(rps(rps("rock", "paper"), rps("rock", "scissors")), "rock"))

# We have nested function calls. The return values of the functions are passed
# to the enclosing functions - function composition. 

# paper, rock
# paper, rock
# paper

# It will return 'paper'