import random #it is a library that makes it available to put in random stuff
def give_instructions(): #basically I put some stuff in this function so it is easier to call
    print('''\nwelcome to my game, wordle.
    you just gotta guess a word
    you have 5 attempts
    (C) means the letter is there and it is placed correctly
    (WP) means the letter is there but wrongly placed
    (NT) means the letter is not there
    good luck      ''')
words =["this", "five", "help", "salt", "coat"] #[] is a list which has strings seperated by a comma

magic_word = random.choice(words) #assign the hidden word with a random string in the list
        
def check_word(guess): #this is a function that checks 
        if magic_word == guess:
            print("congrats, you are awsome")
            return True #this means that the function is valid and if you put it in an if statement it'll be triggered as true
        else: 
            result = "" #a string that states which letters are correct and not and which are misplaced
            for i,j in zip(guess, magic_word): #this means that i is associated with guess and j is associated with magicword, and i is will go over the letters in guess and j for magicword, and zip will pair the alphabet of each together
                if i == j: #if the letter is the same in a certain position 
                    result = result + "(C)" #just add C where the letter is correct
                elif i in magic_word:
                    result = result + "(WP)"
                else:
                    result = result + "(NT)"
        
        print(result)
        return False 
def main():
    give_instructions() #calling the function  
    attempt = 5 #number of attemps the user has
    while (attempt>0): #repeat while the user still has attemps left
        guess = input("guess a four lettered word:") #assign guess as an nput from the user
        if check_word(guess): #if it is true then:
            break
        else: #if it is false then:
            attempt -=1 # same as attempt -1 
            print(f"attempts left = {attempt}" )
    else:
        print("game over buddy")

    
main()
