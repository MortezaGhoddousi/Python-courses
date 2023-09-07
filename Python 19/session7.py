# def find_and_replace(mylist, tofind, toreplace):
#     # ind = 0
#     # for item in mylist:
#     #     if item == tofind:
#     #         mylist[ind] = toreplace
#     #     ind = ind+1

#     for index, item in enumerate(mylist):
#         if item == tofind:
#             mylist[index] = toreplace
#     return mylist

# mylist = ["Morteza", "Javad", "Reza"]
# print(mylist)
# mylist = find_and_replace(mylist, "Morteza", "MORTEZA")
# print(mylist)


def pr (x, y, *args):
    print(x, y)
    for i in args:
        print(i)

pr("Morteza", "Javad", "Reza")