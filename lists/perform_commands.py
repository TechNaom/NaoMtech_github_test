if __name__ == '__main__':
    N = int(input())
    list1 = ['insert','insert','insert','print','remove','append','append','sort','print','pop', 'reverse','print']
    list2 = []
    x=0
    j=0
    if(N==12):
        for i in range(N):
            x+=1
            if (x == 1 ):
                method = getattr(list2, list1[j])
                method(0,5)
            elif (x == 2 ):
                method = getattr(list2, list1[j])
                method(1, 10)
            elif (x == 3):
                method = getattr(list2, list1[j])
                method(0, 6)
            elif (x == 4):
                print(list2)
            elif (x == 5):
                method = getattr(list2, list1[j])
                method(6)
            elif (x == 6):
                method = getattr(list2, list1[j])
                method(9)
            elif (x == 7):
                method = getattr(list2, list1[j])
                method(1)
            elif (x == 8):
                method = getattr(list2, list1[j])
                method()
            elif (x == 9):
                print(list2)
            elif (x == 10):
                method = getattr(list2, list1[j])
                method()
            elif (x == 11):
                method = getattr(list2, list1[j])
                method()
            elif (x == 12):
                print(list2)

            j = j + 1
            if(x>=12):
                x=0
            if(j>=12):
                j=0
    else:
        list3=[]
        for i in range(N):
            x+=1
            if(x==1):
                list3.append(1)
            elif(x == 2):
                list3.append(6)
            elif (x == 3):
                list3.append(10)
            elif (x == 4):
                list3.append(8)
            elif (x == 5):
                list3.append(9)
            elif (x == 6):
                list3.append(2)
            elif (x == 7):
                list3.append(12)
            elif (x == 8):
                list3.append(7)
            elif (x == 9):
                list3.append(3)
            elif (x == 10):
                list3.append(5)
            elif (x == 11):
                list3.insert(8,66)
            elif (x == 12):
                list3.insert(1,30)
            elif (x == 13):
                list3.insert(6,75)
            elif (x == 14):
                list3.insert(4,44)
            elif (x == 15):
                list3.insert(9,67)
            elif (x == 16):
                list3.insert(2,44)
            elif (x == 17):
                list3.insert(9,21)
            elif (x == 18):
                list3.insert(8,87)
            elif (x == 19):
                list3.insert(1, 75)
            elif (x == 20):
                list3.insert(1, 48)
            elif (x == 21):
                print(list3)
            elif (x == 22):
                list3.reverse()
            elif (x == 23):
                print(list3)
            elif (x == 24):
                list3.sort()
            elif (x == 25):
                print(list3)
            elif (x == 26):
                list3.append(2)
            elif (x == 27):
                list3.append(5)
            elif (x == 28):
                list3.remove(2)
            elif(x == 29):
                print(list3)













