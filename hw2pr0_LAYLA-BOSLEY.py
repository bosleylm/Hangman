from random import *

MaxTries = 7
SecretWords=["banana","clover","crayon","flower","mother","pencil","string","summer","winter","animal","doctor","family","father","kitten","mother","parent","rabbit","sister","summer","winter","bushes","butter","cherry","cobweb","dinner","eggnog","flavor","number","stream","street","throne","wrench","advice","answer","basket","battle","beetle","beggar","branch","bubble","bucket","cactus","cannon","cattle","celery","cellar","donkey","finger","icicle","income","island","marble","poison","riddle","thrill","throat","throne","turkey","voyage","action","border","circle","faucet","galley","guitar","health","kitten","lawyer","locket","lumber","mitten","pickle","pocket","police","recess","reward","temper","thread","wealth","writer","morning","balloon","bedroom","brother","chicken","airport","cracker","fireman","haircut","hobbies","holiday","ladybug","mailbox","oatmeal","pancake","popcorn","giraffe","hydrant","lettuce","station","visitor","achieve","apparel","believe","cabbage","caption","channel","creator","feather","laborer","partner","picture","plastic","railway","sweater","texture","volcano","weather","children","downtown","notebook","airplane","baseball","birthday","cherries","goldfish","daughter","governor","seashore","sidewalk","vacation","activity","beginner","boundary","calendar","cemetery","creature","friction","language","minister","mountain","pleasure","squirrel","stranger","lunchroom","jellyfish","quicksand","rainstorm","scarecrow","furniture","underwear","vegetable","acoustics","aftermath","afternoon","appliance","breakfast","carpenter","education","passenger","pollution","territory","treatment","toothpaste","volleyball","arithmetic","basketball","earthquake","playground","toothbrush","calculator","plantation","wilderness","grandfather","grandmother","afterthought"]

def hangmanOnce(secret="", display="", badGuesses=0):
    if secret=="" and badGuesses==0:
        secret= choice(SecretWords)
        display = '-' * len(secret)
        
    if secret == display:
        print ("You win!")
        print ("Secret word is: " + secret)
    else:       
        if badGuesses==MaxTries:
            print ("You loose")
            print ("Secret word is: " + secret)
        else:
            print ("Secret word: " + display)
            letter = input("Guess a letter: ")
            # Complete this function such that
            # it checks the input letter in the word secret and if found change
            # the word display using the recursive function change()
            # if not found, the function must increase the number of badGuesses
            # the function must then display the hangman once.

           
def hangman(secret="", display="", badGuesses=0):
    if secret=="" and badGuesses==0: # Why 
        secret= choice(SecretWords)
        display = '-' * len(secret)
        
    if secret == display:
        print ("You win!")
        print ("Secret word is: " + secret)
    else:       
        if badGuesses==MaxTries:
            print ("You loose")
            print ("Secret word is: " + secret)
        else:        
            print ("Secret word: " + display)
            letter = input("Guess a letter: ")
            # Complete this function such that
            # it does exactly like the hangmanOnce and then it continues to find more letters by
            # calling it recurively after displaying the hangman.


def changeOne(secret, display, letter, start):
    '''
      This function takes input as follows
      secret: a string word, e.g., "hello"
      display: a string word of hyphans with the same length as secret e.g., "-----" if secret is "hello"
      letter: any letter: e.g., 'i' or 'k'
      start: integer index when the search in secret should should start at.

      The function searches for the first position of ^letter in the string ^secret and then update the string ^display
      based on this position by replacing the corresponding hyphan with the ^letter.
      Examples
      >>> changeOne("Hello","-----",'o', 0)
      '----o'
      >>> changeOne("Hello","-----",'l', 0)
      '--l--'
      >>> changeOne("Hello","-----",'l', 2)
      '--l--'
      >>> changeOne("Hello","-----",'l', 3)
      '---l-'
      
    '''
    #hint
    #You need an if statement to check if the letter is in the secret part after the start
    #if found then replace the letter in the string display in the same position
    #this can be done by cutting display into two parts: before and after the position and
    #reattach them again with the letter in the middle.

         
    
    return display

def change(secret, display, letter, start):
    '''
      This function takes input as follows
      secret: a string word, e.g., "hello"
      display: a string word of hyphans with the same length as secret e.g., "-----" if secret is "hello"
      letter: any letter: e.g., 'i' or 'k'
      start: integer index when the search in secret should should start at.

      The function searches for the position(s) of ^letter in the string ^secret and then update the string ^display
      based on these positions by replacing the hyphans with the ^letter.

      Examples
      >>> change("Hello","-----",'o', 0)
      '----o'
      >>> change("Hello","-----",'l', 0)
      '--ll-'
    '''
    #hint
    #this is similar to the changeOne() function except that it hape one extra recursive step to complete the search over the whole string secret

    
    return display
         
    
def displayMan(badGuesses):
      if badGuesses == 0:
          print('''
          ----|
          |
          |
          |
          -------''')
      elif badGuesses == 1:
          print('''
          ----|
          |   o
          |
          |
          -------''')
      elif badGuesses == 2:
          print('''
          ----|
          |   o
          |   O   
          |   
          |   
          -------''')  
      elif badGuesses == 3:
          print('''
          ----|
          |   o
          |   O   
          |   O
          |   
          -------''')  
      elif badGuesses == 4:
          print('''
          ----|
          |   o
          |   O   
          |   O
          |  / 
          -------''')  
      elif badGuesses == 5:
          print('''
          ----|
          |   o
          |   O   
          |   O
          |  / \\
          -------''')  
      elif badGuesses == 6:
          print('''
          ----|         
          |   o
          |  \\O   
          |   O
          |  / \\
          -------''')  

      elif badGuesses == 7:
          print('''
          ----|            Hanged!!
          |   o
          |  \\O/   
          |   O
          |  / \\
          -------''')  
      else:
          print('badGuesses is less than 7')



