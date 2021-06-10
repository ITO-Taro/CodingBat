# WARMUP-1
# 1. The parameter weekday is True if it is a weekday, and the parameter vacation is True if we are on vacation. We sleep in if it is not a weekday or we're on vacation. Return True if we sleep in.
sleepIn = lambda weekday, vacation: True if not weekday or vacation else False
# print(sleepIn(True, True))
# print(sleepIn(False, False))
# print(sleepIn(True, False))
# print(sleepIn(False, True))

# 2. We have two monkeys, a and b, and the parameters a_smile and b_smile indicate if each is smiling. We are in trouble if they are both smiling or if neither of them is smiling. Return True if we are in trouble.
monkey_trouble = lambda a_smile, b_smile: True if a_smile == b_smile else False
# print(monkey_trouble(True, False))
# print(monkey_trouble(True, True))
# print(monkey_trouble(False, False))

# 3. Given two int values, return their sum. Unless the two values are the same, then return double their sum.
sum_double = lambda x, y: (x+y)*2 if x == y else (x+y)
# print(sum_double(3, 3))


# 4. Given an int n, return the absolute difference between n and 21, except return double the absolute difference if n is over 21. 
diff21 = lambda x: int(((x-21)**2)**0.5*2) if x > 21 else int(((x-21)**2)**0.5)
# print(diff21(3), diff21(50))

# 5. We have a loud talking parrot. The "hour" parameter is the current hour time in the range 0..23. We are in trouble if the parrot is talking and the hour is before 7 or after 20. Return True if we are in trouble.
parrot = lambda x, y: True if x == True and y not in range(7, 21) else False
# print(parrot(True, 4), parrot(True, 20), parrot(False, 6))

# 6. Given 2 ints, a and b, return True if one if them is 10 or if their sum is 10.
makes10 = lambda x, y: True if x == 10 or y == 10 or x+y == 10 else False
# print(makes10(5, 5), makes10(1,2), makes10(10, 4))

# 7. Given an int n, return True if it is within 10 of 100 or 200. Note: abs(num) computes the absolute value of a number.
near_hundred = lambda x: True if x in range(90, 111) or x in range(190, 211) else False
# print(near_hundred(98), near_hundred(111), near_hundred(204.89), near_hundred(250), near_hundred(-101))

# 8. Given 2 int values, return True if one is negative and one is positive. Except if the parameter "negative" is True, then return True only if both are negative.
pos_neg = lambda x, y, z: True if (x < 0 and y > 0 and z is False) or (x > 0 and y < 0 and z is False) or (x < 0 and y < 0 and z is True) else False
# print(pos_neg(1, -100, False), pos_neg(1, 1, True), pos_neg(-9, -8, False), pos_neg(-1, -2, True))

# 9. Given a string, return a new string where "not " has been added to the front. However, if the string already begins with "not", return the string unchanged.
def not_string(x):
    if len(x) > 2 and x[0] == "n" and x[1] == "o" and x[2] == "t":
        return x
    else:
        return "not " + x
# print(not_string("noy"), not_string("notton"), not_string("   "), not_string("no"))
# not_string = lambda x: x == x if x[0] is "n" and x[1] is "o" and x[2] is "t"  else ("not" + x) if "not" not in x
# print(not_string(natto)

#  10. Given a non-empty string and an int n, return a new string where the char at index n has been removed. The value of n will be a valid index of a char in the original string (i.e. n will be in the range 0..len(str)-1 inclusive).
def missing_char(x, n):
    x = x.replace(x[n], '')
    return x
# missing_char = lambda x, n: x[:n] + x[n+1:]
# print(missing_char('taro', 1))

#  LIST-1
#  1. Given an array of ints, return True if 6 appears as either the first or last element in the array. The array will be length 1 or more.
first_last6 = lambda x: True if x[0] == 6 or x[-1] == 6 else False
# print(first_last6([1, 2, 6]), first_last6([6, 0, 12]), first_last6([0, 6, 4]), first_last6([6]))

#  2. Given an array of ints, return True if the array is length 1 or more, and the first element and the last element are equal.
same_first_last = lambda x: True if len(x) > 0 and x[0] == x[-1] else False
# print(same_first_last([1]), same_first_last([1, 2, 3]), same_first_last([3, 4, 5, 3]), same_first_last([0, 0, 0, 0]), same_first_last([]), same_first_last([8]))

