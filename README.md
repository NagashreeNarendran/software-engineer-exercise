# Steps done
1. Updated the existing object_analisis.py with new test cases to showcase the existing issues in the original file
2. Issues:
a) Both the functions uses multiple "for" loops for data computation.This increases the space complexity and time complexity of each function.
b) Using multiple "for" loops during condition check causes only the first matching data entry to be returned even though multiple json enteries satisy the aboundant and farthest conditions.
c) Failure conditions such as entry not found are not handled in the original file.
d) Added new json input enteries to illustrate existing issue.
e) Uploaded the output screenshot in the repo
3. Solution:
a) Added a new file object_analysis_improved.py to fix the issues,improve performance and code readability.
b) Replaced multiple condition checks and multiple "for" loops with dictionary and list data structures to reduce time complexity,space complexity and improve the performance of the program.
c) Added multiple sample input json files to test the complete functionality.
d)Handled failure cases and entry not found exceptional cases in the new file.
e) Uploaded output screenshot in the repo
