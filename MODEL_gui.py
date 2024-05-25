from subprocess import call
import tkinter as tk
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from PIL import Image, ImageTk
from sklearn.metrics import classification_report, accuracy_score
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from joblib import dump
import xgboost as xgb
from sklearn.naive_bayes import MultinomialNB
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

root = tk.Tk()
root.title("Cyberattack Detection Using ML")

w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.configure(background="black")

image = Image.open('oo.jpg')
image = image.resize((1355, 650), Image.LANCZOS)
background_image = ImageTk.PhotoImage(image)
background_label = tk.Label(root, image=background_image)
background_label.image = background_image
background_label.place(x=0, y=70)

lbl = tk.Label(
    root,
    text="Cyberattack Detection Using ML",
    font=("times", 40, "bold"),
    height=1,
    width=43,
    bg="black",
    fg="white",
)
lbl.place(x=0, y=0)


                                                                  # SUPPORT VECTOR MACHINE

def Model_Training1():
    data = pd.read_csv("test.csv")
    data = data.dropna()
    x = data.drop(['Average_Packet_Size', 'Duration', 'Label'], axis=1)
    y = data['Label']

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.30, random_state=123)

    from sklearn.svm import SVC
    svcclassifier = SVC(kernel='linear')
    svcclassifier.fit(x_train, y_train)

    y_pred = svcclassifier.predict(x_test)

    print("Classification Report : ", classification_report(y_test, y_pred))
    ACC = accuracy_score(y_test, y_pred) * 100
    print("Accuracy : %.2f%%" % ACC)
    repo = classification_report(y_test, y_pred)

    label4 = tk.Label(root,text=str(repo),width=45,height=15,bg='seashell2',fg='black',font=("Tempus Sanc ITC",14))
    label4.place(x=350,y=150)
    
    label5 = tk.Label(root,
                  text="Accuracy : {:.2f}% \n\n Model saved as attack_SVM.joblib".format(ACC),
                  width=45, height=4, bg='black', fg='white', font=("Tempus Sanc ITC", 14))
    label5.place(x=350,y=460)

    from joblib import dump
    dump(svcclassifier, "attack_SVM.joblib")
    print("Model saved as attack_SVM.joblib")



                                                                # NAIVE BAYES


def Model_Training2():
    data = pd.read_csv("test.csv")
    data = data.dropna()
    x = data.drop(['Average_Packet_Size', 'Duration', 'Label'], axis=1)
    y = data['Label']

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.30, random_state=123)

    naive_bayes_classifier = MultinomialNB()
    naive_bayes_classifier.fit(x_train, y_train)

    y_pred = naive_bayes_classifier.predict(x_test)

    print("Classification Report : ", classification_report(y_test, y_pred))
    ACC = accuracy_score(y_test, y_pred) * 100
    print("Accuracy : %.2f%%" % ACC)
    repo = classification_report(y_test, y_pred)

    label4 = tk.Label(root, text=str(repo), width=45, height=15, bg='seashell2', fg='black', font=("Tempus Sanc ITC", 14))
    label4.place(x=350, y=150)

    label5 = tk.Label(root,
                  text="Accuracy : {:.2f}% \n\n Model saved as attack_NaiveBayes.joblib".format(ACC),
                  width=45, height=4, bg='black', fg='white', font=("Tempus Sanc ITC", 14))

    label5.place(x=350, y=460)

    dump(naive_bayes_classifier, "attack_NaiveBayes.joblib")
    print("Model saved as attack_NaiveBayes.joblib")


                                                                # DECISION TREE


# def Model_Training3():
#     data = pd.read_csv("test.csv")
#     data = data.dropna()
#     x = data.drop(['Average_Packet_Size', 'Duration', 'Label'], axis=1)
#     y = data['Label']

#     x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.30, random_state=123)

#     # Defining the hyperparameters grid for Grid Search
#     param_grid = {
#         'criterion': ['gini', 'entropy'],
#         'max_depth': [None, 10, 15, 20],
#         'min_samples_split': [2, 5, 10],
#         'min_samples_leaf': [1, 2, 4],
#     }

#     # Creating the Decision Tree Classifier
#     decision_tree_classifier = DecisionTreeClassifier(random_state=123)

#     # Performing Grid Search with 10-fold cross-validation
#     grid_search = GridSearchCV(decision_tree_classifier, param_grid, cv=10)
#     grid_search.fit(x_train, y_train)

