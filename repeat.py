def repeated(string):
    # Your code goes here
    count = 0
    textLower = string.lower()
    for x in set(textLower):
        if textLower.count(x) > 1:
            count += 1
    return count


def duplicate_count(text):
    textDic = {}
    for i in text.lower(): #change text to lowercase.
        if textDic.get(i) is None: # if i is not in dictionary, add i to dictionary with value of 0
            textDic[i] = 0
        else:
            textDic[i] = 1 # if i is already in dictionary, assign value of 1
    return sum(textDic.values()) #sum of all values in dict.

print(repeated("aaabbcddee"))
print(duplicate_count("aaabbcddee"))
