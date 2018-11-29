# Wine Reviews by Country
Big Data  
Group 1  
### Developer Names:  
- Sierra King  
- Sirisha Vinukonda  
- Anusha Chowdary kollu  
- Liz Conard   
### Developer Pairs:   
###### Pair 1:   
- Sierra King
- Sirisha Vinukonda  
###### Pair 2:  
- Anusha Chowdary kollu
- Liz Conard  

## Links  
Repository: https://github.com/s523286/Group1MapReduce  
Issue Tracker: https://github.com/s523286/Wine-Reviews-By-Country/issues

## Introductory  
We are doing a project in python to perform MapReduce functions on Wine Reviews. The functions we will be performing are sum, count, minimum, and maximum.

## Data Source
We have taken a dataset of Wine Reviews which has 51MB. The variety of the dataset is structured. The file extension is .csv which means it is an excel file.  The dataset provides information on the country the wine is from, the number of points that the wine was rated, and the price of the wine. 

## Data Source Link
https://www.kaggle.com/zynicide/wine-reviews

## The Challenge
The volume of the data is 51MB.
The variety of the data is structured.
The value of the dataset would be important to those interested in the rating of specific wine, where certain wines are from, and the price of the wine.
The veracity of the data is clear and truthworthy.

## Big Data Questions

##### Sierra King:   
For each country, find the total lowest points.
##### Sirisha Vinukonda:  
For each country, find the total highest points. 
##### Anusha Chowdary Kollu:  
For each country, find the average price for each bottle.
##### Liz Conard:
For each country, find the total sum of points.
 
## Set Up Instructions

#### Below are the steps necessary to work on our big data problem:
- Download the data source from the data source link, provided above.
- Create a folder (within your C drive if applicable) and name that folder your project name.
- That folder will contain 5 additional folders that you will create along with a .gitignore file and a ReadMe.md file.
- One of the folders you will create will be titled "data." You will store your data inside that file.
- The other 4 folders will be titled "avg_price_of_country," "min_price," "max_price," and "sum_of_points."
- In each of the 4 folders, you will have a mapper.py, reducer.py, and another copy of your data.

## Commands to Execute the Mapper and Reducer on Your PC
```DOS
python mapper.py
python sort.py
python reducer.py
```

## Big Data Solutions

### Question 1
- For each country, find the total lowest points.
#### Mapper Input Example
| country | description                                                                                                                                                                                                                                                                                                                                                                     | designation       | points | price | province   | region_1    | region_2 | variety            | winery |
|---------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|--------|-------|------------|-------------|----------|--------------------|--------|
| Spain      | This tremendous 100% varietal wine hails from   Oakville and was aged over three years in oak. Juicy red-cherry fruit and a   compelling hint of caramel greet the palate, framed by elegant, fine tannins   and a subtle minty tone in the background. Balanced and rewarding from start   to finish, it has years ahead of it to develop further nuance. Enjoy   2022â€“2030. | Martha's Vineyard | 87    | 65   | California | Napa Valley | Napa     | Cabernet Sauvignon | Heitz  |
#### Mapper Output or Reducer Input Example
Key: US, Value: 87 (example: Spain, 87)
#### Reducer Ouput Example
Key: US, Value: 78(lowest: 78)
#### Language
Python
#### Kind of Chart
Bar Graph

### Question 2
- For each country, find the total highest points.
#### Mapper Input Example
| country | description                                                                                                                                                                                                                                                                                                                                                                     | designation       | points | price | province   | region_1    | region_2 | variety            | winery |
|---------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|--------|-------|------------|-------------|----------|--------------------|--------|
| Spain      | This tremendous 100% varietal wine hails from   Oakville and was aged over three years in oak. Juicy red-cherry fruit and a   compelling hint of caramel greet the palate, framed by elegant, fine tannins   and a subtle minty tone in the background. Balanced and rewarding from start   to finish, it has years ahead of it to develop further nuance. Enjoy   2022â€“2030. | Martha's Vineyard | 96     | 235   | California | Napa Valley | Napa     | Cabernet Sauvignon | Heitz  |

#### Mapper Output or Reducer Input Example
Key: Spain, Value: 96 (example: US, 96)
#### Reducer Ouput Example
Key: Spain, Value: 96(highest points= 5679)
#### Language
Python
#### Kind of Chart
Bar Graph  

