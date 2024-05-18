# RANDOM TEST CASE PRIORITIZATION :-

import pickle 
import random
pathforbranchpicklefile = '/Users/nikhil/Documents/CS206_SoftwareTesting/SoftwareTestingProject/cs206-project-defectdetective/totinfo_branch.pickle'
pathforstatementpicklefile = '/Users/nikhil/Documents/CS206_SoftwareTesting/SoftwareTestingProject/cs206-project-defectdetective/totinfo_statement.pickle'
pathforuniversetxtfile = '/Users/nikhil/Documents/CS206_SoftwareTesting/SoftwareTestingProject/cs206-project-defectdetective/benchmarks/totinfo/universe.txt'

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


testcoveredbranch_dict_random = {}
testcoveredstatement_dict_random = {}
listofstatementkeys = list(temp_dict_statementcoverage.keys())
listofbranchkeys = list(temp_dict_branchcoverage.keys())

random_number = random.choice(listofstatementkeys)
testcoveredbranch_dict_random = temp_dict_branchcoverage[random_number]
testcoveredstatement_dict_random = temp_dict_statementcoverage[random_number]
testsuite_random = []
testsuite_random.append(random_number)



while True:
    
    if len(testsuite_random)>=8:
        break

    random_number_list = sorted(list(temp_dict_branchcoverage.keys()), key=lambda x: random.random())
    random_number = random_number_list[0]
    

    if newcoverage(testcoveredbranch_dict_random,testcoveredstatement_dict_random,temp_dict_branchcoverage[random_number],temp_dict_statementcoverage[random_number]) == True:
        for branch_keys in temp_dict_branchcoverage[random_number].keys():
                if testcoveredbranch_dict_random[branch_keys] <=  0 and temp_dict_branchcoverage[random_number][branch_keys] >0:
                    testcoveredbranch_dict_random[branch_keys] = temp_dict_branchcoverage[random_number][branch_keys]
        for statement_keys in temp_dict_statementcoverage[random_number].keys():
                if testcoveredstatement_dict_random[statement_keys] == False and temp_dict_statementcoverage[random_number][statement_keys]== True:
                    testcoveredstatement_dict_random[statement_keys] = True 
        
        testsuite_random.append(random_number)
    else :
        print("NO New Coverage")


filefor_writingtestcases = "/Users/nikhil/Documents/CS206_SoftwareTesting/SoftwareTestingProject/cs206-project-defectdetective/benchmarks/totinfolog_random.txt"
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
for i in range(len(testsuite_random)):
    
    finaltestcasesuites.append(dictionary_mapping_for_universe_text[testsuite_random[i]])
for i in range(len(finaltestcasesuites)):
    file_faults.writelines(finaltestcasesuites[i])

