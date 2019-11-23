# 导入colormath库
from colormath.color_objects import LabColor
import colormath
from colormath.color_diff import delta_e_cie1994
from colormath.color_diff import delta_e_cie2000
from colormath.color_diff import delta_e_cmc
# 代码二省去Yxy到Lab的转化
L=[87.86741111406972, 87.32443036534754, 85.98144068323823]
a=[-15.999098550928403, -15.177720926246751, -12.766918928785065]
b=[78.51938967753217, 86.37073015942863, 92.96415914568861]

#转化为colormath能读懂的数据
color0=LabColor(lab_l=L[0],lab_a=a[0],lab_b=b[0])  
color1=LabColor(lab_l=L[1],lab_a=a[1],lab_b=b[1])
color2=LabColor(lab_l=L[2],lab_a=a[2],lab_b=b[2])
print("++++++++++++++++++CMC(2:1)色差计算++++++++++++++")
print(colormath.color_diff.delta_e_cmc(color0, color1, pl=2, pc=1))
print(colormath.color_diff.delta_e_cmc(color1, color2, pl=2, pc=1))
print(colormath.color_diff.delta_e_cmc(color0, color2, pl=2, pc=1))
print("++++++++++++++++++++++++++++++++++++++++++++++++",'\n')


print("++++++++++++++CIE94色差计算公式++++++++++++++++++++")
print(colormath.color_diff.delta_e_cie1994(color0, color1, K_L=1, K_C=1, K_H=1, K_1=0.045, K_2=0.015))
print(colormath.color_diff.delta_e_cie1994(color1, color2, K_L=1, K_C=1, K_H=1, K_1=0.045, K_2=0.015))
print(colormath.color_diff.delta_e_cie1994(color0, color2, K_L=1, K_C=1, K_H=1, K_1=0.045, K_2=0.015))
print("+++++++++++++++++++++++++++++++++++++++++++++++++",'\n')

print("++++++++++++++++CIEDE2000色差公式++++++++++++++++++")
print(colormath.color_diff.delta_e_cie2000(color0, color1, Kl=1, Kc=1, Kh=1))
print(colormath.color_diff.delta_e_cie2000(color1, color2, Kl=1, Kc=1, Kh=1))
print(colormath.color_diff.delta_e_cie2000(color0, color2, Kl=1, Kc=1, Kh=1))
print("+++++++++++++++++++++++++++++++++++++++++++++++++")