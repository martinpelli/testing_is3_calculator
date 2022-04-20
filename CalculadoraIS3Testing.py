import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec

from CalculadoraIS3TestingData import operations
from CalculadoraIS3TestingData import errors
from CalculadoraIS3TestingData import testCases


class FindElements(unittest.TestCase):

    PATH_TO_DRIVER = "/home/pelli/Documents/chromedriver"
    PATH_TO_BROWSER = '/usr/bin/brave'
    PATH_TO_OUTPUT_FILE = "/home/pelli/Documents/testCases.txt"
    ERROR_NOTIFICATION_LABEL_XPATH = "//*[@id='errorMsgField']"


    def setUp(self):
        chromedriver = self.PATH_TO_DRIVER
        option = webdriver.ChromeOptions()
        option.binary_location = self.PATH_TO_BROWSER
        service = Service(chromedriver)
        self.driver = webdriver.Chrome(service=service, options=option)
        self.file = open(self.PATH_TO_OUTPUT_FILE, "a")

    def testCalculatorIS3(self):
        driver = self.driver
        driver.get("https://gerabarud.github.io/is3-calculadora/")
        wait = WebDriverWait(driver, 2)

        buildDropdown = Select(driver.find_element(by=By.XPATH, value="//*[@id='selectBuild']"))
        buildDropdown.select_by_visible_text("7")
        
        operationDropdown = Select(driver.find_element(by=By.XPATH, value="//*[@id='selectOperationDropdown']"))
        firstNumberInput = driver.find_element(by=By.XPATH, value="//*[@id='number1Field']")
        secondNumberInput = driver.find_element(by=By.XPATH, value="//*[@id='number2Field']")
        calculateButton = driver.find_element(by=By.XPATH, value="//*[@id='calculateButton']")
        answerOutput = driver.find_element(by=By.XPATH, value="//*[@id='numberAnswerField']")
        clearButton = driver.find_element(by=By.XPATH, value="//*[@id='clearButton']")
        errorNotificationLabel = driver.find_element(by=By.XPATH, value="//*[@id='errorMsgField']")
        
        for operation in operations:

            self.file.write("------------------------\n")
            self.file.write(f'Tests for operation {operation}\n\n')
            operationDropdown.select_by_visible_text(operation)

            for testCase in testCases[operation]:

                firstNumber = str(testCase[0])
                secondNumber = str(testCase[1])
                expectedResult = str(testCase[2])

                firstNumberInput.send_keys(firstNumber)
                secondNumberInput.send_keys(secondNumber)
                calculateButton.click()
                actualResult = answerOutput.get_attribute('value')              

                try:
                    assert expectedResult == actualResult
                except:
                    #Si el assert dio false esporque el resultado no coincidió con el resultado esperado
                    #Si el error esperado está dentro de los errores notificados por la calculadora
                    if expectedResult in errors:
                        try:
                            #Esperamos a que se muestre la notificación de error
                            wait.until(Ec.visibility_of_element_located((By.XPATH, self.ERROR_NOTIFICATION_LABEL_XPATH)))
                            #Si el texto de la notificación es igual al del resultado esperado el test da OK
                            if errorNotificationLabel.text == expectedResult:
                                self.writeOKTestInFile(firstNumber, secondNumber, expectedResult)
                            else:
                                actualResult = errorNotificationLabel.text
                                self.writeFAILEDTestInFile(firstNumber, secondNumber, expectedResult, actualResult)
                        except:
                            #Si el tiempo para esperar llegó a su fin es porque la notifiación no se mostró y el test falló
                            actualResult = "Calculator didn't show notification error"
                            self.writeFAILEDTestInFile(firstNumber, secondNumber, expectedResult, actualResult)
                    else:
                        self.writeFAILEDTestInFile(firstNumber, secondNumber, expectedResult, actualResult)
                else:
                    #Si el assert dió true es porque el test está bien
                    self.writeOKTestInFile(firstNumber, secondNumber, expectedResult)
                finally:
                    self.file.write("\n")
                    firstNumberInput.clear()
                    secondNumberInput.clear()
                    clearButton.click()

    def writeOKTestInFile(self, firstNumber, secondNumber, expectedResult):
        self.file.write("Test OK: Inputs( "+ firstNumber + ", " + secondNumber + " )\n")
        self.file.write("Real Result: " + expectedResult + "\n")
    
    def writeFAILEDTestInFile(self, firstNumber, secondNumber, expectedResult, actualResult):
        self.file.write("Test FAILED: Inputs( "+ firstNumber + ", " + secondNumber + " )\n")
        self.file.write("Expected Result: " + expectedResult + "\n")
        self.file.write("Actual Result: " + actualResult + "\n")

    def tearDown(self):
        self.file.close()
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()        
