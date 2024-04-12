import wikipedia as wp
print("MENU")
print("1.summary\n2.important topics\n3.Exit")
while True:
    choice=int(input("Enter your choice:"))
    if choice==1:
        topic=input("Enter your topic:")
        result=wp.summary(topic,30)
        choice1=input("Do you want to save it as a txt file?")
        if choice1=='y':
            file_name=input("Enter the file name:")
            with open(f"E:/edcom/{file_name}.txt",'w', encoding = "UTF-8") as a:
                a.write(result)
            print("The file is saved successfully.")
        elif choice1=='n':
            print("The result is \n ",result)
    elif choice==2:
        title=input("Enter your topic:")
        result1=wp.search(title,20)
        print("fThe topics related to{title} are ")
        for i in result1:
            print(i,"\n")
    elif choice==3:
        break
