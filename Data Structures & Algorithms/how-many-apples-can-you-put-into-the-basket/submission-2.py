class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:

        lenweights = len(weight)


        if sum(weight) <= 5000:
            return lenweights

        else:
            weight.sort()
            indx = 0 
            curr = 0
            apples = 0

            while indx < lenweights:
                if curr + weight[indx] > 5000:
                    return apples

                else:
                    curr += weight[indx]
                    apples += 1
                    indx += 1

            return apples

        