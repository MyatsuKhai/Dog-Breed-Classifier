#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/calculates_results_stats.py
#                                                                             
# PROGRAMMER:
# DATE CREATED:                                  
# REVISED DATE: 
# PURPOSE: 
#from get_input_args import get_input_args
#from classifier import classifier 
#from get_pet_labels import get_pet_labels
#from classify_images import classify_images
#from adjust_results4_isadog import adjust_results4_isadog
#results = get_pet_labels()
#resultss_dic = classify_images(results)
#rint("it is:",resultss_dic)
#dogfile = "/home/workspace/dognames.txt"
#results_dic = adjust_results4_isadog(resultss_dic, dogfile)
#print ("ans:",results_dic)
def calculates_results_stats(results_dic):
    results_stats_dic = {}
    results_stats_dic['n_dogs_img'] = 0
    results_stats_dic['n_match'] = 0
    results_stats_dic['n_correct_dogs'] = 0
    results_stats_dic['n_correct_notdogs'] = 0
    results_stats_dic['n_correct_breed'] = 0 
    for key in results_dic:
        if results_dic[key][2] == 1:
            results_stats_dic['n_match'] += 1
            if results_dic[key][3] == 1:
                results_stats_dic['n_correct_breed'] +=1
        if results_dic[key][3] == 1:
            results_stats_dic['n_dogs_img'] +=1
            if results_dic[key][4] == 1:
               results_stats_dic['n_correct_dogs'] +=1
        else:
            if results_dic[key][4] == 0:
                results_stats_dic['n_correct_notdogs'] +=1
                
    results_stats_dic['n_images'] = len(results_dic)
    results_stats_dic['n_notdogs_img'] = (results_stats_dic['n_images'] - 
                                      results_stats_dic['n_dogs_img'])
    
    results_stats_dic['pct_match'] = (results_stats_dic['n_match'] /
                                                results_stats_dic['n_images'])*100.0
    
    results_stats_dic['pct_correct_dogs'] = (results_stats_dic['n_correct_dogs'] /
                                                results_stats_dic['n_dogs_img'])*100.0
    
    results_stats_dic['pct_correct_breed'] = (results_stats_dic['n_correct_dogs'] /
                                                results_stats_dic['n_match'])*100.0
            
    if results_stats_dic['n_notdogs_img'] > 0:
        results_stats_dic['pct_correct_notdogs'] = (results_stats_dic['n_correct_notdogs'] /
                                                results_stats_dic['n_notdogs_img'])*100.0
    else:
        results_stats_dic['pct_correct_notdogs'] = 0.0
        
    return results_stats_dic
#print(calculates_results_stats(results_dic))
