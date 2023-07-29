import requests
import base64

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import streamlit as st
from PIL import Image


def save_album_image(img_url, track_id):
    r = requests.get(img_url)
    open('img/' + track_id + '.jpg', "wb").write(r.content)
    
def get_album_image(track_id):
    return Image.open('img/' + track_id + '.jpg')