#  3. Return an int array length 3 containing the first 3 digits of pi, {3, 1, 4}.
def make_pi(x = [3, 1, 4]):
    return [3, 1, 4]
# print(make_pi())

#  4. Given 2 arrays of ints, a and b, return True if they have the same first element or they have the same last element. Both arrays will be length 1 or more.
common_end = lambda x, y: True if x[0] == y[0] or x[-1] == y[-1] else False
# print(common_end([1,2,3], [1,2,4]), common_end([0,2,3], [1,2,3]), common_end([1,2,3], [1,2,3]), common_end([1,2,3], [0,2,4]),common_end([1], [1,2,2,2,5,3]), common_end([1], [2,2,2,2,5,1]), common_end([1,2,3], [2]))

#  5. Given an array of ints length 3, return the sum of all the elements.
sum3 = lambda x: sum(x) 
# print(sum3([1,2,3]), sum3([1,2,0]), sum3([0,0,0]))

#  6. Given an array of ints length 3, return an array with the elements "rotated left" so {1, 2, 3} yields {2, 3, 1}.
rotate_left3 = lambda x: [x[1], x[2], x[0]]
# def rotate_left3(x):
#    return [x[1], x[2], x[0]]
# print(rotate_left3([1,2,3]), rotate_left3([2,3,1]), rotate_left3([0,0,5]))

#  7. Given an array of ints length 3, return a new array with the elements in reverse order, so {1, 2, 3} becomes {3, 2, 1}.
reverse3 = lambda x: [x[2], x[1], x[0]]
# print(reverse3([1,2,3]))

#  8. Given an array of ints length 3, figure out which is larger, the first or last element in the array, and set all the other elements to be that value. Return the changed array.
max_end3 = lambda x: [x[0]]*3 if x[0] >= x[-1] else [x[-1]]*3
# print(max_end3([1,2,1]), max_end3([10, 0, 0]), max_end3([1,2,5]))

#  9. Given an array of ints, return the sum of the first 2 elements in the array. If the array length is less than 2, just sum up the elements that exist, returning 0 if the array is length 0.
sum2 = lambda x: sum(x[:2])

#  10. Given 2 int arrays, a and b, each length 3, return a new array length 2 containing their middle elements.
middle_way = lambda x, y: [x[1], y[1]]
# print(middle_way([1,2,3], [7,8,9]))

#  11. Given an array of ints, return a new array length 2 containing the first and last elements from the original array. The original array will be length 1 or more.
make_ends = lambda x: [x[0], x[-1]]
# print(make_ends([1,2,3]), make_ends([7,8,9]), make_ends([0,0,0,0,0,5]))

#  12. Given an int array length 2, return True if it contains a 2 or a 3.
has23 = lambda x: True if 2 in x[:2] or 3 in x[:2] else False
# print(has23([2,9]), has23([2,2]), has23([3,8]), has23([9,3]), has23([4,5]))

# LOGIC-1
# 1. When squirrels get together for a party, they like to have cigars. A squirrel party is successful when the number of cigars is between 40 and 60, inclusive. Unless it is the weekend, in which case there is no upper bound on the number of cigars. Return True if the party with the given values is successful, or False otherwise.
cigar_party = lambda x, y: True if (x in range(40, 61) and (y == 0)) or (x >= 40 and (y == 1)) else False
# print(cigar_party(30, False))
def cigar_party(x, y):
    if x in range(40, 61) and (y == 0):
        return True
    elif x >= 40 and (y == 1):
        return True
    else:
        return False

# 2. You and your date are trying to get a table at a restaurant. The parameter "you" is the stylishness of your clothes, in the range 0..10, and "date" is the stylishness of your date's clothes. The result getting the table is encoded as an int value with 0=no, 1=maybe, 2=yes. If either of you is very stylish, 8 or more, then the result is 2 (yes). With the exception that if either of you has style of 2 or less, then the result is 0 (no). Otherwise the result is 1 (maybe).
def date_fashion(x, y):
    if ((x >= 8) and (y > 2)) or ((y >= 8) and (x > 2)):
        return 2
    elif (x < 3) or (y < 3):
        return 0
    else:
        return 1
