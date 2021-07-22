from New_GUI1 import *


class Calculator:
    def __init__(self):
        ui.CLR_MAIN.clicked.connect(self.clear)
        ui.CAL_BMI.clicked.connect(self.bmi)
        ui.CAL_IDL.clicked.connect(self.idwt)
        ui.CAL_BF.clicked.connect(self.bodyfat)
        ui.CAL_BMR.clicked.connect(self.bmr)

    def clear(self):
        ui.Age_lineEdit_2.setText("")
        ui.Height_LineEdit_2.setText("")
        ui.Weight_LineEdit_2.setText("")

    def bmi(self):
        height = float(ui.Height_LineEdit_2.text())
        weight = float(ui.Weight_LineEdit_2.text())
        try:
            BMI = float(weight / (height * height)*10000)
            bmi_r = round(BMI, 4)
            ui.BM_SCORE.setText(str(bmi_r))
            if BMI<16:
                ui.CAT_RES.setText("Severe Thinness")
            elif BMI>=16 and BMI<17:
                ui.CAT_RES.setText("Moderate Thinness")
            elif BMI>=17 and BMI<18.5:
                ui.CAT_RES.setText("Mild Thinness")
            elif BMI>=18.5 and BMI<25:
                ui.CAT_RES.setText("Normal")
            elif BMI>=25 and BMI<30:
                ui.CAT_RES.setText("Overweight")
            elif BMI>=30 and BMI<35:
                ui.CAT_RES.setText("Obese Class I")
            elif BMI>=35 and BMI<40:
                ui.CAT_RES.setText("Obese Class II")
            else:
                ui.CAT_RES.setText("Obese Class III")
        except:
            pass

    def idwt(self):
        height = float(ui.Height_LineEdit_2.text())
        try:
            male = 50 + (0.91*(height-152.4))
            male_id = round(male, 4)
            female = 45.5 + (0.91*(height-152.4))
            female_id = round(female, 4)
            if ui.Male_2.isChecked():
                ui.IDL_SCORE.setText(str(male_id))
            else:
                ui.IDL_SCORE.setText(str(female_id))
        except:
            print("Error")

    def bodyfat(self):
        height = float(ui.Height_LineEdit_2.text())
        age = int(ui.Age_lineEdit_2.text())
        weight = float(ui.Weight_LineEdit_2.text())
        try:
            bmi1 = float(weight / (height * height)*10000)
            bmi_bf = round(bmi1, 4)
            ui.BMIBF_ANS.setText(str(bmi_bf))
            male1 = ((1.20*bmi1)+(0.23*age) - 16.2)
            male_bf = round(male1, 4)
            female1 =((1.20*bmi1)+(0.23*age) - 5.4)
            female_bf = round(female1, 4)
            if ui.Male_2.isChecked():
                ui.BF_SCORE.setText(str(male_bf) + "%")
            else:
                ui.BF_SCORE.setText(str(female_bf) + "%")
        except:
            print("Error")

    def bmr(self):
        height = float(ui.Height_LineEdit_2.text())
        age = int(ui.Age_lineEdit_2.text())
        weight = float(ui.Weight_LineEdit_2.text())
        try:
            male_cal = (10*weight)+(6.25*height)-(5*age)+5
            male_bmr_cal = round(male_cal, 4)
            female_cal = (10*weight)+(6.25*height)-(5*age)-161
            female_bmr_cal = round(female_cal, 4)
            male_kj = ((10*weight)+(6.25*height)-(5*age)+5)*4.184
            male_bmr_kj = round(male_kj, 4)
            female_kj = ((10*weight)+(6.25*height)-(5*age)-161)*4.184
            female_bmr_kj = round(female_kj, 4)
            if ui.Male_2.isChecked():
                if ui.CAL_RADIO.isChecked():
                    ui.RES_BOX.setText(str(male_bmr_cal))
                if ui.KJ_RADIO.isChecked():
                    ui.RES_BOX.setText(str(male_bmr_kj))
            if ui.Female_2.isChecked():
                if ui.CAL_RADIO.isChecked():
                    ui.RES_BOX.setText(str(female_bmr_cal))
                if ui.KJ_RADIO.isChecked():
                    ui.RES_BOX.setText(str(female_bmr_kj))
        except:
            pass


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    File = open("Combinear.qss", 'r')
    with File:
        qss = File.read()
        app.setStyleSheet(qss)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    Calculator = Calculator()
    sys.exit(app.exec_())

