# Write a function called check_access that takes three parameters:
# -   age (an integer)
# -   is_member (a boolean)
# -   has_invitation (a boolean)
# The function should return True if any of these conditions are met:
# 1.  The person is at least 18 years old AND is a member
# 2.  The person has an invitation (regardless of age or membership)
# 3.  The person is at least 21 years old (regardless of membership or invitation)

def check_access(age, is_member, has_invite):
    if has_invite:
        return True
    else:
        if age >= 18 and is_member:
            return True
        else:
            return age >= 21

def check_access(age, is_member, has_invite):
    return has_invite or ((age >= 18 and is_member) or age >= 21)
        
print(check_access(23, False, False) == True)
print(check_access(21, True, False) == True)
print(check_access(19, True, False) == True)
print(check_access(17, False, True) == True)
print(check_access(16, True, False) == False)
print(check_access(16, False, False) == False)