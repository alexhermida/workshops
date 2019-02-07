
# Refactor next functions to be more Pythonic

def message_formatting(msg_id, msg_type, msg_description):
    message = "Message with identifier " + str(msg_id) + " has type " + msg_type + " and the description is " + msg_description + "."

    return message

def iterate_list(elements):
    list_indexes = []
    for i in range(len(elements)):
        list_indexes.append(elements[i])
    return list_indexes

def reverse_list(elements):
    list_indexes = []
    for i in range(len(elements) -1 , -1, -1):
        list_indexes.append(elements[i])
    return list_indexes
