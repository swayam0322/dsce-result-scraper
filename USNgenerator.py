with open('ECE.txt','a') as f:
    for i in range(1,245):
        f.write("1DS21EC"+str(i).zfill(3)+"\n")
