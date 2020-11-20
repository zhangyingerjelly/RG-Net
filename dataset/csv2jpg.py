import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import os
from skimage import io, exposure, img_as_uint, img_as_float
'''
label_max=3
path='E:\\SAR\\exp3_2\\test\\label'
files = os.listdir(path)
for file in files:
    case_train=np.loadtxt(os.path.join(path,file),delimiter=',',skiprows=0)
    case=np.array(case_train)
    
    minmax=case/label_max
    #img=Image.fromarray(minmax)
    #plt.imshow(minmax)
    #plt.show()

    name_jpg=(file.split('.'))[0]
    
    dir_name='E:\\SAR\\exp3_2\\test\\label_img'
    if not os.path.isdir(dir_name):
        os.makedirs(dir_name)
    io.use_plugin('matplotlib')
    io.imsave(os.path.join(dir_name,name_jpg+'.png'), minmax)
    #img.convert('L').save(os.path.join(dir_name,name_jpg+'.jpg')) #‘RGB’被拓展成了三通道一样的RGB图像 'L':代表灰度图
    #io.use_plugin('matplotlib')
    #label=io.imread(os.path.join(dir_name,name_jpg+'.jpg'))
    #print(label.shape)
    #print(label[25][25])
    #print(label[25][26])
    #print(label[25][27])
    #print(label[25][28])
    
    
 '''   


abs_max=300
names=['real','imag']
for name in names:
    files = os.listdir(os.path.join('E:\\SAR\\exp3_2\\test',name))
    for file in files:
        case_train=np.loadtxt(os.path.join('E:\\SAR\\exp3_2\\test',name,file),delimiter=',',skiprows=0)
        case=np.array(case_train)
    #数字先做归一化，Minmax方法变化到0-1，这样子才能变成图像灰度。但是存在一个问题：10和5原本说明叠加的次数不同，这样子图像与图像之间的区别就只能靠像素点在图像上范围大小来确定了。
    #多个信息是否能被看成像图像一样的RGB三通道？
        minmax=case/abs_max #(-1,1) 不能直接存储负数，否则imread以后会变成0    
        norm=0.5*minmax+0.5 #(0,1)
        name_jpg=(file.split('.'))[0]
        dir_name=os.path.join('E:\\SAR\\exp3_2\\test',name+'_img')
        if not os.path.isdir(dir_name):
            os.makedirs(dir_name)
        #im.convert('L').save(os.path.join(dir_name,name_jpg+'.jpg')) #‘RGB’被拓展成了三通道一样的RGB图像 'L':代表灰度图
        io.use_plugin('matplotlib')
        io.imsave(os.path.join(dir_name,name_jpg+'.png'), norm)
        print(name_jpg)
        
 
            
   

