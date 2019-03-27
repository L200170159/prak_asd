def binSe(list, target):

    low = 0

    high = len(list) - 1

    while(low<=high):

        mid = (low+high)//2

        if(list[mid] == target):

            return "target di index "+str(mid)

        elif(target<list[mid]):

            high = mid - 1

        else:

            low = mid +1

    return "target tidak ditemukan di index berapapun"
