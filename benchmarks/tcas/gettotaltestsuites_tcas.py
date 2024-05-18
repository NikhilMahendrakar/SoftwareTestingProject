import pickle 

pathforbranchpicklefile = '/Users/nikhil/Documents/CS206_SoftwareTesting/SoftwareTestingProject/cs206-project-defectdetective/tcas_branch.pickle'
pathforstatementpicklefile = '/Users/nikhil/Documents/CS206_SoftwareTesting/SoftwareTestingProject/cs206-project-defectdetective/tcas_statement.pickle'
pathforuniversetxtfile = '/Users/nikhil/Documents/CS206_SoftwareTesting/SoftwareTestingProject/cs206-project-defectdetective/benchmarks/tcas/universe.txt'


with open(pathforbranchpicklefile,'rb') as f:
    temp_dict_branchcoverage = pickle.load(f)
with open(pathforstatementpicklefile,'rb') as f1:
    temp_dict_statementcoverage = pickle.load(f1)


def covered(branch_coverage, statement_coverage):
    for statement_keys in statement_coverage.keys():
        if statement_coverage[statement_keys] == False:
            return False
    for branch_keys in branch_coverage.keys():
        if branch_coverage[branch_keys] <= 0:
            return False
    return True

def newcoverage(branch1, statement1, branch2, statement2):
    for key in statement2.keys():
        if statement2[key] == True and statement1[key] == False:
            return True
    for key1 in branch2.keys():
        if branch2[key1] > 0 and branch1[key1] <=0:
            return True
    
    return False






        


random_test_suites = {}
totalcoverage_test_suites = {}
additional_test_suites = {}

# TOTAL COVERAGE PRIORITIZATION
# I will give 50% weightage for both branch and statement converage 

testcases_dict_priority = {}
for keys in temp_dict_branchcoverage.keys():
    temp_dict = temp_dict_branchcoverage[keys]
    count_branch_coverage = 0
    for key in temp_dict.keys():
        if temp_dict[key] > 0:
            count_branch_coverage = count_branch_coverage + 1
    branch_coverage_cent = count_branch_coverage / len(temp_dict)
    testcases_dict_priority[keys] = branch_coverage_cent * 50

for keys in temp_dict_statementcoverage.keys():
    temp_dict = temp_dict_statementcoverage[keys]
    count_statement_coverage = 0
    for key in temp_dict.keys():
        if temp_dict[key] == True:
            count_statement_coverage = count_statement_coverage + 1
    statement_coverage_cent = count_statement_coverage / len(temp_dict)
    temp_calculation = testcases_dict_priority[keys]
    testcases_dict_priority[keys] = statement_coverage_cent * 50 + temp_calculation

sorted_testcase_priority = dict(sorted(testcases_dict_priority.items(), key=lambda x:x[1]))
sorted_testcase_priority = dict(reversed(list(sorted_testcase_priority.items())))
listofkeys = list(sorted_testcase_priority.keys())
indexforkeys = 0
testcoveredstatement_dict = temp_dict_statementcoverage[listofkeys[indexforkeys]]
testcoveredbranch_dict = temp_dict_branchcoverage[listofkeys[indexforkeys]]
testsuites = []
testsuites.append(listofkeys[indexforkeys])
indexforkeys = indexforkeys + 1
while indexforkeys < len(listofkeys):
    if(covered(testcoveredbranch_dict,testcoveredstatement_dict)==False):
        temp_key = listofkeys[indexforkeys]
        if (newcoverage(testcoveredbranch_dict,testcoveredstatement_dict,temp_dict_branchcoverage[temp_key],temp_dict_statementcoverage[temp_key])):
            for branch_keys in temp_dict_branchcoverage[temp_key].keys():
                if testcoveredbranch_dict[branch_keys] <=  0 and temp_dict_branchcoverage[temp_key][branch_keys] >0:
                    testcoveredbranch_dict[branch_keys] = temp_dict_branchcoverage[temp_key][branch_keys]
            for statement_keys in temp_dict_statementcoverage[temp_key].keys():
                if testcoveredstatement_dict[statement_keys] == False and temp_dict_statementcoverage[temp_key][statement_keys]== True:
                    testcoveredstatement_dict[statement_keys] = True 


            testsuites.append(temp_key)
            indexforkeys = indexforkeys + 1
        
        else:
            indexforkeys = indexforkeys + 1


        




    
    else :
        print("break")
        

filefor_writingtestcases = "/Users/nikhil/Documents/CS206_SoftwareTesting/SoftwareTestingProject/cs206-project-defectdetective/benchmarks/tcaslog_total.txt"
file_faults = open(filefor_writingtestcases,'w+')



dictionary_mapping_for_universe_text = {}
index_for_mapping = 0
file = open(pathforuniversetxtfile)
while True:

    unverse_str = file.readline()
    if len(unverse_str)==0:
        break
    dictionary_mapping_for_universe_text[index_for_mapping] = unverse_str
    index_for_mapping =  index_for_mapping + 1

finaltestcasesuites = []
for i in range(len(testsuites)):
    
    finaltestcasesuites.append(dictionary_mapping_for_universe_text[testsuites[i]])
for i in range(len(finaltestcasesuites)):
    file_faults.writelines(finaltestcasesuites[i])

print("break")








    
        









    

