from pathlib import Path
import os




def readfileandfolder():
     path = Path('')
     item = list(path.rglob('*'))
     for i,entry in enumerate(item):
          print(f"{i+1}={entry}")




def createfile():
    try:
        readfileandfolder()
        name=input("please tell me your file name:-")
        p = Path(name)
        if not p.exists():
                with open(p,"w") as fs:
                 data=input("what you write the data in this file:-")
                 fs.write(data)
                 print("your file is complete successfully:-")
        else:
                print("your file is already exist :-")
    except Exception as ttt:
         print(f"your error is {ttt}")


def readfile():
     readfileandfolder()
     name=input("which file you need for read :-")
     p=Path(name)
     try:
          if p.exists() and p.is_file():
            with open(p,'r') as fs:
             data=fs.read()
            print(data)
            print("your data is read successfully ")
          else:
           print("your file is not read ")
     except Exception as ttt:
         print(f"your error is {ttt}")

def updatefile():
    readfileandfolder()
    name =input("which file you want to update ")
    p =Path(name)
    print("press  1 for changing the file name :-")
    print("press  2 for overwritting the file name :-")
    print("press  3 for appending  the file name :-")

    res =int(input("please tell me your response:-"))

    try:
       if res ==1 :
        name2 =input("please tell me your new name for rename the file :-")
        p2 =Path(name2)
        p.rename(p2)
       elif res ==2 :
        with open(p,'w') as fs:
            data=input("what the write in this file :-")
            fs.write(data)
       else:
        with open(p,'a') as fs :
            data =input("what the appenting the file :-" )
            fs.write(""+data)

            print("your data is updated:-")
    except Exception as ttt:
       print(f"your error is {ttt}")


def deletefile():
    readfileandfolder()
    name=input("which file you want delete :-")
    p=Path(name)
    if p.exists() and p.is_file():
        os.remove(name)
        print("your file successfully delete:-")
    else:
        print("your file is not deleted")
        
     




     
     


print("press 1 for create file:- ")
print("press 2 for read  file:- ")
print("press 3 for update  file:- ")
print("press 4 for delete file:- ")


cheak=int(input("please select the number:-"))

if cheak == 1 :
     createfile()

if cheak == 2 :
     readfile()

if cheak == 3 :
    updatefile()

if cheak == 4 :
    deletefile()

     