#     # Getting the best model from Grid Search
#     best_decision_tree_classifier = grid_search.best_estimator_

#     # Fitting the best model on the training data
#     best_decision_tree_classifier.fit(x_train, y_train)

#     # Making predictions using the best model
#     y_pred = best_decision_tree_classifier.predict(x_test)

#     # Classification report
#     print("Classification Report : ", classification_report(y_test, y_pred))
#     ACC = accuracy_score(y_test, y_pred) * 100
#     print("Accuracy : {:.2f}%".format(ACC))
#     repo = classification_report(y_test, y_pred)

#     # Display results in tkinter labels
#     label4 = tk.Label(root, text=str(repo), width=45, height=15, bg='seashell2', fg='black', font=("Tempus Sanc ITC", 14))
#     label4.place(x=250, y=100)

#     label5 = tk.Label(root,
#                   text="Accuracy : {:.2f}% \n\n Model saved as attack_DecisionTree.joblib".format(ACC),
#                   width=45, height=4, bg='black', fg='white', font=("Tempus Sanc ITC", 14))
#     label5.place(x=250, y=420)

#     # Save the best model
#     dump(best_decision_tree_classifier, "attack_DecisionTree.joblib")
#     print("Model saved as attack_DecisionTree.joblib")

def Model_Training3():
    data = pd.read_csv("test.csv")
    data = data.dropna()
    x = data.drop(['Average_Packet_Size', 'Duration', 'Label'], axis=1)
    y = data['Label']

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.30, random_state=123)

    decision_tree_classifier = DecisionTreeClassifier(random_state=123)
    decision_tree_classifier.fit(x_train, y_train)

    y_pred = decision_tree_classifier.predict(x_test)

    print("Classification Report : ", classification_report(y_test, y_pred))
    ACC = accuracy_score(y_test, y_pred) * 100
    print("Accuracy : %.2f%%" % ACC)
    repo = classification_report(y_test, y_pred)

    label4 = tk.Label(root, text=str(repo), width=45, height=15, bg='seashell2', fg='black', font=("Tempus Sanc ITC", 14))
    label4.place(x=350, y=150)

    label5 = tk.Label(root,
                  text="Accuracy : {:.2f}% \n\n Model saved as attack_DecisionTree.joblib".format(ACC),
                  width=45, height=4, bg='black', fg='white', font=("Tempus Sanc ITC", 14))

    label5.place(x=350, y=460)

    dump(decision_tree_classifier, "attack_DecisionTree.joblib")
    print("Model saved as attack_DecisionTree.joblib")



                                                                    # RANDOM FOREST 

def Model_Training4():
    data = pd.read_csv("test.csv")
    data = data.dropna()
    x = data.drop(['Average_Packet_Size', 'Duration', 'Label'], axis=1)
    y = data['Label']

    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.30, random_state=123)

    # Define the parameter grid for GridSearchCV
    param_grid = {
        'n_estimators': [50, 100, 150],  # Test different numbers of trees
        'max_depth': [None, 10, 20],  # Test different maximum depths of trees
        'min_samples_split': [2, 5, 10]  # Test different minimum samples required to split a node
    }

    # Create a RandomForestClassifier instance
    random_forest_classifier = RandomForestClassifier(random_state=123)

    # Create GridSearchCV instance
    grid_search = GridSearchCV(random_forest_classifier, param_grid, cv=5)

    # Fit the GridSearchCV instance on training data
    grid_search.fit(x_train, y_train)

    # Get the best estimator and use it for predictions
    best_random_forest = grid_search.best_estimator_
    y_pred = best_random_forest.predict(x_test)

    print("Classification Report : ", classification_report(y_test, y_pred))
    ACC = accuracy_score(y_test, y_pred) * 100
    print("Accuracy : %.2f%%" % ACC)
    repo = classification_report(y_test, y_pred)

    label4 = tk.Label(root, text=str(repo), width=45, height=15, bg='seashell2', fg='black', font=("Tempus Sanc ITC", 14))
    label4.place(x=350, y=150)

    label5 = tk.Label(root,
                      text="Accuracy : {:.2f}% \n\n Model saved as attack_RandomForest.joblib".format(ACC),
                      width=45, height=4, bg='black', fg='white', font=("Tempus Sanc ITC", 14))

    label5.place(x=350, y=460)

    # Dump the best model found by GridSearchCV
    dump(best_random_forest, "attack_RandomForest.joblib")
    print("Model saved as attack_RandomForest.joblib")


