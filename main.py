import os,sys,time
import pyautogui as p
import keyboard

logo = """
            
        ███╗░░██╗██████╗░░░░██╗░█████╗░
        ████╗░██║██╔══██╗░░░██║██╔══██╗
        ██╔██╗██║██████╦╝░░░██║███████║
        ██║╚████║██╔══██╗░░░██║██╔══██║
        ██║░╚███║██████╦╝██╗██║██║░░██║
        ╚═╝░░╚══╝╚═════╝░╚═╝╚═╝╚═╝░░╚═╝
"""
def main():
    os.system("cls")
    for i in logo:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.01)    
    opp = """
        1. 5X Speed
        2. 3X Speed
        3. 1X Speed
        4. Custom
        0. Exit          
          """
    for i in opp:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.01) 
    select = input("Choose Option: ")
    if select == '1':
        fast()
    elif select == '2':
        medium()
    elif select == '3':
        slow()
    elif select == '4':
        custom()
    elif select == '0':
        exit()
        print("Thank You.")
    else:
        print("Invalid Option")
def fast():
    mess = input("Write Message: ")
    rng = input("Enter Limit: ")
    count = 0
    time.sleep(4)
    for i in range(int(rng)):
        p.typewrite(mess, 0.01)
        p.press("enter")
        count += 1
        print(f"Success -> {count}")
    print("""
          1. Main Manu
          0. Exit
          """)
    alt = input("Enter to Continue: ")
    if alt == '':
        fast()
    elif alt =='1':
        main()
    elif alt == '0':
        exit()
        print("Thank You.")
    else:
        print("Invalid Opetion")
        fast()

def medium():
    mess = input("Write Message: ")
    rng = input("Enter Limit: ")
    count = 0
    time.sleep(4)
    for i in range(int(rng)):
        p.typewrite(mess,0.2)
        p.press("enter")
        count += 1
        print(f"Success -> {count}")
    print("""
          1. Main Manu
          0. Exit
          """)
    alt = input("Enter to Continue: ")
    if alt == '':
        medium()
    elif alt =='1':
        main()
    elif alt == '0':
        exit()
        print("Thank You.")
    else:
        print("Invalid Opetion")
        medium()
def slow():
    mess = input("Write Message: ")
    rng = input("Enter Limit: ")
    count = 0
    time.sleep(4)
    for i in range(int(rng)):
        p.typewrite(mess, 0.4)
        p.press("enter")
        count += 1
        print(f"Success -> {count}")
    print("""
          1. Main Manu
          0. Exit
          """)
    alt = input("Enter to Continue: ")
    if alt == '':
        slow()
    elif alt =='1':
        main()
    elif alt == '0':
        exit()
        print("Thank You.")
    else:
        print("Invalid Opetion")
        slow()
        
def custom():
    mess = input("Write Message: ")
    rng = input("Enter Limit: ")
    dely = input("Enter Dealy For Per Message example- 0.1 : ")
    sl = float(dely)
    count = 0
    time.sleep(4)
    for i in range(int(rng)):
        p.typewrite(mess, sl)
        p.press("enter")
        count += 1
        print(f"Success -> {count}")
    print("""
          1. Main Manu
          0. Exit
          """)
    alt = input("Enter to Continue: ")
    if alt == '':
        custom()
    elif alt =='1':
        main()
    elif alt == '0':
        exit()
        print("Thank You.")
    else:
        print("Invalid Opetion")
        custom()
main()