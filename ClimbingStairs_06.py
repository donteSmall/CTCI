def climbstairs(num_of_staircase):
    can = {}


    def helper(num_of_staircase):

        if num_of_staircase == 1 or num_of_staircase == 2:
            print("Here --->" + str(num_of_staircase))
            return num_of_staircase
        # check to see if it already inside the can
        elif num_of_staircase in can:
                # return that value thats inside can
            print("Return that value thats inside can : " + str(num_of_staircase))

            return can[num_of_staircase]
        else:
            print("Num of staircase input --> "+ str(num_of_staircase))
            can[num_of_staircase]= helper(num_of_staircase - 1) + helper(num_of_staircase - 2)
            return can[num_of_staircase]

    return helper(num_of_staircase)
# Time : O(n)
# Space: O(N)
print(climbstairs(5))
