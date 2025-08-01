successCount = 0
questionList = [("What is ...?", "mars"), ("Who ...?", "josh")]
for (question, solution) in questionList:
    userAnswer = input(question)
    if process(userAnswer) == solution:
        successCount += 1

print(f"Result: {successCount}/{len(questionList)}")