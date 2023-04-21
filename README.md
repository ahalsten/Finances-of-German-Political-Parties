# Finances of German Political Parties
 Sponsoring and Donations
 
https://github.com/ahalsten/Finances-of-German-Political-Parties.git

Use data on sponsorship activities from 2019 through 2022, voluntarily provided by the German parties SPD and the Greens, to analyze the networks between sponsors and parties. Allows the user to view a plot, look at the firms that sponsored both parties, learn the total amount of sponsorships throughout these years, and find the firms that sponsored most consistently. 

How to interact with the program:
- Download the json file: mydata.json
- Download the three html files: commonsponsors.html, topsponsors.html, total.html
- Run program_sponsors_ahalsten.py
- Use browser to navigate to the following URL: http://localhost:5000/
- Optional, add graph.png, commonsponsors, total, or topsponsors

Required Python packages for the project to work:
- pandas
- thefuzz (consider installing thefuzz[speedup])
- networkx
- json
- flask_caching
- matplotlib
- matplotlib.pyplot
- flask
- io 
