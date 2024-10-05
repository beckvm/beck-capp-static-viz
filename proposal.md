# Project Proposal

Tori Beck

Subject:
I'd like to explore the city of Chicago's annual operating budgets from the past 5 years (2019-2023) to observe where money is being allocated and how that changes over time.
In relation to this budget data, I want to take a look at some data about social and economic indicators including poverty, education, health care, and crime rates to see whether or not 
there are any patterns between where money is spent and how these indicators change.  For example, is there any visible relationship between police budgets and crime rates? 
How does health care coverage evolve as the Department of Health's budget changes? Does the number of people using public transit to commute change alongside CDOT's expenditures?
Having a clearer understanding of where the city's money is going is important for transparency and I think it will be interesting to observe whether these allocations of money coincide 
with changes in socioeconomic wellbeing.  While I obviously can't make any claims about causation, visualizing side-by-side where the money is going and how demographic indicators change over the years might yield some insights.

Data sources:

1. Annual operating budgets 2019-2023:  
2023 (Rows: 3,447, Columns: 10) https://data.cityofchicago.org/Administration-Finance/Budget-2023-Budget-Ordinance-Appropriations/xbjh-7zvh/about_data  
2022 (Rows: 3,446, Columns :10) https://data.cityofchicago.org/Administration-Finance/Budget-2022-Budget-Ordinance-Appropriations/2cr6-8u6w/about_data  
2021 (Rows: 3,384, Columns: 10) https://data.cityofchicago.org/Administration-Finance/Budget-2021-Budget-Ordinance-Appropriations/6tbx-h7y2/about_data  
2020 (Rows: 3,509, Columns: 10) https://data.cityofchicago.org/Administration-Finance/Budget-2020-Budget-Ordinance-Appropriations/fyin-2vyd/about_data  
2019 (Rows: 3,507, Columns: 10) https://data.cityofchicago.org/Administration-Finance/Budget-2019-Budget-Ordinance-Appropriations/h9rt-tsn7/about_data  
These are the annual operating budgets for the city of Chicago from the Chicago Data Portal, detailing which departments are allocated how much money.  
Some departments I think may be relevant include the CPD, Department of Health, Department of Housing, and CDOT.  

2. Crime Data 2019-2023:  
About 81,000 rows, 22 columns  
https://data.cityofchicago.org/Public-Safety/Crimes-2001-to-Present/ijzp-q8t2/about_data  
This is city of Chicago crime data from the Chicago Police Department.  The data includes incidents of crime from 2001 to present, however I'll only be utilizing the data from   
2019-2023.  The columns include information about dates, descriptions of the crime, whether an arrest was made, and locations.    
This data will likely be seen on the aggregate, instead of individual crime reports.  

3. ACS Social and Economic Data 2019-2023  
https://www.census.gov/data/developers/data-sets/acs-1year.html  
I'll be pulling this data using the Census API to get the tables for the desired social and economic characteristics over a five year period.  
The data comes from the ACS 1 year estimates.  These are the tables I am interested in:  
    - Selected Economic Characteristics:  
    About 150 rows and 2 columns per year, however the data is grouped and will need to be ungrouped, possibly increasing the columns and decreasing the rows.  
    Example 2023 data: https://data.census.gov/table/ACSDP1Y2022.DP03?q=dp Chicago city, Cook County, Illinois&y=2022&moe=false  
    Characteristics include employment, commute to work, poverty, health insurance coverage, and income.   
    - Selected Social characteristics:
    About 170 Rows and 2 columns per year, however the data is grouped and will need to be ungrouped, possibly increasing the columns and decreasing the rows.   
    Example 2023 data: https://data.census.gov/table/ACSDP1Y2023.DP02?q=dp Chicago city, Cook County, Illinois&moe=false&tp=false   
    Characteristics include households, education, school enrollment, disability, citizenship, and internet use.  
   
Questions:
Is the scope of this project too broad or unclear?
I've not directly used the census API for ACS data before, will it be straightforward enough to get the data quickly?
