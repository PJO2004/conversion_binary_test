import os.path


class MAIN_Start:
    def __init__(self):
        self.memory = ""
        if not os.path.exists("./DB/USER_DB"):
            with open("./DB/USER_DB", "w") as Userdata:
                Userdata.write(f"admin:admin123,\n")
                Userdata.close()

    def SignUPAnswer(self):
        UserAnswer = input("Do you Want to Sign Up?\n>>")
        if UserAnswer == "YES" or UserAnswer == "Y":
            return "Y"
        elif UserAnswer == "NO" or UserAnswer == "N":
            pass
        else:
            print("Please answer is YES/Y OR NO/N\n")
            self.SignUPAnswer()

    def SignUp(self):
        UserName = input("PLEASE WRITE YOUR USERNAME\n>>")
        password = input("PLEASE WRITE YOUR PASSWORD\n>>")

        with open("./DB/USER_DB", "a") as Userdata:
            Userdata.write(f"{UserName}:{password},\n")
            Userdata.close()

    def withdrawal(self):
        UserName = input("PLEASE WRITE YOUR WANT DELETE DELETE USERNAME\n>>")

        if UserName == "admin":
            print("[경고] 'admin' 은 지울 수 없습 니다.")
            print("END THE PROGRAM")

        else:
            with open("./DB/USER_DB", "r") as Userdata:
                for data in Userdata:
                    Name = data.split(":")[0]
                    Password = data.split(":")[:2]

                    if Name == UserName:
                        pass
                    else:
                        self.memory += f"{Name}:{Password},\n"
                Userdata.close()

            self.reloading()

    def reloading(self):
        with open("./DB/USER_DB", "w") as Userdata:
            Userdata.write(self.memory)
            Userdata.close()

        print("DELETE SUCCESS")