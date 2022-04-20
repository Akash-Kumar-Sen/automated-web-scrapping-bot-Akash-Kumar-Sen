import warnings
from slugify import slugify


from scrapper.get_csv import __generate_csv
from scrapper.scrapper import _generate_data_instances,_get_categories


def driver_function():
    warnings.filterwarnings("ignore")

    categories=_get_categories()

    for i in range(len(categories)):
        print(i+1 , '.' ,categories[i][1])

    choices = input("Please Select Category Number : ")
    page_number = input("Please enter the page number : ")


    try:
        choices=int(choices)
        page_number=int(page_number)
    except ValueError:
        print('Please only input digits')


    

    csv_list=_generate_data_instances(extension=categories[choices-1][0],page_number=page_number)

    csv_name=slugify(categories[choices-1][1])+'-'+'page-number-'+str(page_number)+'.csv'

    __generate_csv(csv_name=csv_name,csv_list=csv_list)



if __name__ == "__main__":
    driver_function()

#Driver Code