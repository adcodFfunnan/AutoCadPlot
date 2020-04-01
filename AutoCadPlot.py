from PyQt5.QtWidgets import *
from PyQt5 import QtGui
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QVariant





class WidgetGallery(QDialog):
    def __init__(self):

        

        


        super(WidgetGallery, self).__init__()

        

        self.createTopRightGroupBox()
        self.CreatePrinterPropertis()
        self.CreatePaperPropertis()
        self.CreateCoordinatesInput_1()
        self.CreateCoordinatesInput_2()
        self.CreateButton()
        self.CreatePlotOptions()
        self.CreateDrawingOrientation()
        self.CreatePaperLenght()
        self.CreateOutputFolder()
        self.CheckPrinterForOutputFolder()
        self.resize(600,300)
        font=self.font()
        font.setPointSize(font.pointSize()*1.3)
        self.setFont(font)
        
        
        
        self.setWindowTitle("AutoCadPlot")
        self.setWindowIcon(QtGui.QIcon("data\img\min.png"))
        flags=Qt.WindowFlags(Qt.Window | Qt.WindowCloseButtonHint)
        self.setWindowFlags(flags)
     

       
       
        

        mainLayout = QGridLayout()
       
        mainLayout.addWidget(self.GroupBox,1,2)
        mainLayout.addWidget(self.GroupBoxPrinter,1,1)
        mainLayout.addWidget(self.GroupBoxPaper,2,1)
        mainLayout.addWidget(self.GroupBoxCoordinates_start,3,1)
        mainLayout.addWidget(self.GroupBoxCoordinates_end,4,1)
        mainLayout.addWidget(self.groupBoxPaperLength,2,2)
        mainLayout.addWidget(self.groupBoxPlotOptions,3,2)
        mainLayout.addWidget(self.groupBoxDrawingOrientation,4,2)
        mainLayout.addLayout(self.ButtonLayout,5,2)
        mainLayout.addWidget(self.groupBoxOutputFolder,5,1)
        
     
     
        mainLayout.setColumnStretch(1,1)
        mainLayout.setColumnStretch(2,1)
        self.setLayout(mainLayout)


    def createTopRightGroupBox(self):
        self.GroupBox=QGroupBox("Plot style table (pen assigments)")
       
        layout=QGridLayout()
        self.styleComboBox_PlotStyle=QComboBox()
        self.styleComboBox_PlotStyle.addItems(self.getInputAndOrderIt()[4:6])
        layout.addWidget(self.styleComboBox_PlotStyle,1,1)
     
        self.GroupBox.setLayout(layout)

    def CreatePrinterPropertis(self):
        self.GroupBoxPrinter=QGroupBox("Printer/plotter")
        layout=QGridLayout()
        self.styleComboBox_printer=QComboBox()
        label=QLabel("Name: ")
        self.styleComboBox_printer.addItems(self.getInputAndOrderIt()[2:4])
        layout.addWidget(label,1,1)
        layout.addWidget(self.styleComboBox_printer,1,2)
        layout.setColumnStretch(2,1)
        self.styleComboBox_printer.currentIndexChanged.connect(self.CheckPrinterForOutputFolder)
       
        self.GroupBoxPrinter.setLayout(layout)

    def CreatePaperPropertis(self):
        self.GroupBoxPaper=QGroupBox("Paper size ")
        layout=QGridLayout()
        label=QLabel("Paper: ")
        self.styleComboBox=QComboBox()      
        self.styleComboBox.addItems(self.getInputAndOrderIt()[0:2])


        layout.addWidget(label,1,1)
        layout.addWidget(self.styleComboBox,1,2)
        layout.setColumnStretch(2,1)
        self.GroupBoxPaper.setLayout(layout)

    def getInputAndOrderIt(self):
        data=self.openFileForRead("data\pickle.txt")
        list=[]
        string=""
        for char in data:
            if char!="\n":
                string=string+char
            else:
                list.append(string)
                string=""
        return list




    def save_as_default(self):
        
        
        pickle_string=self.openFileForRead("data\pickle.txt")
        list=self.getInputAndOrderIt()
        if self.styleComboBox.currentText()!=list[0]:
            list[1]=list[0]
            list[0]=self.styleComboBox.currentText()

        if self.styleComboBox_printer.currentText()!=list[2]:
            for i in range(3):
                if self.styleComboBox_printer.currentText()==list[i+2]:
                    list[i+2]=list[2]
                    list[2]=self.styleComboBox_printer.currentText()
                    break

            

        if self.styleComboBox_PlotStyle.currentText()!=list[4]:
            list[5]=list[4]
            list[4]=self.styleComboBox_PlotStyle.currentText()

        if self.line.text()!=list[6]:
            list[6]=self.line.text()

        if self.checkBox_1.isChecked()==True:
            list[7]="True"
        else:
            list[7]=""


        if self.checkBox_1_radio.isChecked()==True:
            list[8]="True"
        else:
            list[8]=""

        if self.checkBox_2_radio.isChecked()==True:
            list[9]="True"
        else:
            list[9]=""

        if self.line_outputFolder.text()!=list[10] and self.CheckIfIt_is_Locked==0:
            list[10]=self.line_outputFolder.text()






        data=""
        for item in list:
            data+=item
            data+="\n"

        self.writeInFile("data\pickle.txt",data)









    


       



    def CreateCoordinatesInput_1(self):
        self.GroupBoxCoordinates_start=QGroupBox("Start coordinates")
        layout=QGridLayout()
        self.lineEdit_X_S=QLineEdit()
        self.lineEdit_Y_S=QLineEdit()
        label_X=QLabel("X: ")
        label_Y=QLabel("Y: ")
        layout.addWidget(label_X,1,1)
        layout.addWidget(label_Y,2,1)
        layout.addWidget(self.lineEdit_X_S,1,3)
        layout.addWidget(self.lineEdit_Y_S,2,3)
        layout.setRowStretch(3,1)
        
        self.GroupBoxCoordinates_start.setLayout(layout)

    def CreateCoordinatesInput_2(self):
        self.GroupBoxCoordinates_end=QGroupBox("End coordinates")
        layout=QGridLayout()
        self.lineEdit_X_E=QLineEdit()
        self.lineEdit_Y_E=QLineEdit()
        label_X=QLabel("X: ")
        label_Y=QLabel("Y: ")
        layout.addWidget(label_X,1,1)
        layout.addWidget(label_Y,2,1)
        layout.addWidget(self.lineEdit_X_E,1,3)
        layout.addWidget(self.lineEdit_Y_E,2,3)
        layout.setRowStretch(3,1)
        self.GroupBoxCoordinates_end.setLayout(layout)

    def CreateButton(self):
       
        self.ButtonLayout=QGridLayout()
        okButton=QPushButton("OK")
        okButton.clicked.connect(self.on_buttonOK_clicked)

        cancelButton=QPushButton("Cancel")
        cancelButton.clicked.connect(self.on_buttonCancel_clicked)
        helpButton=QPushButton("Save As Default")
       
        self.ButtonLayout.addWidget(okButton,2,1)
        self.ButtonLayout.addWidget(cancelButton,2,2)
        self.ButtonLayout.addWidget(helpButton,2,3)
        helpButton.clicked.connect(self.save_as_default)
        self.ButtonLayout.setRowStretch(1,1)
        
        

    def CreatePlotOptions(self):
        self.groupBoxPlotOptions=QGroupBox("Plot options")
        layout=QGridLayout()
        self.checkBox_1=QCheckBox("Plot object lineweights")
        self.checkBox_1.setChecked(bool(self.getInputAndOrderIt()[7]))
        layout.addWidget(self.checkBox_1)
        layout.setRowStretch(2,1)
     
        self.groupBoxPlotOptions.setLayout(layout)

    def CreateDrawingOrientation(self):
        self.groupBoxDrawingOrientation=QGroupBox("Drawing orientation")
        layout=QGridLayout()
        self.checkBox_1_radio=QRadioButton("Portrait")
        self.checkBox_1_radio.setChecked(bool(self.getInputAndOrderIt()[8]))
        self.checkBox_2_radio=QRadioButton("Landscape")
        self.checkBox_2_radio.setChecked(bool(self.getInputAndOrderIt()[9]))

        layout.addWidget(self.checkBox_1_radio)
        layout.addWidget(self.checkBox_2_radio)
        layout.setRowStretch(3,1)
        self.groupBoxDrawingOrientation.setLayout(layout)

    def CreatePaperLenght(self):
        self.groupBoxPaperLength=QGroupBox("Drawing lenght")
        layout=QHBoxLayout()
        self.line=QLineEdit()
        self.line.setText(self.getInputAndOrderIt()[6])
        layout.addWidget(self.line)
        self.groupBoxPaperLength.setLayout(layout)

    def CreateOutputFolder(self):
        self.groupBoxOutputFolder=QGroupBox("Output folder")
        layout=QGridLayout()
        self.line_outputFolder=QLineEdit()
        self.line_outputFolder.setText(self.getInputAndOrderIt()[10])
        layout.addWidget(self.line_outputFolder)
        layout.setRowStretch(2,1)
        self.groupBoxOutputFolder.setLayout(layout)
        self.CheckIfIt_is_Locked=0

    def CheckPrinterForOutputFolder(self):

        if self.styleComboBox_printer.currentText()!="DWG To PDF":
            self.line_outputFolder.setStyleSheet("background-color: rgb(224,224,224);")
            self.line_outputFolder.setReadOnly(1)
            self.CheckIfIt_is_Locked=1
        else:
            self.line_outputFolder.setStyleSheet("background-color: rgb(255,255,255);")
            self.line_outputFolder.setReadOnly(0)
            self.CheckIfIt_is_Locked=0







    def on_buttonOK_clicked(self):
        if (self.getCoordinatesInput()==1):
            final_string=self.setCoordinates()
            self.writeInFile("AutoCadPlot.scr",final_string)

    def on_buttonCancel_clicked(self):
        app.exit()

    def setCoordinates(self):
        X1=self.ListInputCoordinates[0]
        Y1=self.ListInputCoordinates[1]
        X2=self.ListInputCoordinates[2]
        Y2=self.ListInputCoordinates[3]

        Check_DWG_Format=0

        PaperFormat=self.styleComboBox.currentText()
        if PaperFormat=="A4" and self.styleComboBox_printer.currentText()=="DWG To PDF":
            PaperFormat="ISO expand A4 (297.00 x 210.00 MM)"
            Check_DWG_Format=1

        else:
            if PaperFormat=="A3" and self.styleComboBox_printer.currentText()=="DWG To PDF":
                PaperFormat="ISO expand A3 (420.00 x 297.00 MM)"
                Check_DWG_Format=1
        



        LanscapeOrPortrait=""
        if self.checkBox_1_radio.isChecked()==True:
            LanscapeOrPortrait="Portrait"
        else:
            LanscapeOrPortrait="Landscape"

        PlotWithPlotStyle=""

        if self.checkBox_1.isChecked()==True:
            PlotLineWeight="Yes"
        else:
            PlotLineWeight="No"     




        howMuch=int(abs(X2-X1)/self.drawingLength)
        space=(abs(X2-X1)-self.drawingLength*howMuch)/(howMuch-1)

       
       
        listXCoordinates=[]
        listYCoordinates=[]
        first_string="PLOT"+"\n"+"Y"+"\n"+"\n"+self.styleComboBox_printer.currentText()+".pc3"+"\n"+PaperFormat+"\n"+"\n"+LanscapeOrPortrait+"\n"+"\n"+"Window"+"\n"
        second_string="\n"+"Fit"+"\n"+"Center"+"\n"+"\n"+self.styleComboBox_PlotStyle.currentText()+"\n"+PlotLineWeight+"\n"+"\n"
        third_string="\n"+"\n"+"\n"
        final_string=""
        j=0
        X1=X1-space
        for i in range(howMuch):
            X1=X1+space
            listXCoordinates.append(X1-0.025)
            listYCoordinates.append(Y1+0.025)
            X1+=self.drawingLength
            listXCoordinates.append(X1+0.025)
            listYCoordinates.append(Y2-0.025)
        for i in range(howMuch):
            final_string+=first_string
            final_string+=str(listXCoordinates[j])+","+str(listYCoordinates[j])+"\n"
            j+=1
            final_string+=str(listXCoordinates[j])+","+str(listYCoordinates[j])
            j+=1
            final_string+=second_string
            if Check_DWG_Format==1:
                final_string+=self.line_outputFolder.text()+"\\"+str(i+1)+".pdf"
            else:
                final_string+="N"

            
            final_string+=third_string

     
        

        return final_string


    def writeInFile(self,filename,data):
        txt=open(filename,'w')
        txt.write(data)
        txt.close()

    def openFileForRead(self,filename):
        txt=open(filename,'r')
        data=txt.read()
        txt.close()
        return data
        



    def getCoordinatesInput(self):

        succes=0
        alert=QMessageBox()
        alert.setWindowIcon(QtGui.QIcon("data\img\min.png"))
        

        alert.setWindowTitle("AutoCadPlot")
        alert.setText("Check inputs")
        start_x=self.lineEdit_X_S.text()
        start_y=self.lineEdit_Y_S.text()
        end_x=self.lineEdit_X_E.text()
        end_y=self.lineEdit_Y_E.text()
        self.ListInputCoordinates=[start_x,start_y,end_x,end_y]
        for i in range(4):
            try:
                self.ListInputCoordinates[i]=float(self.ListInputCoordinates[i])
                
                
            except:
               
                alert.exec_()
                break

            if i==3:

                try:
                    self.drawingLength=float(self.line.text())

                except:

                     alert.exec_()
                     break


                
                succes=1
               
        return succes    

    




if __name__ == '__main__':

    import sys
    app = QApplication(sys.argv)
   
    gallery = WidgetGallery()
    gallery.show()    
    sys.exit(app.exec_())



