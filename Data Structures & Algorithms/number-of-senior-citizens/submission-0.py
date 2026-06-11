class Solution:
    def countSeniors(self, details: List[str]) -> int:


        count = 0 

        for person in details:

            listed = list(person)

            age = listed[11] + listed[12]

            if int(age) > 60:
                count += 1

        return count