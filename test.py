def withdraw(amount):

    amountList = [0, 0, 0]

    if amount >= 40 and amount <= 10000:

        if amount >= 100:
            amountList[0] = amount // 100
            hundred_remainder = amount - (amountList[0] * 100)

            if hundred_remainder >= 50 and hundred_remainder%50 >= 20:
                amountList[1] = hundred_remainder//50
                twenty_remainder = hundred_remainder -(amountList[1] * 50)

                if twenty_remainder >= 20:
                    amountList[2] = twenty_remainder // 20

            elif hundred_remainder == 50:
                amountList[1] = hundred_remainder // 50

            else:
                amountList[2] = hundred_remainder // 20

        elif amount >= 50 and amount%50 >= 20:
            amountList[1] = amount // 50
            fifty_remainder = amount - (amountList[1] * 50)

            if fifty_remainder >= 20:
                amountList[2] = fifty_remainder // 20

        elif amount == 50:
            amountList[1] = amount // 50

        else:
            amountList[2] = amount // 20


        return amountList

print(withdraw(150))
print(withdraw(60))
print(withdraw(860))
print(withdraw(540))
print(withdraw(370))


# def no_notes(amount):
#   notes = [100, 50, 20]
#   note_counter= [0,0,0]
#
#   for i, j in zip(notes, note_counter):
#       if amount >= i:
#           j = amount // i
#           amount = amount - j * i
#           dict = (i, " : ", j)
#           return dict


# print(no_notes(860))