import cv2 as cv
import numpy as np
import os
from PIL import Image


# img = cv.imread('captcha_samples/captcha_0.jpeg',0)
# line = cv.imread('line.jpeg',cv.IMREAD_GRAYSCALE)
# thre, line_bw = cv.threshold(line, 128, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)
# inverted_line = cv.bitwise_not(line)

# captcha = cv.absdiff(img, inverted_line)
# kernel = np.ones((4,1),np.uint8)
# erosion = cv.erode(captcha,kernel,iterations = 2)
# resized = cv.resize(erosion, (erosion.shape[1], 100))
# other_kernel = np.ones((4,1),np.uint8)
# dilated = cv.dilate(resized, other_kernel, iterations=2)
# # kernel = np.ones((7,5),np.float32)/25
# # dst = cv.filter2D(resized,-1,kernel)
# dst = cv.medianBlur(dilated, 5)
# cv.imwrite("mystery.jpg", dst)


# import requests
# from bs4 import BeautifulSoup as soup
# s = requests.Session()
# line = cv.imread('line.jpeg',0)
# inverted_line = cv.bitwise_not(line)
#
#
# def generate_and_save_captcha(index):
#     r = s.get("http://searchpan.in/search-pan-details-pan-no/")
#     my_soup = soup(r.text, "html.parser")
#     my_url = my_soup.find("img", {"id": "captcha_img"})["src"]
#     response = s.get(my_url, stream=True)
#     filename = "captcha_samples/captcha_" + str(index) + ".jpeg"
#     with open(filename,
#               "wb") as f:  # I know that "wb" and "w" do the same thing on mac, this is for universality
#         f.write(response.content)
#     del response
#
#
COL = X = 0
ROW = Y = 1


# def get_pixels(matrix, magic_no):
#     pixels =[]
#     # print(matrix)
#     for ri, row in enumerate(matrix):
#         print(ri, row)
#         for ci, col in enumerate(row):
#             cell = (ci, col)
#             print(ci, col)
#             if matrix[cell[ROW], cell[COL]] == magic_no:
#                 pixels.append(cell)
#     return pixels

def find_black(img):
    black=[]
    pix = img.load()
    # img.show()
    for x in range(img.size[0]):
       for y in range(img.size[1]):
           r, g, b, = pix[x,y]

           if r<128 and g <128 and b <128:
               black.append((x,y))
    return black

# def make_readable(filename):
    # img = cv.imread(filename, cv.IMREAD_GRAYSCALE)
    # (thresh, im_bw) = cv.threshold(img, 128, 255, cv.THRESH_BINARY | cv.THRESH_OTSU)

    # captcha = cv.absdiff(img, inverted_line)
    # kernel = np.ones((4,1),np.uint8)
    # erosion = cv.erode(captcha,kernel,iterations = 2)
    # other_kernel = np.ones((4,1), np.uint8)
    # dilated = cv.dilate(erosion, other_kernel, iterations=2)
    # resized = cv.resize(dilated, (dilated.shape[1], 100))
    # resized = cv.resize(erosion, (erosion.shape[1], 100))
    # name_list = filename.split("_")
    # print(name_list[2])
    # cv.imwrite("readable_captchas/readable_captcha_" + name_list[2], resized)
#

def make_black_white(filename):
    img = Image.open(filename)
    pix = img.load()
    for x in range(img.size[0]):
        for y in range(img.size[1]):
            r, g, b = pix[x, y]
            if r > 100 or g > 100 or b > 100:
                pix[x, y] = (255, 255, 255)
    return img

def make_x_dict(black_array):
    x_dict = dict()
    for pix in black_array:
        if pix[0] not in x_dict:
            x_dict[pix[0]] = [pix[1]]
        else:
            x_dict[pix[0]].append(pix[1])
    for x in x_dict:
        x_dict[x] = (min(x_dict[x]), max(x_dict[x]))
    return x_dict

def remove_line(filename,x_dict):
    captcha = make_black_white(filename)
    pix = captcha.load()
    for x in x_dict:
        if pix[x, x_dict[x][0]-1]>(50,50,50) and pix[x, x_dict[x][1]+1]>(50,50,50):
            for y in range(x_dict[x][0], x_dict[x][1]+1):
                pix[x,y] = (255,255,255)
    name_list = filename.split("_")
    captcha.save("readable_captchas/readable_captcha_" + name_list[2], "jpeg")


line = make_black_white("line.jpeg")
line.show()
blacks = find_black(line)
x_dict = make_x_dict(blacks)

#
if __name__ == '__main__':
    # for i in range(0,30):
    #     generate_and_save_captcha(i)
    for filename in os.listdir("captcha_samples"):
        remove_line("captcha_samples/"+filename, x_dict)
#     print(get_pixels(line_bw, 0))
#
#
#     # print(blacks)
#     # rgb = img.convert("RGB")
#     # for x,y in blacks:
#     #     if pix[x,y+1]>0 and pix[x, y-1]>0:
#     #         pix.putpixel((x,y), 255)
#
#     #     r ,g ,b = pix[pixel[0], pixel[1]]
#     #     if r<128 and g<128 and b<128:
#     #         pix[x,y] = (255)
#



