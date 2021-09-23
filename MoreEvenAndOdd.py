nums = [None]*10
odds = []
lens = len(nums)
for i in range(lens):
    val = int(input("Enter number: "))
    nums[i] = val
for i in range(lens):
    if (nums[i] % 2 != 0):
        odds.append(nums[i])
oddslen = len(odds)
if (oddslen == 0):
    print("No odd numbers were entered")
    quit()
large = odds[0]
for i in range(oddslen):
    if (odds[i] > large):
        large = odds[i]
print(nums)
print(odds)
print("The largest odd number is: ", large)
