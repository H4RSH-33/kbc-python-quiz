import time

def KaunBanegaCrorePati():
    try:
        questions = [
            ["What comes next in the sequence: 2, 4, 8, 16,?","18","32","20","24",2],

            ["What is the capital of Japan?","Tokyo","Seoul","Osaka","Kyoto",1],

            ["What does 'CPU' stand for in computing?","Central Power Unit","Central Processing Unit","Core Performance Unit","Computer Processing Unit",2],

            ["Who wrote the Indian national anthem?","Swami Vivekananda","Subhash Chandra Bose","Rabindranath Tagore","Bankim Chandra",3],

            ["HTML is used to:","Style websites","Secure websites","Link to servers","Structure content on the web",4],

            ["Which number logically fits? If 1 → 2, 2 → 4, 3 → 6, then 5 → ?","20","8","25","10",4],

            ["What is the extension for Python files?","(.cpp)","(.exe)","(.java)","(.py)",4],
            
            ["Which is the longest river in the world?","Amazon","Yangtze","Ganga","Nile",4],

            ["Who is the founder of Linux?","Linus Torvalds","Steve Wozniak","Dennis Ritchie","Richard Stallman",1],

            ["Which company created the React.js library?","Facebook","Amazon","Microsoft","Google",1],

            ["In databases, SQL is used for:","Designing servers","Querying and managing data","Encrypting data","Drawing UI",2],

            ["What is the smallest prime number?","2","5","3","1",1],

            ["What does 'Git' help with in software development?","Compiling Code","Web Design","Version Control","Machine Learning",3],

            ["Who is considered the first computer programmer in history?","John von Neumann","Charles Babbage","Alan Turing","Ada Lovelace",4],

            ["What planet is known as the 'Morning Star'?","Mars","Venus","Mercury","Saturn",2],

            ["What does the company Nvidia primarily manufacture?","RAM chips","Graphics Processing Units (GPUs)","CPUs","Hard drives",2],

            ["What does 'Open Source' mean in software development?","Software is trial-based","The source code is publicly available for use and modification","Software is free","Software can’t be sold",2],

            ["Who coined the term 'Artificial Intelligence'?","Elon Musk","John McCarthy","Alan Turing","Marvin Minsky",2],

            ["What is the primary role of a compiler?","Create a UI","Run the program","Debug errors","Convert high-level code to machine code",4],

            ["What does 'HTTP' stand for in web development?","HyperText Transmission Process","HyperText Transfer Protocol","HighText Transfer Protocol","Hyper Tool Transfer Protocol",2],
        ]
        i=1
        sum = 0
        for question in questions:
            print(f"💰 Your question is: {question[0]}")
            time.sleep(0.5)
            print("\n")
            print(f"A.{question[1]}")
            time.sleep(0.5)
            print(f"B.{question[2]}")
            time.sleep(0.5)
            print(f"C.{question[3]}")
            time.sleep(0.5)
            print(f"D.{question[4]}")
            print("\n")
            print("🔢 Enter your answer:\n  ➤ Type 1 for option A\n  ➤ Type 2 for option B\n  ➤ Type 3 for option C\n  ➤ Type 4 for option D")
            ans = int(input("Your answer: _: "))
            
            if (ans == question[5]):
                time.sleep(1.5)
                print("======")
                print("Congratulations, that was indeed a Correct answer✅!")
                amount = 1000 + (i - 1) * 52631.578947

                sum += amount
                i+=1
                print(f"You've won Rs.{round(sum,2)} till now!")
                print("Moving on to the next question.")
                print("======================================================")
                time.sleep(3)
            else:
                time.sleep(1)
                print("======")
                print("❌ Oops! That was the wrong answer.")
                print("But hey, you played really well! 👏")
                print(f"You're still taking home ₹{round(sum, 2)} — congratulations! 🎉")
                print("Better luck next time!")
                break

        if sum > 10000000.0:
            print("Congratulations, you are a crorepati !!")

    except Exception as e:
        print("Only Enter the integers in between 1 to 4 !")
        print("Do you want to restart the game again?")
        re = input("Enter (yes/no):").lower()
        if re == "yes":
            print("\n")
            KaunBanegaCrorePati()
        else:
            print("Bye!")

print("🟨 Welcome to the Kaun Banega Crorepati!! 🟨")
ask = input("🎮 Do you want to start the game? (yes/no):").lower()
print("🟢 Great! Let's begin...")
time.sleep(1)
if ask == "yes":
    KaunBanegaCrorePati()