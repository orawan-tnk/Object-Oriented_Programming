i = 0
while True :
    num = int(input('ใส่คำ: '))
    if num > 0 :
        i += num 
        print(f'ผลรวมตอนนี้ {i}')
    elif num == 0 :
        print(f'ผลรวมตอนนี้ {i}')    
        print(f'ผลรวมทั้งหมด {i}')  
        break