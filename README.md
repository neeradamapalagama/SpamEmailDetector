# Spam Message Detector
#### Video Demo:  https://youtu.be/qYL5iPkw74s
#### Description: Spam Message Detector is a command-line program designed to detect spam messages. This is my CS50P Final Project. CS50's Introduction to Programming with Python - Harvard University (This project was submitted on 12th January 2024.)

### Overview

Spam Message Detector is a command-line program designed to detect spam messages. This can be used to check messages, emails, notifications etc. Just copy & paste your text to get started. This is build using python and machine learning libraries.

### Features

- **Detect Spam Messages**: Run the program with command "python project.py" and just copy & paste your text message and enter. The results will be shown shortly. 
- **Update**: The model can be updated using command `--update` to use newly added data.
- **Reset**:The model can be reset using `--reset` command to set default models and datasets.
- **Menu**: The menu can be displayed again using `--menu` command.


### Technologies Used

- **Programming Language**: Python (And Machine Learning Technology)
- **Libraries**: `scikit-learn`, `pandas`, `imbalanced-learn`, `joblib`
- **Dataset**: spam.csv dataset (Reference: [https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset/data](https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset/data))

### Project Files

Inside the SpamEmailDetector folder, here are an introduction to the most important files and folders.

* `project.py` : Main program file
* `test_project.py`: Test cases for main program functions
* `data/` : Contains datasets
* `count_vectorizer.joblib` : Saved count vectorizer file
* `model.joblib` : Saved model file
* `requirements.txt` : Includes the requred libraries to run the program


### Main Program File (`project.py`)

This program only takes one command line arguments. Otherwise, the program will raise a usage error. First, the main menu is displayed. The message which is wanted to be checked should be copy & paste to the terminal. After enter key was pressed, the results will be generated shortly. If the model file is missing when starting the program, the program will be automatically reset. It will create a new model file. The model file is used to predict the messages. It saves the time because no need to fit the model every time.


There are 4 options in the menu.

1. Update: The model can be updated using command `--update` to use new data. This program collet user input data randomly and save those in the dataset. The model is fitted using the dataset which includes the newly added data.
2. Reset: The model can be reset using `--reset` to set default model and dataset. If the model has poor accuracy, resetting the model will solve the problem.
3. Menu: The menu can be displayed again using `--menu` command. If you can't find the menu, this can be helpful.
4. Exit: The program can be terminated using `--exit` command.

The program will check the input of the user. If the input isn’t seemed like a message, ` Invalid Message!` will be displayed. For valid input, after prediction, the results will be displayed. (Mostly it’ll take less than a second because saved model is used) 

#### Data Collection

This program collects random input data and store them in the dataset to improve the model. It collects messages that have 20-250 words with probability of 50%. User can be distracted if it all ways collects data. A question will be asked from the user to get the accuracy of the latest prediction. If accurate, original prediction is saved but if not, the opposite message type is saved in dataset with the input message. When updating the dataset, the original or latest csv dataset is loaded. Then it adds the new message in the dataset. These new data isn’t used until the user execute the update command. The delete command will delete all new collected data and sets the default dataset.

#### Model

Random Forest Classifier is used to fit and predict the data. After every fit, the model accuracy is displayed. `joblib` library is used to store the predicted model. This saves time because no need to fit the model every time starting the program. `scikit-learn` (Machine Learning Library) is used to create the model. `pandas` is used to handle dataset. CountVectorizer and SMOTE (imbalanced-learn library) is used to transform data into a data type that supports the random forest classifier. (String words to numerical array)

#### Other Functions

* `message_type()`: Generate a user friendly message from the message type
* `model()`: Fit and save the model
* `model_reset()`: Reset the model default models and datasets
* `model_update()`: Update the model to include newly added data
* `is_valid()`: Check the validity of the input
* `message_type_reverse()`: Returns the opposite type of the message type
* `check_file()`: Check the existence of a file or a directory
* `get_accuracy()`: Converts numerical accuracy value to user readable message.

### Testing (`test_project.py`)

test_project.py checks all functions in the main program (`project.py`). `test_model_reset` & `test_model_update` are commented because it changes the dataset when testing. (If it's fine with the user, those 2 also can be run)

### Conclusion

* Spam Message Detector is very useful program for every one in our daily life. 
* This helps to protect from malicious content.
* Users don't have to manually read every unwanted messages so let the program detect the spam messages to save time.
* Some modifications and upgrades can be done in future when needed.
