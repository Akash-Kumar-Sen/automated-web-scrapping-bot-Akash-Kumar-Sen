from time import sleep
from requests import get
from bs4 import BeautifulSoup
import csv 


from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager



def _get_categories():
    site_url = 'https://clutch.co/'
    request_result=get(site_url)

    soup_obj = BeautifulSoup(request_result.text,"html.parser")

    category_list=[]
    categories = soup_obj.find_all("a", {"class": "sitemap-nav__item"})

    for item in categories:
        category_list.append((str(item['href']),item.getText()))


    return category_list


def _generate_data_instances(extension,page_number):

    if page_number<=1:
        site_url='https://clutch.co'+extension
    else:
        site_url='https://clutch.co' + extension + '?page=' + str(page_number-1)
        
    print(site_url)
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get(site_url)

    # Fetch info from driver
    company_name=driver.find_elements_by_class_name("company_info")
    website=driver.find_elements_by_class_name("website-link__item")
    location=driver.find_elements_by_class_name("locality")
    rating_number=driver.find_elements_by_class_name("sg-rating__number")
    reviews=driver.find_elements_by_class_name("sg-rating__reviews")
    hourly_rate=driver.find_elements_by_css_selector('div.list-item[data-content="<i>Avg. hourly rate</i>"]')
    min_project_size=driver.find_elements_by_css_selector('div.list-item[data-content="<i>Min. project size</i>"]')
    employee_size=driver.find_elements_by_css_selector('div.list-item[data-content="<i>Employees</i>"]')

    max_length_obtained=min(
        len(company_name),
        len(website),
        len(location),
        len(rating_number),
        len(reviews),
        len(hourly_rate),
        len(min_project_size),
        len(employee_size)
        )
    csv_row_list=[]

    for i in range(max_length_obtained):

        # Correcting the format of website link in the website
        website_link=website[i].get_attribute("href")
        website_list=website_link.split('?')
        # Creating a new data instance
        row_instance_list=[
            company_name[i].text,
            website_list[0],
            location[i].text,
            rating_number[i].text,
            reviews[i].text,
            hourly_rate[i].text,
            min_project_size[i].text,
            employee_size[i].text
        ]

        csv_row_list.append(row_instance_list)
    driver.quit()
    
    # 10 seconds sleep for not getting blocked.
    sleep(10)

    return csv_row_list
