import json
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome("C:/Users/noorm/OneDrive/Desktop/Linkedin_scrapping/chromedriver.exe") ## Location of your chromeDriver

class Scraping:

    def __init__(self, email,password):
        self.email = email
        self.password = password
    
    def getEmail(self):
        return self.email
    
    def getPassword(self):
        return self.password
    
    def login_user(self):
        driver.get('https://www.linkedin.com/login')

        # locate email form by_class_name
        username = driver.find_element(By.ID,'username')

        # send_keys() to simulate key strokes
        username.send_keys(self.getEmail())

        # sleep for 0.5 seconds
        time.sleep(0.5)

        # locate password form by_class_name
        password = driver.find_element(By.ID,'password')

        # send_keys() to simulate key strokes
        password.send_keys(self.getPassword())
        time.sleep(0.5)

        # locate submit button by_xpath
        sign_in_button = driver.find_element(By.XPATH,'//*[@type="submit"]')

        # .click() to mimic button click
        sign_in_button.click()
        time.sleep(3)

    def setURLlist(self, urlList):
        self.url_list = urlList
    
    def get_wholePage(self,url):
        driver.get(url)
        start = time.time()
        
        # will be used in the while loop
        initialScroll = 0
        finalScroll = 1000

        while True:
            driver.execute_script(f"window.scrollTo({initialScroll},{finalScroll})")
            # this command scrolls the window starting from
            # the pixel value stored in the initialScroll
            # variable to the pixel value stored at the
            # finalScroll variable
            initialScroll = finalScroll
            finalScroll += 1000
        
            # we will stop the script for 3 seconds so that
            # the data can load
            time.sleep(3)
            # You can change it as per your needs and internet speed
        
            end = time.time()
        
            # We will scroll for 20 seconds.
            # You can change it as per your needs and internet speed
            if round(end - start) > 20:
                break

        soup = BeautifulSoup(driver.page_source, 'lxml')
        
        return soup

    def get_experiencePage(self,url):

        experience_page_url = url+"details/experience/"
        driver.get(experience_page_url)
        time.sleep(3)
        start = time.time()
        
        # will be used in the while loop
        initialScroll = 0
        finalScroll = 1000

        while True:
            driver.execute_script(f"window.scrollTo({initialScroll},{finalScroll})")
            
            initialScroll = finalScroll
            finalScroll += 1000

            time.sleep(1)
        
            end = time.time()

            if round(end - start) > 5:
                break
        soup = BeautifulSoup(driver.page_source, 'lxml')
        return soup
    
    def get_educationPage(self,url):
        education_page_url = url+"details/education/"
        driver.get(education_page_url)
        start = time.time()
        
        initialScroll = 0
        finalScroll = 1000

        while True:
            driver.execute_script(f"window.scrollTo({initialScroll},{finalScroll})")

            initialScroll = finalScroll
            finalScroll += 1000
        
            time.sleep(1)
            # You can change it as per your needs and internet speed
        
            end = time.time()
        
            if round(end - start) > 5:
                break
        soup = BeautifulSoup(driver.page_source,'lxml')
        return soup

    def get_skillPage(self,url):
        skill_page_url = url+"details/skills/"
        driver.get(skill_page_url)
        time.sleep(3)
        start = time.time()
        
        # will be used in the while loop
        initialScroll = 0
        finalScroll = 1000

        while True:
            driver.execute_script(f"window.scrollTo({initialScroll},{finalScroll})")

            initialScroll = finalScroll
            finalScroll += 1000

            time.sleep(1)
        
            end = time.time()
        
            if round(end - start) > 5:
                break
        soup = BeautifulSoup(driver.page_source,'lxml')
        return soup
    
    def get_projectPage(self,url):
        project_page_url = url+"details/projects/"
        driver.get(project_page_url)
        time.sleep(3)
        start = time.time()
        
        initialScroll = 0
        finalScroll = 1000

        while True:
            driver.execute_script(f"window.scrollTo({initialScroll},{finalScroll})")

            initialScroll = finalScroll
            finalScroll += 1000

            time.sleep(1)
        
            end = time.time()
        
            if round(end - start) > 5:
                break
        soup = BeautifulSoup(driver.page_source,'lxml')
        return soup
    
    def get_languagePage(self,url):
        project_page_url = url+"details/languages/"
        driver.get(project_page_url)
        time.sleep(3)
        start = time.time()
        
        # will be used in the while loop
        initialScroll = 0
        finalScroll = 1000

        while True:
            driver.execute_script(f"window.scrollTo({initialScroll},{finalScroll})")

            initialScroll = finalScroll
            finalScroll += 1000

            time.sleep(1)
        
            end = time.time()
        
            if round(end - start) > 5:
                break
        soup = BeautifulSoup(driver.page_source,'lxml')
        return soup
    
    def stop_work(self):
        driver.quit()

    def get_name(self,url):
        soup = self.get_wholePage(url)
        name = soup.find('h1').get_text().strip()
        intro = soup.find('div', {'class': 'display-flex ph5 pv3'})
        if intro is None:
            return {"name":name,"about":"None"}
        else:
            intro = intro.find('div',{'class':'inline-show-more-text inline-show-more-text--is-collapsed'})
            intro= intro.find('span')
            introR = intro.get_text().strip()
            return {"name":name,"about":introR}

    def get_experience(self,url):
        soup = self.get_experiencePage(url)
        list_exp = soup.find_all("li",{"class":"pvs-list__paged-list-item artdeco-list__item pvs-list__item--line-separated"})
        experience =[]
        if list_exp[0].find_all("span",{"class":"mr1 hoverable-link-text t-bold"}) is None:
            return experience
        else:
            for index in range(len(list_exp)):
                title_span = list_exp[index].find_all("span",{"class":"mr1 hoverable-link-text t-bold"})

                if len(title_span)>1:
                    timeline_li = list_exp[index].find_all("span",{"class":"t-14 t-normal"})
                    timeline = timeline_li[0].find("span",{"class":"visually-hidden"}).get_text()
                    timeline = timeline.split(" · ")[0]
                    company = title_span[0].find("span",{"class":"visually-hidden"}).get_text()
                    company = company.split(" · ")[0]
                    designation = title_span[1].find("span",{"class":"visually-hidden"}).get_text()
                    experience.append({"company":company,"timeline":timeline,"designations":designation})
                else:
                    title_span = list_exp[index].find("span",{"class":"mr1 t-bold"})
                    designation = title_span.find("span",{"class":"visually-hidden"}).get_text()
                    company_li = list_exp[index].find_all("span",{"class":"t-14 t-normal"})
                    company = company_li[0].find("span",{"class":"visually-hidden"}).get_text()
                    company = company.split(" · ")[0]
                    timeline_li = list_exp[index].find_all("span",{"class":"t-14 t-normal t-black--light"})
                    timeline = timeline_li[0].find("span",{"class":"visually-hidden"}).get_text()
                    timeline = timeline.split(" · ")[0]
                    experience.append({"company":company,"timeline":timeline,"designations":designation})
                
            return experience
    def get_education(self,url):
        soup = self.get_educationPage(url)
        list_edu = soup.find_all("li",{"class":"pvs-list__paged-list-item artdeco-list__item pvs-list__item--line-separated"})
        educations =[]
        if list_edu[0].find("span",{"class":"mr1 hoverable-link-text t-bold"}) is None:
            return educations
        else:
            for index in range(len(list_edu)):
                institution_span = list_edu[index].find("span",{"class":"mr1 hoverable-link-text t-bold"})
                institution = institution_span.find("span",{"class":"visually-hidden"}).get_text()
                degree_span = list_edu[index].find("span",{"class":"t-14 t-normal"})
                degree = degree_span.find("span",{"class":"visually-hidden"}).get_text()
                timeline_span = list_edu[index].find("span",{"class":"t-14 t-normal t-black--light"})
                timeline = timeline_span.find("span",{"class":"visually-hidden"}).get_text()
                educations.append({"institution":institution,"degree":degree,"timeline":timeline})
            return educations  
    def get_projects(self,url):
        soup = self.get_projectPage(url)
        list_projects= soup.find_all("li",{"class":"pvs-list__paged-list-item artdeco-list__item pvs-list__item--line-separated"})
        projects= []
        if list_projects[0].find("span",{"class":"mr1 t-bold"}) is None:
            return projects
        else:
            for index in range(len(list_projects)):
                topic_span = list_projects[index].find("span",{"class":"mr1 t-bold"})
                topic =  topic_span.find("span",{"class":"visually-hidden"}).get_text()
                timeline_span = list_projects[index].find("span",{"class":"t-14 t-normal"})
                timeline = timeline_span.find("span",{"class":"visually-hidden"}).get_text()
                projects.append({"topic":topic,"timeline":timeline})
            return projects
    def get_skills(self,url):
        soup = self.get_skillPage(url)
        list_skills = soup.find_all("li",{"class":"pvs-list__paged-list-item artdeco-list__item pvs-list__item--line-separated"})
        skills = []
        if list_skills[0].find("span",{"class":"mr1 hoverable-link-text t-bold"}) is None:
            return skills
        else:
            for index in range(len(list_skills)):
                skill_span = list_skills[index].find("span",{"class":"mr1 hoverable-link-text t-bold"})
                skill = skill_span.find("span",{"class":"visually-hidden"}).get_text()
                skills.append(skill)
            return skills
    def get_languages(self,url):
        soup = self.get_languagePage(url)
        list_language= soup.find_all("li",{"class":"pvs-list__paged-list-item artdeco-list__item pvs-list__item--line-separated"})
        languages = []
        if list_language[0].find("span",{"class":"mr1 t-bold"}) is None:
            return languages
        else:
            for index in range(len(list_language)):
                language_span = list_language[index].find("span",{"class":"mr1 t-bold"})
                language = language_span.find("span",{"class":"visually-hidden"}).get_text()
                languages.append(language)
            return languages


    def store_all_information(self,url_list):
        self.setURLlist(url_list)
        self.login_user()
        json_result = []
        for index in range(len(self.url_list)):
            intro = self.get_name(self.url_list[index])
            name= intro["name"]
            about = intro["about"]
            json_result.append({"linkedin url":self.url_list[index],"name":name,
            "about":about,"experience":self.get_experience(self.url_list[index]),
            "education":self.get_education(self.url_list[index]),"projects":self.get_projects(self.url_list[index]),
            "skills":self.get_skills(self.url_list[index]),"language":self.get_languages(self.url_list[index])})
        json_data = json.dumps(json_result,indent=2)
        self.stop_work()
        return json_data