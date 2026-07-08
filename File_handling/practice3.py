count = 0
with open("practice3.txt", "r") as f:
    data = f.read()
    print(data)


    # num = ""
    # for i in range(len(data)):
    #     if(data[i] == ","):
    #         print(num)
    #         num = ""
    #     else:
    #         num += data[i]


    nums = data.split(",")
    # print(nums)
    for vol in nums:
        if(int(vol) % 2 == 0):
            count += 1

print(count)