import imageio
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image

def comp_2d(image_2d, alpha):
    # 样本去中心化
    center = np.mean(image_2d, axis=0)
    cov_mat = image_2d - np.mean(image_2d, axis=0)

    # np.cov计算协方差矩阵
    # np.linalg.eig计算特征值和特征向量
    # 求出的特征值就是有序的
    eig_val, eig_vec = np.linalg.eig(np.cov(cov_mat))

    # 特征值从小到大排序
    idx = np.argsort(eig_val)
    idx = idx[::-1]
    eig_vec = eig_vec[:,idx]
    eig_val = eig_val[idx]

    # 特征值个数选取
    eig_val_sum = np.sum(eig_val)
    p = np.linalg.matrix_rank(image_2d)
    part_eig_val = 0
    for i in range(p):
        part_eig_val = part_eig_val + eig_val[i]
        if part_eig_val > (alpha * eig_val_sum):
            break

    # 选取主特征值的个数
    numpc = i
    eig_vec = eig_vec[:, range(numpc)]

    # 投影到新空间中
    score = np.dot(eig_vec.T,cov_mat)

    # 计算空间占用
    rate = (np.size(eig_vec)+np.size(score)+np.size(center))/np.size(image_2d)
    # print(rate)

    # 重建图像
    recon = np.dot(eig_vec, score) + np.mean(image_2d, axis=0)# 归一化可使图像质量更好
    s = 0
    for i in recon:
        for j in i:
            if j>=256:
                s+=1
                print(j,end=' ')
                print(np.uint8(np.absolute(j)), end=' ')
    print('\n')
    print(s)
    recon_img_mat = np.uint8(np.absolute(recon))# 绝对值，离散；成为合法rgb值
    return recon_img_mat

def PCA(imagepath, newpath, alpha):
    pic = imageio.imread(imagepath)
    pic_np = np.array(pic)
    pic_r = pic_np[:,:,0]
    pic_g = pic_np[:,:,1]
    pic_b = pic_np[:,:,2]

    # np.set_printoptions(threshold=np.inf)
    # print(pic_r)
    # print(pic_g)
    # print(pic_b)

    print('r ceng zao dian')
    pic_r_recon = comp_2d(pic_r, alpha)
    print('g ceng zao dian')
    pic_g_recon = comp_2d(pic_g, alpha)
    print('b ceng zao dian')
    pic_b_recon = comp_2d(pic_b, alpha)

    recon_color_image = np.dstack((pic_r_recon, pic_g_recon, pic_b_recon))
    recon_color_image = Image.fromarray(recon_color_image)
    recon_color_image.show()
    #imageio.imwrite(newpath, recon_color_image)

if __name__ == "__main__":
    alpha = 0.9

    imagepath = "images/beach/beach74.tif"
    newpath = 'newimage/test/001.jpg'
    PCA(imagepath, newpath, alpha)