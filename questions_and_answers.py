# Think we should create a dictionary where we read in   #
# the questions from the file and tie the correct answer to them  #
import sys
import random

trivia = {}

with open("test_questions", "r") as f:
   for line in f:
      tokens = line.split("/")
      trivia[tokens[0]] = tokens[1].rstrip()
   
   #print trivia
   question = random.choice(list(trivia.items()))
   answer = question[1]
   question = question[0]
   
   print question, answer