class Solution:
    def isPathCrossing(self, path: str) -> bool:

        points = [(0,0)]
        xcount = 0
        ycount = 0

        for direction in path:

            if direction == "N":
                ycount += 1
                points.append((xcount, ycount))

            elif direction == "S":
                ycount -= 1
                points.append((xcount, ycount))

            elif direction == "E":
                xcount += 1
                points.append((xcount, ycount))

            elif direction == "W":
                xcount -= 1
                points.append((xcount, ycount))

            if len(points) != len(set(points)):
                return True

        return False

        

        