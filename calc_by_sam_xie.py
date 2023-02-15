import sys

def s_express_calc(expression_str):

    # convert the string into a list. the conversion follows the fashion "(123)" -> ["(", "123", ")"]
    def compiler(input_string):

        compiled_list = []
        limit = len(input_string)
        counter = 0
        number_container = []

        while counter < limit:

            current_elem = input_string[counter]

            # for "impressing" purpose only
            # validating user inputs
            # allowed_characters = ["(", "m", "u", "l", "t", "i", "p", "l", "y", " ", "a", "d", "d", ")"]
            # if current_elem not in allowed_character and current_elem.isnumeric() == False:
            #       return [-1]

            if current_elem != " ":

                if current_elem == "a":
                    counter = counter + len("add")
                    compiled_list.append("+")
                    continue

                elif current_elem == "m":
                    counter = counter + len("multiply")
                    compiled_list.append("*")
                    continue

                elif current_elem == "e":
                    counter = counter + len("exponent")
                    compiled_list.append("e")

                else:
                    if current_elem.isnumeric() is True:
                        number_container.append(current_elem)

                    else:
                        if len(number_container) > 0:
                            num_elem = "".join(number_container)
                            compiled_list.append(num_elem)
                            #reset number container
                            number_container = []

                        compiled_list.append(current_elem)

                    counter = counter + 1

            else:
                if len(number_container) != 0:
                    num_elem = "".join(number_container)
                    compiled_list.append(num_elem)
                    #reset number container
                    number_container = []

                counter = counter + 1

        if len(number_container) != 0:
            num_elem = "".join(number_container)
            compiled_list.append(num_elem)    

        return compiled_list

    #create a calc function that computes a lowest level expression, aka one pair of (), instead of (())
    def parenthesis_calc(arr):
        '''
        returns a number string
        sign is either * or +
        arr has the numbers after sign
        '''

        sign = arr[-1]
        arr = arr[:-1]

        if sign == "+":
            total = 0
            for i in arr:
                total = total + int(i)
            return str(total) 

        elif sign == "*":
            total = 1
            for i in arr:
                total = total * int(i)
            return str(total)

        # for "impressing" purpose only
        # with the ability to compute exponents
        else:
            total = int(arr[1]) ** int(arr[0])
            return str(total)

    # create a traverse through the compiled list
    def traversal(arr):

        counter = 0
        limit = len(arr)
        tracker = []

        while counter < limit:
            current_elem = arr[counter]
            collector = []
            # start the trimming and put the trimmed element into the collector
            if current_elem == ")":
                trim_counter = len(tracker) - 1
                while tracker[trim_counter] != "(":
                    trimmed = tracker.pop()
                    collector.append(trimmed)
                    trim_counter = trim_counter - 1
                
                # compute the collector array and assign
                new_num = parenthesis_calc(collector)
                # tracker[trim_counter] = the computed result #replace the '(' in tracker replace with the computed result
                tracker[trim_counter] = str(new_num)

            else:
                tracker.append(current_elem)

            counter = counter + 1

        return tracker

    compiled_s = compiler(expression_str)

    # for "impressing" purpose only
    # if compiled_s returns [-1], means input error detected
    #       return "wrong input"

    result = traversal(compiled_s)
    return int(result[0])

s_expression = sys.argv[1]
ans =  s_express_calc(s_expression)
print(ans)
