
# LOGICAL OPERATORS (AND, OR, NOT)
# We use logical operators when we need to check multiple conditions at once.

has_high_income = True 
has_good_credit = True
has_criminal_record = False 

# 1. THE 'AND' OPERATOR
# AND: ALL conditions must be True for the block to execute.
if has_high_income and has_good_credit: 
    print("Eligible for loan (Passed AND test)")

# 2. THE 'OR' OPERATOR
# OR: At least ONE condition must be True for the block to execute.
# Even if they didn't have high income, good credit alone would pass this test.
if has_high_income or has_good_credit:
    print("Eligible for loan (Passed OR test)")

# 3. THE 'NOT' OPERATOR
# NOT: Inverts the boolean value (True becomes False, False becomes True).
# Since has_criminal_record is False, 'not has_criminal_record' becomes True.
if has_good_credit and not has_criminal_record:
    print("Eligible for loan (Passed NOT test)")

# Output:
# Eligible for loan (Passed AND test)
# Eligible for loan (Passed OR test)
# Eligible for loan (Passed NOT test)