# print(date_fashion(5,5))
# date_fashion = lambda x, y: 2 if (x >= 8) or (y >= 8) 1 elif (x in range(3, 8) and y in range(3, 8) else 0


#  3. The squirrels in Palo Alto spend most of the day playing. In particular, they play if the temperature is between 60 and 90 (inclusive). Unless it is summer, then the upper limit is 100 instead of 90. Given an int temperature and a boolean is_summer, return True if the squirrels play and False otherwise.
squirrel_play = lambda x, y: True if ((60<= x <= 101) and (y == 1)) or ((60 <= x <= 91) and (y == 0)) else False
# alternatively lambda x, y: True if (x in range(60, 101) and y == 1) or (x in range(60, 91) and y == 0) else False

#  4. You are driving a little too fast, and a police officer stops you. Write code to compute the result, encoded as an int value: 0=no ticket, 1=small ticket, 2=big ticket. If speed is 60 or less, the result is 0. If speed is between 61 and 80 inclusive, the result is 1. If speed is 81 or more, the result is 2. Unless it is your birthday -- on that day, your speed can be 5 higher in all cases.
def caught_speeding(x, y):
    if (x <= 60 and (y == 0)) or (x <= 65 and (y == 1)):
        return 0
    elif (x in range (61, 81) and (y == 0)) or x in range (61, 86) and (y == 1):
        return 1
    elif (x >= 81 and y == 0) or (x >= 86 and y == 1):
        return 2
    else:
        print('Driving too slow?')
# print(caught_speeding(65, 1))

#  5. Given 2 ints, a and b, return their sum. However, sums in the range 10..19 inclusive, are forbidden, so in that case just return 20.
sorta_sum = lambda x, y: 20 if (10<=(x+y)<=19) else (x+y)
# print(sorta_sum(7, 8), sorta_sum(5, 4))

#  6. Given a day of the week encoded as 0=Sun, 1=Mon, 2=Tue, ...6=Sat, and a boolean indicating if we are on vacation, return a string of the form "7:00" indicating when the alarm clock should ring. Weekdays, the alarm should be "7:00" and on the weekend it should be "10:00". Unless we are on vacation -- then on weekdays it should be "10:00" and weekends it should be "off".
def alarm_clock(x, y):
    if (1 <= x <= 5) and (y == 0):
        return "7:00"
    elif ((x == 0 or 6) and (y == 0)) or (((1 <= x <= 5)) and (y == 1)):
        return '10:00'
    else:
        return 'off'

#  7. The number 6 is a truly great number. Given two int values, a and b, return True if either one is 6. Or if their sum or difference is 6. Note: the function abs(num) computes the absolute value of a number.
love6 = lambda x, y: True if ((x+y) == 6 or abs(x-y) == 6) or (x == 6 or y == 6) else False

#  8. Given a number n, return True if n is in the range 1..10, inclusive. Unless outside_mode is True, in which case return True if the number is less or equal to 1, or greater or equal to 10.
in1to10 = lambda x, y: True if ((1 <= x <= 10) and (y == 0)) or (((x <= 1) or (x >= 10)) and (y == 1)) else False

#  9. Given a non-negative number "num", return True if num is within 2 of a multiple of 10. Note: (a % b) is the remainder of dividing a by b, so (7 % 5) is 2. See also: Introduction to Mod
near_ten = lambda x: True if ((0<=(x%10)<=2) or (8<=(x%10)<=9)) else False
# print(near_ten(19))

#  LOGIC-2
#  3. Given 3 int values, a b c, return their sum. However, if one of the values is 13 then it does not count towards the sum and values to its right do not count. So for example, if b is 13, then both b and c do not count.
def lucky_sum(x,y,z):
    for n in x, y, z:
        if x == 13:
            return 0
        elif y == 13:
            return x
        elif z == 13:
            return x+y
        else:
            return x+y+z
# print(lucky_sum(1,2,3), lucky_sum(13,6,7), lucky_sum(1,13,4), lucky_sum(1,2,13))

#  4. Given 3 int values, a b c, return their sum. However, if any of the values is a teen -- in the range 13..19 inclusive -- then that value counts as 0, except 15 and 16 do not count as a teens. Write a separate helper "def fix_teen(n):"that takes in an int value and returns that value fixed for the teen rule. In this way, you avoid repeating the teen code 3 times (i.e. "decomposition"). Define the helper below and at the same indent level as the main no_teen_sum().
def fix_teen(n):
    if (n in range(13, 15) or n in range(17,20)):
        n = 0
    return n
