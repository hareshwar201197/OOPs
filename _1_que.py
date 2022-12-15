# Read only region start
class UserMainCode(object):
    @classmethod

    def sortstudentmarks(cls,input1,input2,input3):

        ''''
        input1 : int
        input2 : int
        input3 : int[-]
        
        Expected return type : int[]
        '''

        # Read only region end
        # write code here


        average = []
        for i in range (input2):
            plus = 0
            for y in range (input1):
                plus +=input3[y][i]

            average.append(plus)
        value = 10000000000
        for i in average:
            if value > i:
                value = i
        index_min = average.index(value)
        scores = []
        for i in input3:
            i.pop(index_min)

        for i in input3:
            scores.append(sum(i))

        return scores

