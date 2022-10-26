from selenium import webdriver
from selenium.common import NoSuchElementException, WebDriverException
from selenium.webdriver.common.by import By
import os
import chromedriver_autoinstaller
from selenium.webdriver.chrome.service import Service as ChromiumService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.core.utils import ChromeType
import time
import pyautogui
from datetime import datetime
import random

import undetected_chromedriver as uc
driver = uc.Chrome(enable_cdp_events=True, use_subprocess=True, version_main=106)

popular_investors = ["rallek", "miyoshi", "reinhardtcoetzee", "sharonconnolly", "cphequities", "rubymza", "richardstroud", "ingruc", "pino428", "triangulacapital", "jordenboer", "slow_and_steady", "monabel", "emge2116", "doopiecash", "magic_kaito", "ioatri",
       "balticseal", "daniel4653", "fifty-five", "calintrading", "sgstjc", "greatcompanies", "karlo_s", "lukaszkisicki", "trojaneto", "chiay0327", "carlos_delarosa", "trex8u247", "estebanopatril", "nintingale", "taherkamari", "zofesu",
      "andreamarcon16", "nestorarmstrong", "bhavesh_spx", "theosanders", "dividends_income", "andresvicunat", "tomwintjes", "nicoroumeau", "mjtfernandez", "myhungetoro", "maxdividend", "victorvatin",
      "aguero1010", "ilakha", "beatthemarketz", "acetoandrea", "jacksmann", "renoi974", "tomchapman1979", "axisnet", "imbolex", "thinhleduc", "jianswang", "marianopardo", "wesl3y", "hyjbrighter", "misterg23", "ligkclaw",
      "alexandrucinca", "rubymza", "jaynemesis", "gserdan", "tradefx525", "eddyb123", "returninvest", "matanspalatrin1", "lee88eng", "bamboo108", "liborvasa", "jeppekirkbonde", "liamdavies", "arash007", "canzhao", "knw500",
      "thibautr", "fundmanagerzech", "sashok281", "alnayef", "campervans", "pizarrosaul", "sandra31168", "social-investor", "prototypevr", "harryh1993", "vidovm", "meldow", "robertunger", "sparkliang", "abbroush",
      "abeershahid", "coolcontribution", "chocowin", "vladd35", "aukie2008", "noasnoas", "b--art", "simonneau"]
popular_investors = ["rallek"]

datetime_now = datetime.today().strftime('%m-%d-%Y-h%H')
directory = r"offline_webpage_portfolio_pages/" + datetime_now
if not os.path.exists(directory):
      os.makedirs(directory)

number_of_record = 0
final_profile = ""
fail_pages = ""
name_check = ""
rank_check = ""

print("Begin crawling: " + str(len(popular_investors)) + " investors' data")
seed = random.randrange(3, 8)

for pi in popular_investors:
      time.sleep(seed * random.random())

      # GET_PORTFOLIO_DATA #

      # CHECK_WEBSITE #
      try:
            url_string = "https://www.etoro.com/people/" + pi + "/portfolio"
            driver.get(url_string)
      except WebDriverException as e:
            print("NO_PAGE_FOUND: " + url_string)
            print("ERROR: " + str(e))
            fail_pages += pi + ", "
            continue
      # CHECK_WEBSITE #

      time.sleep(seed * random.random())

      # DOWNLOAD_WEBSITE #
      final_portfolio_profile = pi
      with open(directory + "/" + pi + ".html", "w", encoding='utf-8') as f:
            try:
                  f.write(driver.page_source)
            except WebDriverException as e:
                  print("CANT_SAVE_PI_PORTFOLIO_PAGE: " + pi)
                  print("CANT_SAVE_PI_PORTFOLIO_PAGE_URL: " + url_string)
                  print("ERROR: " + str(e))
                  final_portfolio_profile += pi + ", "
                  continue
      # DOWNLOAD_WEBSITE #

      # CHECK_PI_FULLNAME #
      try:
            name_check = driver.find_element(By.XPATH, "//h1[@automation-id='user-head-not-nickname']").text
            print("check_pi_fullname: " + name_check)
      except NoSuchElementException:
            name_check = ""
            print("FAILED_TO_GET_FULLNAME: " + pi)
      # CHECK_PI_FULLNAME #

      # CHECK_PI_FIRST_TICKET #
      try:
            first_ticket = driver.find_element(By.XPATH, "(//*[contains(@class,'i-portfolio-table-name-symbol')])[1]").text
      except NoSuchElementException:
            try:
                  first_ticket = driver.find_element(By.XPATH, "//h1[@automation-id='cd-public-portfolio-table-item-title']").text
                  print("check_pi_first_ticket: " + first_ticket)
            except NoSuchElementException:
                  first_ticket = ""
                  print("FAILED_TO_GET_FIRST_TICKET: " + pi)
      # CHECK_PI_FIRST_TICKET #


      if len(name_check) != "" and len(first_ticket) != "":
            number_of_record += 1
      else:
            fail_pages += pi + ", "
            print("FAILED_PI_PORTFOLIO: " + pi)

      time.sleep(seed * random.random())

      #GET_PERFORMANCE_DATA #

      driver.find_element(By.XPATH, "//a[@automation-id='et-tab-stats']").click()
      directory = r"offline_webpage_infor_pages/" + datetime_now
      if not os.path.exists(directory):
            os.makedirs(directory)

      try:
            button_see_more = driver.find_element(By.XPATH, "//span[@automation-id='cd-user-stats-performance-chart-show-more-text']")
            driver.execute_script("arguments[0].click();", button_see_more)
      except NoSuchElementException as e:
            print("No element is found")
            print("Error: " + str(e))
      except WebDriverException as e:
            print("no show more button")
            print("Error: " + str(e))

      time.sleep(seed * random.random())


      final_profile = pi
      with open(directory + "/" + pi + ".html", "w", encoding='utf-8') as f:
            try:
                  f.write(driver.page_source)
            except WebDriverException as e:
                  print("Cant save " + pi + ".html file")
                  print("Error: " + str(e))
                  fail_pages += pi + ", "

      try:
            name_check = driver.find_element(By.XPATH, "//span[@automation-id='user-header-full-name']").text
      except NoSuchElementException:
            name_check = ""

      try:
            name_check = driver.find_element(By.XPATH, "//h1[@automation-id='user-head-nickname']").text
      except NoSuchElementException:
            name_check = ""

      try:
            rank_check = driver.find_element(By.XPATH, "//*[contains(@class,'risk-default')]").text
      except NoSuchElementException:
            rank_check = ""

      try:
            rank_check = driver.find_element(By.XPATH, "//*[contains(@class,'risk-label')]").get_attribute("class")
      except NoSuchElementException:
            rank_check = ""

      try:
            rank_check = driver.find_element(By.XPATH, "//*[contains(@class,'risk-label')]").get_attribute("class")
      except NoSuchElementException:
            rank_check = ""

      print("name_check: " + name_check)
      print("rank_check: " + rank_check)

      if len(name_check) != "" and len(rank_check) != "":
            number_of_record += 1
      else:
            fail_pages += pi + ", "
            print("failed crawl: " + pi)


driver.quit()
print("Report: \n" +
      "Crawled: " + str(number_of_record) + "/" + str(len(popular_investors)) + "\n" +
      "Success Rate: " + str(number_of_record*100/len(popular_investors)) + "\n" +
      "Failed pages: " + fail_pages + "\n" +
      "Stop at: " + final_profile)

