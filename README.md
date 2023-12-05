# Train neural network app #

## In General ##
This app aims to visualise training neural network process, it also may be interesting for those who want realize neural network algorithm from scratch. In this version of app NN can be trained on any dataset for your choice for solve any multiclassification task. NN uses [sigmoid](https://towardsdatascience.com/activation-functions-neural-networks-1cbd9f8d91d6 "sigmoid") activation function for each neuron. And [logloss](https://www.analyticsvidhya.com/blog/2020/11/binary-cross-entropy-aka-log-loss-the-cost-function-used-in-logistic-regression/ "Logloss") loss as a loss function.
You may chose an architecture of neural network and look how it trains in real time. This process is illustrated by changing of thickness and color of lines which corresponds to weights of neural network.

## Structure of the project ##
* Start.py - this module starts app
* create_X_Y_train.py - this module extracts necessary features from original Titanic dataset
* draw_scheme- this module creates image which corresponds to current state of neural network
* neural_network_class.py - this module implements logic of creating and training neural network
* requirements.txt - this file contains information about libs which you need to execute the project
* datasets - this folder contains some examples of datasets.

## How to start ##
1) Download all project files and place them in one folder
2) From the command line using the pip package manager, run pip install -r requirements.txt
3) Run the "Start.py" file with a program capable of opening .py format files

## After start user guide ##
1) Chose train and targets via browse buttons. You can chose one of datasets placed in datasets folder. In the field "Architecture" you need to enter n numbers separated by a space, where each value means the number of neurons in the current layer,
and the number of this value displays the number of the layer. FIRST NUMBER SHOULD CORRESPOND TO NUMBER OF FEATURES,LAST NUMBER SHOULD CORRESPOND TO NUMBER OF CLASSES. The number of neurons in hidden layers should be LESS OR EQUAL to 20. The cause of this restriction is impossibility
to show more neurons in the image field.

2) Once you have entered the correct value in the "Architecture" field, click "submit". You will see a neural network given
you architecture.
What do you see in front of you?
* Vertical sequence of circles - neural network layer
* A circle is one neuron
* The lines connecting the neurons are the weights of the neural network.
* Line colors means: black - negative weight, white - positive weight.
* After you chose one of modes you will see the iteration number and the value of cost function after iteration passed in the "3" rectangle field at the right side
  
3) Next, select one of the modes:
* "make_one_iteration" - in this mode, after each press of the "make_one_iteration" button, one epoch of neural network training occurs.
* "train" - in this mode, after pressing the "train" button, the neural network is sequentially trained until it is pressed
"Stop" button
* The "Stop" button allows you to stop training the neural network.

