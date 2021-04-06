# -*- coding: utf-8 -*-
"""
Created on Sat Apr  3 10:40:00 2021

@author: admin
"""

import streamlit as st 
from PIL import Image
import pickle
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import cv2 as cv
from  PIL import Image, ImageOps


html_temp = """
   <div class="" style="background-color:blue;" >
   <div class="clearfix">           
   <div class="col-md-12">
   <center><p style="font-size:40px;color:white;margin-top:10px;">Poornima Institute of Engineering & Technology</p></center> 
   <center><p style="font-size:30px;color:white;margin-top:10px;">Digital Image Processing lab</p></center> 
   </div>
   </div>
   </div>
   """
st.markdown(html_temp,unsafe_allow_html=True)
  
st.title("""
        IMAGE OPERATION
         """
         )
file= st.file_uploader("Please upload image", type=("jpg", "png"))

if file is None:
  st.text("Please upload an Image")
else:
  file_bytes = np.asarray(bytearray(file.read()), dtype=np.uint8)
  image = cv.imdecode(file_bytes, 1)
  st.image(file,caption='Uploaded Image.', use_column_width=True)
  st.text(image.shape)
  
def change_size(image_data):
  
  scale_per = 50
  width = int(image.shape[1]*scale_per / 100)
  height = int(image.shape[0]*scale_per / 100)
  img_res = cv.resize(image,(width,height))
  st.image(img_res,caption='RESIZED IMAGE', use_column_width=True, channels="BGR")
  
  st.text(img_res.shape)
  
  #st.text("original shape:", image.shape)  # outpot on prompt
  #st.text("resized shape", img_res.shape)  # outpot on prompt
  #plt.subplot(121)
  #plt.imshow(image)
  #plt.subplot(122)
  #plt.imshow(img_res)
  
  return 0

def change_size_hr(image_data):
  
  scale_per = 50
  width = int(image.shape[1]*scale_per / 100)
  img_resh = cv.resize(image,(width, image.shape[0]))
  st.image(img_resh,caption='RESIZED HORIZONTALLY IMAGE', use_column_width=True, channels="BGR")
  
  st.text(img_resh.shape)
  
  #st.text("original shape:", image.shape)  # outpot on prompt
  #st.text("resized shape", img_res.shape)  # outpot on prompt
  #plt.subplot(121)
  #plt.imshow(image)
  #plt.subplot(122)
  #plt.imshow(img_res)
  
  return 0
    
def change_size_ver(image_data):
  
  scale_per = 50
  height = int(image.shape[0]*scale_per / 100)
  img_resver = cv.resize(image,(image.shape[1], height))
  st.image(img_resver,caption='RESIZED VERTICALLY IMAGE', use_column_width=True, channels="BGR",output_format="auto")
  
  
  st.text(img_resver.shape)
  
  #st.text("original shape:", image.shape)  # outpot on prompt
  #st.text("resized shape", img_res.shape)  # outpot on prompt
  #plt.subplot(121)
  #plt.imshow(image)
  #plt.subplot(122)
  #plt.imshow(img_res)
  
  return 0
    
if st.button("RESIZE"):
  result=change_size(image)

if st.button("RESIZE-HORIZONTALLY"):
  result=change_size_hr(image)
  
if st.button("RESIZE-VERTICALLY"):
  result=change_size_ver(image)
  
if st.button("About"):
  st.header(" Sandeep Tuli")
  st.subheader("Assistant Professor, Department of Computer Engineering")
html_temp = """
   <div class="" style="background-color:orange;" >
   <div class="clearfix">           
   <div class="col-md-12">
   <center><p style="font-size:20px;color:white;margin-top:10px;">Digital Image processing Experiment</p></center> 
   </div>
   </div>
   </div>
   """
st.markdown(html_temp,unsafe_allow_html=True)
