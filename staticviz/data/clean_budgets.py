import pandas as pd

def clean_budget_data():
    """
    Clean and combine budget data
    """
    budget_2019 = pd.read_csv("city_budgets/2019_budget.csv")
    budget_2020 = pd.read_csv("city_budgets/2020_budget.csv")
    budget_2021 = pd.read_csv("city_budgets/2021_budget.csv")
    budget_2022 = pd.read_csv("city_budgets/2022_budget.csv")
    budget_2023 = pd.read_csv("city_budgets/2023_budget.csv")

    budget_2019 = budget_2019.rename(columns = {"2019 ORDINANCE (AMOUNT $)": "ordinance"})
    budget_2019["year"] = "2019"
    budget_2020 = budget_2020.rename(columns = {"2020 ORDINANCE (AMOUNT $)": "ordinance"})
    budget_2020["year"] = "2020"
    budget_2021 = budget_2021.rename(columns = {"2021 ORDINANCE (AMOUNT $)": "ordinance"})
    budget_2021["year"] = "2021"
    budget_2022 = budget_2022.rename(columns = {"2022 ORDINANCE (AMOUNT $)": "ordinance"})
    budget_2022["year"] = "2022"
    budget_2023 = budget_2023.rename(columns = {"2023 ORDINANCE (AMOUNT $)": "ordinance"})
    budget_2023["year"] = "2023"

    budgets = pd.concat([budget_2019, budget_2020, budget_2021, budget_2022, budget_2023],
                        ignore_index = True, axis = 0)
    
    budgets = budgets.rename(columns = {"FUND TYPE": "fund_type",
                                        "FUND CODE": "fund_code",
                                        "FUND DESCRIPTION": "fund_desc",	
                                        "DEPARTMENT NUMBER": "dept_num",
                                        "DEPARTMENT DESCRIPTION": "dept_desc",
                                        "APPROPRIATION AUTHORITY": "approp_auth",
                                        "APPROPRIATION AUTHORITY DESCRIPTION": "approp_auth_desc",
                                        "APPROPRIATION ACCOUNT": "approp_acc",
                                        "APPROPRIATION ACCOUNT DESCRIPTION": "approp_acc_desc"})
    
    dict_departments = {"department": ["Office of the Mayor", "Office of Inspector General",
                                       "Office of Budget and Management",
                                       "Department of Technology and Innovation",
                                       "City Council", "Department of Housing",
                                       "Department of Cultural Affairs and Special Events",
                                       "Office of City Clerk", "Department of Finance",
                                       "City Treasurer's Office", "Department of Administrative Hearings",
                                       "Department of Law", "Department of Human Resources",
                                       "Department of Procurement Services", 
                                       "Department of Fleet and Facility Management",
                                       "Board of Election Commissioners", "Chicago Department of Public Health",
                                       "Chicago Commission on Human Relations",
                                       "Mayor's Office for People with Disabilities",
                                       "Department of Family and Support Services",
                                       "Office of Public Safety Administration",
                                       "Department of Planning and Development",
                                       "Chicago Police Board", "Chicago Police Department",
                                       "Office of Emergency Management and Communications",
                                       "Chicago Fire Department", "Civilian Office of Police Accountability",
                                       "Community Commission for Public Safety and Accountability",
                                       "Department of Buildings", "Department of Business Affairs and Consumer Protection",
                                       "Department of Environment",
                                       "Chicago Animal Care and Control", "License Appeal Commission",
                                       "Board of Ethics", "Department of Streets and Sanitation",
                                       "Chicago Department of Transportation", 
                                       "Chicago Department of Aviation", "Department of Water Management",
                                       "Chicago Public Library", "Finance General"],
                        "dept_num": [1, 3, 5, 6, 15, 21, 23, 25, 27, 28, 30, 31,
                                     33, 35, 38, 39, 41, 45, 48, 50, 51, 54, 55,
                                     57, 58, 59, 60, 62, 67, 70, 72, 73, 77, 78,
                                     81, 84, 85, 88, 91, 99]}
    
    departments = pd.DataFrame(dict_departments)

    budgets = budgets.join(departments.set_index("dept_num"), on = "dept_num")
    
    budgets.to_csv("./budgets.csv", index = False)

clean_budget_data()



