fac = int(input()) #number of facility taken from the user
tanks = 0
tank_capacity = ''


for facilityNum in range(1, fac + 1):
    tanks = int(input()) #Number of tanks
    tank_capacity = input()
    tank_capacity_lst = []
    
    zeroCount = 0
    sum = 0
    
    for eachTank in tank_capacity.split():
        tank_capacity_lst.append(int(eachTank))
        
    tank_capacity_lst = tank_capacity_lst[0: -1]
    
    for i in tank_capacity_lst:
        if i == 0 :
            zeroCount += 1
        else:
            break
    for j in tank_capacity_lst:
        sum += j
        
    total = sum + tank_capacity_lst.count(0) - zeroCount
    print(total)