class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:

        boats = 0
        left = 0
        right = len(people) - 1
        people.sort()

        while right >= left:

            if people[right] > limit or people[right] + people[left] > limit:
                boats += 1
                right -= 1

            else:
                boats += 1
                right -= 1
                left += 1

        return boats



        

        