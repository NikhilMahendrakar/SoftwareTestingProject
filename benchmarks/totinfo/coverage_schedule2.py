import json
import re 
import os
import pickle


Totalbranchcoverage_foralltestcases = {}
indexforbranch = 0
Totalstatementcoverage_foralltestcases = {}
indexforstatement = 0


indexnumber_test = 1

os.chdir("/Users/nikhil/Documents/CS206_SoftwareTesting/SoftwareTestingProject/cs206-project-defectdetective/benchmarks/totinfo")
print(os.getcwd())

file = open(r"/Users/nikhil/Documents/CS206_SoftwareTesting/SoftwareTestingProject/cs206-project-defectdetective/benchmarks/totinfo/universe.txt")
while True:
    unverse_str = file.readline()
    
    indexnumber_test = indexnumber_test + 1

    
    if len(unverse_str) == 0:
        break
    sys_str = "/Users/nikhil/Documents/CS206_SoftwareTesting/SoftwareTestingProject/cs206-project-defectdetective/benchmarks/totinfo/totinfo "  + unverse_str 
    os.system("/opt/homebrew/bin/gcc-13 -Wno-return-type -g --coverage -O0 -o totinfo /Users/nikhil/Documents/CS206_SoftwareTesting/SoftwareTestingProject/cs206-project-defectdetective/benchmarks/totinfo/totinfo.c")
    os.system(sys_str)
    coverage_str_1 = "/opt/homebrew/bin/gcov-13 -b --json-format totinfo.c"
    coverage_str_2 = "/opt/homebrew/bin/gcov-13 -b totinfo.c"
    os.system(coverage_str_1)
    os.system(coverage_str_2)
    os.system("gzip -d totinfo.gcov.json.gz")
    pathforjson = os.getcwd() + '/totinfo.gcov.json'
    pathforgcov = os.getcwd() + '/totinfo.c.gcov'
   
    statement_coverage = {}
    branch_coverage = {}
    branch_coverage_list = []
    print(unverse_str)



    # Parsing the JSON File
    with open(pathforjson,'r') as temp_file:

        temp_dict = json.load(temp_file)
        main_list = temp_dict['files'][0]['lines']
        line_number = 1
        # print(main_list)
        for i in range(len(main_list)):
            if main_list[i]['count'] >= 1:
                statement_coverage[line_number] = True
            else :
                statement_coverage[line_number] = False
            line_number = line_number + 1
        branch_number = 1
        for i in range(len(main_list)):
            temp_list = main_list[i]['branches']
            if(len(temp_list)>0):
                for i in range(len(temp_list)):
                    tempappend = -1
                    branch_coverage[branch_number] = tempappend
                    branch_number = branch_number+1
    
    # Parsing the GCOV file
    with open(pathforgcov, 'r') as gcovfile:
        
        while True:
            unverse_str1 = gcovfile.readline()
            if len(unverse_str1) == 0:
                break
            if re.search('branch', unverse_str1) != None:
                main_content_list = re.findall(r'\d+', unverse_str1)
                if(len(main_content_list)==2):
                    branch_coverage_list.append(int(main_content_list[1]))
                elif(len(main_content_list)==1):
                    branch_coverage_list.append(-1)
                else:
                    print("Yahan nahin aana chahiye")

    i = 0
    for key in branch_coverage.keys():
        branch_coverage[key] = branch_coverage_list[i]
        i = i+1
    
    

    count_statementcoverage = 0
    for key in branch_coverage:
        if branch_coverage[key] > 0:
            count_statementcoverage = count_statementcoverage + 1
    print(count_statementcoverage/len(branch_coverage))
    count_statementcoverage = 0
    for key in statement_coverage:
        if statement_coverage[key] == True:
            count_statementcoverage = count_statementcoverage + 1
    print(count_statementcoverage/len(statement_coverage))

    
    Totalbranchcoverage_foralltestcases[indexforbranch] = branch_coverage
    Totalstatementcoverage_foralltestcases[indexforstatement] = statement_coverage
    indexforbranch = indexforbranch + 1
    indexforstatement = indexforstatement + 1
    
    
    

    
    os.remove("/Users/nikhil/Documents/CS206_SoftwareTesting/SoftwareTestingProject/cs206-project-defectdetective/benchmarks/totinfo/totinfo")
    os.remove("/Users/nikhil/Documents/CS206_SoftwareTesting/SoftwareTestingProject/cs206-project-defectdetective/benchmarks/totinfo/totinfo.c.gcov")
    os.remove("/Users/nikhil/Documents/CS206_SoftwareTesting/SoftwareTestingProject/cs206-project-defectdetective/benchmarks/totinfo/totinfo.gcda")
    os.remove("/Users/nikhil/Documents/CS206_SoftwareTesting/SoftwareTestingProject/cs206-project-defectdetective/benchmarks/totinfo/totinfo.gcno")
    os.remove("/Users/nikhil/Documents/CS206_SoftwareTesting/SoftwareTestingProject/cs206-project-defectdetective/benchmarks/totinfo/totinfo.gcov.json")
    
with open(r'/Users/nikhil/Documents/CS206_SoftwareTesting/SoftwareTestingProject/cs206-project-defectdetective/totinfo_branch.pickle', 'wb') as handle:
    pickle.dump(Totalbranchcoverage_foralltestcases, handle, protocol=pickle.HIGHEST_PROTOCOL)


with open(r'/Users/nikhil/Documents/CS206_SoftwareTesting/SoftwareTestingProject/cs206-project-defectdetective/totinfo_statement.pickle', 'wb') as handle:
    pickle.dump(Totalstatementcoverage_foralltestcases, handle, protocol=pickle.HIGHEST_PROTOCOL)    


    




    
 
        
                   
    

    

    


        
    
    

        
        