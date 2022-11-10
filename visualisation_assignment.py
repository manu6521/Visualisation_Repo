# -*- coding: utf-8 -*-
"""
Created on Thu Nov 10 13:12:35 2022

@author: manuv
"""
import pandas as pd
import matplotlib.pyplot as plt

def read_data():
    """ 
    This function read data from 'org.csv' 
    """
    df = pd.read_csv("org.csv")
    return df;

def payscale_comparison():
    """
    This function plots minimum and maximum payscale of  
    position held by different employees in an organization
    """
    plt.figure()
    pay_min = updated_data["Payscale Minimum "]
    pay_max = updated_data["Payscale Maximum "]
    job = updated_data["Generic Job Title"]
    plt.plot(job[:10],pay_min[:10], marker = 'o',label = "Payscale Minimum ")
    plt.xticks(rotation=90,horizontalalignment="center")
    plt.plot(job[:10],pay_max[:10], marker = 'o',label ="Payscale Maximum ")
    plt.title("MINIMUM AND MAXIMUM PAY SCALE BY JOB TITLE")
    plt.legend()
    plt.xlim(10,-5)
    plt.xlabel("Generic Job Title")
    plt.ylabel("Pay Scale")
    plt.savefig("line.png",bbox_inches="tight")
    plt.show()

def player_stats():
    """
    This function analyse the median , maximum , minimum runs scored by
    the player
    """
    cric_df = pd.read_csv("cric.csv")
    plt.figure()
    plt.boxplot([cric_df["ODI RUNS"]],labels = ["Kohli"])
    plt.title("ODI RUNS SCORED PER YEAR")
    plt.savefig("box.png", bbox_inches="tight")
    plt.show()
     
def payscale_comparison_group():
    """
    This function plots minimum and maximum payscale of  
    different occupational group
    """
    plt.figure()
    prof = updated_data["Professional/Occupational Group"]
    pay_scale = updated_data["Payscale Maximum "]
    plt.bar(prof,pay_scale)
    plt.xticks(rotation=90,horizontalalignment="center")
    plt.legend()
    plt.xlabel("Professional/Occupational Group")
    plt.ylabel("Payscale Maximum ")
    plt.title("PAY SCALE BY PROFESSION")
    plt.savefig("bar.png", bbox_inches="tight")
    plt.show()

data = read_data()
updated_data = data.drop_duplicates(subset = ["Generic Job Title"])

#calling function to visualise line plot
payscale_comparison()

#calling function to visualise box plot
player_stats()

#calling function to visualise bar plot
payscale_comparison_group()
