import PySimpleGUI as sg
from draw_scheme import *
from neural_network_class import *
from create_X_Y_train import *

def create_window(width,height):
    """
        Creates window
        Input:width,height
        return:window object
    """
    #create layout. We will have 2 raws. 
    #create first raw. It consists from Text, In and buttons elements
    raw_1 = [sg.Text("Architecture:"),
        sg.In(size=(30,1),enable_events=True,key='-INPUT-'),
        sg.Text("Chose a file"),
        sg.In(size=(20,1),key="-FILE_PATH-"),
        sg.FileBrowse(key="-IN_FILE-"),
        sg.Button("submit",key="-SUB-"),
        sg.Button("make one iteration",key="-TRAIN_ONE-"), 
        sg.Button("train",key="-TRAIN-"),
        sg.Button("Stop",key="-STOP-"),]
    #create second raw. It consists from 3 frames.
    #create first frame. It consists from 5 Text elements placed vertical(description of each feature)
    frame_1 = [
        [sg.Text("Pclass")],
        [sg.Text("Sex")],
        [sg.Text("Age")],
        [sg.Text("Fare")],
        [sg.Text("SibSp")],
    ]
    #create second frame. It consists from 1 Image element(neural network scheme)
    frame_2 = [
        [sg.Image(key="-IMAGE-",size=(500,500))]
    ]
    #create third frame. It consists from 1 Text(information about cost function and number of iteration)
    frame_3 = [
        [sg.Text(size=(30,3),key="-TOUT-")]
    ]
    
    raw_2 = [
        sg.Frame("1",frame_1,),
        sg.Frame("2",frame_2,),
        sg.Frame("3",frame_3,),
    ]
    layout=[
        raw_1,
        raw_2,
    ]
    #end of layout creating
    window=sg.Window("Visualizing neural network training process",layout,size=(width,height))
    return window
def create_and_maintain_GUI():
    """
        Creates and maintanes GUI
    """
    window=create_window(1024,768)
    def update_window_after_one_iteration(number_of_iteration):
        k=number_of_iteration+1
        nn.make_one_iteration(*create(),nn.cost)
        draw_neural_network_scheme(arch,nn.weights,nn.find_max_weight())
        window["-IMAGE-"].update(filename="neural_network.png")
        window["-TOUT-"].update("epoch number {0}, cost value is {1}".format(k,round(nn.cost,5)))
    while True:#event loop
        event,values=window.read(timeout=10)
        try:
            if event=="-SUB-":
                arch=list(map(int,values["-INPUT-"].split()))
                nn=model(arch)
                draw_neural_network_scheme(arch,nn.weights,nn.find_max_weight())
                window["-IMAGE-"].update(filename="neural_network.png")
                window["-TOUT-"].update("You have just created neural network with {0} architecture!".format(nn.arch))
                k=0
            if event=="-TRAIN_ONE-":
                update_window_after_one_iteration(k)
                k+=1
            if event == "-TRAIN-":
                while nn.stop!=True:
                    window.refresh()
                    if event=="-STOP-":
                        break
                    update_window_after_one_iteration(k)
                    k+=1
                    event, values = window.read(timeout=10)
        except:
            window["-INPUT-"].update("enter correct neural network architecure")
        if event==sg.WIN_CLOSED:
            break
    window.close()
    
def run_app():
    """
        running app
    """
    create_and_maintain_GUI()
     
if __name__=="__main__":
    run_app()
