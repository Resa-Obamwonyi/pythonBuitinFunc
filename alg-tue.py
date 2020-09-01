def find_outlier(integers):
    odd_outlier = [x for x in integers if x % 2 != 0]
    even_outlier = [x for x in integers if x % 2 == 0]

    if len(odd_outlier) == 1:
        return odd_outlier[0]
    else:
        return even_outlier[0]