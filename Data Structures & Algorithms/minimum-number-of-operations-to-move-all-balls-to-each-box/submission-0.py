class Solution:
    def minOperations(self, boxes: str) -> List[int]:


        ret = []
        lboxes = len(boxes)

        for indx in range(0, lboxes):

            moves = 0
            for calc in range(0, lboxes):
                if indx != calc and boxes[calc] == '1':
                    moves += abs(indx - calc)

            ret.append(moves)

        return ret




        