total_amount = int(input("请输入需要找的零钱总数: "))


# 100
hundred_amount = total_amount // 100
remained_amount = total_amount % 100

# 50
fifty_amount = remained_amount // 50
remained_amount = remained_amount % 50

# 20
twenty_amount = remained_amount // 20
remained_amount = remained_amount % 20

# 10
ten_amount = remained_amount // 10
remained_amount = remained_amount % 10

# 5
five_amount = remained_amount // 5
remained_amount = remained_amount % 5


# 2
two_amount = remained_amount // 2
remained_amount = remained_amount % 2

# 1
one_amount = remained_amount
# print(f'一共需要找{total_amount}元, {ten_amount}张10元纸币, {five_amount}张5元纸币, {two_amount}张2元纸币, {one_amount}张1元纸币')
print('一共需要找%d元, %d张100元纸币, %d张50元纸币, %d张20元纸币, %d张10元纸币, %d张5元纸币, %d张2元纸币, %d张1元纸币'
      %(total_amount, hundred_amount, fifty_amount, twenty_amount, ten_amount, five_amount, two_amount, one_amount))