### Question 3
- For each country, find the average price for each bottle.
#### Mapper Input Example
| country | description                                                                                                                                                                                                                                                                                                                                                                     | designation       | points | price | province   | region_1    | region_2 | variety            | winery |
|---------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|--------|-------|------------|-------------|----------|--------------------|--------|
| US      | This tremendous 100% varietal wine hails from   Oakville and was aged over three years in oak. Juicy red-cherry fruit and a   compelling hint of caramel greet the palate, framed by elegant, fine tannins   and a subtle minty tone in the background. Balanced and rewarding from start   to finish, it has years ahead of it to develop further nuance. Enjoy   2022â€“2030. | Martha's Vineyard | 96     | 235   | California | Napa Valley | Napa     | Cabernet Sauvignon | Heitz  |

#### Mapper Output or Reducer Input Example
Key: US, Value: 235 (example: US, 235)
#### Reducer Ouput Example
Key: US, Value: 235(Average: sum=158/count=20)
#### Language
Python
#### Kind of Chart
Bar Graph

### Question 4
- For each country, find the total sum of points.
#### Mapper Input Example
| country | description                                                                                                                                                                                                                                                                                                                                                                     | designation       | points | price | province   | region_1    | region_2 | variety            | winery |
|---------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------|--------|-------|------------|-------------|----------|--------------------|--------|
| US      | This tremendous 100% varietal wine hails from   Oakville and was aged over three years in oak. Juicy red-cherry fruit and a   compelling hint of caramel greet the palate, framed by elegant, fine tannins   and a subtle minty tone in the background. Balanced and rewarding from start   to finish, it has years ahead of it to develop further nuance. Enjoy   2022â€“2030. | Martha's Vineyard | 96     | 235   | California | Napa Valley | Napa     | Cabernet Sauvignon | Heitz  |

#### Mapper Output or Reducer Input Example
Key: US, Value: 96 (example: US, 96)
#### Code for mapper.py
``` python
# Referenced Dr. Case's slides on MapReduce in Python
# mapper.py will map our data, wineData.txt, to key/value pairs

# opens wineData.txt as a read only file
f = open("wineData.txt","r")
# opens o.txt as a file to write to
o = open("o.txt", "w")

# for loop to iterate through all the lines
for line in f:
    # sets variable, data, as each line seperated by a tab
    data = line.strip().split("\t")
    # if statement to skip bad lines
    if len(data) == 13:
        # sets variable names to each column in data
        country, description, designation, points, price, province, region_1, region_2, taster_name, taster_twitter_handle, title, variety, winery = data
        # writes the country column and points column in o.txt
        o.write("{0}\t{1}\n".format(country, points))
        print(country + '\t' + points + '\n')

# closes both files
f.close()
o.close()
```

#### Actual Mapper Output
![gs1](https://github.com/s523286/Wine-Reviews-By-Country/blob/master/sum_of_points/images/mapper.JPG)
#### Code for sort.py
``` python
# Referenced Dr. Case's slides on MapReduce in python
# sort.py will sort our key/value pairs alphabetically

# opens o.txt as a read only file (contains key-value pairs from mapper)
o = open( "o.txt", "r")
# opens s.txt as a file to write to
s = open("s.txt", "w")

# reads in all the lines of the file and sorts them
lines = o.readlines()
lines.sort()

# writes out each sorted line to the s.txt file
for line in lines:
    s.write(line)

# closes both files
o.close()
s.close()
```
#### Code for reducer.py
``` python
# Referenced Dr. Case's Slides on MapReduce in Python
# reducer.py will use the key/value pairs: country, points
# This file sums the points for each country

# opens s.txt as a read-only file (contains the sorted list)
s = open("s.txt", "r")
# opens r.txt as a file to write to
# r = open("r.txt", "w")

# instantiating variables for later use
oldKey = None
thisKey = ""
thisValue = 0

# for loop to iterate through each line
for line in s:
    # seperates each value with a tab
    data = line.strip().split('\t')
    # if statement to ignore a bad input line
    if len(data) != 2:
        continue
    # read in our variables and set them equal to data
    country, points = data

    # make sure country is not null
    if country != thisKey:
        if thisKey:
            # output the last key value pair result
            print(thisKey + '\t' + str(thisValue) + '\n')

        # start over when changing keys
        thisKey = country
        thisValue = 0

    # apply the sum function
    thisValue += int(points)

# output the final key and value
print(thisKey + '\t' + str(thisValue) + '\n')

# close the files
s.close()
# r.close()
```
#### Reducer Ouput Example
Key: US, Value: 96(sum= 560400)
#### Actual Reducer Output
![gs1](https://github.com/s523286/Wine-Reviews-By-Country/blob/master/sum_of_points/images/reducer.JPG)
#### Language
Python
#### Kind of Chart
Bar Graph


