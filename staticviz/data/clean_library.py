import pandas as pd

def clean_library_visitors_data():
    """
    Clean and combine library visitors data
    """
    visitors_2019 = pd.read_csv("library_data/2019_library_visitors.csv")
    visitors_2020 = pd.read_csv("library_data/2020_library_visitors.csv")
    visitors_2021 = pd.read_csv("library_data/2021_library_visitors.csv")
    visitors_2022 = pd.read_csv("library_data/2022_library_visitors.csv")
    visitors_2023 = pd.read_csv("library_data/2023_library_visitors.csv")


    visitors_2019["year"] = "2019"
    visitors_2019 = visitors_2019.rename(columns = {"LOCATION": "BRANCH"})
    visitors_2020["year"] = "2020"
    visitors_2021["year"] = "2021"
    visitors_2022["year"] = "2022"
    visitors_2022 = visitors_2022.rename(columns = {"Location": "LOCATION"})
    visitors_2023["year"] = "2023"
    visitors_2023 = visitors_2023.rename(columns = {"Location": "LOCATION"})

    visitors = pd.concat([visitors_2019, visitors_2020, visitors_2021, visitors_2022, visitors_2023],
                        ignore_index = True, axis = 0)
    visitors = visitors.replace("Harold Washtington Library Center", "Harold Washington Library Center")

    visitors = pd.melt(visitors, id_vars = ["BRANCH", "year"], 
                        value_vars = ['JANUARY', 'FEBRUARY', 'MARCH', 'APRIL', 'MAY', 'JUNE', 
                            'JULY', 'AUGUST', 'SEPTEMBER', 'OCTOBER', 'NOVEMBER', 
                            'DECEMBER'], var_name = "month", value_name = "num_visitors")

    visitors.to_csv("./library_visitors.csv", index = False)

clean_library_visitors_data()

def clean_library_circulation_data():
    """
    Clean and combine budget data
    """
    circulation_2019 = pd.read_csv("library_data/2019_library_circulation.csv")
    circulation_2020 = pd.read_csv("library_data/2020_library_circulation.csv")
    circulation_2021 = pd.read_csv("library_data/2021_library_circulation.csv")
    circulation_2022 = pd.read_csv("library_data/2022_library_circulation.csv")
    circulation_2023 = pd.read_csv("library_data/2023_library_circulation.csv")


    circulation_2019["year"] = "2019"
    circulation_2019 = circulation_2019.rename(columns = {"LOCATION": "BRANCH"})
    circulation_2020["year"] = "2020"
    circulation_2020 = circulation_2020.drop(columns = "LOCATION") 
    circulation_2021["year"] = "2021"
    circulation_2021 = circulation_2021.drop(columns = "Location") 
    circulation_2022["year"] = "2022"
    circulation_2022 = circulation_2022.drop(columns = "Location") 
    circulation_2023["year"] = "2023"
    circulation_2023 = circulation_2023.drop(columns = "Location") 

    circulation = pd.concat([circulation_2019, circulation_2020, circulation_2021, circulation_2022, circulation_2023],
                        ignore_index = True, axis = 0)

    circulation = pd.melt(circulation, id_vars = ["BRANCH", "year"], 
                        value_vars = ['JANUARY', 'FEBRUARY', 'MARCH', 'APRIL', 'MAY', 'JUNE', 
                            'JULY', 'AUGUST', 'SEPTEMBER', 'OCTOBER', 'NOVEMBER', 
                            'DECEMBER'], var_name = "month", value_name = "circulation_num")

    circulation.to_csv("./library_circulation.csv", index = False)

clean_library_circulation_data()








