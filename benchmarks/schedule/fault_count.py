import os 
import re
import subprocess


os.chdir("/Users/nikhil/Documents/CS206_SoftwareTesting/SoftwareTestingProject/cs206-project-defectdetective/benchmarks/schedule")
print(os.getcwd())

file = open(r"/Users/nikhil/Documents/CS206_SoftwareTesting/SoftwareTestingProject/cs206-project-defectdetective/benchmarks/schedulelog_additional.txt")
totallist_testcases = []
while True:
    temp_str = 0
    univer_str = file.readline()
    if len(univer_str) == 0:
        break
    totallist_testcases.append(univer_str)


for i in range(len(totallist_testcases)):
    
    
    

    
    
    lines = totallist_testcases[i].split(" ")
    print(lines)
    
    main_str = ""
    if(len(lines)==5):
        main_str = "/Users/nikhil/Documents/CS206_SoftwareTesting/SoftwareTestingProject/cs206-project-defectdetective/benchmarks/schedule/" + lines[4].strip()
        main_str = lines[0] + " "+ lines[1] + " " +lines[2] + " " + lines[3] + " " + main_str 
    elif (len(lines)==8):
        
    

        cmd2 = "/Users/nikhil/Documents/CS206_SoftwareTesting/SoftwareTestingProject/cs206-project-defectdetective/benchmarks/schedule/" + lines[7].strip()
        main_str = lines[0] + " "+ lines[1] + " " +lines[2] + " " + lines[3] + " " +lines[4] + " " + lines[5] + " " +lines[6] + " "+cmd2
    elif (len(lines)==4):
        cmd2 = "/Users/nikhil/Documents/CS206_SoftwareTesting/SoftwareTestingProject/cs206-project-defectdetective/benchmarks/schedule/" + lines[3].strip()
        main_str = lines[0] + " "+ lines[1] + " " +lines[2] + " " + cmd2

    

    sys_str = "/Users/nikhil/Documents/CS206_SoftwareTesting/SoftwareTestingProject/cs206-project-defectdetective/benchmarks/schedule/schedule" 
   
    
    import subprocess 
    
    listappendoriginal = []

    
    proc = subprocess.Popen([sys_str,main_str], stdout=subprocess.PIPE,stderr=subprocess.PIPE, text=True)
    output = proc.stdout
    
    listappendoriginal.append(output)

dictionary_forallmutants = {}

directory = "/Users/nikhil/Documents/CS206_SoftwareTesting/SoftwareTestingProject/cs206-project-defectdetective/benchmarks/schedule"
for filename in os.listdir(directory):
    f = os.path.join(directory,filename)
    pattern = r"v\d+"
    
    if re.search(pattern,f):

        path2 = f + "/schedule.c"
        path1 = f + "/schedule"
        temp_list = []
        
        for i in range(len(totallist_testcases)):
            unverse_str1 = totallist_testcases[i]
            if len(unverse_str1)==0:
                break
            lines = unverse_str1.split(" ")
            print(lines)
            main_str = ""
            if(len(lines)==1):
                main_str =  "/Users/nikhil/Documents/CS206_SoftwareTesting/SoftwareTestingProject/cs206-project-defectdetective/benchmarks/schedule/"+ lines[0].strip()
            else:
                cmd1 = lines[0]
    

                cmd2 = "/Users/nikhil/Documents/CS206_SoftwareTesting/SoftwareTestingProject/cs206-project-defectdetective/benchmarks/schedule/" + lines[1].strip()
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
    




    
    