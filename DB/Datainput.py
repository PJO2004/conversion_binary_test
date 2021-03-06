from .db.database import Session, engine, Base, List, iList
from .db import models

Base.metadata.create_all(engine)


class MAIN_Start:

    def __init__(self):
        self.memory = ""
        self.db = Session()
        try:
            self.CreateUser(user="admin", pwd="admin123")
        except:
            pass

        print(List)
        print(iList)

    def CreateUser(self, ID=0, user="", pwd=""):
        new_user = models.user_DB(id=ID, gameuser=user, pwd=pwd)
        self.db.add(new_user)

        try:
            self.db.commit()
        except:
            self.db.rollback()
            raise
        finally:
            self.db.close()

    def InputLOG(self, Step="", User="", time=""):
        try:
            Index = iList + 1
        except TypeError:
            Index = 0
        new_LOG = models.LOG(index=Index, User=User, Step=Step, time=time)
        self.db.add(new_LOG)
        self.db.commit()
        self.db.refresh(new_LOG)

    # 회원 가입
    def SignUPAnswer(self):
        UserAnswer = input("Do you Want to Sign Up?\n>>")
        if UserAnswer == "YES" or UserAnswer == "Y":
            return "Y"
        elif UserAnswer == "NO" or UserAnswer == "N":
            return "N"
        else:
            print("Please answer is YES/Y OR NO/N\n")
            return self.SignUPAnswer()

    def SignUp(self):
        UserName = input("PLEASE WRITE YOUR USERNAME : ")
        if UserName == List[0][0]:
            print("[경고] 'admin' 은 만들 수 없습니다.")
            return self.SignUp()
        else:
            password = input("PLEASE WRITE YOUR PASSWORD : ")
            self.CreateUser(ID=List[-1][0]+1, user=UserName, pwd=password)
            return

    # 회원 탈퇴
    def withdrawal(self):
        UserName = input("PLEASE WRITE YOUR WANT DELETE DELETE USERNAME\n>>")

        if UserName == "admin":
            print("[경고] 'admin' 은 지울 수 없습니다.")
            print("END THE PROGRAM")

        else:

            conn = engine.connect()
            for user in List:
                if user[1] == UserName:
                    select_query = f"delete from user_db where gameuser = '{UserName}'"
                    conn.execute(select_query)

            print("DELETE SUCCESS")

