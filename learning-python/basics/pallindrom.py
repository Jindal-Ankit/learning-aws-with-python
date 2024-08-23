
def is_pallindrome(testStr):
    temp = str(testStr).lower()

    newStr = ""
    for ch in temp:
        if(ch.isalnum() == True):
            newStr += ch
    
    lastIndex  = len(newStr) -1  
    reversedStr = ""
    while(lastIndex >= 0 ):
        reversedStr += newStr[lastIndex]
        lastIndex -= 1
    
    if(newStr == reversedStr):
        return True
    else:
        return False

print(is_pallindrome("abcbaa"))

