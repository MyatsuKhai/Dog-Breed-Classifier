#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/classify_images.py
#                                                                             
# PROGRAMMER: Myat Hsu Kai
# DATE CREATED: 22/8/2022                                
# REVISED DATE: 
# PURPOSE:
from classifier import classifier 
def classify_images(image_dir,results_dic,model):
    for k in results_dic:
        model_label =" "
        file_path = k
        test_image =image_dir + file_path
        model_label +=classifier(test_image,model)
        model_label =model_label.lower().strip()
        val = results_dic[k][0]
        if val in model_label:
            results_dic[k].extend([model_label])
            results_dic[k].extend([1])
        else:
            results_dic[k].extend([model_label])
            results_dic[k].extend([0])
    return results_dic