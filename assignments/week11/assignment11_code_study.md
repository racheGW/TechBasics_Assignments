### Assignment 11 "Code Reading Exercise" Weller

1. Where did you find the code and why did you choose it? (Provide the link)

I looked on git hub for a python code that involved organisation. After looking through some of the examples I choose: (https://github.com/rohithasrk/GSoC-Organisation-Scraper.git). Specifically the scrape.py file.


---

2.  What does the program do? What's the general structure of the program? 

After some research I found out that the code is a web scraper, so it searches the GSOC (Google summer of Code) organisations from the 2019 archive. With that you can search for keywords like „machine learning“ or „python“. Based on this it would find matching organisations from the archive and show their name, link and how many times they appeared in th GSOC from 2009-2018. 

General Structure: 

- imports to being in libraries 
- setup to define variables 
- main function() 
    - asks for a keyword,
    - scrapes the gsoc 2019 website,
    - checks each org’s tech tags,
    - prints results if they match your 
- main execution block 
    - calls scrape() if you run the script directly.
 

unknown structure: 
- signal handler
    - exit with ctrl+c 
- helper function: no_of_times 
    - checks how many times an organization has been in gsoc before 2019.
---

3. Function analysis: pick one function and analyze it in detail:

- What does this function do?

This function checks how many times an organization appeared in past GSOC programs
  
- What are the inputs and outputs?

input: org_name (string like "apache software foundation")

output: an integer shows how many .txt files contain this name (1 per year)

- How does it work (step by step)?

After doing some research I analyses how the code works step by step. 

1. starts with a count of 0
2. then it loops through each year 
3. then for each year: 
    - then opens a file like resources/ 2009.txt and reads the list of organisation names (line by line) 
    - check if the chosen organisation is in the list of that year 
    - then if yes it increases the count 
4. if anything goes wrong (like a missing file), it prints the error.
5. then it return the total count found 
---

5.  Takeaways: are there anything you can learn from the code? (How to structure your code, a clean solution for some function you might also need...)

- exit with ctrl+c with signal.signal() 
- storing past data in .txt files 


6. What parts of the code were confusing or difficult at the beginning to understand?

- use of signal_handler(), signal.signal() 
- use of proxies 
- loop for reading the .txt file
- class names 

- Were you able to understand what it is doing after your own research?

After I did some research I was able to understand some of my issues with the code. However I think the code was still to advanced for my skill level to properly analyze. 

---
