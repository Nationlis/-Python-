"""
代码参考如下：
男性最适宜运动心率=（220-年龄-安静心率） X （60%~80%）+安静心率

女性最适宜运动心率=（210-年龄-安静心率） X （60%~80%）+安静心率
"""

age=float(input('请输入age='))
HRrest=float(input('请输入HRrest='))
gender=input("请输入male or female :")
if gender=="male":
    n=220
  
else:
    n=210
  
low=(n-age-HRrest)*0.6+HRrest
high=(n-age-HRrest)*0.8+HRrest
print('最适宜的心率是：',low,'~',high)
input("运行完毕，请按回车键退出...")

