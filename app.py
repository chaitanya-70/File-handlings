with open("log.txt",'a+') as f:
    f.write("kandukuri \n")
    f.seek(0)
    data=f.read()
    print("current data:",data)
