total_amount = int(input("请输入需要找的零钱总数: "))

# print(type(total_amount))
# 零钱类型假定有: 100; 50; 20; 10; 5; 2; 1


# 10
ten_amount = total_amount // 10
remained_amount = total_amount % 10

# 5
five_amount = remained_amount // 5
remained_amount = remained_amount % 5


# 2
two_amount = remained_amount // 2
remained_amount = remained_amount % 2

# 1
one_amount = remained_amount
print(f'一共需要找{total_amount}元, {ten_amount}张10元纸币, {five_amount}张5元纸币, {two_amount}张2元纸币, {one_amount}张1元纸币')