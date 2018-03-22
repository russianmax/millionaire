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
print questions
