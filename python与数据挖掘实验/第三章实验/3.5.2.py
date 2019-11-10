# 递归求斐波那契数列第n项
# f(n) = f(n-1)+f(n-2)
# 😄是真的慢
def f(n):
    if n<=2:
        return 1
    else:
        return f(n-1)+f(n-2)

print(f(10))