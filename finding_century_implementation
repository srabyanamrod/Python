def century_year(year):

    str_year = str(year)

    if(len(str_year)<3):
        return 1   # between 0-99
    elif(len(str_year) == 3):
        if(str_year[1:3]=="00"): #100,200,300...
            return int(str_year[0])
        else:    #
            return int(str_year[0])+1  #102,204,305,407..
    else:
        if(str_year[2:4]=="00"):   #1700,1800,1900
            return int(str_year[:2])
        else:
            return int(str_year[:2])+1 #1903,2017,1678...

print(century_year(2005))
print(century_year(103))
print(century_year(1400))
print(century_year(1872))
print(century_year(2100))
