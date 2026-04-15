# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 13:11:55 2026

@author: Rouzbeh
"""

projects = []

def add_project(name, planned, actual, status):
    project = {
        "name": name,
        "planned": planned,
        "actual": actual,
        "status": status
    }
    projects.append(project)

def analyze_projects():
    completed = 0
    
    for p in projects:
        diff = p["actual"] - p["planned"]
        
        print("\nProject:", p["name"])
        print("Planned:", p["planned"], "hours")
        print("Actual:", p["actual"], "hours")
        print("Status:", p["status"])
        
        if diff > 0:
            print("Over budget by", diff, "hours")
        else:
            print("Under/On budget by", abs(diff), "hours")
        
        if p["status"].lower() == "completed":
            completed += 1

    print("\nTotal completed projects:", completed)


add_project("Website Design", 10, 12, "Completed")
add_project("Data Analysis", 8, 7, "Completed")
add_project("App Development", 15, 18, "Not completed")

analyze_projects()