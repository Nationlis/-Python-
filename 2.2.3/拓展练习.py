age=float(input('请输入age='))
HRrest=float(input('请输入HRrest='))
EHR=float(input('请输入EHR=')) #输入运动后的心率
gender=input("请输入male or female :")
if gender=='male':
  n=220
else:
  n=210
low=(n-age-HRrest)*0.6+HRrest
high=(n-age-HRrest)*0.8+HRrest

