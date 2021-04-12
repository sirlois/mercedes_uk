RESULTS_TXT_LOCATION = "results_folder\prices_result.txt"
RESULT_SCREENSHOT_FILE = "results_folder\screenshot.png"

CHROME_DRIVER = 'browser_drivers/chromedriver.exe'
OPERA_DRIVER = 'browser_drivers/operadriver.exe'

WEBSITE_URL = 'https://www.mercedes-benz.co.uk/passengercars/mercedes-benz-cars/car-configurator.html/motorization/CCci/GB/en/A-KLASSE/KOMPAKT-LIMOUSINE'
# WEBSITE_URL = 'https://www.mercedes-benz.co.uk/'


XPATH_DIESEL_CHECKBOX = '//*[@id="owcc-cont"]/div/owcc/cc-app-root/div/cc-app-container/div/div[2]/div[2]/div[1]/cc-motorization/cc-motorization-filters-section/cc-motorization-filters/form/fieldset[1]/div[2]/div[2]/wb-checkbox-control/label/wb-icon'
XPATH_STRING_NUMBER_OF_CARS = '//*[@id="owcc-cont"]/div/owcc/cc-app-root/div/cc-app-container/div/div[2]/div[2]/div[1]/cc-motorization/cc-motorization-comparison/div/cc-motorization-comparison-status/div/div[1]'
XPATH_NEXT_CAR_BUTTON = '//*[@id="owcc-cont"]/div/owcc/cc-app-root/div/cc-app-container/div/div[2]/div[2]/div[1]/cc-motorization/cc-motorization-comparison/div/div/cc-slider/div/cc-slider-ui-container/cc-slider-buttons/div/button[2]'
XPATH_COOKIES_BANNER = '/html/body/div[1]/div[3]/div/div[2]/div/div/div[2]/div[1]/button[1]'

def get_xpath_from_car(car_number):
    return f'//*[@id="owcc-cont"]/div/owcc/cc-app-root/div/cc-app-container/div/div[2]/div[2]/div[1]/cc-motorization/cc-motorization-comparison/div/cc-slave-slider/div/div/div/cc-slave-slide[{car_number}]/div/cc-motorization-header/div/div/div[2]'
