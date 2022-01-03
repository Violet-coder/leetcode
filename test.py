def string_decode(inputString, rowNumber):
    if not inputString:
        return ""

    result = ""
    n = len(inputString)
    print(n)
    row = rowNumber
    col = n // rowNumber
    print("row", row, "col", col)

    string_metrix = [[""] * col for _ in range(row)]
    for i in range(row):
        for j in range(col):
            string_metrix[i][j] = inputString[i * col + j]

    print("string_metrix", string_metrix)
    x = 0
    y = 0
    next_x = 0
    while x < col and y < row:
        print("x", x, "y", y)
        if string_metrix[y][x] != "_":
            result += string_metrix[y][x]
        else:
            result += " "
        x += 1
        y += 1
        if x >= col or y >= row:
            y = 0
            next_x += 1
            print("next_x", next_x)
            x = next_x

    return result.strip()

input = "I_l____Ve___ait___mo"
rowNumer = 4

# print(string_decode(input, rowNumer))

def decrpt_string(input_string, k):
    result = ""
    for s in input_string:
        if s.isupper():
            # find the distance between "A" and this char
            s_unicode = ord(s)
            s_distance = s_unicode - ord("A")

            # find distance between the converted char and "A"
            shift = k%26
            shifted_s_distance = (s_distance + 26 - k) % 26

            # calculte the unicode for this new char
            shifted_s_unicode = ord("A") + shifted_s_distance

            # convert the unicode to char
            shifted_s = chr(shifted_s_unicode)

            result += shifted_s
        else:
            result += s

    return result

input_string = "BCDE"
print("decrpt_string", decrpt_string(input_string, 2))


def badNumbers(bad_numbers, lower, upper):
    bad_numbers.sort()
    last_good_number = lower
    longest_segment = 0
    current_segment = 0

    for bad_number in bad_numbers:
        if bad_number > upper:
            break
        current_segment = bad_number - last_good_number
        if current_segment > longest_segment:
            longest_segment = current_segment
        last_good_number = bad_number + 1

    current_segment = upper - last_good_number + 1
    if current_segment > longest_segment:
        longest_segment = current_segment

    return longest_segment
bad_numbers = [37,7,22,15,49,60]
print("bad numbers", badNumbers(bad_numbers, 3, 48))


def cntConnections(grid):
    if not grid:
        return 0
    result = 0
    pre_node_cnt = 0

    for i in range(len(grid)):
        cur_node_cnt = 0
        for j in range(len(grid[i])):
            cur_node_cnt += grid[i][j]
        print("cur_node_cnt", cur_node_cnt)
        if cur_node_cnt > 0 and pre_node_cnt > 0:
            result += cur_node_cnt * pre_node_cnt
            print("result", result)
        if cur_node_cnt > 0:
            pre_node_cnt = cur_node_cnt

    return result


def cntConnectionsTest(grid):
    if not grid:
        return 0


    result = 0
    pre_node_cnt = 0

    for i in range(len(grid)):
        cur_node_cnt = 0
        if i > len(grid) - 1:
            return result
        for j in range(len(grid[i])):
            cur_node_cnt += grid[i][j]
            result += grid[i][j] * pre_node_cnt
        if cur_node_cnt > 0:
            pre_node_cnt = cur_node_cnt
    return result
grid = [[1,1,1], [0, 1, 1], [0, 0, 0], [1, 1, 1]]

# print("cntConnectionsTest", cntConnectionsTest(grid))

def maxProfit(profits, k):
    if not profits:
        return 0

    n = len(profits)
    half_n = n // 2
    cur_sum = 0

    for i in range(k):
        cur_sum += profits[i]
        cur_sum += profits[i + half_n]
    max_profit = cur_sum

    for i in range(1, half_n):
        cur_sum -= profits[i - 1] + profits[i + k - 1]
        cur_sum -= profits[i + half_n - 1] + profits[(i + k - 1 + half_n) % n]
        max_profit = max(cur_sum, max_profit)

    return max_profit
profits = [3,-5,]
k = 1
print("maxProfit", maxProfit(profits, k))


def decodeString(s):
    result = [0] * 26
    num = 1
    n = len(s)
    i = n - 1
    while i >= 0:
        cur_char = s[i]
        if cur_char == ")":
            k = i - 1
            num_str = ''
            while k >= 0 and s[k] != "(":
                num_str = s[k] + num_str
                k -= 1
            i = k - 1
            num = int(num_str)
        elif cur_char == "#":
            result[int(s[i - 2] + s[i - 1]) - 1] += num
            print("result #", result)
            num = 1
            i -= 3
        elif cur_char.isdigit():
            result[int(cur_char) - 1] += num
            print("result", result)
            num = 1
            i -= 1
    return result


s = "1226#24#(15)1(27)"
print("decodeString", decodeString(s))