def no_teen_sum(x,y,z):
    return fix_teen(x) + fix_teen(y) + fix_teen(z)
    # print(no_teen_sum(15, 13, 18))

# LIST-2
# 1. Return the number of even ints in the given array. Note: the % "mod" operator computes the remainder, e.g. 5 % 2 is 1.
# x = [1,2,3,4,5,6,7,8]
def count_evens(x):
    x1 = []
    for i in x:
        if i % 2 == 0:
            x1.append(i)
    return len(x1)
# print(count_evens(x))

# 2. Given an array length 1 or more of ints, return the difference between the largest and smallest values in the array. Note: the built-in min(v1, v2) and max(v1, v2) functions return the smaller or larger of two values.
 # x1 = [3,7,1,0,12,8,4,5,2,13,2,5]
def big_diff(x):
    x = sorted(x)
    return x[-1]-x[0]
# print(big_diff(x1))

# 3. Return the "centered" average of an array of ints, which we'll say is the mean average of the values, except ignoring the largest and smallest values in the array. If there are multiple copies of the smallest value, ignore just one copy, and likewise for the largest value. Use int division to produce the final average. You may assume that the array is length 3 or more.
def centered_average(x):
    x = sorted(x)
    x.remove(x[0]), x.remove(x[-1])
    x = set(x)
    return int((sum(x)/len(x)))
# print(centered_average(x1))

# 4. Return the sum of the numbers in the array, returning 0 for an empty array. Except the number 13 is very unlucky, so it does not count and numbers that come immediately after a 13 also do not count.
def sum13(x):
    while (13 in x):
        n1 = x.index(13)
        x = (x[:n1] + x[(n1+2):])
    else:
        sum(x)
    return sum(x)
# print(sum13([1,2,2,1]), sum13([1,13,4,5,13,7,7,8]))

# 5. Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and extending to the next 7 (every 6 will be followed by at least one 7). Return 0 for no numbers.
x1 = [4,5,6,1,1,7,8]
x2 = [4,5,6,1,1,7,8,9,6,1,1,7,5,5,5,6,2,7]
x3 = [2,7,6,2,6,2,7]
x4 = [1, 6, 2, 2, 7, 1, 6, 99, 99, 7]
x5 = [4,5,6,1,1,7,8,9,6,1,1,7,5,5,5,6,2,7,5,5,5,6,7,10004,60,0,6,2,7,6,100000000000,2,7,10,3,6,123,456,789,123,456,789,7,1,2,3]
x6 = [4,5,6,1,1,7,8,9,6,1,1,7,5,5,5,6,2,7,6,5,8,6,1,2,3,7,6,7]
x7 = [6, 8, 1, 6, 7]
x8 = []
x9 = [6,7,11]
x10 = [11,6,7,11]
x11 = [2,2,6,7,7]
def sum67(x):
    while (6 in x) and (7 in x):
        n1 = x.index(6)
        n2 = x.index(7)
        if n1 < n2:
            x = (x[:n1] + x[(n2+1):])
        elif n1 > n2:
            x0 = (x[:(n2+1)])
            x = (x[n1:])
            n2 = x.index(7)
            x = (x0 + x[(n2+1):])
        else:
            return sum(x)
        return sum(x)
# print(sum67(x1), sum67(x2), sum(x3), sum67(x4), sum67(x5), sum67(x6), sum67(x7), sum67(x8),sum67(x9),sum67(x10),sum67(x11))

# 6. Given an array of ints, return True if the array contains a 2 next to a 2 somewhere.
def has22(x):
    if (2 in x):
        n = x.index(2)
        if ((n < (len(x)-1)) and ((x[n+1]) == 2)):
            return True
        while (2 in x[(n+1):]):
            x = x[(n+1):]
            n = x.index(2)
            if ((n < (len(x)-1)) and ((x[n+1]) == 2)):
                return True
        else:
            return False
    else:
        return False
# print(has22([]), has22([1,2,2]), has22([1,2,1]), has22([5,2,2,3]), has22([0,0,0]), has22([1,1,2]), has22([1,2,1,2]), has22([2,2,0]), has22([4, 2, 4, 2, 2, 5]), has22([5, 2, 5, 2]), has22([1,2,1,1,1,1,2,1,1,1,2,2]))

