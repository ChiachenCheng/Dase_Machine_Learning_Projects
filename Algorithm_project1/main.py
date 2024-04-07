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
    rates.append(rate)

    # 重建图像
    recon = np.dot(eig_vec, score) + np.mean(image_2d, axis=0)# 归一化可使图像质量更好
    if quzao == True:
        for i in range(len(recon)): # 去除噪点
            for j in range(len(recon[i])):
                if recon[i][j] > 256:
                    recon[i][j] = 255
    recon_img_mat = np.uint8(np.absolute(recon))# 绝对值，离散；成为合法rgb值

    # 计算重构误差
    error = np.linalg.norm(image_2d - recon_img_mat,"fro")
    errors.append(error)

    return recon_img_mat

def PCA(imagepath, newpath, alpha):
    pic = imageio.imread(imagepath)
    pic_np = np.array(pic)
    pic_r = pic_np[:,:,0]
    pic_g = pic_np[:,:,1]
    pic_b = pic_np[:,:,2]

    pic_r_recon = comp_2d(pic_r, alpha)
    pic_g_recon = comp_2d(pic_g, alpha)
    pic_b_recon = comp_2d(pic_b, alpha)

    recon_color_image = np.dstack((pic_r_recon, pic_g_recon, pic_b_recon))
    recon_color_image = Image.fromarray(recon_color_image)
    # recon_color_image.show()
    # imageio.imwrite(newpath, recon_color_image)

if __name__ == "__main__":
    alpha = 0.99
    quzao = False

    rates = []
    errors = []
    for i in range(100):
        imagepath = "images/beach/beach" + str(i).zfill(2) + ".tif"
        newpath = 'newimage/beach/' + str(i).zfill(3) + '.jpg'
        PCA(imagepath, newpath, alpha)
    print(np.array(rates).mean())
    print(np.array(errors).mean())

    rates = []
    errors = []
    for i in range(100):
        imagepath = "images/agricultural/agricultural" + str(i).zfill(2) + ".tif"
        newpath = 'newimage/agricultural/' + str(i).zfill(3) + '.jpg'
        PCA(imagepath, newpath, alpha)
    print(np.array(rates).mean())
    print(np.array(errors).mean())

    rates = []
    errors = []
    for i in range(100):
        imagepath = "images/airplane/airplane" + str(i).zfill(2) + ".tif"
        newpath = 'newimage/airplane/' + str(i).zfill(3) + '.jpg'
        PCA(imagepath, newpath, alpha)
    print(np.array(rates).mean())
    print(np.array(errors).mean())

    print('alpha =',end=' ')
    print(alpha)