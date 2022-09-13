## Final Report 

**Extract**
The data was initially in CSV format from Kaggle (COVID 19 Containment measures data). I used Pandas to read directly from the CSV file.  

**Transform**
I grouped by country, city, and keyword to see what appeared most frequently. I then tokenized the keywords to see what came up most frequently. Then I made a frequency distribution of trigrams in the keywords. I used the NTLK package for doing NLP analysis with Python. I wanted to combine similar descriptions, but lacked the time (considering analysis was not a required step). Mostly wanted to practice with Python NLP tools. 

**Load**
I used SqlAlchemy and PsycoPG to push the data to PostgreSQL. I kept the tables very simple, storying the text along with value counts as 5 separate tables (keyword_table, country_table, city_table, keyword_count_table, and trigram_table). 