# LOGIC-2
# 1. We want to make a row of bricks that is goal inches long. We have a number of small bricks (1 inch each) and big bricks (5 inches each). Return True if it is possible to make the goal by choosing from the given bricks. This is a little harder than it looks and can be done without any loops.
def make_bricks(x,y,z):
    n = y * 5
    if (x == 0 and z == n) or (y == 0 and x >= z):
        return True
    elif ((x > 0) and (y > 0)):
        if ((z == x) or (z == n)):
            return True
        elif (z > n) and ((z-n) <= x):
            return True 
        elif (z < n) and ((z%5) <= x):
            return True
        else:
            return False
    elif (x == 0):
        if ((z%5 == 0) and (n > z)):
            return True
    else:
        return False
# print((1),make_bricks(3,1,8))
# print((2),make_bricks(3,1,9)) 
# print((3),make_bricks(3,2,10))
# print((4),make_bricks(3,2,8))
# print((5),make_bricks(3,2,9)) 
# print((6),make_bricks(6,1,11))
# print((7),make_bricks(1,4,11))
# print((8),make_bricks(0,3,10))
# print((9),make_bricks(1,4,12)) 
# print((10),make_bricks(3,1,7))
# print((11),make_bricks(1,1,7)) 
# print((12),make_bricks(2,1,7))
# print((13),make_bricks(7,1,11))
# print((14),make_bricks(7,1,8))
# print((15),make_bricks(7,1,13)) 
# print((16),make_bricks(43,1,46))
# print((17),make_bricks(40,1,46)) 
# print((18),make_bricks(40,2,47))
# print((19),make_bricks(40,2,50))
# print((20),make_bricks(40,2,52)) 
# print((21),make_bricks(22,2,33))
# print((22),make_bricks(0,2,10))
# print((23),make_bricks(1000000, 1000, 1000100))
# print((24),make_bricks(2, 1000000, 100003)) 
# print((25),make_bricks(20,0,19))
# print((26),make_bricks(20,0,21))
# print((27),make_bricks(20,4,51)) 
# print((28),make_bricks(20,4,39))

# 2. Given 3 int values, a b c, return their sum. However, if one of the values is the same as another of the values, it does not count towards the sum.
def lone_sum(w,x,y):
    if w == x == y:
        return 0
    elif w == x:
        w == 0 and x == 0
        return y
    elif w == y:
        w == 0 and y == 0
        return x
    elif x == y:
        x == 0 and y == 0
        return w
    else:
        return w+x+y
# print(lone_sum(1,2,3))

# 3. For this problem, we'll round an int value up to the next multiple of 10 if its rightmost digit is 5 or more, so 15 rounds up to 20. Alternately, round down to the previous multiple of 10 if its rightmost digit is less than 5, so 12 rounds down to 10. Given 3 ints, a b c, return the sum of their rounded values. To avoid code repetition, write a separate helper "def round10(num):" and call it 3 times. Write the helper entirely below and at the same indent level as round_sum().
'''
import math
def round_sum(x,y,z):
    x = math.ceil((x-5)/10)*10
    y = math.ceil((y-5)/10)*10
    z = math.ceil((z-5)/10)*10
    return (x+y+z)
'''
# def round_sum(x,y,z):
#     x = (round(float(x)/10))*10
#     y = (round(float(y)/10))*10
#     z = (round(float(z)/10))*10
#     return (x+y+z)

def round_sum(x,y,z):
    def round10(n):
        return (round(float(n)/10))*10
    x = round10(x)
    y = round10(y)
    z = round10(z)
    return (x+y+z)
# print(round_sum(2,3,4))

# 4. Given three ints, a b c, return True if one of b or c is "close" (differing from a by at most 1), while the other is "far", differing from both other values by 2 or more. Note: abs(num) computes the absolute value of a number.
def close_far(x,y,z):
    if y in range((x-1), (x+2)) or z in range((x-1), (x+2)):
        if abs(y-x) >= 2 and abs(y-z) >= 2:
            return True
        elif abs(z-x) >= 2 and abs(y-z) >= 2:
            return True
        else:
            return False
    else:
        return False
# print(close_far(1,2,3))

