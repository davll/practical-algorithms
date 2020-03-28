class Solution:
    def arraysIntersection(self, arr1: List[int], arr2: List[int], arr3: List[int]) -> List[int]:
        i, j, k = 0, 0, 0
        a, b, c = map(len, [arr1, arr2, arr3])
        result = []
        while i < a and j < b and k < c:
            if arr1[i] == arr2[j] and arr2[j] == arr3[k]:
                result.append(arr1[i])
                i, j, k = i+1, j+1, k+1
            else:
                x = min(arr1[i], arr2[j], arr3[k])
                if x == arr1[i]:
                    i += 1
                if x == arr2[j]:
                    j += 1
                if x == arr3[k]:
                    k += 1
        return result
