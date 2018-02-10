#------------------------
# 2018-02-9
# Find character in string
def findChar (str, ch):
    index = 0
    while (index < len(str)):
        if str[index] == ch:
            print ("found character {} in {} at location {}".format (ch, str, index))    
            print ("found character", ch, "at location", index, "'n string", str)    
            return index
        index = index + 1
    
    print ("Did not find character {} in {}".format(ch, str))
    return -1
    
print ("Enter string to search in:")
stringToSearch = input()
print ("Enter character to search in {}".format(stringToSearch))
characterToSearch = input()
foundChar = findChar(stringToSearch, characterToSearch)
#-----------------------------------------------------




