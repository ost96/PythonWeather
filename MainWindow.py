from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys
import vtk
from vtk.qt.QVTKRenderWindowInteractor import *


class MainWindow(QWidget):

    def __init__(self):
        super().__init__()
        self.hasLoadBeenVisited = False
        self.frame = QFrame()
        self.initUI()


    def initUI(self):
        # CZĘŚ APLIKACJI Z WYKRESAMI
        hboxw1 = QHBoxLayout()
        lbl = QLabel("Choose city:")
        hboxw1.addWidget(lbl)

        dropdown1 = QComboBox()
        dropdown1.addItem("Warszawa")
        dropdown1.addItem("Kraków")
        dropdown1.addItem("Poznań")
        hboxw1.addWidget(dropdown1)

        # CZĘŚ APLIKACJI Z MAPĄ POLSKI
        hbox1 = QHBoxLayout()
        lbl = QLabel("Choose date:")
        hbox1.addWidget(lbl)

        dropdown1 = QComboBox()
        dropdown1.addItem("16.01.19")
        dropdown1.addItem("17.01.19")
        dropdown1.addItem("18.01.19")
        hbox1.addWidget(dropdown1)

        hbox2 = QHBoxLayout()

        vtk_widget = QVTKRenderWindowInteractor(self.frame)

        png_reader = vtk.vtkPNGReader()
        png_reader.SetFileName("Polska.png")
        png_reader.Update()
        image_data = png_reader.GetOutput()

        image_actor = vtk.vtkImageActor()
        image_actor.SetInputData(image_data) #mb zła wersja


        ren = vtk.vtkRenderer()

        ren.AddActor(image_actor)

        render_window = vtk_widget.GetRenderWindow()

        render_window.AddRenderer(ren)

        render_window_interactor = vtk.vtkRenderWindowInteractor()
        render_window_interactor.SetRenderWindow(render_window)

        # 2 linijki poniżej regulują interaktor, nie wiem czemu nie działa.
        int_style = vtk.vtkInteractorStyleTrackballCamera()
        render_window_interactor.SetInteractorStyle(int_style)

        render_window.Render()

        vtk_widget.Initialize()
        vtk_widget.Start()
        hbox2.addWidget(vtk_widget)

        mainhbox = QHBoxLayout()

        vbox1 = QVBoxLayout()
        vbox1.addLayout(hboxw1)

        vbox2 = QVBoxLayout()
        vbox2.addLayout(hbox1)
        vbox2.addLayout(hbox2)

        mainhbox.addLayout(vbox1)
        mainhbox.addLayout(vbox2)
        self.setLayout(mainhbox)
        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainWindow()
    sys.exit(app.exec_())