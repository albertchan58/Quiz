import round1, round2, round3, random, math, rules

def main():
    print("Welcome to the FUN MATH QUIZ!\n")
    print("There will be 3 rounds in total and 5 questions in each round:")
    print("Round 1:\tMultiply & Divide")
    print("Round 2:\tSolving Quadratic Equations")
    print("Round 3:\tSolving Right Triangles\n")
    rules.rules()
    print("ARE YOU READY TO START??(Enter anything to start the game)")
    input()
    score = 0
    questions = 0
    print("ROUND 1 BEGIN")
    for i in range(5):
        print("ROUND 1 QUESTION "+str(i+1)+"\n")
        if (round1.r1(score, questions)):
            score += 1
        questions += 1
    print("ROUND 2 BEGIN")
    for i in range(5):
        print("ROUND 2 QUESTION "+str(i+1)+"\n")
        if (round2.r2(score, questions)):
            score += 1
        questions += 1
    print("ROUND 3 BEGIN")
    for i in range(5):
        print("ROUND 3 QUESTION "+str(i+1)+"\n")
        if (round3.r3(score, questions)):
            score += 1
        questions += 1
    
main()
