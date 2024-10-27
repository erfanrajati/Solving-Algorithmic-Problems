# General Algorithm: Divide and Conquer
# given array arr of contestants,
# the most prizes given is:
#     the max of:
#         max_prize given by left category + max power of right category
#         max_prize given by right category + max power of left category

def cat_by_cat(arr):
    l = len(arr)
    if l == 2:
        return sum(arr)
    else:
        left_max = cat_by_cat(arr[:l//2]) + max(arr[l//2:])
        right_max = cat_by_cat(arr[l//2:]) + max(arr[:l//2])
        return max(left_max, right_max)
    

def main():
    cont_count = int(input())
    cont_list = [int(c) for c in input().split()]

    print(cat_by_cat(cont_list))

if __name__ == "__main__":
    main()