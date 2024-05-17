Questions = [
    ["What is the largest animal in the world ? ","Blue Whale","Tiger","Elephant","Lion","1"],
    ["Which planet is suitable for human ? ","Jupyter","Mars","Earth","Saturn","3"],
    ["How many days in a year ?","609","365","200","None","2"],
    ["Which team wins FIFA World Cup in 2022 ? ", "Germany","Netherland","Brazil","Argentina","4"],
    ["Which language is suitable for Machine Learning ?","Python","Ruby","Swift","Php","1"]
]
print("Welcome to the KBC Game\n")
levels = [1000,2000,3000,5000,10000,20000,40000,80000]
Earning = 0
for i in range(len(Questions)):
    print(f'Question for Tk.{levels[i]}\n')
    print(f'Question : {Questions[i][0]}\n')
    print(f'a.{Questions[i][1]}  b.{Questions[i][2]}')
    print(f'c.{Questions[i][3]}  d.{Questions[i][4]}\n')
    reply = input("Choose your answer from (1-4) : ")
    print("Should we lock your answer ?")
    user = input("Enter yes or no : ")
    if user == "yes":
      if reply == Questions[i][-1]:
        print(f'Congratulations! You have won Tk.{levels[i]}\n')
        Earning = Earning + levels[i]
        print(f'Your current balance is Tk.{Earning}')
      else:
        print("Sorry,Your answer is incorrect.\n")
        break
    elif user == "no":
        reply = input("Choose your answer from (1-4) : ")
        if reply == Questions[i][-1]:
          print(f'Congratulations! You have won Tk.{levels[i]}\n')
          Earning = Earning + levels[i]
          print(f'Your current balance is Tk.{Earning}\n')
        else:
          print("Sorry,Your answer is incorrect.\n")
          break

print(f'You have earned Tk.{Earning}')
