import re
from PIL import Image, ImageDraw, ImageFont
import random
import time
import pyautogui
from pyautogui import ImageNotFoundException
import shutil
import os

pyautogui.FAILSAFE = True  # 开启鼠标保护模式，防止程序意外退出
# 随机数
sj = random.randint(1, 3)


def find_and_click(image_path, confidence):
    while True:
        try:
            image_location = pyautogui.locateOnScreen(image_path, grayscale=True, confidence=confidence)
            if image_location:
                time.sleep(0.5)
                position = pyautogui.center(image_location)
                pyautogui.click(position)
                break
            else:
                print(f"{image_path} 未找到指定的图片")
        except ImageNotFoundException:
            print(f"{image_path} 图片未找到，程序出现异常")
        time.sleep(sj)


wx = find_and_click('./images/wx.jpg', 0.8)

xcx = find_and_click('./images/xcx.jpg', 0.8)

qf = find_and_click('./images/qf.jpg', 0.8)
time.sleep(1)
qx1 = find_and_click('./images/qx1.jpg', 0.8)

qx = find_and_click('./images/qx.jpg', 0.8)

zhtg = find_and_click('./images/zhtg.jpg', 0.8)

fbht = find_and_click('./images/fbht.jpg', 0.8)

dyxs = find_and_click('./images/dyxs.jpg', 0.8)
time.sleep(1)

ht = find_and_click('./images/ht.jpg', 0.8)
time.sleep(1)
pyautogui.click()

gj = find_and_click('./images/gj.jpg', 0.8)

wztq = find_and_click('./images/wztq.jpg', 0.8)

zt = find_and_click('./images/zt.jpg', 0.8)
time.sleep(0.5)

ztlj = find_and_click('./images/ztlj.jpg', 0.8)

ylwz = find_and_click('./images/ylwz.jpg', 0.8)

# 复制文章
fzwz = find_and_click('./images/fzwz.jpg', 0.8)

qx2 = find_and_click('./images/qx2.jpg', 0.8)

wz = find_and_click('./images/1.jpg', 0.9)
pyautogui.doubleClick()

djwz = find_and_click('./images/djwz.jpg', 0.8)
pyautogui.moveRel(30, None)  # 向右移动30
time.sleep(0.3)
pyautogui.doubleClick()
time.sleep(0.3)
pyautogui.hotkey('ctrl', 'a')
time.sleep(0.3)
pyautogui.hotkey('del')
time.sleep(0.3)

pyautogui.hotkey('ctrl', 'v')

time.sleep(0.5)
pyautogui.click()
time.sleep(0.3)
pyautogui.hotkey('ctrl', 's')

time.sleep(2)

source_file = './1.txt'
destination_file = './fenge/2.txt'

# 先执行复制操作
shutil.copy(source_file, destination_file)

# 打开源文件和目标文件进行内容处理，假设源文件是UTF-8编码
with open(source_file, 'r', encoding='utf-8') as read_file, open(destination_file, 'w', encoding='utf-8') as write_file:
    line_count = 0
    for line in read_file:
        # 对于每行，分割为30字节长度的部分，并在每个部分后添加换行符
        parts = [line[i:i + 30] for i in range(0, len(line), 30)]
        # 将处理过的行写入目标文件
        write_file.write('\n'.join(parts))


