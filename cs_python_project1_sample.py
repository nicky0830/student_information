attribute_name = ["student_id", "name", "department", "sex", "age", "nationality", "grade"]
attribute_type = ["INT", "CHAR(20)", "CHAR(50)", "CHAR(1)", "INT", "CHAR(3)", "FLOAT"]
student_list = []

# -------------------------------------
# 1. initialization
# -------------------------------------
# Input 	: None (No parameters)
# Output 	: None (No return)
# -------------------------------------
# Read the file 'student_information.txt'
# Add student information into the global variable 'student_list'
def initialization():
    f = open("student_information.txt", "r")


# -------------------------------------
# 2. addition
# -------------------------------------
# Input 	: string (one student information)
# Output 	: boolean (success or failure)
# -------------------------------------
# Add one student information by using the input string
# Check the length of the 'CHAR' attribute and the same 'student_id'
def addition(student_information):
    return True


# -------------------------------------
# 3. removal
# -------------------------------------   
# Input 	: string (a condition)
# Output 	: boolean (success or failure)
# Remove student information which satisfy a condition
def removal(condition):
    return True


# -------------------------------------
# 4. show
# -------------------------------------       
# Input 	: string (a condition)
# Output 	: None (No return)
# -------------------------------------
# Print student information satisfying a condition
def show(condition):
    


# -------------------------------------
# 5. statistic
# -------------------------------------       
# Input 	: two strings (a condition, an attribute name)
# Output 	: None (No return)
# -------------------------------------        
# Print statistics of an attribute in tuples satisfying a condition
def statistic(condition, att_name):
    
    
    
# -------------------------------------
# 6. writing
# -------------------------------------       
# Input 	: None (No parameters)
# Output 	: None (No return)
# -------------------------------------        
# Write the 'student_list' to 'student_information.txt' file
def writing():
    f = open("student_information.txt", "w")

    
# -------------------------------------
# 7. main
# -------------------------------------       
def main():
    


initialization()
main()
writing()