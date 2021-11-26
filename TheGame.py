from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLabel, QInputDialog, QPushButton
from Example import EndGameScreen
from numpy.random import uniform
import sqlite3

from WindowSample import WindowSample
import GlobalVariables


class NotEnoughMoneyError(Exception):
    pass


class DepositAmountMustBeGreaterThanZero(Exception):
    pass


class TheGame(QWidget, WindowSample):
    def __init__(self, user_name):
        super().__init__()


        self.mainScreenSymbol = "<html><head/><body><p align=\"center\"><span style=\" font-family:\'SF Pro\'; font-size:144pt;\">􀯛</span></p></body></html>"
        self.sourceOfIncomeScreenSymbol = "<html><head/><body><p align=\"center\"><span style=\" font-family:\'SF Pro\'; font-size:144pt;\">􀖗</span></p></body></html>"
        self.developmentScreenSymbol = "<html><head/><body><p align=\"center\"><span style=\" font-family:\'SF Pro\'; font-size:144pt;\">􀝻</span></p></body></html>"

        self.propertyScreenSymbol = "<html><head/><body><p align=\"center\"><span style=\" font-family:\'SF Pro\'; font-size:144pt;\">􀎞</span></p></body></html>"

        self.sportScreenSymbol = "<html><head/><body><p align=\"center\"><span style=\" font-family:\'SF Pro\'; font-size:144pt;\">􀡥</span></p></body></html>"
        self.coursesScreenSymbol = "<html><head/><body><p align=\"center\"><span style=\" font-family:\'SF Pro\'; font-size:121pt;\">􀫓</span></p></body></html>"

        self.activeScreen = 'mainScreen'
        self.activeChapter = ''
        self.youAreStarting = ''
        self.youAreInvestingIn = ''
        self.youWantToBuy = ''
        self.youWantToWorkAs = ''
        self.userIsWorkingAs = ''

        self.moneyInvestedInGold = 0
        self.moneyInvestedInStartup = 0
        self.moneyInvestedInCurrency = 0

        self.startupEarningsRatio = 0
        self.currencyEarningsRatio = 0
        self.goldEarningsRatio = 0

        self.allIncomeFromSmallBusiness = 0
        self.allIncomeFromMediumBusiness = 0
        self.allIncomeFromBigBusiness = 0

        self.priceOfTheSmallHouse = 75000
        self.priceOfTheMediumHouse = 225000
        self.priceOfTheBigHouse = 750000

        self.userMoney = 20000
        self.userName = user_name
        self.userHealth = 100
        self.userAge = 18
        self.yearsOld = 'лет'
        self.userEnergy = 20
        self.salary = 0
        self.decreaseInHealth = 0
        self.userIsWorking = False
        self.userHasAHouse = False

        self.smallBusinessCount = 0
        self.mediumBusinessCount = 0
        self.bigBusinessCount = 0

        self.smallBusinessEarningsRatio = 0
        self.mediumBusinessEarningsRatio = 0
        self.bigBusinessEarningsRatio = 0

        self.smallBusinessIncome = 0
        self.mediumBusinessIncome = 0
        self.bigBusinessIncome = 0

        #MainScreen
        self.smallHousesCount = 0
        self.mediumHousesCount = 0
        self.bigHousesCount = 0

        self.medicineSkill = 0
        self.jurisprudenceSkill = 0
        self.programmingSkill = 0

        self.endGameScreen = EndGameScreen()

        self.buyButton = QPushButton('Купить', self)
        self.sellButton = QPushButton('Продать', self)

        self.liveAYearButton = QPushButton('Прожить год', self)
        self.skillsButton = QPushButton('Навыки', self)
        self.propertyButton = QPushButton('Имущество', self)

        self.littleHouseButton = QPushButton(f'Маленький дом,  75000$ ({self.smallHousesCount})', self)
        self.mediumHouseButton = QPushButton(f'Средний дом,  225000$ ({self.mediumHousesCount})', self)
        self.bigHouseButton = QPushButton(f'Большой дом,  750000$ ({self.bigHousesCount})', self)

        self.skillsLabel = QLabel(self)
        self.medicineLabel = QLabel(self)
        self.jurisprudenceLabel = QLabel(self)
        self.programmingLabel = QLabel(self)

        self.investedMoneyLabel = QLabel('Вложенные средства:  0$', self)

        #SourceOfIncomeScreen
        self.studentHatPictureLabel = QLabel(self)

        self.workButton = QPushButton('Работа', self)
        self.businessButton = QPushButton('Бизнес', self)
        self.depositsButton = QPushButton('Вклады', self)

        self.lawyerButton = QPushButton('Юрист,  12500$', self)
        self.doctorButton = QPushButton('Доктор,  45000$', self)
        self.programmerButton = QPushButton('Программист,  37500$', self)

        self.toGetAJobButton = QPushButton('Устроиться на работу', self)
        self.quitButton = QPushButton('Уволиться c работы', self)

        self.smallBusinessButton = QPushButton(f'Малый бизнес,  ({self.smallBusinessCount})', self)
        self.mediumBusinessButton = QPushButton(f'Средний бизнес,  ({self.mediumBusinessCount})', self)
        self.bigBusinessButton = QPushButton(f'Крупный бизнес,  ({self.bigBusinessCount})', self)

        self.startBusinessButton = QPushButton('Открыть бизнес', self)
        self.sellBusinessButton = QPushButton('Продать бизнес', self)

        self.startupButton = QPushButton('Стартап(Риск: Высокий)', self)
        self.currencyButton = QPushButton('Валюта(Риск: Средний)', self)
        self.goldButton = QPushButton('Золото(Риск: Низкий)', self)

        self.toInvestMoneyButton = QPushButton('Вложить деньги', self)
        self.withdrawAllMoneyButton = QPushButton('Вывести все деньги', self)

        self.investMoneyLabel = QLabel(self)

        self.incomeLabel = QLabel()

        #DevelopmentScreen
        self.backButton = QPushButton('Назад', self)

        self.sportButton = QPushButton('Спорт', self)
        self.coursesButton = QPushButton('Курсы', self)

        self.goJoggingButton = QPushButton('Сходить на пробежку,  0$', self)
        self.goToTheGymButton = QPushButton('Сходить в тренажерный зал,  350$', self)
        self.goToThePoolButton = QPushButton('Сходить в бассейн,  250$', self)

        self.programmingButton = QPushButton('Программирование,  700$', self)
        self.medicineButton = QPushButton('Медицина,  800$', self)
        self.socialStudiesButton = QPushButton('Юриспруденция,  500$', self)

        self.setupUi(self)
        self.initUI()

    def initUI(self):
        self.setWindowTitle('Главная')
        self.move(425, 125)
        self.userLabel.setText(f'{self.userName},  {self.userAge} {self.yearsOld}')
        self.moneyLabel.setText(f'{self.userMoney}$')

        #MainScreen
        self.liveAYearButton.resize(250, 45)
        self.liveAYearButton.move(25, 372)
        self.liveAYearButton.clicked.connect(self.liveAYearButtonFunction)

        self.propertyButton.resize(250, 45)
        self.propertyButton.move(25, 330)
        self.propertyButton.clicked.connect(self.showPropertyButtons)

        self.skillsButton.resize(250, 45)
        self.skillsButton.move(25, 288)
        self.skillsButton.clicked.connect(self.showSkillLabels)

        self.littleHouseButton.resize(250, 45)
        self.littleHouseButton.move(25, 342)
        self.littleHouseButton.hide()
        self.littleHouseButton.clicked.connect(self.showBuySellButtons)

        self.mediumHouseButton.resize(250, 45)
        self.mediumHouseButton.move(25, 300)
        self.mediumHouseButton.hide()
        self.mediumHouseButton.clicked.connect(self.showBuySellButtons)

        self.bigHouseButton.resize(250, 45)
        self.bigHouseButton.move(25, 259)
        self.bigHouseButton.hide()
        self.bigHouseButton.clicked.connect(self.showBuySellButtons)

        self.buyButton.resize(120, 45)
        self.buyButton.move(25, 332)
        self.buyButton.hide()
        self.buyButton.clicked.connect(self.buyHouse)

        self.sellButton.resize(120, 45)
        self.sellButton.move(155, 332)
        self.sellButton.hide()
        self.sellButton.clicked.connect(self.sellHouse)

        self.skillsLabel.setText("Ваши навыки:")
        self.skillsLabel.move(65, 150)
        self.skillsLabel.setStyleSheet('font-size: 26pt;')
        self.skillsLabel.hide()

        self.medicineLabel.setText(f"Медицина: {self.medicineSkill}")
        self.medicineLabel.move(70, 210)
        self.medicineLabel.setStyleSheet('font-size: 17pt;')
        self.medicineLabel.hide()

        self.jurisprudenceLabel.setText(f"Юриспруденция: {self.jurisprudenceSkill}")
        self.jurisprudenceLabel.move(70, 240)
        self.jurisprudenceLabel.setStyleSheet('font-size: 17pt;')
        self.jurisprudenceLabel.hide()

        self.programmingLabel.setText(f"Программирование: {self.programmingSkill}")
        self.programmingLabel.move(70, 270)
        self.programmingLabel.setStyleSheet('font-size: 17pt;')
        self.programmingLabel.hide()

        #SourceOfIncomeScreen
        self.workButton.resize(250, 45)
        self.workButton.move(25, 372)
        self.workButton.hide()
        self.workButton.clicked.connect(self.showWorkButtons)

        self.businessButton.resize(250, 45)
        self.businessButton.move(25, 330)
        self.businessButton.hide()
        self.businessButton.clicked.connect(self.showBusinessButtons)

        self.depositsButton.resize(250, 45)
        self.depositsButton.move(25, 288)
        self.depositsButton.hide()
        self.depositsButton.clicked.connect(self.showDepositsButtons)

        self.lawyerButton.resize(250, 45)
        self.lawyerButton.move(25, 342)
        self.lawyerButton.hide()
        self.lawyerButton.clicked.connect(self.showToGetAJobQuitButtons)

        self.doctorButton.resize(250, 45)
        self.doctorButton.move(25, 258)
        self.doctorButton.hide()
        self.doctorButton.clicked.connect(self.showToGetAJobQuitButtons)

        self.programmerButton.resize(250, 45)
        self.programmerButton.move(25, 300)
        self.programmerButton.hide()
        self.programmerButton.clicked.connect(self.showToGetAJobQuitButtons)

        self.smallBusinessButton.resize(250, 45)
        self.smallBusinessButton.move(25, 342)
        self.smallBusinessButton.hide()
        self.smallBusinessButton.clicked.connect(self.showStartSellBusinessButtons)

        self.mediumBusinessButton.resize(250, 45)
        self.mediumBusinessButton.move(25, 300)
        self.mediumBusinessButton.hide()
        self.mediumBusinessButton.clicked.connect(self.showStartSellBusinessButtons)

        self.bigBusinessButton.resize(250, 45)
        self.bigBusinessButton.move(25, 258)
        self.bigBusinessButton.hide()
        self.bigBusinessButton.clicked.connect(self.showStartSellBusinessButtons)

        self.startBusinessButton.resize(250, 45)
        self.startBusinessButton.move(25, 342)
        self.startBusinessButton.hide()
        self.startBusinessButton.clicked.connect(self.startBusiness)

        self.sellBusinessButton.resize(250, 45)
        self.sellBusinessButton.move(25, 300)
        self.sellBusinessButton.hide()
        self.sellBusinessButton.clicked.connect(self.sellBusiness)

        self.startupButton.resize(250, 45)
        self.startupButton.move(25, 342)
        self.startupButton.hide()
        self.startupButton.clicked.connect(self.showInvestWithdrawButtons)

        self.currencyButton.resize(250, 45)
        self.currencyButton.move(25, 300)
        self.currencyButton.hide()
        self.currencyButton.clicked.connect(self.showInvestWithdrawButtons)

        self.goldButton.resize(250, 45)
        self.goldButton.move(25, 258)
        self.goldButton.hide()
        self.goldButton.clicked.connect(self.showInvestWithdrawButtons)

        self.toGetAJobButton.resize(250, 45)
        self.toGetAJobButton.move(25, 300)
        self.toGetAJobButton.hide()
        self.toGetAJobButton.clicked.connect(self.getAJob)

        self.quitButton.resize(250, 45)
        self.quitButton.move(25, 342)
        self.quitButton.hide()
        self.quitButton.clicked.connect(self.quit)

        self.toInvestMoneyButton.resize(250, 45)
        self.toInvestMoneyButton.move(25, 300)
        self.toInvestMoneyButton.hide()
        self.toInvestMoneyButton.clicked.connect(self.toInvestMoney)

        self.withdrawAllMoneyButton.resize(250, 45)
        self.withdrawAllMoneyButton.move(25, 342)
        self.withdrawAllMoneyButton.hide()
        self.withdrawAllMoneyButton.clicked.connect(self.withdrawAllMoney)

        self.investedMoneyLabel.resize(250, 45)
        self.investedMoneyLabel.move(31, 258)
        self.investedMoneyLabel.hide()

        self.investMoneyLabel.setText("Вложить деньги")
        self.investMoneyLabel.move(10, 10)
        self.investMoneyLabel.hide()
        self.investMoneyLabel.setStyleSheet('font-size: 17pt;')

        #DevelopmentScreen
        self.sportButton.resize(250, 45)
        self.sportButton.move(25, 372)
        self.sportButton.hide()
        self.sportButton.clicked.connect(self.showSportButtons)

        self.coursesButton.resize(250, 45)
        self.coursesButton.move(25, 330)
        self.coursesButton.hide()
        self.coursesButton.clicked.connect(self.showCoursesButtons)

        self.goToThePoolButton.resize(250, 45)
        self.goToThePoolButton.move(25, 342)
        self.goToThePoolButton.hide()
        self.goToThePoolButton.clicked.connect(self.improveHealthAsResultOfGoingToThePool)

        self.goToTheGymButton.resize(250, 45)
        self.goToTheGymButton.move(25, 300)
        self.goToTheGymButton.hide()
        self.goToTheGymButton.clicked.connect(self.improveHealthFromGoingToTheGym)

        self.goJoggingButton.resize(250, 45)
        self.goJoggingButton.move(25, 258)
        self.goJoggingButton.hide()
        self.goJoggingButton.clicked.connect(self.improveHealthFromJogging)

        self.socialStudiesButton.resize(250, 45)
        self.socialStudiesButton.move(25, 342)
        self.socialStudiesButton.hide()
        self.socialStudiesButton.clicked.connect(self.improveSocialStudies)

        self.programmingButton.resize(250, 45)
        self.programmingButton.move(25, 300)
        self.programmingButton.hide()
        self.programmingButton.clicked.connect(self.improveProgramming)

        self.medicineButton.resize(250, 45)
        self.medicineButton.move(25, 258)
        self.medicineButton.hide()
        self.medicineButton.clicked.connect(self.improveMedicine)

        self.backButton.resize(237, 38)
        self.backButton.move(32, 388)
        self.backButton.hide()
        self.backButton.setStyleSheet('background-color: rgb(228, 54, 70);')
        self.backButton.clicked.connect(self.backButtonClicked)

        self.mainButton.clicked.connect(self.mainButtonClicked)
        self.sourceOfIncomeButton.clicked.connect(self.sourceOfIncomeButtonClicked)
        self.developmentButton.clicked.connect(self.developmentButtonClicked)

    def backButtonClicked(self):
        if self.activeChapter == 'propertyScreen':
            self.hidePropertyButtons()
            self.showMainButtonsFunction()
            self.pictureLabel.setText(self.mainScreenSymbol)
            self.hideSkillLabels()
            self.warningLabel.hide()
            self.investedMoneyLabel.hide()

        if self.activeChapter == 'skillsScreen':
            self.hideSkillLabels()
            self.showMainButtonsFunction()
            self.pictureLabel.show()
            self.pictureLabel.setText(self.mainScreenSymbol)
            self.hideSkillLabels()

        if self.activeChapter == 'buySellScreen':
            self.hideBuySellButtons()
            self.showPropertyButtons()
            self.pictureLabel.show()
            self.warningLabel.hide()

        if self.activeChapter == 'workScreen':
            self.hideWorkButtons()
            self.showIncomeButtons()
            self.backButton.hide()
            self.warningLabel.hide()

        if self.activeChapter == 'businessScreen':
            self.hideBusinessButtons()
            self.showIncomeButtons()
            self.backButton.hide()
            self.warningLabel.hide()

        if self.activeChapter == 'depositsScreen':
            self.warningLabel.hide()
            self.hideDepositsButtons()
            self.showIncomeButtons()
            self.backButton.hide()

        if self.activeChapter == 'startSellBusinessScreen':
            self.hideStartSellBusinessButtons()
            self.showBusinessButtons()
            self.warningLabel.hide()

        if self.activeChapter == 'toGetAJobScreen':
            self.hideToGetAJobQuitButtons()
            self.showWorkButtons()
            self.warningLabel.hide()

        if self.activeChapter == 'investWithdrawScreen':
            self.hideInvestWithdrawButtons()
            self.warningLabel.hide()
            self.showDepositsButtons()
            self.investedMoneyLabel.hide()

        if self.activeChapter == 'sportsScreen':
            self.warningLabel.hide()
            self.hideSportButtons()
            self.showDevelopmentButtons()
            self.backButton.hide()
            self.pictureLabel.setText(self.developmentScreenSymbol)
            self.pictureLabel.setGeometry(25, 115, 240, 171)

        if self.activeChapter == 'coursesScreen':
            self.warningLabel.hide()
            self.hideCoursesButtons()
            self.showDevelopmentButtons()
            self.backButton.hide()
            self.pictureLabel.setText(self.developmentScreenSymbol)
            self.pictureLabel.setGeometry(25, 115, 240, 171)

    #MainScreen
    def liveAYearButtonFunction(self):
        self.warningLabel.hide()

        self.userAge += 1

        if str(self.userAge)[-1] == '0' or str(self.userAge)[-1] == '5' or str(self.userAge)[-1] == '6' or str(self.userAge)[-1] == '7' or str(self.userAge)[-1] == '8' or str(self.userAge)[-1] == '9':
            self.yearsOld = 'лет'
        elif str(self.userAge)[-1] == '1':
            self.yearsOld = 'год'
        else:
            self.yearsOld = 'года'

        self.userLabel.setText(f'{self.userName},  {self.userAge} {self.yearsOld}')
        self.userEnergy = 20
        if self.userIsWorking:
            self.userEnergy -= 8
        if self.smallBusinessCount > 0 or self.mediumBusinessCount > 0 or self.bigBusinessCount > 0:
            self.userEnergy -= 4
        self.energyLabel.setText(f'<html><head/><body><p>Энергия: {self.userEnergy}<span style=\" font-family:\'SF Pro\';\">􀋥</span></p></body></html>')
        self.userMoney += self.salary

        self.priceOfTheSmallHouse = int(self.priceOfTheSmallHouse * 1.05)
        self.priceOfTheMediumHouse = int(self.priceOfTheMediumHouse * 1.065)
        self.priceOfTheBigHouse = int(self.priceOfTheBigHouse * 1.07)

        self.littleHouseButton.setText(f'Маленький дом,  {self.priceOfTheSmallHouse}$ ({self.smallHousesCount})',)
        self.mediumHouseButton.setText(f'Средний дом,  {self.priceOfTheMediumHouse}$ ({self.mediumHousesCount})')
        self.bigHouseButton.setText(f'Большой дом,  {self.priceOfTheBigHouse}$ ({self.bigHousesCount})',)

        self.startupEarningsRatio = uniform(-0.75, 2)
        self.currencyEarningsRatio = uniform(-0.15, 0.4)
        self.goldEarningsRatio = uniform(-0.005, 0.07)

        self.smallBusinessEarningsRatio = int(uniform(-7500, 70000))
        self.mediumBusinessEarningsRatio = int(uniform(-25000, 180000))
        self.bigBusinessEarningsRatio = int(uniform(-75000, 550000))

        self.allIncomeFromSmallBusiness = self.smallBusinessEarningsRatio * self.smallBusinessCount
        self.allIncomeFromMediumBusiness = self.mediumBusinessEarningsRatio * self.mediumBusinessCount
        self.allIncomeFromBigBusiness = self.bigBusinessEarningsRatio * self.bigBusinessCount
        self.userMoney += self.allIncomeFromSmallBusiness + self.allIncomeFromMediumBusiness + self.allIncomeFromBigBusiness

        self.moneyInvestedInStartup = self.moneyInvestedInStartup + (self.moneyInvestedInStartup * self.startupEarningsRatio)
        self.moneyInvestedInStartup = int(self.moneyInvestedInStartup)
        self.moneyInvestedInGold = self.moneyInvestedInGold + (self.moneyInvestedInGold * self.goldEarningsRatio)
        self.moneyInvestedInGold = int(self.moneyInvestedInGold)
        self.moneyInvestedInCurrency = self.moneyInvestedInCurrency + (self.moneyInvestedInCurrency * self.currencyEarningsRatio)
        self.moneyInvestedInCurrency = int(self.moneyInvestedInCurrency)

        self.moneyLabel.setText(f'{self.userMoney}$')

        if self.userAge >= 25 and self.userAge <= 30:
            self.decreaseInHealth = 1
            self.userHealth -= self.decreaseInHealth

        if self.userAge >= 31 and self.userAge <= 34:
            self.decreaseInHealth = 2
            self.userHealth -= self.decreaseInHealth

        if self.userAge >= 35 and self.userAge <= 37:
            self.decreaseInHealth = 3
            self.userHealth -= self.decreaseInHealth

        if self.userAge >= 38 and self.userAge <= 39:
            self.decreaseInHealth = 4
            self.userHealth -= self.decreaseInHealth

        if self.userAge >= 40 and self.userAge <= 41:
            self.decreaseInHealth = 5
            self.userHealth -= self.decreaseInHealth

        if self.userAge > 41:
            self.decreaseInHealth += 1
            self.userHealth -= self.decreaseInHealth

        if self.smallHousesCount == 0 and self.mediumHousesCount == 0 and self.bigHousesCount == 0:
            self.userHasAHouse = False

        if self.userHasAHouse == False and self.userAge >= 25:
            self.userHealth -= 15
            self.warningLabel.show()
            self.warningLabel.setText('Теперь вы бездомный и теряете здоровье!')

        if self.userHealth <= 0:
            if int(self.userMoney) > int(GlobalVariables.lastMoney):
                GlobalVariables.lastName = self.userName
                GlobalVariables.lastAge = f'{self.userAge} {self.yearsOld}'
                GlobalVariables.lastMoney = self.userMoney
                # Подключение к БД
                con = sqlite3.connect('userSpecifications.db')

                # Создание курсора
                cur = con.cursor()

                # Выполнение запроса и получение всех результатов
                res_locations_depths1 = cur.execute("""UPDATE user SET name = ? WHERE id = 1""",
                                                   (GlobalVariables.lastName,)).fetchall()
                res_locations_depths2 = cur.execute("""UPDATE user SET age = ? WHERE id = 1""",
                                                    (GlobalVariables.lastAge,)).fetchall()
                res_locations_depths3 = cur.execute("""UPDATE user SET money = ? WHERE id = 1""",
                                                    (GlobalVariables.lastMoney,)).fetchall()
                con.commit()

                con.close()
            self.endGameScreen.show()
            self.hide()
        self.healthLabel.setText(f'Здоровье: {self.userHealth}')
        self.healthLabel.show()

    def hideMainButtonsFunction(self):
        self.liveAYearButton.hide()
        self.skillsButton.hide()
        self.propertyButton.hide()

    def showMainButtonsFunction(self):
        self.liveAYearButton.show()
        self.skillsButton.show()
        self.propertyButton.show()

    def hideSkillLabels(self):
        self.skillsLabel.hide()
        self.medicineLabel.hide()
        self.jurisprudenceLabel.hide()
        self.programmingLabel.hide()
        self.backButton.hide()

    def showSkillLabels(self):
        self.skillsLabel.show()
        self.medicineLabel.show()
        self.jurisprudenceLabel.show()
        self.programmingLabel.show()
        self.hideMainButtonsFunction()
        self.backButton.show()
        self.pictureLabel.hide()
        self.activeChapter = 'skillsScreen'
        self.setWindowTitle('Навыки')

    def hidePropertyButtons(self):
        self.littleHouseButton.hide()
        self.mediumHouseButton.hide()
        self.bigHouseButton.hide()
        self.backButton.hide()

    def showPropertyButtons(self):
        self.littleHouseButton.show()
        self.mediumHouseButton.show()
        self.bigHouseButton.show()
        self.hideMainButtonsFunction()
        self.pictureLabel.show()
        self.pictureLabel.setText(self.propertyScreenSymbol)
        self.pictureLabel.setGeometry(50, 80, 191, 171)
        self.backButton.show()
        self.activeChapter = 'propertyScreen'
        self.setWindowTitle('Имущество')

    def hideBuySellButtons(self):
        self.buyButton.hide()
        self.sellButton.hide()
        self.backButton.hide()

    def showBuySellButtons(self):
        propertyType = self.sender().text().split()[0]

        self.buyButton.show()
        self.sellButton.show()
        self.hidePropertyButtons()
        self.backButton.show()
        self.activeChapter = 'buySellScreen'

        if propertyType == 'Маленький':
            self.youWantToBuy = 'smallHouse'
            self.setWindowTitle('Маленький дом')
        if propertyType == 'Средний':
            self.youWantToBuy = 'mediumHouse'
            self.setWindowTitle('Средний дом')
        if propertyType == 'Большой':
            self.youWantToBuy = 'bigHouse'
            self.setWindowTitle('Большой дом')

    def buyHouse(self):
        if self.youWantToBuy == 'smallHouse':
            if self.userEnergy >= 2:
                if self.userMoney >= self.priceOfTheSmallHouse:
                    self.warningLabel.hide()
                    self.userMoney -= self.priceOfTheSmallHouse
                    self.moneyLabel.setText(f'{self.userMoney}$')
                    self.moneyLabel.show()
                    self.userEnergy -= 2
                    self.energyLabel.setText(f'<html><head/><body><p>Энергия: {self.userEnergy}<span style=\" font-family:\'SF Pro\';\">􀋥</span></p></body></html>')
                    self.smallHousesCount += 1
                    self.littleHouseButton.setText(f'Маленький дом,  {self.priceOfTheSmallHouse}$ ({self.smallHousesCount})')
                else:
                    self.warningLabel.show()
                    self.warningLabel.setText('Недостаточно средств')
            else:
                self.warningLabel.show()
                self.warningLabel.setText('Недостаточно энергии')

        elif self.youWantToBuy == 'mediumHouse':
            if self.userEnergy >= 2:
                if self.userMoney >= self.priceOfTheMediumHouse:
                    self.warningLabel.hide()
                    self.userMoney -= self.priceOfTheMediumHouse
                    self.moneyLabel.setText(f'{self.userMoney}$')
                    self.moneyLabel.show()
                    self.userEnergy -= 2
                    self.energyLabel.setText(f'<html><head/><body><p>Энергия: {self.userEnergy}<span style=\" font-family:\'SF Pro\';\">􀋥</span></p></body></html>')
                    self.mediumHousesCount += 1
                    self.mediumHouseButton.setText(f'Средний дом,  {self.priceOfTheMediumHouse}$ ({self.mediumHousesCount})')
                else:
                    self.warningLabel.show()
                    self.warningLabel.setText('Недостаточно денег')
            else:
                self.warningLabel.show()
                self.warningLabel.setText('Недостаточно энергии')
        elif self.youWantToBuy == 'bigHouse':
            if self.userEnergy >= 2:
                if self.userMoney >= self.priceOfTheBigHouse:
                    self.warningLabel.hide()
                    self.userMoney -= self.priceOfTheBigHouse
                    self.moneyLabel.setText(f'{self.userMoney}$')
                    self.moneyLabel.show()
                    self.userEnergy -= 2
                    self.energyLabel.setText(f'<html><head/><body><p>Энергия: {self.userEnergy}<span style=\" font-family:\'SF Pro\';\">􀋥</span></p></body></html>')
                    self.bigHousesCount += 1
                    self.bigHouseButton.setText(f'Крупный дом,  {self.priceOfTheBigHouse}$ ({self.bigHousesCount})')
                else:
                    self.warningLabel.show()
                    self.warningLabel.setText('Недостаточно денег')
            else:
                self.warningLabel.show()
                self.warningLabel.setText('Недостаточно энергии')
        self.userHasAHouse = True

    def sellHouse(self):
        if self.youWantToBuy == 'smallHouse':
            if self.smallHousesCount > 0:
                if self.userEnergy >= 2:
                    self.warningLabel.hide()
                    self.userMoney += self.priceOfTheSmallHouse
                    self.moneyLabel.setText(f'{self.userMoney}$')
                    self.moneyLabel.show()
                    self.userEnergy -= 2
                    self.energyLabel.setText(f'<html><head/><body><p>Энергия: {self.userEnergy}<span style=\" font-family:\'SF Pro\';\">􀋥</span></p></body></html>')
                    self.smallHousesCount -= 1
                    self.littleHouseButton.setText(f'Маленький дом,  {self.priceOfTheSmallHouse}$ ({self.smallHousesCount})')
                else:
                    self.warningLabel.show()
                    self.warningLabel.setText('Недостаточно энергии')
            else:
                self.warningLabel.show()
                self.warningLabel.setText('У вас нет такого дома!')
        elif self.youWantToBuy == 'mediumHouse':
            if self.mediumHousesCount > 0:
                if self.userEnergy >= 2:
                    self.warningLabel.hide()
                    self.userMoney += self.priceOfTheMediumHouse
                    self.moneyLabel.setText(f'{self.userMoney}$')
                    self.moneyLabel.show()
                    self.userEnergy -= 2
                    self.energyLabel.setText(f'<html><head/><body><p>Энергия: {self.userEnergy}<span style=\" font-family:\'SF Pro\';\">􀋥</span></p></body></html>')
                    self.mediumHousesCount -= 1
                    self.mediumHouseButton.setText(f'Средний дом,  {self.priceOfTheMediumHouse}$ ({self.mediumHousesCount})')
                else:
                    self.warningLabel.show()
                    self.warningLabel.setText('Недостаточно энергии')
            else:
                self.warningLabel.show()
                self.warningLabel.setText('У вас нет такого дома!')
        elif self.youWantToBuy == 'bigHouse':
            if self.bigHousesCount > 0:
                if self.userEnergy >= 2:
                    self.warningLabel.hide()
                    self.userMoney += self.priceOfTheBigHouse
                    self.moneyLabel.setText(f'{self.userMoney}$')
                    self.moneyLabel.show()
                    self.userEnergy -= 2
                    self.energyLabel.setText(f'<html><head/><body><p>Энергия: {self.userEnergy}<span style=\" font-family:\'SF Pro\';\">􀋥</span></p></body></html>')
                    self.bigHousesCount -= 1
                    self.bigHouseButton.setText(f'Крупный дом,  {self.priceOfTheBigHouse}$ ({self.bigHousesCount})')
                else:
                    self.warningLabel.show()
                    self.warningLabel.setText('Недостаточно энергии')
            else:
                self.warningLabel.show()
                self.warningLabel.setText('У вас нет такого дома!')


    #SourceOfIncomeScreen
    def hideIncomeButtons(self):
        self.workButton.hide()
        self.businessButton.hide()
        self.depositsButton.hide()

    def showIncomeButtons(self):
        self.workButton.show()
        self.businessButton.show()
        self.depositsButton.show()

    def hideWorkButtons(self):
        self.lawyerButton.hide()
        self.doctorButton.hide()
        self.programmerButton.hide()
        self.investedMoneyLabel.hide()
        self.warningLabel.hide()

    def showWorkButtons(self):
        self.lawyerButton.show()
        self.doctorButton.show()
        self.programmerButton.show()
        self.hideIncomeButtons()
        self.backButton.show()
        self.activeChapter = 'workScreen'
        self.setWindowTitle('Работа')

    def getAJob(self):
        self.warningLabel.hide()
        if not self.userIsWorking:
            if self.youWantToWorkAs == 'doctor':
                self.investedMoneyLabel.hide()
                if self.userEnergy >= 8:
                    if self.medicineSkill >= 50:
                        self.investedMoneyLabel.setText('Вы устроились на работу')
                        self.investedMoneyLabel.show()
                        self.userIsWorkingAs = 'doctor'
                        self.userIsWorking = True
                        self.userEnergy -= 8
                        self.salary = 45000
                        self.energyLabel.show()
                        self.energyLabel.setText(f'<html><head/><body><p>Энергия: {self.userEnergy}<span style=\" font-family:\'SF Pro\';\">􀋥</span></p></body></html>')
                    else:
                        self.warningLabel.show()
                        self.warningLabel.setText('Недостаточно навыка!')
                else:
                    self.warningLabel.show()
                    self.warningLabel.setText('Недостаточно энергии!')

            elif self.youWantToWorkAs == 'lawyer':
                self.investedMoneyLabel.hide()
                if self.userEnergy >= 8:
                    if self.jurisprudenceSkill >= 20:
                        self.investedMoneyLabel.show()
                        self.investedMoneyLabel.setText('Вы устроились на работу')
                        self.userIsWorkingAs = 'lawyer'
                        self.userIsWorking = True
                        self.userEnergy -= 8
                        self.salary = 12500
                        self.energyLabel.show()
                        self.energyLabel.setText(f'<html><head/><body><p>Энергия: {self.userEnergy}<span style=\" font-family:\'SF Pro\';\">􀋥</span></p></body></html>')
                    else:
                        self.warningLabel.show()
                        self.warningLabel.setText('Недостаточно навыка!')
                else:
                    self.warningLabel.show()
                    self.warningLabel.setText('Недостаточно энергии!')

            elif self.youWantToWorkAs == 'programmer':
                self.investedMoneyLabel.hide()
                if self.userEnergy >= 8:
                    if self.programmingSkill >= 40:
                        self.investedMoneyLabel.setText('Вы устроились на работу')
                        self.investedMoneyLabel.show()
                        self.userIsWorkingAs = 'programmer'
                        self.userIsWorking = True
                        self.userEnergy -= 8
                        self.salary = 37500
                        self.energyLabel.show()
                        self.energyLabel.setText(f'<html><head/><body><p>Энергия: {self.userEnergy}<span style=\" font-family:\'SF Pro\';\">􀋥</span></p></body></html>')
                    else:
                        self.warningLabel.show()
                        self.warningLabel.setText('Недостаточно навыка!')
                else:
                    self.warningLabel.show()
                    self.warningLabel.setText('Недостаточно энергии!')
        else:
            self.warningLabel.show()
            self.warningLabel.setText('Вы уже имеете работу!')

    def quit(self):
        self.warningLabel.hide()
        if self.userIsWorking:
            if self.youWantToWorkAs == 'doctor':
                self.investedMoneyLabel.hide()
                if self.userEnergy >= 1:
                    self.investedMoneyLabel.setText('Вы уволились с работы')
                    self.salary = 0
                    self.userIsWorking = False
                    self.userEnergy -= 1
                    self.energyLabel.show()
                    self.energyLabel.setText(f'<html><head/><body><p>Энергия: {self.userEnergy}<span style=\" font-family:\'SF Pro\';\">􀋥</span></p></body></html>')
                    self.userIsWorkingAs = ''
                else:
                    self.warningLabel.show()
                    self.warningLabel.setText('Недостаточно энергии!')

            elif self.youWantToWorkAs == 'lawyer':
                self.investedMoneyLabel.hide()
                if self.userEnergy >= 1:
                    self.investedMoneyLabel.setText('Вы уволились с работы')
                    self.salary = 0
                    self.userIsWorking = False
                    self.userEnergy -= 1
                    self.energyLabel.show()
                    self.energyLabel.setText(f'<html><head/><body><p>Энергия: {self.userEnergy}<span style=\" font-family:\'SF Pro\';\">􀋥</span></p></body></html>')
                    self.userIsWorkingAs = ''
                else:
                    self.warningLabel.show()
                    self.warningLabel.setText('Недостаточно энергии!')

            elif self.youWantToWorkAs == 'programmer':
                self.investedMoneyLabel.hide()
                if self.userEnergy >= 1:
                    self.investedMoneyLabel.setText('Вы уволились с работы')
                    self.salary = 0
                    self.userIsWorking = False
                    self.userEnergy -= 1
                    self.energyLabel.show()
                    self.energyLabel.setText(f'<html><head/><body><p>Энергия: {self.userEnergy}<span style=\" font-family:\'SF Pro\';\">􀋥</span></p></body></html>')
                    self.userIsWorkingAs = ''
                else:
                    self.warningLabel.show()
                    self.warningLabel.setText('Недостаточно энергии!')
        else:
            self.warningLabel.show()
            self.warningLabel.setText('Вы не имеете работу!')

    def hideBusinessButtons(self):
        self.smallBusinessButton.hide()
        self.mediumBusinessButton.hide()
        self.bigBusinessButton.hide()

    def showBusinessButtons(self):
        self.smallBusinessButton.show()
        self.mediumBusinessButton.show()
        self.bigBusinessButton.show()
        self.hideIncomeButtons()
        self.backButton.show()
        self.activeChapter = 'businessScreen'
        self.setWindowTitle('Бизнес')

    def hideDepositsButtons(self):
        self.startupButton.hide()
        self.currencyButton.hide()
        self.goldButton.hide()

    def showDepositsButtons(self):
        self.startupButton.show()
        self.currencyButton.show()
        self.goldButton.show()
        self.hideIncomeButtons()
        self.backButton.show()
        self.activeChapter = 'depositsScreen'
        self.setWindowTitle('Вклады')

    def hideInvestWithdrawButtons(self):
        self.toInvestMoneyButton.hide()
        self.withdrawAllMoneyButton.hide()
        self.warningLabel.hide()

    def showInvestWithdrawButtons(self):
        investment = self.sender().text()

        self.hideDepositsButtons()
        self.toInvestMoneyButton.show()
        self.withdrawAllMoneyButton.show()
        self.activeChapter = 'investWithdrawScreen'

        if investment == 'Стартап(Риск: Высокий)':
            self.youAreInvestingIn = 'startup'
            self.investedMoneyLabel.show()
            self.investedMoneyLabel.setText(f'Вложенные средства: {self.moneyInvestedInStartup}$')
            self.setWindowTitle('Стартап')
        elif investment == 'Валюта(Риск: Средний)':
            self.youAreInvestingIn = 'currency'
            self.investedMoneyLabel.show()
            self.investedMoneyLabel.setText(f'Вложенные средства: {self.moneyInvestedInCurrency}$')
            self.setWindowTitle('Валюта')
        elif investment == 'Золото(Риск: Низкий)':
            self.youAreInvestingIn = 'gold'
            self.investedMoneyLabel.show()
            self.investedMoneyLabel.setText(f'Вложенные средства: {self.moneyInvestedInGold}$')
            self.setWindowTitle('Золото')

    def hideStartSellBusinessButtons(self):
        self.startBusinessButton.hide()
        self.sellBusinessButton.hide()
        self.backButton.hide()

    def showStartSellBusinessButtons(self):
        business_type = self.sender().text().split()[0]

        self.startBusinessButton.show()
        self.sellBusinessButton.show()
        self.hideBusinessButtons()
        self.backButton.show()
        self.activeChapter = 'startSellBusinessScreen'

        if business_type == 'Малый':
            self.youAreStarting = 'smallBusiness'
            self.startBusinessButton.setText('Открыть бизнес,  200000$')
            self.sellBusinessButton.setText('Продать бизнес,  210000$')
            self.startBusinessButton.show()
            self.setWindowTitle('Малый бизнес')
        elif business_type == 'Средний':
            self.youAreStarting = 'mediumBusiness'
            self.startBusinessButton.setText('Открыть бизнес,  450000$')
            self.sellBusinessButton.setText('Продать бизнес,  465000$')
            self.startBusinessButton.show()
            self.setWindowTitle('Средний бизнес')
        elif business_type == 'Крупный':
            self.youAreStarting = 'bigBusiness'
            self.startBusinessButton.setText('Открыть бизнес,  1000000$')
            self.sellBusinessButton.setText('Продать бизнес,  1080000$')
            self.startBusinessButton.show()
            self.setWindowTitle('Крупный бизнес')

    def startBusiness(self):
        if self.youAreStarting == 'smallBusiness':
            if self.userEnergy >= 3:
                if self.userMoney >= 200000:
                    self.userEnergy -= 3
                    self.energyLabel.setText(f'<html><head/><body><p>Энергия: {self.userEnergy}<span style=\" font-family:\'SF Pro\';\">􀋥</span></p></body></html>')
                    self.warningLabel.hide()
                    self.userMoney -= 200000
                    self.moneyLabel.setText(f'{self.userMoney}$')
                    self.moneyLabel.show()
                    self.smallBusinessCount += 1
                    self.smallBusinessButton.setText(f'Малый бизнес,  ({self.smallBusinessCount})')
                else:
                    self.warningLabel.show()
                    self.warningLabel.setText('Недостаточно средств')
            else:
                self.warningLabel.show()
                self.warningLabel.setText('Недостаточно энергии')
        elif self.youAreStarting == 'mediumBusiness':
            if self.userEnergy >= 3:
                if self.userMoney >= 450000:
                    self.userEnergy -= 3
                    self.energyLabel.setText(f'<html><head/><body><p>Энергия: {self.userEnergy}<span style=\" font-family:\'SF Pro\';\">􀋥</span></p></body></html>')
                    self.warningLabel.hide()
                    self.userMoney -= 450000
                    self.moneyLabel.setText(f'{self.userMoney}$')
                    self.moneyLabel.show()
                    self.mediumBusinessCount += 1
                    self.mediumBusinessButton.setText(f'Средний бизнес,  ({self.mediumBusinessCount})')
                else:
                    self.warningLabel.show()
                    self.warningLabel.setText('Недостаточно средств')
            else:
                self.warningLabel.show()
                self.warningLabel.setText('Недостаточно энергии')
        elif self.youAreStarting == 'bigBusiness':
            if self.userEnergy >= 3:
                if self.userMoney >= 1000000:
                    self.userEnergy -= 3
                    self.energyLabel.setText(f'<html><head/><body><p>Энергия: {self.userEnergy}<span style=\" font-family:\'SF Pro\';\">􀋥</span></p></body></html>')
                    self.warningLabel.hide()
                    self.userMoney -= 1000000
                    self.moneyLabel.setText(f'{self.userMoney}$')
                    self.moneyLabel.show()
                    self.bigBusinessCount += 1
                    self.bigBusinessButton.setText(f'Крупный бизнес,  ({self.bigBusinessCount})')
                else:
                    self.warningLabel.show()
                    self.warningLabel.setText('Недостаточно средств')
            else:
                self.warningLabel.show()
                self.warningLabel.setText('Недостаточно энергии')

    def sellBusiness(self):
        if self.youAreStarting == 'smallBusiness':
            if self.smallBusinessCount > 0:
                if self.userEnergy >= 3:
                    self.userEnergy -= 3
                    self.energyLabel.setText(f'<html><head/><body><p>Энергия: {self.userEnergy}<span style=\" font-family:\'SF Pro\';\">􀋥</span></p></body></html>')
                    self.warningLabel.hide()
                    self.userMoney += 210000
                    self.moneyLabel.setText(f'{self.userMoney}$')
                    self.moneyLabel.show()
                    self.smallBusinessCount -= 1
                    self.smallBusinessButton.setText(f'Малый бизнес,  ({self.smallBusinessCount})')
                else:
                    self.warningLabel.show()
                    self.warningLabel.setText('Недостаточно энергии')
            else:
                self.warningLabel.show()
                self.warningLabel.setText('У вас нет такого бизнеса!')
        elif self.youAreStarting == 'mediumBusiness':
            if self.mediumBusinessCount > 0:
                if self.userEnergy >= 3:
                    self.userEnergy -= 3
                    self.energyLabel.setText(f'<html><head/><body><p>Энергия: {self.userEnergy}<span style=\" font-family:\'SF Pro\';\">􀋥</span></p></body></html>')
                    self.warningLabel.hide()
                    self.userMoney += 465000
                    self.moneyLabel.setText(f'{self.userMoney}$')
                    self.moneyLabel.show()
                    self.mediumBusinessCount -= 1
                    self.mediumBusinessButton.setText(f'Средний бизнес,  ({self.mediumBusinessCount})')
                else:
                    self.warningLabel.show()
                    self.warningLabel.setText('Недостаточно энергии')
            else:
                self.warningLabel.show()
                self.warningLabel.setText('У вас нет такого бизнеса!')
        elif self.youAreStarting == 'bigBusiness':
            if self.bigBusinessCount > 0:
                if self.userEnergy >= 3:
                    self.userEnergy -= 3
                    self.energyLabel.setText(f'<html><head/><body><p>Энергия: {self.userEnergy}<span style=\" font-family:\'SF Pro\';\">􀋥</span></p></body></html>')
                    self.warningLabel.hide()
                    self.userMoney += 1080000
                    self.moneyLabel.setText(f'{self.userMoney}$')
                    self.moneyLabel.show()
                    self.bigBusinessCount -= 1
                    self.bigBusinessButton.setText(f'Крупный бизнес,  ({self.bigBusinessCount})')
                else:
                    self.warningLabel.show()
                    self.warningLabel.setText('Недостаточно энергии')
            else:
                self.warningLabel.show()
                self.warningLabel.setText('У вас нет такого бизнеса!')

    def hideToGetAJobQuitButtons(self):
        self.toGetAJobButton.hide()
        self.quitButton.hide()
        self.warningLabel.hide()
        self.investedMoneyLabel.hide()

    def showToGetAJobQuitButtons(self):
        work = self.sender().text().split()[0]

        self.hideWorkButtons()
        self.toGetAJobButton.show()
        self.quitButton.show()
        self.activeChapter = 'toGetAJobScreen'

        if work == 'Доктор,':
            self.youWantToWorkAs = 'doctor'
            self.investedMoneyLabel.show()
            self.investedMoneyLabel.setText('Нужен навык медицины 50!')

        if work == 'Юрист,':
            self.youWantToWorkAs = 'lawyer'
            self.investedMoneyLabel.show()
            self.investedMoneyLabel.setText('Нужен навык юриспруденции 20!')

        if work == 'Программист,':
            self.youWantToWorkAs = 'programmer'
            self.investedMoneyLabel.show()
            self.investedMoneyLabel.setText('Нужен навык программиста 40!')

        if self.userIsWorking:
            self.investedMoneyLabel.show()
            self.investedMoneyLabel.setText('Вы уже работаете')

    def toInvestMoney(self):
        try:
            self.investMoneyLabel.setText('Вложить деньги')
            investmentAmount, invest_ok_pressed = QInputDialog.getText(self, "Вложить деньги",
                                                                       "Введите сумму вклада")
            if invest_ok_pressed:
                if investmentAmount.isdigit():
                    investmentAmount = int(investmentAmount)

                    if investmentAmount > self.userMoney:
                        raise NotEnoughMoneyError
                    elif investmentAmount <= 0:
                        raise DepositAmountMustBeGreaterThanZero
                    else:
                        self.warningLabel.hide()
                        self.investedMoneyLabel.show()

                        if self.youAreInvestingIn == 'gold':
                            self.moneyInvestedInGold += investmentAmount
                            self.investedMoneyLabel.setText(f'Вложенные средства: {self.moneyInvestedInGold}$')
                            self.userMoney -= investmentAmount
                            self.moneyLabel.setText(f'{self.userMoney}$')

                        if self.youAreInvestingIn == 'currency':
                            self.moneyInvestedInCurrency += investmentAmount
                            self.investedMoneyLabel.setText(f'Вложенные средства: {self.moneyInvestedInCurrency}$')
                            self.userMoney -= investmentAmount
                            self.moneyLabel.setText(f'{self.userMoney}$')

                        if self.youAreInvestingIn == 'startup':
                            self.moneyInvestedInStartup += investmentAmount
                            self.investedMoneyLabel.setText(f'Вложенные средства: {self.moneyInvestedInStartup}$')
                            self.userMoney -= investmentAmount
                            self.moneyLabel.setText(f'{self.userMoney}$')
                else:
                    self.warningLabel.show()
                    self.warningLabel.setText('Введите корректную сумму вклада!')

        except NotEnoughMoneyError:
            self.warningLabel.show()
            self.warningLabel.setText('Недостаточно средств')
        except DepositAmountMustBeGreaterThanZero:
            self.warningLabel.show()
            self.warningLabel.setText('Сумма вклада должна быть больше нуля!')

    def withdrawAllMoney(self):
        if self.youAreInvestingIn == 'gold':
            self.userMoney += self.moneyInvestedInGold
            self.moneyInvestedInGold = 0
            self.moneyLabel.setText(f'{self.userMoney}$')
            self.investedMoneyLabel.setText(f'Вложенные средства: {self.moneyInvestedInGold}$')

        if self.youAreInvestingIn == 'currency':
            self.userMoney += self.moneyInvestedInCurrency
            self.moneyInvestedInCurrency = 0
            self.moneyLabel.setText(f'{self.userMoney}$')
            self.investedMoneyLabel.setText(f'Вложенные средства: {self.moneyInvestedInCurrency}$')

        if self.youAreInvestingIn == 'startup':
            self.userMoney += self.moneyInvestedInStartup
            self.moneyInvestedInStartup = 0
            self.moneyLabel.setText(f'{self.userMoney}$')
            self.investedMoneyLabel.setText(f'Вложенные средства: {self.moneyInvestedInStartup}$')

    #DevelopmentScreen
    def hideDevelopmentButtons(self):
        self.sportButton.hide()
        self.coursesButton.hide()

    def showDevelopmentButtons(self):
        self.sportButton.show()
        self.coursesButton.show()

    def hideSportButtons(self):
        self.goJoggingButton.hide()
        self.goToTheGymButton.hide()
        self.goToThePoolButton.hide()
        self.backButton.hide()

    def showSportButtons(self):
        self.goJoggingButton.show()
        self.goToTheGymButton.show()
        self.goToThePoolButton.show()
        self.hideDevelopmentButtons()
        self.pictureLabel.setText(self.sportScreenSymbol)
        self.pictureLabel.setGeometry(15, 70, 270, 171)
        self.backButton.show()
        self.activeChapter = 'sportsScreen'
        self.setWindowTitle('Спорт')

    def hideCoursesButtons(self):
        self.socialStudiesButton.hide()
        self.programmingButton.hide()
        self.medicineButton.hide()
        self.backButton.hide()

    def showCoursesButtons(self):
        self.hideDevelopmentButtons()
        self.socialStudiesButton.show()
        self.programmingButton.show()
        self.medicineButton.show()
        self.pictureLabel.setText(self.coursesScreenSymbol)
        self.pictureLabel.setGeometry(52, 70, 191, 171)
        self.backButton.show()
        self.activeChapter = 'coursesScreen'
        self.setWindowTitle('Курсы')

    def hideAllButtonsOfMainScreen(self):
        self.hideMainButtonsFunction()
        self.hideSkillLabels()
        self.hidePropertyButtons()
        self.hideBuySellButtons()
        self.warningLabel.hide()

    def hideAllButtonsOfSourceOfIncomeScreen(self):
        self.hideIncomeButtons()
        self.hideWorkButtons()
        self.hideBusinessButtons()
        self.hideDepositsButtons()
        self.withdrawAllMoneyButton.hide()
        self.toInvestMoneyButton.hide()
        self.hideStartSellBusinessButtons()
        self.hideToGetAJobQuitButtons()
        self.investedMoneyLabel.hide()

    def hideAllButtonsOfDevelopmentScreen(self):
        self.hideDevelopmentButtons()
        self.hideSportButtons()
        self.hideCoursesButtons()
        self.hideSportButtons()
        self.hideCoursesButtons()

    def improveMedicine(self):
        if self.userMoney >= 800:
            if self.userEnergy >= 2:
                self.warningLabel.hide()
                self.medicineSkill += 1
                self.medicineLabel.setText(f"Медицина: {self.medicineSkill}")
                self.userMoney -= 800
                self.moneyLabel.setText(f'{self.userMoney}$')
                self.userEnergy -= 2
                self.energyLabel.setText(f'<html><head/><body><p>Энергия: {self.userEnergy}<span style=\" font-family:\'SF Pro\';\">􀋥</span></p></body></html>')
            else:
                self.warningLabel.show()
                self.warningLabel.setText('Недостаточно энергии')
        else:
            self.warningLabel.show()
            self.warningLabel.setText('Недостаточно средств')

    def improveProgramming(self):
        if self.userMoney >= 700:
            if self.userEnergy >= 2:
                self.warningLabel.hide()
                self.programmingSkill += 1
                self.programmingLabel.setText(f"Программирование: {self.programmingSkill}")
                self.userMoney -= 700
                self.moneyLabel.setText(f'{self.userMoney}$')
                self.userEnergy -= 2
                self.energyLabel.setText(f'<html><head/><body><p>Энергия: {self.userEnergy}<span style=\" font-family:\'SF Pro\';\">􀋥</span></p></body></html>')
            else:
                self.warningLabel.show()
                self.warningLabel.setText('Недостаточно энергии')
        else:
            self.warningLabel.show()
            self.warningLabel.setText('Недостаточно средств')

    def improveSocialStudies(self):
        if self.userMoney >= 500:
            if self.userEnergy >= 2:
                self.warningLabel.hide()
                self.jurisprudenceSkill += 1
                self.jurisprudenceLabel.setText(f"Юриспруденция: {self.jurisprudenceSkill}")
                self.userMoney -= 500
                self.moneyLabel.setText(f'{self.userMoney}$')
                self.userEnergy -= 2
                self.energyLabel.setText(f'<html><head/><body><p>Энергия: {self.userEnergy}<span style=\" font-family:\'SF Pro\';\">􀋥</span></p></body></html>')
            else:
                self.warningLabel.show()
                self.warningLabel.setText('Недостаточно энергии')
        else:
            self.warningLabel.show()
            self.warningLabel.setText('Недостаточно средств')

    def improveHealthFromJogging(self):
        self.warningLabel.hide()
        if self.userEnergy >= 2:
            if self.userHealth < 100:
                self.userHealth += 1
                self.healthLabel.setText(f'Здоровье: {self.userHealth}')
            else:
                self.userHealth = 100
                self.healthLabel.setText(f'Здоровье: {self.userHealth}')
            self.userEnergy -= 2
            self.energyLabel.setText(f'<html><head/><body><p>Энергия: {self.userEnergy}<span style=\" font-family:\'SF Pro\';\">􀋥</span></p></body></html>')
        else:
            self.warningLabel.show()
            self.warningLabel.setText('Недостаточно энергии')

    def improveHealthAsResultOfGoingToThePool(self):
        self.warningLabel.hide()
        if self.userEnergy >= 2:
            if self.userMoney >= 250:
                self.userEnergy -= 2
                self.userMoney -= 250
                self.warningLabel.hide()
                self.energyLabel.setText(
                    f'<html><head/><body><p>Энергия: {self.userEnergy}<span style=\" font-family:\'SF Pro\';\">􀋥</span></p></body></html>')
                if self.userHealth < 99:
                    self.userHealth += 2
                else:
                    self.userHealth = 100
                self.moneyLabel.setText(f'{self.userMoney}$')
                self.healthLabel.setText(f'Здоровье: {self.userHealth}')
            else:
                self.warningLabel.show()
                self.warningLabel.setText('Недостаточно средств')
        else:
            self.warningLabel.show()
            self.warningLabel.setText('Недостаточно энергии')

    def improveHealthFromGoingToTheGym(self):
        self.warningLabel.hide()
        if self.userEnergy >= 2:
            if self.userMoney >= 350:
                self.userEnergy -= 2
                self.userMoney -= 350
                self.warningLabel.hide()
                self.energyLabel.setText(f'<html><head/><body><p>Энергия: {self.userEnergy}<span style=\" font-family:\'SF Pro\';\">􀋥</span></p></body></html>')
                if self.userHealth < 98:
                    self.userHealth += 3
                else:
                    self.userHealth = 100
                self.moneyLabel.setText(f'{self.userMoney}$')
                self.healthLabel.setText(f'Здоровье: {self.userHealth}')
            else:
                self.warningLabel.show()
                self.warningLabel.setText('Недостаточно средств')
        else:
            self.warningLabel.show()
            self.warningLabel.setText('Недостаточно энергии')

    def mainButtonClicked(self):
        self.hideAllButtonsOfMainScreen()

        if self.activeScreen == 'sourceOfIncomeScreen':
            self.hideAllButtonsOfSourceOfIncomeScreen()
        elif self.activeScreen == 'developmentScreen':
            self.hideAllButtonsOfDevelopmentScreen()

        self.pictureLabel.show()
        self.pictureLabel.setText(self.mainScreenSymbol)

        self.setWindowTitle('Главная')
        self.activeScreen = 'mainScreen'
        self.showMainButtonsFunction()

    def sourceOfIncomeButtonClicked(self):
        self.hideAllButtonsOfSourceOfIncomeScreen()

        if self.activeScreen == 'mainScreen':
            self.hideAllButtonsOfMainScreen()
        elif self.activeScreen == 'developmentScreen':
            self.hideAllButtonsOfDevelopmentScreen()


        self.pictureLabel.setGeometry(50, 80, 191, 171)
        self.pictureLabel.show()
        self.pictureLabel.setText(self.sourceOfIncomeScreenSymbol)
        self.setWindowTitle('Источник дохода')
        self.activeScreen = 'sourceOfIncomeScreen'
        self.showIncomeButtons()

    def developmentButtonClicked(self):
        self.hideAllButtonsOfDevelopmentScreen()
        self.warningLabel.hide()

        if self.activeScreen == 'mainScreen':
                self.hideAllButtonsOfMainScreen()
        elif self.activeScreen == 'sourceOfIncomeScreen':
            self.hideAllButtonsOfSourceOfIncomeScreen()

        self.pictureLabel.show()
        self.pictureLabel.setGeometry(25, 115, 240, 171)
        self.pictureLabel.setText(self.developmentScreenSymbol)

        self.setWindowTitle('Развитие')
        self.activeScreen = 'developmentScreen'
        self.showDevelopmentButtons()
