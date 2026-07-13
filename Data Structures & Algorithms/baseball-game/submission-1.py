class Solution:
    def calPoints(self, operations: List[str]) -> int:
        rec = 0
        secondlast = 0
        last = 0
        scores = []

        for op in operations:

            if op == "+":
                amnt = (scores[-1] + scores[-2])
                rec += amnt
                scores.append(amnt)

            elif op == "D":
                amnt = (scores[-1] * 2)
                rec += amnt
                scores.append(amnt)

            elif op == "C":
                rec -= scores[-1]
                scores.pop()

            else: 
                rec += int(op)
                scores.append(int(op))

        return rec



        