# def Model_Training4():
#     data = pd.read_csv("test.csv")
#     data = data.dropna()
#     x = data.drop(['Average_Packet_Size', 'Duration', 'Label'], axis=1)
#     y = data['Label']

#     x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.30, random_state=123)

#     random_forest_classifier = RandomForestClassifier(n_estimators=100, random_state=123)
#     random_forest_classifier.fit(x_train, y_train)

#     y_pred = random_forest_classifier.predict(x_test)

#     print("Classification Report : ", classification_report(y_test, y_pred))
#     ACC = accuracy_score(y_test, y_pred) * 100
#     print("Accuracy : %.2f%%" % ACC)
#     repo = classification_report(y_test, y_pred)


#     label4 = tk.Label(root, text=str(repo), width=45, height=15, bg='seashell2', fg='black', font=("Tempus Sanc ITC", 14))
#     label4.place(x=250, y=100)

#     label5 = tk.Label(root,
#                   text="Accuracy : {:.2f}% \n\n Model saved as attack_RandomForest.joblib".format(ACC),
#                   width=45, height=4, bg='black', fg='white', font=("Tempus Sanc ITC", 14))

#     label5.place(x=250, y=420)

#     dump(random_forest_classifier, "attack_RandomForest.joblib")
#     print("Model saved as attack_RandomForest.joblib")



                                                                      # XGBOOST


def Model_Training5():
    data = pd.read_csv("test.csv")
    data = data.dropna()
    x = data.drop(['Average_Packet_Size', 'Duration', 'Label'], axis=1)
    y = data['Label']
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.30, random_state=123)

    xgboost_classifier = xgb.XGBClassifier()
    xgboost_classifier.fit(x_train, y_train)

    y_pred = xgboost_classifier.predict(x_test)

    print("Classification Report : ", classification_report(y_test, y_pred))
    ACC = accuracy_score(y_test, y_pred) * 100
    print("Accuracy : %.2f%%" % ACC)
    repo = classification_report(y_test, y_pred)

    label4 = tk.Label(root, text=str(repo), width=45, height=15, bg='seashell2', fg='black', font=("Tempus Sanc ITC", 14))
    label4.place(x=350, y=150)

    label5 = tk.Label(root,
                  text="Accuracy : {:.2f}% \n\n Model saved as attack_XGBoost.joblib".format(ACC),
                  width=45, height=4, bg='black', fg='white', font=("Tempus Sanc ITC", 14))

    label5.place(x=350, y=460)
    dump(xgboost_classifier, "attack_XGBoost.joblib")
    print("Model saved as attack_XGBoost.joblib")



def call_file():
    call(['python', 'Check.py'])



def window():
    root.destroy()

button1 = tk.Button(root, foreground="black", background="#fcf151", font=("Tempus Sans ITC", 14, "bold"),
                    text="SVM_Model", command=Model_Training1, width=15, height=2)
button1.place(x=1100, y=100)

button2 = tk.Button(root, foreground="black", background="#fcf151", font=("Tempus Sans ITC", 14, "bold"),
                    text="NB_Model", command=Model_Training2, width=15, height=2)
button2.place(x=1100, y=200)

button3 = tk.Button(root, foreground="black", background="#fcf151", font=("Tempus Sans ITC", 14, "bold"),
                    text="DT_Model", command=Model_Training3, width=15, height=2)
button3.place(x=1100, y=300)

button4 = tk.Button(root, foreground="black", background="#fcf151", font=("Tempus Sans ITC", 14, "bold"),
                    text="RF_Model", command=Model_Training4, width=15, height=2)
button4.place(x=1100, y=400)

button5 = tk.Button(root, foreground="black", background="#fcf151", font=("Tempus Sans ITC", 14, "bold"),
                    text="XGBoost_Model", command=Model_Training5, width=15, height=2)
button5.place(x=1100, y=500)


button6 = tk.Button(root, foreground="black", background="#fcf151", font=("Tempus Sans ITC", 14, "bold"),
                    text="Check Performance", command=call_file, width=15, height=2)
button6.place(x=1100, y=600)

exit = tk.Button(root, text="Exit", command=window, width=15, height=2, font=('Tempus Sans ITC', 14, 'bold'), bg="red",
                 fg="white")
exit.place(x=1100, y=720)


root.mainloop()
