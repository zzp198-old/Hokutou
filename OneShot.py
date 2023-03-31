from sympy import *

CD = Symbol('CD')

result = solve(0.159 * CD + 0.03 * CD * 1.77 - 100, [CD])
print('不计算克制,猫球加成3%的情况下一刀秒所需爆伤:', result)

result = solve((0.159 * CD + 0.03 * CD * 1.77) * 1.1 - 100, [CD])
print('计算克制,猫球加成3%的情况下一刀秒所需爆伤:', result)

result = solve(0.159 * CD + 0.03 * CD * 1.77 - 50, [CD])
print('不计算克制,猫球加成3%的情况下一刀半血所需爆伤:', result)

result = solve((0.159 * CD + 0.03 * CD * 1.77) * 1.1 - 50, [CD])
print('计算克制,猫球加成3%的情况下一刀半血所需爆伤:', result)

result = solve((0.159 * CD + 0.03 * CD * 1.77) * 1.15 - 100, [CD])
print('不计算克制,挂标记,猫球加成3%的情况下一刀秒杀所需爆伤:', result)

result = solve((0.159 * CD + 0.03 * CD * 1.77) * 1.1 * 1.15 - 100, [CD])
print('计算克制,挂标记,猫球加成3%的情况下一刀秒杀所需爆伤:', result)
