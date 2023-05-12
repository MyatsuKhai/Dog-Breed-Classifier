#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Myat Hsu Kai
# DATE CREATED: 20/8/2022                                 
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
from os import listdir
   
def get_pet_labels(image_dir):
    file = listdir(image_dir)
    results_dic = dict()
    for i in range(0,len(file),1):
        name = " "
        if file[i] not in results_dic:
            pet_images = file[i].lower().split("_")
            for word in pet_images:
                if word.isalpha():
                    name += word + " "
            results_dic[file[i]] = [name.strip()]
        else:
            print("Warning!!")
    return results_dic 