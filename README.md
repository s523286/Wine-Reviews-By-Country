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
#### Code for Mapper
```
# opens the file to read and write from
i = open("wineData.txt", "r")
o = open("o.txt", "w")

# reading the lines in 
for line in i:
  # splitting and stripping the data
  data = line.strip().split("\t")
  if (len(data) == 13):
    # titles the fields
    country, description, designation, points, price, province, region_1, region_2, taster_name, taster_twitter_handle, title, variety, winery = data
    # writing out the o file with the intermediate key-value pairs
    o.write(country + "\t" + points + "\n")

# closes the files
i.close()
o.close()
```

#### Actual Mapper Output
![mapper output](https://github.com/s523286/Wine-Reviews-By-Country/blob/master/min_points/images/wineMapper.PNG)

#### Reducer Ouput Example
Key: US, Value: 78(lowest: 78)
#### Code for Reducer
```
# opens the file to read and write from 
s = open("s.txt","r")
r = open("r.txt", "w")

# setting thisKey and min to 0
thisKey = ""
min = 0.0

# It is going to read every line in and strip and split it
for line in s:
  data = line.strip().split("\t")

# if the data isnt in key value pairs then it will continue
  if len(data) != 2:
    continue

# Setting country and points to data
  country, points = data

  if country != thisKey:
    if thisKey:
      # output the key value pair result
      r.write(thisKey + '\t' + str(min)+'\n')

    # start over when changing keys
    thisKey = country 
    min = points
  
  # statment to find the minimum points
  if int(points) < min:
    min = int(points)

# output the final entry when done
r.write(thisKey + '\t' + str(min)+'\n')

# closes the files
s.close()
r.close()
```

#### Actual Mapper Output
![reducer output](https://github.com/s523286/Wine-Reviews-By-Country/blob/master/min_points/images/wineReducer.PNG)

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
#### Code for mapper.py
``` python
# Reference from Dr. Case's slides on MapReduce in Python
# mapper.py will map our data to key/value pairs

 # open file, read-only raw data
f = open("wineData.txt","r") 

# open file, write - just our key, value pairs
o = open("o.txt", "w")

# input comes from STDIN (standard input)
for line in f:
    line = line.strip()
    line = line.split("\t")

    if len(line) ==13:
        country = line[0]
        price = line[4]
# Prints the output in the format of country, price
        o.write("{0}\t{1}\n".format(country, price))
f.close()
o.close()
```

#### Actual Mapper Output
![mapper_output](https://user-images.githubusercontent.com/31708972/49242207-d4df8b80-f3cf-11e8-9bf1-799f0fff9226.png)

#### Code for sort.py
``` python
#Referenced Dr. Case's slides on MapReduce in python
#sort.py will sort our key/value pairs alphabetically
o = open( "o.txt", "r")
s = open("s.txt", "w")
# reads from each line in a file and sort them
lines = o.readlines()
lines.sort()

# writes the sorted output to s.txt file
for line in lines:
    s.write(line)

o.close()
s.close()

```
#### Code for reducer.py
``` python
# Reference from Dr. Case's Slides on MapReduce in Python
# reducer.py will use the key/value pairs: country, price

# This file is used find the average price for each bottle in the country
s = open("s.txt", "r")
r = open("r.txt", "w")

oldKey = None
thisKey = ""
thisValue = 0.0
count=0.0

for line in s:
    data = line.strip().split('\t')
# if bad input line
    if len(data) != 2:  
# ignore it
        continue  

# read into variables
    country, price = data  

    if country != thisKey:
        if thisKey:
# resultant ouput in the form of key value pair
            r.write(thisKey + '\t' + str(thisValue/count) + '\n')
            print(thisKey + '\t' + str(thisValue/count) + '\n')

# start over when changing keys
        thisKey = country
        thisValue = 0.0
        count = 0.0

# apply the aggregation function
    thisValue += float(price)
# apply the count function
    count += 1
# final ouput in the key value pair i.e.,(country, average)
r.write(thisKey + '\t' + str(thisValue/count) + '\n')
print(thisKey + '\t' + str(thisValue/count) + '\n')

s.close()
r.close()

```
#### Reducer Ouput Example
Key: US, Value: 235(Average: sum=158/count=20)
#### Actual Reducer Output
![reducer_output](https://user-images.githubusercontent.com/31708972/49242239-e45ed480-f3cf-11e8-9ea3-f2eaacbb9730.png)
#### Graphical Representation of Final Output
![graph](https://user-images.githubusercontent.com/31708972/49242285-f93b6800-f3cf-11e8-986c-2db0a5101de6.PNG)
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
![gs2](https://github.com/s523286/Wine-Reviews-By-Country/blob/master/sum_of_points/images/reducer.JPG)
#### Language
Python
#### Kind of Chart
Choropleth Map
![gs3](https://github.com/s523286/Wine-Reviews-By-Country/blob/master/sum_of_points/images/ChoroplethMap.JPG)
#### How to Create the Chart
- Your final output from above will produce a text file called “r.txt” in your sum_of_points folder. 
- If you open that text file, you can copy and paste it right into excel. It will automatically separate the columns for you. 
      -If not, select the first column and go to the data tab, and then click “text to columns.” That will take you through the steps to tell excel that there is a tab delimiter. 
- Then, insert a row above row 1. There you can label column A as “Country” and column B as “Points.” 
- Your excel file should look similar to the one below:
![gs4](https://github.com/s523286/Wine-Reviews-By-Country/blob/master/sum_of_points/images/ExcelFile.JPG)
- We will use this excel file to create our visual in Tableau. Save the file somewhere on your PC.
- Open Tableau and import the excel file.
- Click on the tab labeled "sheet1."
- From there, double click on country to create a map and drag points to color.
- You can edit the colors however you would like. Your final Tableau worksheet should look like the one below:
![gs5](https://github.com/s523286/Wine-Reviews-By-Country/blob/master/sum_of_points/images/TableauWorksheet.JPG)




