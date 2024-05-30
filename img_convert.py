#!/usr/bin/env python
# -*- coding:utf-8 -*-
###
# File: /Users/majiefeng/Desktop/FUNSD/img/img_convert.py
# Project: /Users/majiefeng/Desktop/FUNSD/img
# Created Date: 2024-05-30 16:49:38
# Author: JeffreyMa
# -----
# Last Modified: 2024-05-30 16:59:41
# Modified By: JeffreyMa
# -----
# Copyright (c) 2024 USTC
# -----
# HISTORY:
# Date      	By	Comments
# ----------	---	----------------------------------------------------------
###
from PIL import Image

def resize_image(input_image_path, reference_image_path, output_image_path):
    # 打开参考图片，获取其宽度
    with Image.open(reference_image_path) as reference_image:
        reference_width = reference_image.width
        # 获取参考图片的长宽比
        aspect_ratio = reference_image.height / reference_image.width

    # 打开要调整大小的图片
    with Image.open(input_image_path) as image_to_resize:
        # 根据参考图片的宽度设置新宽度
        new_width = int(reference_width*0.6)
        # 根据长宽比计算新高度
        new_height = int(new_width * aspect_ratio)
        
        # 调整图片大小
        resized_image = image_to_resize.resize((new_width, new_height))
        
        # 保存调整大小后的图片
        resized_image.save(output_image_path)

# 使用示例
input_image_path = '/Users/majiefeng/Desktop/FUNSD/img/funsd_logo_sr.png'
reference_image_path = '/Users/majiefeng/Desktop/FUNSD/img/funsd_logo.png'
output_image_path = '/Users/majiefeng/Desktop/FUNSD/img/funsd_logo_sr_s.png'
resize_image(input_image_path, reference_image_path, output_image_path)