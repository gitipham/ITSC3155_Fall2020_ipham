# Python Activity
#
# Fill in the code for the functions below.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code.

# # Part A.
def array_2_dict(emails, contacts):
    # YOUR CODE HERE
    
    keys = contacts
    values = emails
    if len(emails) == 0:
        return dict(keys)
    else:
        return dict(zip(keys, values))


# # Part B.
def array2d_2_dict(contact_info, contacts):
    # YOUR CODE HERE
    count = 0
    for i in contacts:
        tempDict = dict()
        if count < len(contact_info) and len(contact_info[count]) != 0:
            tempDict["email"] = contact_info[count][0];
            tempDict["phone"] = contact_info[count][1];
            count += 1
        contacts[i] = tempDict
    return contacts    


# # Part C.
def dict_2_array(contacts):
    # YOUR CODE HERE

    return

