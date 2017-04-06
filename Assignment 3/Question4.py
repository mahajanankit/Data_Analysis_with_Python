import nltk
import pandas

#Reading the csv into a dataframe
rpath="C:/Users/Ankit Mahajan/Desktop/Notes/DataAnalysis4Python_Spring17/Assignments/Assignment 3/data"

#Importing functions from nltk
tokenizer = nltk.tokenize.RegexpTokenizer(r'\w+')
stemmer = nltk.stem.PorterStemmer()

#Reading the csv into a dataframe
fields = ["Awards"]
df = pandas.read_csv(rpath+"/movies_awards.csv", sep=",", usecols=fields).dropna()

#Picking out different award categories in the data
    #tokenizing and splitting strings into words
q = pandas.Series(tokenizer.tokenize(str(df.Awards.str.split()))).unique()
    #removing everything except Proper Nouns
q = [x[0] for x in nltk.pos_tag(q) if x[1] == 'NNP' and not x[0].isdigit()]
    #Finding unique words from all which have a common stem
c = list(pandas.Series(stemmer.stem(x) for x in q).unique())
for i in q:
    if stemmer.stem(i) in c:
        c.remove(stemmer.stem(i))
    else:
        q.remove(i)

#Calculating values for General Category
df['Won_General'] = df.Awards.str.extract('(\d+) win', expand=True)
df['Nominated_General'] = df.Awards.str.extract('(\d+) nomination', expand=True)

#Calculating values for extracted awards categories
for x in q:
    df['Won_'+x] = df.Awards.str.extract(('Won (\d+) '+x), expand=True)
    df['Nomination_'+x]= df.Awards.str.extract(('Nominated for (\d+)'+x), expand=True)

#Deleting columns which don't have any values
for column in df:
    if df[column].isnull().all():
        df.__delitem__(column)

#exporting to a csv
df=df.fillna(0)
df.to_csv("./Output/Question4.csv")

#Displaying a few rows
df.head()