# WAP to return sum of unique elements only from a list.
# set(): No duplicates, no insertioon order, mutable, s = set() 
# s.add() => adds single element, s.update(list, range(5)) => multiple elements to set, s1=s.copy(), s.pop()=> removes random element from set, 
# s.remove(x), s.discard(x), s.clear() => removes all elements, s1=s.union(s2) => returns union of two sets, 
# # s1=s.intersection(s2) => returns intersection of two sets, s1=s.difference(s2) => returns difference of two sets, 
# s1=s.symmetric_difference(s2) => returns symmetric difference of two sets, s1=s.issubset(s2) => checks if s1 is subset of s2, 
# s1=s.issuperset(s2) => checks if s1 is superset of s2, s1=s.isdisjoint(s2) => checks if s1 and s2 are disjoint sets.
# set comprehension: {x for x in iterable if condition}, frozenset() => immutable set,

def sum_of_unique_elements(nums):
    seen_once = set()
    for num in nums:
        if num in seen_once:
            seen_once.remove(num)
        else:
            seen_once.add(num)

    return sum(seen_once)

def sum_of_unique_elements_alternative(nums):
    return sum(num for num in set(nums) if nums.count(num) == 1)


# Example usage
nums = [1, 2, 2, 3, 4, 4, 5]
print(sum_of_unique_elements_alternative(nums))  # Output: 9