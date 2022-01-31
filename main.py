from API.create import Create
from API.conversion import Conversion
from API.timer import Timer
from DB.Datainput import MAIN_Start
from DB.UserConnecting import MAIN_CONNECT


timer = Timer()
cre = Create()
con = Conversion()
db = MAIN_Start()


def DB(User="", pwd=""):
    userdata = MAIN_CONNECT(UserName=User, Password=pwd)
    return userdata


def RUN():
    try:
        Answer = int(input("단계를 1~5중 선택 하시오. [종료를 원할시 아무 키나 누르면 됩니다.] \n>>"))
        timer.CountDown()
        start = timer.__Start__()
        for i in range(10):
            Decimal_Data = cre.Create_Decimal(cre.Choose_Step(User_Answer=Answer), User_Answer=Answer)
            print(Decimal_Data)
            con.test(con.Decimal_To_Binary(Decimal_Data, User_Answer=Answer))
        end = timer.__End__()
        count = timer.Count(__Start__=start, __End__=end)
        print(f"종료\n모든 10진수를 변환 하였 습니다.\n총 걸린 시간 : {count}")

        RUN()

    except ValueError:
        print("Program 을 종료 합니다.")


if __name__ == '__main__':
    UserName = input("UserName : ")
    Password = input("Password : ")
    user = DB(User=UserName, pwd=Password)

    if user.State == "MAIN CONNECTING":
        RUN()
