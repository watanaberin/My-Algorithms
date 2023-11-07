
import random
from typing import List
def quicksort(nums: List[int]) -> List[int]:
    
    if len(nums) <= 1:
        return nums
    pivot = random.choice(nums)
    lt = [v for v in nums if v < pivot]
    eq = [v for v in nums if v == pivot]
    gt = [v for v in nums if v > pivot]

    return quicksort(lt) + eq + quicksort(gt)