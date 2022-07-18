import csv
from jinja2 import Template

""" Source file is file where we have our test data in .csv format and we are passing path fetch data"""
source_file = "C:\\Users\\wasim\\PycharmProjects\\Project_Test\\test.csv"

""" Ref_file is a file where we are applying  Jinja2 format in {{}} for our variable data map"""

Ref_file="C:\\Users\\wasim\\PycharmProjects\\Project_Test\\wasim.jn"


""" Opening Ref_file and loading in template format """
with open(Ref_file) as ref:
    MOP=Template(ref.read(),keep_trailing_newline=True)

""" Opening Source CSV file and storing in reader variable in Dictionary key& value pair"""
with open(source_file, encoding='utf-8-sig') as f:
    reader = csv.DictReader(f)

    for row in reader:

        configFile= MOP.render(
            Name = row["Host Name"],
            LB_Name = row["Loopback Interface"],
            LB_IP = row["Loopback ip"],
            P_Name = row["ISIS process name"],
            Area_ID = row["ISIS area ID"],
            System_ID = row["ISIS system id"],
            Family_name = row["Address family"],
            )

        with open("C:\\Users\\wasim\\PycharmProjects\\Project_Test\\MOP\\" + row["Host Name"] + ".txt","w") as txtf:
            txtf.write(configFile)
