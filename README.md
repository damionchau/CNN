Overview:
This documentation provides instructions for setting up and running a Convolutional Neural Network (CNN) baseline for image classification. It also includes information on utilizing the OpenAI API for a 
Python example app and running the Happy Garden game with Pygame.

CNN Baseline:
format this to professional documenation format:

CNN Training and Challenge Test-------------------------------------------------------------------------------------------------------------------------------------------------

This code contains various modules and programs needed to set up in order to validate and run the programs

Convolutional Neural Network Baseline

You must run the Basline code in order to initially train your AI model through a series of images on the internet

You must adjust the epoch value, sample size and learning rate in order to increase the accuracy of the CNN in reading specific images.

Once the CNN Baseline test is finished, the program will then generate a .h5 file which will then be used tested through

Once your .h5 file has been generated after the CNN you will call it in the test images py file you will need to import the following


import tensorflow as tf
import matplotlib.pyplot as plt
import pathlib
import certifi

from tensorflow.keras.preprocessing.image import load_img
from tensorflow.keras.preprocessing.image import img_to_array
from tensorflow.keras.models import load_model

Once that is done, you can copy image address links and place it into the URL tab for the CNN to examine and determine under the different class names.



OpenAI API Quickstart - Python Example App
This is an example pet name generator app used in the OpenAI API quickstart tutorial. It utilizes the Flask web framework. Follow the steps below to set it up:

you will need to execute the following 

$ python -m venv venv
$ . venv/bin/activate
$ pip install -r requirements.txt
$ cp .env.example .env
$ flask run

For the ChatGPT Loop  Query, 

you will need to import the following:

import os
import openai #remember to pip install pandas openai
from dotenv import load_dotenv  #remember to pip install python-dotenv
load_dotenv()

then you will be able to run an OpenAI engine within the consoile and you can change different variables

From there you are allowed to change the AI engine as well as different variables such as prompts, N values and temperature values
You can also modify the prompt to adhere to a specific condition

For happy garden you will need to import the following to run pygame 



import pgzrun
import pygame
import pgzero
from random import randint
from pgzero.builtins import Actor
import time


The objective of this game is to water the flowers before they wilter and turn into fangflowers and attack your gardenthe garden.