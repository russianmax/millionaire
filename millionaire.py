# CA278 Group Project: Who Wants to Be a Millionaire
# Josh Malone: 15357971
# Maksims Kompanijecs: 15306971
# Michael Hubem: 15396501
# Matthew Farrelly: 15366246

def intro():
   name = raw_input("Hello, welcome to Who Wants to be a Millionaire! What is your name?" + "\n")
   print "Ok " + name + " this is how the game works:" + "\n"
   print "You are asked a multiple choice question, with options A, B, C and D. If you get the correct answer, you earn money and move onto the next question. If you guess incorrectly then you lose the money you have earned, although there are check-points along the way that allow you to keep a certain amount of money should you get a question wrong further on." + "\n" +"The questions increase in difficulty as you progress but you can make use of the 3 'lifelines' we will give you:" 
   print "1. 50/50" + "\n" + "This allows you to cut the possible answers from 4, down to 2."
   print "2. Phone a Friend" + "\n" + "Place a call to a predetermined friend that will hopefully help you with an answer."
   print "3. Ask the Audience" + "\n" "Our wonderful people (bots) in the audience will vote on the correct answer and we shall show you the results"
   print "Ready to get started? Lets go!" + "\n" + "==================================================================="


answerlist = ["A","B","C","D", "Correct"]
answerdict = {}
f = open("question.txt")
for lines in f.readlines():
    #print (lines)
    parse = lines.split('[')
    answer = parse[1]
    questions = parse[0]
    answers = parse[1].strip("\n").split(",")
    print(questions)
    #print(answer)
    i = 0
    while i < 5:
        answerdict[answerlist[i]] = answers[i]
        i = i + 1
    print("A: " + answerdict["A"])
    print("B: " + answerdict["B"])
    print("C: " + answerdict["C"])
    print("D: " + answerdict["D"])

    select = raw_input("Select your answer:\n")
    if select in answerdict:
        if answerdict[select] == answerdict["Correct"] and select != "Correct":
            print("Thats correct")
        else:
            print("Thats not correct")
	    break
	
    else:
        if select == answerdict["Correct"]:
            print("Thats correct")
        else:
            print ("Thats not correct") 
	    break
