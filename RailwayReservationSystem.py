import os
import platform
import random
import mysql.connector
from time import sleep
#database connectivity

mydb=mysql.connector.connect(host="localhost", user="root",passwd="7250324730")
mycursor=mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS railway")
mycursor.execute("use railway")
mycursor.execute("CREATE TABLE IF NOT EXISTS railway_user(name varchar(50),passwd varchar(15),email varchar(50),mob varchar(10))")
mycursor.execute("CREATE TABLE IF NOT EXISTS tbooking( tno numeric(4), dfrom varchar(20), arrival varchar(20),mob numeric(10),name varchar(30),sex char(1),nationality varchar(10),age numeric(3),pnr numeric(7))")


def clr():
    print("\n"*19)
def page1():
    #	MAIN SCREEN OF THE SYSTEM
    print("")
    print("")
    print(
        "#######################################################################################################################################################################")

    print(
        "\n\n|*****************                                                      RAILWAY RESERVATION MANAGEMENT                    ****************|")
    print(".")
    print(".")
    print(
        "#######################################################################################################################################################################")

    print("  ")
    print(
        "\n|****************                           DESIGNED AND MAINTAINED BY:                  *****************|")
    print("\n|*****                                                                                     REWATI RAMAN PRASAD    - 17IT016(Information technology)    ****|")
    print(
        "\n|-------------------------------------------------------------------------------------------------------------------------------------------------------------------- |")
    print(
        "\n|	                                                                                                                                                     |")
    print(
        "\n|-------------------------------------------------------------------------------------------------------------------------------------------------------------------- |")
    print(" \n" * 2)

    print(
        "#######################################################################################################################################################################")
    a=input("press enter to continue")
    clr()
    page2()

def page2():
    print("\n ")
    print("#######################################################################################################################################################################")
    print("\n|----------------------------------------------------                 <<LOADING>>                     ---------------------------------------------|")

    print("**                                                                     WELCOME RAILWAY RESERVATION MANAGEMENT                                                        ***")
    if (mydb):
        print("##########\t\t\t\tDatabase successfully connected\t\t\t\t###########".center(70))

    else:
        print("###########\t\t\t\tDatabase not connected\t\t\t\t####################".center(70))
    print("  ")
    print("  ")
    print("  ")
    print("  ")
    print("##################################################################################################################################################################")
    print("\n "*17)
    b=input("press enter to continue")
    clr()
    page3()


def page3():
    while True:
        print("\n\n\n\n")
        print("######################################################################################################################################################################")

        print("\t\t\t\t\t\t(1)   :\t\t\tSIGN_UP\n")
        print("\t\t\t\t\t\t(2)   :\t\t\tSIGN_IN\n")
        print("\t\t\t\t\t\t(3)   :\t\t\t\tEXIT")
        print("\n\n\n#######################################################################################################################################################################\n\n")
        print("\n " * 17)

        choice = int(input("SELECT A OPTION(1~3):"))


        if choice == 1:
            signup()

        elif choice == 2:
                signin()
        elif choice == 3:
            print("EXITING.................")
            break
    else:
        print("wrong value inputed")

def signup():
    clr()
    print(
        "#######################################################################################################################################################################")
    print("\n " * 2)
    print(
        "                                                                    SIGN UP                          ".center(100))
    print("\n " * 2)

    print(
        "#######################################################################################################################################################################")
    print("\n ")
    print("\n" * 5)
    name=input("NAME:-\t")
    email=input("EMAIL:-\t")
    mob=input("MOBILE-No:-\t")
    passwd=input("PASSWORD:-\t")

    sql = "insert into railway_user(name,passwd,email,mob) values(%s,%s,%s,%s)"
    data = (name, passwd, email, mob)
    mycursor.execute(sql, data)
    mydb.commit()

    signin()
def signin():
    clr()
    print("#######################################################################################################################################################################")
    print("\n "*2)
    print("                                                                                WELCOME KINDLY SIGN IN\n                  ( login using your name  and  passwrd)   \n\n                         ")

    print("#######################################################################################################################################################################")
    print("\n ")
    print("\n" *5)
    user_id = input("NAME:\t")


    mycursor.execute("select name from railway_user")
    resultname = mycursor.fetchall()
    for n in resultname:
        if (n[0] == user_id):
            mycursor.execute("select passwd from railway_user")
            resultpassword = mycursor.fetchall()
            password = input("Password:\t")
            for m in resultpassword:
                if (m[0] == password):
                    print("AUTHENTICATED USER".center(200))
                    print("######...............LOADING..............########")
                    sleep(2)
                    main_menu()
                else:
                    continue
                    print("wrong password".center(200))
                    signin()






def main_menu():
    while True:
        print("\n\n\n\n\n\n\n\n")
        print(
            "#######################################################################################################################################################################")
        print(" \n"*2)
        print(
            "\n|----------------------------------------------------         TICKET RESERVATION AREA                      ---------------------------------------------|")

        print(" \n"*2)

        print("#######################################################################################################################################################################")
        print("\n\n\n\n")
        print("\t\t\t\t\t\t(1)   :\t\t\tFOR TICKET BOOKING\n")
        print("\t\t\t\t\t\t(2)   :\t\t\tCHECK PNR NO\n")
        print("\t\t\t\t\t\t(3)   :\t\t\tFOR TICKET CANCELLATION\n")
        print("\t\t\t\t\t\t(4)   :\t\t\tPASSENGER DETAILS\n")
        print("\t\t\t\t\t\t(5)   :\t\t\t\tEXIT")
        print(
            "\n\n\n#######################################################################################################################################################################\n\n")
        choice = int(input("SELECT A OPTION(1~5):"))
        if choice == 1:
            booking()
        elif choice == 2:
            checkpnr()

        elif choice == 3:
            bookscanclelation()


        elif choice == 4:
            pdetails()

        elif choice == 5:
            print("EXITING")
            break
    else:
        print("wrong value inputed")
    c = input("Do you want to continue")


