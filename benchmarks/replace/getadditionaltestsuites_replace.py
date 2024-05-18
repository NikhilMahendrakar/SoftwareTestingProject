import pickle 
import random
pathforbranchpicklefile = '/Users/nikhil/Documents/CS206_SoftwareTesting/SoftwareTestingProject/cs206-project-defectdetective/replace_branch.pickle'
pathforstatementpicklefile = '/Users/nikhil/Documents/CS206_SoftwareTesting/SoftwareTestingProject/cs206-project-defectdetective/replace_statement.pickle'
pathforuniversetxtfile = '/Users/nikhil/Documents/CS206_SoftwareTesting/SoftwareTestingProject/cs206-project-defectdetective/benchmarks/replace/universe.txt'

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

testcoveredbranch_dict_additional = {}
testcoveredstatement_dict_additional = {}
testsuites_additional = []
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

listofkeys_additional = list(sorted_testcase_priority.keys())
testcoveredbranch_dict_additional = temp_dict_branchcoverage[listofkeys_additional[0]]
testcoveredstatement_dict_additional = temp_dict_statementcoverage[listofkeys_additional[0]]
testsuites_additional.append(listofkeys_additional[0])
flag = True
while flag:
    count_additional = 0
    maxtestsuite = -1
    maxcoverage = 0
    for testcase_keys in listofkeys_additional:
        
        
        tempcoverage = 0
        for keys_branch in temp_dict_branchcoverage[testcase_keys].keys():
            if testcoveredbranch_dict_additional[keys_branch] <=0 and temp_dict_branchcoverage[testcase_keys][keys_branch]>0:
                tempcoverage = tempcoverage + 1
        for keys_statement in temp_dict_statementcoverage[testcase_keys].keys():    
            if testcoveredstatement_dict_additional[keys_statement] == False and temp_dict_statementcoverage[testcase_keys][keys_statement] == True:
                tempcoverage = tempcoverage +1
        if tempcoverage > maxcoverage:
            maxcoverage = tempcoverage
            maxtestsuite = testcase_keys
        count_additional = count_additional +1 
        
        if tempcoverage > 0:

            print(tempcoverage)
    if maxtestsuite == -1:
        break
    testsuites_additional.append(maxtestsuite)
    tempassignstatement = temp_dict_statementcoverage[maxtestsuite]
    tempassignbranch = temp_dict_branchcoverage[maxtestsuite]
    for keys in tempassignbranch.keys():
        if testcoveredbranch_dict_additional[keys] <= 0 and tempassignbranch[keys] >0:
            testcoveredbranch_dict_additional[keys]  = tempassignbranch[keys]
    for keys1 in tempassignstatement.keys():
        if testcoveredstatement_dict_additional[keys1] == False and tempassignstatement[keys1] == True:
            testcoveredstatement_dict_additional[keys1] = True
    if covered(testcoveredbranch_dict_additional,testcoveredstatement_dict_additional) == True:
        flag = False
        break

filefor_writingtestcases = "/Users/nikhil/Documents/CS206_SoftwareTesting/SoftwareTestingProject/cs206-project-defectdetective/benchmarks/replacelog_additional.txt"
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
for i in range(len(testsuites_additional)):
    
    finaltestcasesuites.append(dictionary_mapping_for_universe_text[testsuites_additional[i]])
for i in range(len(finaltestcasesuites)):
    file_faults.writelines(finaltestcasesuites[i])






print("break")