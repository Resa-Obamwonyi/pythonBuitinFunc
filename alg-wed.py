def first_non_repeating_letter(str):
    lowerstr = str.lower()
    repeated_list = [x for x in lowerstr if lowerstr.count(x) == 1]
    if len(repeated_list) == 0:
      return ""
    elif repeated_list[0] not in str:
      return repeated_list[0].upper()
    else:
      return repeated_list[0]



print(first_non_repeating_letter("sTreSS"))