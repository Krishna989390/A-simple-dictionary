# This is a dictionary

loops = ''

while loops != 'yes':
    print("Dictionary made by krishna.")
    d1 = {"fear": "Fear is a natural, powerful, and primitive human emotion",
          "disease": "Disease, any harmful deviation from the normal structural or functional state of an organism",
          "coding": "The definition of coding is the process of creating instructions for computers using programming "
                    "languages",
          "Harry Bhai": "A amazing preson giving free tutorials of coding for free \"respect\"",
          "learn": "to get knowledge, a skill"}


    hello = input("Type a word to find meaning\n")
    try:
        print(hello + " : Meaning: " + d1[hello])
    except:
        print("That word was not found on dictionary")
    loops = input("Do you want to quit, if then type yes")