def insert_newlines(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f_in:
        lines = f_in.readlines()

    with open(output_file, 'w', encoding='utf-8') as f_out:
        f_out.write('\n' * 3)  # 在文件开始插入3个换行
        line_count = 0
        for line in lines:
            line_count += 1
            f_out.write(line)
            if line_count == 17:  # 每20行插入3个换行
                f_out.write('\n' * 6)
                line_count = 0  # 重置行计数器


def split_file(input_file, output_prefix, max_files=15, lines_per_file=23):
    with open(input_file, 'r', encoding='utf-8') as f_in:
        lines = f_in.readlines()

    total_files = min(max_files, (len(lines) - 1) // lines_per_file + 1)  # 计算最多生成的文件数
    file_count = 1
    lines_written = 0
    output_file = f"{output_prefix}_{file_count}.txt"
    with open(output_file, 'w', encoding='utf-8') as f_out:
        for line in lines:
            f_out.write(line)
            lines_written += 1
            if lines_written == lines_per_file:
                if file_count >= total_files:  # 达到最大文件数后停止
                    break
                lines_written = 0
                file_count += 1
                output_file = f"{output_prefix}_{file_count}.txt"
                f_out.close()
                f_out = open(output_file, 'w', encoding='utf-8')


input_file = "fenge/2.txt"
output_file = "fenge/1.txt"
insert_newlines(input_file, output_file)
os.remove(input_file)
print("插入换行完成！")

input_file1 = "fenge/1.txt"
output_prefix1 = "fenge/output_file"
split_file(input_file1, output_prefix1)

os.remove(input_file1)
print("文件分隔完成！")


def list_dir(path, list_name):  # 传入存储的list
    for file in os.listdir(path):  # os.listdir(path)，路径下的文件及文件夹，不包含子文件和子文件夹
        file_path = os.path.join(path, file)
        if os.path.isdir(file_path):  # 判断是否目录
            list_dir(file_path, list_name)
        else:
            list_name.append(file_path)


class CodeToPicture(object):

    def single_len(self, string):
        '''获取字符串的单字节长度'''
        tab_len = string.count('\t') * 4
        cn_len = len(re.findall(r'[\u4e00-\u9fa5]', string)) * 2  # 中文
        other_len = len(re.findall(r'[^\t\u4e00-\u9fa5]', string))  # 其他
        total_len = tab_len + other_len + cn_len
        return total_len

    def text_to_image(self, txt_file_path, font_path='msyh.ttc', font_size=30, text_color='white', bg_color='black'):
        fontsize = 30  # 字体大小
        row_size = 30  # 文字行距
        column_size = 60  # 行首缩进
        try:
            if self.font_file:
                font = ImageFont.truetype(font=self.font_file, size=fontsize)
            else:
                font = ImageFont.truetype(font='simsun.ttc', size=fontsize)  # 使用宋体，兼容\t
        except Exception as e:
            # 系统字体：黑体simhei.ttf、楷体simkai.ttf、雅黑msyh.ttc、仿宋simfang.ttf，均不兼容\t
            font = ImageFont.truetype(font='simfang.ttf', size=fontsize)  # 系统字体黑体，不兼容\t

        # 读取文本文件内容
        with open(txt_file_path, 'r', encoding='utf-8') as f:
            text = f.read()

        lines = text.split('\n')  # 计算行数
        row_num = len(lines)  # 总共的行数
        line_max = max(lines, key=self.single_len)  # 单字节最大的行
        left, top, right, bottom = font.getbbox(line_max)
        # 计算图片高度
        image_height = (bottom + row_size) * 23  # 图片高度
        image_width = column_size * 2 + right  # column_size*2 + right           # 图片宽度:行首缩进+行尾缩进+tab长度+中文长度
        image_size = (image_width, image_height)  # 图片尺寸

        # 创建一个白色背景的空白图像
        img = Image.new('RGB', size=image_size, color=bg_color)

        # 在图像上创建一个Draw对象
        draw = ImageDraw.Draw(img)

        # 设置要绘制的文本和字体
        font = ImageFont.truetype(font_path, size=font_size)

        # 绘制文本时使用白色字体
        for n, line in enumerate(text.split('\n')):
            draw.text((column_size, (bottom + row_size) * n), line, font=font, fill=text_color)

        # 保存图像到文件并返回文件路径
        output_file_path = txt_file_path.rsplit('.', 1)[0] + '.png'
        img.save(output_file_path)
        print(output_file_path + ':success')
        return output_file_path


def delete_txt_files(directory):
    # 获取目录下所有文件和子目录
    for root, dirs, files in os.walk(directory):
        for file in files:
            # 检查文件是否以'.txt'结尾
            if file.endswith('.txt'):
                file_path = os.path.join(root, file)
                # 删除文件
                os.remove(file_path)
                print(f"已删除文件: {file_path}")


fileList = []
list_dir(r"./fenge", fileList)
ctp = CodeToPicture()
for file in fileList:
    if file.split(".")[-1] == "txt":
        print(file + ":begin")
        ctp.text_to_image(file)

delete_txt_files("./fenge")

file_path = r'D:\soft\py_demo\xiaoshuo\1.txt'

# 打开文件，并将其内容替换为空
with open(file_path, 'w', encoding='utf-8') as file:
    file.truncate(0)

print(f"文件 '{file_path}' 已清空。")
