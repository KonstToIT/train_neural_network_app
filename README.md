# Train neural network app #

## In General ##
This app aims to visualise training neural network process it also may be interesting for those who want realize neural network algorithm from scratch. In this version of app the NN trains on state-of-the-art for beginner data scientists Titanic Disaster dataset, which you can find by the 
link https://www.kaggle.com/competitions/titanic. 
You may chose an architecture of neural network and look how it trains in real time. 

## Structure of the project ##
* Show_neural_network.py - this module shows GUI
* create_X_Y_train.py - this module extracts necessary features from original Titanic dataset
* draw_scheme- this module creates image which corresponds to current state of neural network
* neural_network_class.py - this module implements logic of creating and training neural network
* requirements.txt - this file contains information about libs which you need to execute the project
* train.csv - this file contains original dataset.
I) How to run?

	1) Download all project files and place them in one folder
	2) From the command line using the pip package manager, run pip install -r requirements.txt
	3) Run the "Show_neural_network.py" file with a program capable of opening .py format files

This program was created to get acquainted with how the process of training a neural network takes place.

II) After launch:

	Instructions for use:
	1) In the field "Architecture" you need to enter n numbers separated by a space, where each number means the number of neurons in the current layer,
	and the number of this number displays the number of the layer. FIRST NUMBER SHOULD BE 5, and LAST 1, because in this version, the neural network
	trained on a specific data set. The number of neurons in hidden layers should be LESS OR EQUAL to 20. The cause of this restriction is impossibility
	to show more neurons in the image field.

	2) Once you have entered the correct value in the "Architecture" field, click "submit". You will see a neural network given
	you architecture.

		What do you see in front of you?
		Vertical sequence of circles - neural network layer
		A circle is one neuron
		The lines connecting the neurons are the weights of the neural network.
		Line colors mean: black - negative weight, white - positive weight.

	3) Next, select one of the modes:
		"make_one_iteration" - in this mode, after each press of the "make_one_iteration" button, one epoch of neural network training occurs.
		"train" - in this mode, after pressing the "train" button, the neural network is sequentially trained until it is pressed
		"Stop" button
		The "Stop" button allows you to stop training the neural network.
		In both modes, the iteration number and the value of the error function for this iteration will be displayed on the right.

	4) After starting training in any of the modes, after a while you will see that the thickness of the lines has changed. Thickness change
	lines reflects the change in the weights of the neural network.
 
All training is done on the "titanic" dataset, which can be found at https://www.kaggle.com/competitions/titanic
