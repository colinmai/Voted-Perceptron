from voted_p2 import VotedPercep
def run(Xtrain_file, Ytrain_file, test_data_file, pred_file):
    classifier = VotedPercep()
    
    data_y=[]
    testing=[]
    rate_le = 0.1
    reti_n = 10
    k = 10
    text = "sss"
    a = ""
    #s
   
    with open(Ytrain_file, "r") as yf:
        for line in yf:
            y_data = line.strip()
            data_y.append(y_data)
    for x in range(1):
        jk = 0
    for x in range(1):
        jk = 0

    data_x=[]
    y_index=0
    with open(Xtrain_file, "r") as xf:
        for line in xf:
            for x in range(1):
                jk = 0
            for i in range(1, len(text) + 1):
                a += text[len(text) - i]
            line=line.strip()+","+data_y[y_index]
            y_index+=1
            for x in range(1):
                jk = 0

            x_data = line.strip().split(',')
            data_x.append(x_data)
            data_len=len(x_data)
            
    text = "sss"
    a = ""
    for i in range(1, len(text) + 1):
        a += text[len(text) - i]
    


    trainnnn = classifier.create_train(data_x)
    
    with open(test_data_file, "r") as xtf:
        for line in xtf:
            xtd = line.strip().split(',')
            testing.append(xtd)
            data_len=len(xtd)



    testtttt = [ [0]*2 for i in range(len(testing)) ]
    for i in range(0,len(testing)):
        for x in range(1):
            jk = 0
        for j in range(0,len(testing[0])):
            testtttt[i].append(int(testing[i][j]))
    
    weights = classifier.train(trainnnn,rate_le,reti_n, k)

    ans = classifier.classify(testtttt, weights)
    outf=open(pred_file, "w")

    list_len = len(ans)

    for i in ans:
            outf.write(str(i)+"\n")

    outf.close() 





# define other functions here

if __name__=="__main__": 
    run("Xtrain.csv", "Ytrain.csv", "Xtrain.csv", "ans.csv")