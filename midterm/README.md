# Midterm Spring 2017

Question 1</br>
    Analysis 1: Problem: Find out top 15 domains with highest outgoing traffic.</br>
        Steps:</br>
        1. Scan through sent box of every user and pick up the recipients of those emails.</br>
        2. Filter the domain names after '@' in the recipient's email address and add the count corresponding to it</br>
        3. Sort the data and picked up the top 15 from them.</br>
        4. Save the data into a csv file.[Here is Analysis1.csv](https://github.com/mahajanankit/mahajan_ankit/blob/master/midterm/Question%201/Analysis%201.csv)</br>
        5. Plot the graph of domain against frequency.
        6. In this graph we get to see top 15 domains which recieved emails from given set of enron users.</br>
        [Please find the graph plot here.](https://github.com/mahajanankit/mahajan_ankit/blob/master/midterm/Question%201/Analysis%201.jpg)</br>
    
    Analysis 2: Problem: Find out distribution of mail-traffic over time.</br>
        Steps:</br>
        1. Scan through each of the emails and pick up the date of it.</br>
        2. Extract the month and year from the date.</br>
        3. Increment the count for each occurence of the particular month and year combination. </br>
        4. Sort the data based on number of emails and picked up the top 25 from them.</br>
        5. Save the data into a csv file.[Here is Analysis2.csv](https://github.com/mahajanankit/mahajan_ankit/blob/master/midterm/Question%201/Analysis%202.csv)</br>
        6. In the graph we get to see top 25 months where the email traffic was maximum.</br>
        [Please find the graph plot here.](https://github.com/mahajanankit/mahajan_ankit/blob/master/midterm/Question%201/Analysis%202.jpg)</br>

    Analysis 3: Problem: Find out top 25 discussed subjects in all the emails.</br>
        Steps:</br>
        1. Scan through each of the emails and extract the subject of each.</br>
        2. Remove the the stop words and pucntuations.</br>
        3. Filter all the words and select only nouns and verbs out of them. 
        3. Increment the count for each occurence of those words. 
        4. Sort subjects based on number of occurences and pick up the top 25 from them.</br>
        5. Save the data into a csv file.[Here is the Analysis3.csv](https://github.com/mahajanankit/mahajan_ankit/blob/master/midterm/Question%201/Analysis%203.csv)</br>
        6. In the graph we get to see top 25 subjects.</br>
        [Please find the graph plot here.](https://github.com/mahajanankit/mahajan_ankit/blob/master/midterm/Question%201/Analysis%203.jpg)
</br></br></br></br></br></br>



Question 2</br>
    Analysis 1: Problem: Favorite topics over the years. Used ArticleSearch Dataset</br>
        Steps:</br>
        1. Scan through json files representing data of each year.</br>
        2. Extract pucblication date and section of the article.</br>
        3. Create a key-value pair for section-count for every year.</br>
        4. Increment value of a section in the year it was published.
        5. S
        6. Export the data to a csv.[Here is Analysis1.csv](https://github.com/mahajanankit/mahajan_ankit/blob/master/midterm/Question%202/Analysis%201.csv)</br>
        
    
    Analysis 2: Problem: Find out the most interesting news in NYT articles. Used Archive Dataset</br>
        Steps:</br>
        1. Scan through each of the artciles in the json.</br>
        2. Extract title and abstract from it.</br>
        3. Split it into words and remove punctuations.</br> 
        4. Filter for nouns and verbs.
        5. Count the occurences of each word.</br>
        6. Plot the graph of word against frequency.</br>
        [Please find the graph plot here.](https://github.com/mahajanankit/mahajan_ankit/blob/master/midterm/Question%202/Analysis%202.jpg)</br>

    Analysis 3: Problem: Find out the most read topics in NYT articles by the readers. Used Top_Stories Dataset</br>
        Steps:</br>
        1. Scan through each of the artciles in the json.</br>
        2. Extract title and abstract from it.</br>
        3. Split it into words and remove punctuations.</br> 
        4. Filter the data and save only nouns and verbs.
        5. Count the frequency of each word.</br>
        6. Plot the graph of word against frequency.</br>
        [Please find the graph plot here.](https://github.com/mahajanankit/mahajan_ankit/blob/master/midterm/Question%202/Analysis%203.jpg)</br>
