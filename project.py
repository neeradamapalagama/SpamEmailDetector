import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split 
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from imblearn.over_sampling import SMOTE
import joblib
import os
import csv
import random
import sys

def main():
    if len(sys.argv) != 1:
        print("Usage: python project.py")
        sys.exit()

    welcomestr = """
    -------------------------
    | Spam Message Detector |
    -------------------------

    Version: 1.0, Last Update: 2024-01-12

    Options
    -------
    
    1. Update the Model: --update
    2. Reset the Model: --reset
    3. Display the Menu: --menu
    4. Exit: --exit

    """
    print(welcomestr)

    while True:

        # Load the saved model
        try:
            m_model = joblib.load('model.joblib')
            cvec = joblib.load('count_vectorizer.joblib')
        except FileNotFoundError:
            print("Error: Couldn't Open the Model\n")
            if not model_reset():
                break
            continue

        # Get the message to check
        message = input("Message: ").strip()

        # Exit the program
        if message == "--exit":
            print() # Make a space when exit
            break

        # Reset the model
        elif message == "--reset":
            model_reset()
            continue

        # Update the model
        elif message == "--update":
            model_update()
            continue

        # Display the menu again
        elif message == "--menu":
            print(welcomestr)
            continue

        # Check validity of the message
        elif not is_valid(message):
            print("Results: Invalid Message!\n")
            continue

        listmessage = [message]
        
        # Predict the message type
        mtype = m_model.predict(cvec.transform(listmessage))[0]

        # Print the message type
        print("\nResults: " + message_type(mtype)+"\n")

        # Collect user input data and predictions randomly to improve the dataset
        if random.random() <= (1 / 2) and 20 <= len(message.split()) <= 250:
            question = input("Is this response accurate (yes/no)? ").strip().lower()
            if question in ["y", "yes"]:
                pass
            elif question in ["n", "no"]:
                mtype = message_type_reverse(mtype)
            else:
                continue

            # If there's already updated file
            if check_file("data/updated/spam.csv"):
                with open("data/updated/spam.csv", "a") as file:
                    writer = csv.DictWriter(file, fieldnames=["Category", "Message"])
                    writer.writerow({"Message": message, "Category": mtype})

            # If there's no any updated file
            else:
                file_data = []
                with open("data/default/spam.csv") as file:
                    writer = csv.DictReader(file)
                    for row in writer:
                        file_data.append(row)
                with open("data/updated/spam.csv", "w") as file:
                    writer = csv.DictWriter(file, fieldnames=["Category", "Message"])
                    writer.writeheader()
                    for row in file_data:
                        writer.writerow(row)
                    writer.writerow({"Message": message, "Category": mtype})
            print()
        

def message_type(t):
    """ Generate the notification by message type"""

    if t == "ham":
        return "Seems It's not a Spam Message! 🙂"
    elif t == "spam":
        return "Warning! It's a Spam Message! ⚠️"
    else:
        raise ValueError("Message types are only ham & spam.")


def model(dataset):
    """ Fit and Save the Model """

    # Read the csv dataset
    try:
        data = pd.read_csv(dataset, encoding='unicode_escape')
    except FileNotFoundError:
        return None

    # Seperate x, y values
    x = data["Message"]
    y = data["Category"]

    cvec = CountVectorizer()
    cx = cvec.fit_transform(x)

    smt = SMOTE()
    x_sm,y_sm=smt.fit_resample(cx,y)

    x_train,x_test,y_train,y_test=train_test_split(x_sm,y_sm,test_size=0.2)

    # Creating and fitting Random Forest Classifier to predict
    mesmodel=RandomForestClassifier(n_estimators=500) 
    mesmodel.fit(x_train,y_train)
    y_pred=mesmodel.predict(x_test) # Predictiong test data

    # Print the model's accuracy
    print("Model Accuracy: " + get_accuracy(accuracy_score(y_test,y_pred)))

    # Save the model as a file
    joblib.dump(mesmodel, 'model.joblib')
    joblib.dump(cvec, 'count_vectorizer.joblib')
    return True


def model_reset():
    """ Reset the model"""

    print("Reset started.")
    print("It will take a while to complete the process.")
    print("Resetting the model ...")
    if model("data/default/spam.csv"):
        print("The reset process has been successfully completed.\n")
        try:
            os.remove("data/updated/spam.csv")
        except FileNotFoundError:
            pass
        return True
    print("Error: The reset process could not be completed successfully.\n")
    return False


def model_update():
    """ Update the model"""

    print("Update started.")
    print("It will take a while to complete the process.")
    print("Updating the model ...")
    if model("data/updated/spam.csv"):
        print("The update process has been successfully completed.\n")
        return True
    print("Error: The update process could not be completed successfully.\n")
    return False
    ...


def is_valid(message):
    """ Check for invalid messages """

    if len(message.split()) < 2:
        return False
    return True

def message_type_reverse(type):
    """ Reverse the message type"""

    if type == "ham":
        return "spam"
    elif type == "spam":
        return "ham"
    else:
        raise ValueError("Message types are only ham & spam.")

def check_file(directory):
    """ Check whether a file or a directory exits """

    try:
        file = open(directory)
        return True
    except FileNotFoundError:
        return None

def get_accuracy(s):
    if s >= 0.9:
        return "Very Good"
    elif s > 0.75:
        return "Good"
    else:
        return "Bad ⚠️ \nPlease Reset the Model for Better Results!"


if __name__ == "__main__":
    main()
