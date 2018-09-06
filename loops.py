heroes=['koshka','rona','gwen','reim','ringo','catherine','lyra']


count=10
num=0

for hero in heroes:
    #print(hero)
    if hero == "koshka":
        print(f"{hero} is offensive")
    while num < count:
        if num==0:
            num+=1
            continue
        elif hero== 'catherine':
            num+=1
            print(f"{hero} is a captain")
