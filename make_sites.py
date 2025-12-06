import os, pandas as pd

courses = pd.read_csv('courses_spring.csv')
courses = courses.dropna()

for index, row in courses.iterrows():
    number = row['number']
    title = row['title']

    page = \
    f"""--- 
title: math{number}
last-modified: 2025-12-05 
tags: 
course: MATH {number}
---

#  {title} (MATH{number})

## Official Course Description

(blank)

### Unofficial Description (Student Feedback)

(blank) 

## Official Prerequisites

(blank)

#### Notes on Enrolling

(blank)

## Degree Requirements Fulfilled

This course satisfies a core requirement or an elective requirement* for the following programs:

Mathematics, BS

Mathematics and Computer Science, BS

Mathematics Minor

## General Advice

(blank)

## General Postrequisites

(blank)

## Resources

(blank)

## Honors

(blank)

### Recent Professors

(blank)"""

    # write page to file math{number}.md
    # if file already exists, skip
    if os.path.exists(f'content/classes/math{number}.md'):
        continue
    else:
        with open(f'content/classes/math{number}.md', 'w') as f:
            f.write(page)