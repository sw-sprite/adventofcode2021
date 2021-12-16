# import binascii
with open("input.txt") as f:
    lines = f.read()

lines = lines.strip("\n")
# integer = int(lines, 16)
# spec = '{fill}{align}{width}{type}'.format(fill='0', align='>', width=len(lines)*4, type='b')
# bi_string = format(integer, spec)

p1_sum = 0

def to_binary(ipt):
    integer = int(ipt, 16)
    spec = '{fill}{align}{width}{type}'.format(fill='0', align='>', width=len(ipt)*4, type='b')
    bi_string = format(integer, spec)
    return bi_string

# parse packets, add up version numbers
def calc(bs):
    global p1_sum
    version, type_id, content = bs[0:3], bs[3:6], bs[6:]
    p1_sum += int(version,2)
    print("═══════════════════════════════════════════════════")
    # print("entering calc with: ", bs)
    # print(int(version, 2), type_id, content)

    # a literal
    if type_id == "100": 
        bi_val = ""
        i = 0
        while True:
            cur_window = content[0+i:5+i]
            bi_val += cur_window[1:5]
            if cur_window[0] == '0':
                break
            i += 5
            # print(cur_window)
            print(bi_val, i)

        print("exiting with literal pkg value:", int(bi_val,2))
        print(bs[i+11:])
        # 11 is 6(header), plus 5 which is the window we just read
        return int(bi_val, 2), bs[i+11:] 

    # operator
    else: 
        length_type_id = content[0]
        subpackets = [] 
        if length_type_id == "0":
            length = int(content[1:16],2)
            op_content = content[16:16+length]
            leftover = content[16+length:]
            while op_content:
                # print("cur subpkg length: ", len(op_content), op_content)
                subpackets.append(None)
                subpackets[-1], op_content = calc(op_content)
        if length_type_id == "1":
            num_subpkg = int(content[1:12],2)
            op_content = content[12:] # 1 + 11
            # print(length)
            for _ in range(num_subpkg):
                subpackets.append(None)
                subpackets[-1], op_content = calc(op_content)
            leftover = op_content
        return subpackets, leftover



# calc(to_binary("D2FE28"))
# calc(to_binary("38006F45291200"))
# calc(to_binary("EE00D40C823060"))
# calc(to_binary("8A004A801A8002F478"))
# calc(to_binary("620080001611562C8802118E34"))
# calc(to_binary("C0015000016115A2E0802F182340"))
# calc(to_binary("A0016C880162017C3686B18A3D4780"))

calc(to_binary(lines))
print("pt 1 version sum: ", p1_sum)