# HIT137 - Group Assignment 2

## Group Members

- **Aashish** - S385593
- **Xueqin Guo** - S367175
- **Syed Omar Faruk** - S375804
- **Rohan Baniya** - S386847

## Table of Contents

- [Introduction](#introduction)
- [Assignment Questions](#assignment-questions)
    - [Question 1](#question-1)
    - [Question 2](#question-2)
    - [Question 3](#question-3)
- [Contributions](#contributions)
- [Challenges and Solutions](#challenges-and-solutions)
- [Contact](#contact)

## Introduction

This repository contains the code and resources for Group Assignment 2 of the HIT137 course for Semester S 2024 at CAS-DAN35. The project is implemented in Python.

## Assignment Questions

### Question 1

Create a program that reads the text file “raw_text.txt”, encrypts its contents using a simple encryption method, and writes the encrypted text to a new file “encrypted_text.txt”. Then create a function to decrypt the content, and a function to check the correctness of decrypted text.

**Requirements:**
The encryption should take two user inputs (n, m), and follow these rules:
- For lowercase letters:
  - If the letter is in first half of alphabet (a-m): shift forward by n * m
  - If the letter is in second half (n-z): shift backward by n + m
- For uppercase letters:
  - If the letter is in first half (A-M): shift backward by n
  - If the letter is in second half (N-Z): shift forward by m^2
- Special characters, and numbers remain unchanged.

### Question 2

Create a program that analyses temperature data collected from multiple weather stations in Australia. The data is stored in multiple CSV files under a temperatures folder, with each file representing data from one year.
You need to:
- Calculate the average temperatures for each season across all years. Save the result to file “average_temp.txt”.
- Find the station/stations have the largest temperature range. Save the result to file “largest_temp_range_station.txt”.
- Find the warmest and coolest station/stations. Save the result to file “warmest_and_coolest_station.txt”.

### Question 3

Create a program that use recursive function to generates a tree pattern using Python's turtle graphics. The program should take the following parameters from the user:
- Left and right branch angles
- Starting branch length
- Recursion depth
- Branch length reduction factor

**Example:**
The tree with branch left at 20 degrees and right at 25 degrees, starting with a branch length of 100 pixels, and make each new branch 70% long as its parent branch, letting it branch out 5 times.

## Contributions

- **Aashish** - Implemented the encryption and decryption functions for Question 1.
- **Xueqin Guo** - Analyzed and processed temperature data for Question 2.
- **Syed Omar Faruk** - Developed the recursive tree pattern generator for Question 3.
- **Rohan Baniya** - Coordinated the project and integrated the contributions from all members.

## Challenges and Solutions

- **Challenge:** Initially faced issues due to missing modules.
  - **Solution:** Installed Homebrew, pip, and cryptography modules to resolve the errors.

- **Challenge:** Encountered errors in temperature analysis related to file directories.
  - **Solution:** Adjusted the file paths in the code and organized the folders/files in the VS Code explorer.

- **Challenge:** Encountered errors while implementing the recursive tree pattern.
  - **Solution:** Installed the Turtle graphics module on macOS through the terminal in VS Code.

## Contact

For any questions or inquiries, please contact the group members via their GitHub usernames:

- **Aashish** ([digitalaashish](https://github.com/digitalaashish))
- **Xueqin Guo** ([Gussie1130](https://github.com/Gussie1130))
- **Syed Omar Faruk** ([Omar6379](https://github.com/Omar6379))
- **Rohan Baniya** ([rohan9824](https://github.com/rohan9824))