def booking():
    clr()
    print("#######################################################################################################################################################################")
    print("\n " * 2)
    print("             ENTER HERE BOOKING  DETAILS   \n ||note||:-booking ticket for  one person at a time          ".center(80))
    print("\n " * 2)
    print("#######################################################################################################################################################################")
    print("\n ")
    print("\n" * 5)

    tno=input("\tTRAIN_NO:-")
    dfrom=input("\tDEPARTED FROM:-")
    arrival=input("\t ARIVAL TO:-")
    mob=input("\tVALID MOBILE NO:-")
    name = input("\tPASSANGER_NAME:-")
    sex=input("\tSEX(M/F):-")
    nationality=input("\tNATIONALITY:-")
    age=input("\tAGE:-")
    pnr = int(random.randint(100000, 254600))

    sql1="insert into tbooking(tno,dfrom,arrival,mob,name,sex,nationality,age,pnr) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    data1=(tno,dfrom,arrival,mob,name,sex,nationality,age,pnr)
    mycursor.execute(sql1, data1)
    mydb.commit()
    sleep(1)
    print("-----------THANKYOU FOR BOOKING TICKET------------------".center(200))
    print("\n"*2)
    sleep(1)
    print("                                           YOUR PNR_NO:-%s",pnr)
    sleep(1)
    print("--------------------HAPPY JOURNEY ------------------".center(200))
    sleep(2)
    main_menu()

def checkpnr():
    clr()
    print("#######################################################################################################################################################################")
    print("\n " * 2)
    print("                                        CHECK PNR STATUS             ".center(200))
    print("\n " * 2)
    print("#######################################################################################################################################################################")
    print("\n ")
    print("\n" * 5)
    pnr=int(input("ENTER YOUR PNR_NO:_"))
    print("\n" * 2)
    print("......LOADING.......".center(200))
    print("\n" * 2)
    print("........FETCHING DATA.........".center(200))
    mycursor.execute("select pnr from tbooking ")
    p=0
    for i in mycursor:
        if (i[0] == pnr):
            p=1

    if p==1:
        print("   PNR MATCHED              your booking is confirmed sir/mam                       ")
        sleep(2)
        print("...................HAPPY JOURNEY................".center(200))
        main_menu()
    else:
        print("\n" * 2)
        print("         sorry! your booking is not confirmed\n                    BETTER LUCK NEXT TIME     ".center(200))
        sleep(3)
        e = input("press enter for continue")
        main_menu()

def bookscanclelation():
    clr()
    print(
        "#######################################################################################################################################################################")
    print("\n " * 2)
    print("                                       TICKET CANCILATION          ".center(200))
    print("\n " * 2)
    print(
        "#######################################################################################################################################################################")
    print("\n ")
    print("\n" * 5)
    pnr = int(input("ENTER YOUR PNR_NO:-"))
    mycursor.execute("select pnr from tbooking ")
    p = 0
    for i in mycursor:
        if (i[0] == pnr):
            p = 1
    if p == 1:
        sql4 = "delete from tbooking where pnr=%(pnr)s"
        data4 = {'pnr': pnr}
        mycursor.execute(sql4, data4)
        mydb.commit()
        print("\n" * 2)
        print("...............YOUR TICKET CANCELATION SUCCESSFUL.THANKS TO VISIT.........")
        sleep(2)
        d = input("enter for continue")
        main_menu()

    else:
        print("....PNR NOT MATCHED...".center(200))
        sleep(3)
        main_menu()





def pdetails():
    clr()
    print(
        "#######################################################################################################################################################################")
    print("\n " * 2)
    print("                                      PASSENGER DETAILS       ".center(200))
    print("\n " * 2)
    print(
        "#######################################################################################################################################################################")
    print("\n ")
    print("\n" * 5)
    pnr = int(input("ENTER YOUR PNR_NO:-"))
    mycursor.execute("select pnr from tbooking ")
    p = 0
    for i in mycursor:
        if (i[0] == pnr):
            p = 1
    if p == 1:
        print("........................LOADING..................".center(200))
        print("\n" * 2)
        print("........................FETCHING DETAILS OF PASSANGER..................".center(200))
        print("\n" * 2)
        sql3 = "select * from tbooking where pnr=%(pnr)s"
        data3 = {'pnr': pnr}
        mycursor.execute(sql3, data3)
        res = mycursor.fetchall()
        print("||Train _NO|..|BOARDING from|..|ARRIVAL|..|MOBILE|...|NAME|..|SEX|..|NATIONALITY|..|AGE|..|PNR||  ")
        print("\n" )
        for i in res:
            print(i)
        sleep(3)
        print("\n" * 2)
        print(".....THANKS FOR VISIT........".center(240))

        c=input("press enter to continue....")
        main_menu()

    else:
        print("\n" * 2)
        print("....PNR NOT MATCHED...".center(200))
        sleep(3)
        main_menu()

page1()
