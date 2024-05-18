import os 
import re
import subprocess


os.chdir("/Users/nikhil/Documents/CS206_SoftwareTesting/SoftwareTestingProject/cs206-project-defectdetective/benchmarks/printtokens2")
print(os.getcwd())

file = open(r"/Users/nikhil/Documents/CS206_SoftwareTesting/SoftwareTestingProject/cs206-project-defectdetective/benchmarks/printtokens2log_random.txt")
totallist_testcases = []
while True:
    temp_str = 0
    univer_str = file.readline()
    if len(univer_str) == 0:
        break
    totallist_testcases.append(univer_str)


for i in range(len(totallist_testcases)):
    
    
    

    
    
    lines = totallist_testcases[i]
    print(lines)
    main_str = ""
    if(len(lines)==1):
        main_str = "/Users/nikhil/Documents/CS206_SoftwareTesting/SoftwareTestingProject/cs206-project-defectdetective/benchmarks/printtokens2/" + lines[0].strip()
    else:
        cmd1 = lines[0]
    

        cmd2 = "/Users/nikhil/Documents/CS206_SoftwareTesting/SoftwareTestingProject/cs206-project-defectdetective/benchmarks/printtokens2/" + lines[1].strip()
        main_str = cmd1 + cmd2
    

    sys_str = "/Users/nikhil/Documents/CS206_SoftwareTesting/SoftwareTestingProject/cs206-project-defectdetective/benchmarks/printtokens2/printtokens2" 
    cmd0 = sys_str + cmd2
    
    import subprocess 
    
    listappendoriginal = []

    
    proc = subprocess.Popen([sys_str,main_str], stdout=subprocess.PIPE,stderr=subprocess.PIPE, text=True)
    output = proc.stdout
    
    listappendoriginal.append(output)

dictionary_forallmutants = {}

directory = "/Users/nikhil/Documents/CS206_SoftwareTesting/SoftwareTestingProject/cs206-project-defectdetective/benchmarks/printtokens2"
for filename in os.listdir(directory):
    f = os.path.join(directory,filename)
    pattern = r"v\d+"
    
    if re.search(pattern,f):

        path2 = f + "/printtokens2.c"
        path1 = f + "/printtokens2"
        temp_list = []
        
        for i in range(len(totallist_testcases)):
            unverse_str1 = totallist_testcases[i]
            if len(unverse_str1)==0:
                break
            lines = unverse_str1.split(" ")
            print(lines)
            main_str = ""
            if(len(lines)==1):
                main_str =  "/Users/nikhil/Documents/CS206_SoftwareTesting/SoftwareTestingProject/cs206-project-defectdetective/benchmarks/printtokens2/"+ lines[0].strip()
            else:
                cmd1 = lines[0]
    

                cmd2 = "/Users/nikhil/Documents/CS206_SoftwareTesting/SoftwareTestingProject/cs206-project-defectdetective/benchmarks/printtokens2/" + lines[1].strip()
                main_str = cmd1 + cmd2

        



                
            temp_proc = subprocess.Popen([path1,main_str], stdout=subprocess.PIPE,stderr=subprocess.PIPE, text=True)
            output1 = temp_proc.stdout
            temp_list.append(output1)
        dictionary_forallmutants[f] = temp_list
        


dictionary_containing_count = {}
total_count= 0
for keys in dictionary_forallmutants.keys():
    list_for_checking  = dictionary_forallmutants[keys]
    count = 0
    for i in range(len(listappendoriginal)):
        if list_for_checking[i] != listappendoriginal[i]:
            count = count + 1
            total_count = total_count + 1
    dictionary_containing_count[keys] = count

print("break")
    




    
    