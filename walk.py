def is_valid_walk(walk):
    # determine if walk is valid
    if len(walk) == 10:
        for i in walk:
            firstCount = int(walk.count(i))
            if not(firstCount == 5):
                return False
            else:
                return True
    else:
        return False



print(is_valid_walk(['n','n','n','s','n','s','n','s','n','s']))