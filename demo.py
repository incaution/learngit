import math
#sg=float(input('请输入您的身高(米)'))
#tz=float(input('请输入您的体重（公斤）'))
#bmi=tz/(sg**2)
#if bmi <=18.4:
#    print('偏瘦')
#elif bmi>18.5 and bmi<23.9:
#    print('正常')
#elif bmi>24.0 and bmi<27.9:
#    print('过重')
#else:
#    print('肥胖')


H = 1.75
W = 80.5
bmi = W / (H **2)

if bmi <= 18.5:
    print('体重过轻')
elif bmi >= 18.5 and bmi < 28:
    print('体重正常')
elif bmi >= 28 and bmi < 32:
    print('体重过重')
elif bmi > 32:
    print('体重严重肥胖')