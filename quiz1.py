liste = [1,2,3,4,5,6,7,8,23,67,21,-500,23,451,67]
mini= liste[0]
for each in liste:
    if(each<mini):
        mini=each
    else:
        continue
print(mini)
