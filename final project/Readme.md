# Final Project Spring 2017

## Data used:
1 - IRS Tax data from 2008-2014
2 - NYT articles

## Instructions to download data
Get the data from the following link - https://www.irs.gov/uac/soi-tax-stats-individual-income-tax-statistics-zip-code-data-soi
get the data for 2009-2014. thefiles would be aggregation files from the link.
Please place the downloaded files in: </br>root/final projet/data/raw data/IRS/


Analysis 1: Problem: Growth of percapita income of states.</br>
    Steps:</br>
    1. Retrieved prepocessed data and filtered it according to user input.</br>
    2. Calculating the total number of tax claims and amoount claimed for each state in a particular year</br>
    3. Calculaing per-capital income based on taxes filed ad number of dependents they carry.</br>
    4. Save the data into a csv file.</br>
    [Here is Analysis1.csv](https://github.com/mahajanankit/mahajan_ankit/blob/master/final%20project/analysis/Analysis1%20output/percapita.csv)</br>
    5. Plot the graph of percapita vs year.
    6. In this graph we get to see different slopes of lines which indicate the rate of growth in the particular state.</br>
    Please find the graph plot here.
	<img src="https://github.com/mahajanankit/mahajan_ankit/blob/master/final%20project/analysis/Analysis1%20output/graph.png"></br>

	
Analysis 2: Problem: Analyzing growth of investment in 2014.
    Steps:</br>
    1. Retrieved prepocessed data and filtered it according to user input.</br>
    2. Grouped data for every state, zipcode and year and aggregated it.</br>
    3. Calculated Investment for every zipcode. </br>
    4. Filtered data to choose the areas where there was a rise in investment.</br>
    5. Plotted a graph to show difference in investment .</br>
    Here is the graph
	<img src="https://github.com/mahajanankit/mahajan_ankit/blob/master/final%20project/analysis/Analysis2%20output/year_wise_graph.png"></br>
    6. Plotted a zipcode specific rise in investment graph which has a regression line to indicate average growth. Thie area of lighter shade indicates growth.</br>
    [Please find the graph plot here.
	<img src="https://github.com/mahajanankit/mahajan_ankit/blob/master/final%20project/analysis/Analysis2%20output/growth_graph.png"></br>

	
Analysis 3: Find out the most inflencing topics on average income using NYT articles. Used entire Archive Dataset.</br>
    Steps:</br>
    1. Retrieved prepocessed data and filtered it according to user input</br>
    2. Caulated the change in average income of people.</br>
    3. Used NYT api to extract data and filter all the words and select only nouns and verbs out of them. </br>
    4. Increment the count for each occurence of those words. </br>
    5. Sort subjects based on number of occurences. These are the words which have a good relation to the change in america's economy.</br>
    6. Save the data into a csv file.</br>
	[Here is the csv](https://github.com/mahajanankit/mahajan_ankit/blob/master/final%20project/analysis/Analysis3%20output/reason%20analysis.csv)</br>
    7. In the graph we get to see change in US economy.</br>
    Please find the graph plot here.
	<img src="https://github.com/mahajanankit/mahajan_ankit/blob/master/final%20project/analysis/Analysis3%20output/graph.png"></br></br></br></br></br></br>

    
Analysis 4: Problem: Analyzing the wealth of people from different classes of economy.</br>
    Steps:</br>
    1. Retrieved prepocessed data.</br>
    2. Grouped data according to different classes in it.</br>
    3. Split it according to years.</br> 
    4. Plotted a graph of average income against time.</br>
    5. This graph helps us to understand that there has been a litlle chnge in all the income classes except for the top class. The class shows great variation.</br>
    6. Plot the graph of word against frequency.</br>
    Please find the graph plot here.
	<img src="https://github.com/mahajanankit/mahajan_ankit/blob/master/final%20project/analysis/Analysis4%20output/graph.png"></br>

	
Analysis 5: Problem: Unemployment analyzation.</br>
    Steps:</br>
    1. Retrieved prepocessed data and filtered it according to user input.</br>
    2. Calulated the unemployment every zip code.</br>
    3. Mapped the unemployement to the county using zipcodes.</br> 
    4. Plotted a geo-map to display unemployment in every county of the state.
    Please find the graph plot here.
	<img src="https://github.com/mahajanankit/mahajan_ankit/blob/master/final%20project/analysis/Analysis5%20output/map.png"></br>