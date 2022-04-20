import csv


def __generate_csv(csv_name,csv_list):

    header=['Company','Website','Location','Rating','Review Count','Hourly Rate','Min Project Size','Employee Size']

    with open(csv_name, 'w', encoding='UTF8',newline='') as f:
        writer = csv.writer(f)
        # write the header
        writer.writerow(header)
        # write the data
        writer.writerows(csv_list)


    print("File named "+csv_name+" Is Generated into the current working directory")