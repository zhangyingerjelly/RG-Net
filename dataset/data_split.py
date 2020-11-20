import pandas as pd
real=[]
imag=[]
label=[]
for i in range(1,11):
    real.append('echo_real_'+str(i)+'.png')
    imag.append('echo_imag_'+str(i)+'.png')
    label.append('label_'+str(i)+'.png')
dic={'real':real,'imag':imag,'label':label}
df=pd.DataFrame(dic)
df.to_csv('E:\\SAR\\exp3_2\\test\\SAR_datasets_info.csv',index=False)








