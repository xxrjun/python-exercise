def bucketsort(data):
    max_score = 100
    bucket = []
    
    for i in range(max_score+1):
        bucket.append(0)
    for score in data:
        bucket[score] = bucket[score] + 1

    index = 0
    for i in range(len(bucket)):
        if bucket[i] != 0:
            for j in range(bucket[i]):
                data[index] = i
                index += 1

data = [89, 34, 78, 67, 100, 66, 79, 92, 96, 96]
print('排序前: {}'.format(data))
bucketsort(data)
print('排序後: {}'.format(data))