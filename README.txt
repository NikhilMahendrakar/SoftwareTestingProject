File Description
Name.txt - include the name, Sid ane email

CS206_Software_Testing.pdf - includes the experimental resulta and observations

fault_exposed.csv - collected the results from faultcount.py

faultcount.py-  will evaluate the total number of faults generated by each test suites.

For each benchmark contains of four programs which will evaluate the test suits for respective benchmark program
-> coverage_<benchmarkprogram>.py (statement + branch for each benchmark program)
-> getadditionaltestsuites_<benchmarkprogram>.py(Additional test case priortization)
-> genrandomtestsuites_<benchmarkprogram>.py(Random test case priortization)
-> gettotalcoverage_<benchmarkprogram>.py(Total test case priortization)

Place the file path according to this format

pathforbranchpicklefile = '/Users/nikhil/Documents/CS206_SoftwareTesting/SoftwareTestingProject/cs206-project-defectdetective/totinfo_branch.pickle'
pathforstatementpicklefile = '/Users/nikhil/Documents/CS206_SoftwareTesting/SoftwareTestingProject/cs206-project-defectdetective/totinfo_statement.pickle'
pathforuniversetxtfile = '/Users/nikhil/Documents/CS206_SoftwareTesting/SoftwareTestingProject/cs206-project-defectdetective/benchmarks/totinfo/universe.txt'


