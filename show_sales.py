import sys

nums = sys.argv[1:]

with open('bakery.csv', encoding='utf=8') as f:
    if len(nums) == 2:
        start_num = int(nums[0])
        end_num = int(nums[1])
    elif len(nums) == 0:
        start_num = 0
        end_num = sum(1 for line in f)
        f.seek(0)
    elif len(nums) == 1:
        start_num = int(nums[0])
        end_num = sum(1 for line in f)
        f.seek(0)

    for num, line in enumerate(f):
        if start_num <= num + 1 <= end_num:
            print(line.strip())

