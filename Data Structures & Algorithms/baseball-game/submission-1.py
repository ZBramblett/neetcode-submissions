class Solution:
    def calPoints(self, operations: List[str]) -> int:
        sums = 0
        record = []
        for i in range(len(operations)):
            if operations[i] == "+":
                x = record.pop()
                y = record.pop()
                z = x + y
                record.append(y)
                record.append(x)
                record.append(z)
            elif operations[i] == "D":
                x = record.pop()
                z = (2 * x)
                record.append(x)
                record.append(z)
            elif operations[i] == "C":
                record.pop()
            else:
                record.append(int(operations[i]))

        for i in range(len(record)):
            sums = sum(record)

        return sums
        