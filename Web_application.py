"""

# -*- coding: utf-8 -*-

Created on Wed Sep 20 21:47:51 2023
@author: ahsan
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu


hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True) 

# loading the saved models

diabetes_model = pickle.load(open("Diabete_disease_modelw.sav", "rb"))

heart_model = pickle.load(open("Heart_disease_model.sav", "rb"))

parkinsons_model = pickle.load(open("Parkinson's_disease_model 1.sav", "rb"))

kidney_model = pickle.load(open("CKD_disease_model.sav", "rb"))

# sidebar for navigation
with st.sidebar:
    selected = option_menu('My Predictive System',
                           ['Home',
			    'Diabetes Disease Prediction',					
                            'Heart Disease Prediction',
                            'Parkinson Disease Prediction',
			    'Chronic Kidney Disease',]
                           icons=['house','activity','heart','person','activity'],
                           default_index=0)



#***********************************************************************
#***********************************************************************

if selected == "Home":
	

# Title
 st.title(" An Aided Tool For Multi-Disease Prediction System")
 st.subheader("Welcome to our prediction platform!")
 
 st.write(""" _Diseases Predictor is a web app that employs machine learning algorithms to assess your health.
 It uses your input data, including symptoms, medical history, lifestyle, and demographics to predict the likelihood of specific diseases._
 """)
# Image
 st.image(" https://0701.static.prezi.com/preview/v2/jvbd435orunfn5dsui3nrst6v36jc3sachvcdoaizecfr3dnitcq_3_0.png", width=700)
 #https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRuuuJ4XZ7hYuBPFtsaw_wTf1yJYmI29Uy7Ig&usqp=CAU
# Content



 st.write("""

**How it works:**

_The system operates by training machine learning models on extensive medical datasets 
to recognize patterns for disease prediction._

**How to use it:**

_To use our disease prediction system, simply select the disease you are interested in from the sidebar.
You will then be asked to provide some information about yourself, such as your symptoms, medical history, lifestyle habits, and demographic data. Once you have provided this information, 
our system will generate a prediction of the likelihood of you having the disease._

**Please note:**

_Remember, this tool is not a substitute for professional medical advice.
 Always consult a doctor for health concerns._
""")
 st.write(""" _If you're having trouble understanding our request or unsure what to input, click "help"._ """)
 if st.button(" Help"):
        st.write(""" 
## _**All About Diseases we discuss in this app**_
---	
---	
""")


        st.write(""" 
# **_Diabtese Disease_**

				 
**Gender:**  This is your biological identification as male , female or other.

**Age:**  Your age, which helps determine your risk of developing diabetes as it often increases with age.

**Hypertension:**  It's high blood pressure, a condition where your blood pushes against the walls of your arteries with too much force.

**Heart Disease:**  This refers to various conditions that affect the heart, which can increase diabetes risk.

**Smoking History:**  Whether or not you have a history of smoking, which can be a risk factor.

**BMI (Body Mass Index):**  This is a measure of your body weight compared to your height. Higher values may indicate a higher risk of diabetes.

**Hemoglobin A1c Level:**  A measure of your average blood sugar levels over several months. High levels suggest a risk of diabetes.

**Blood Glucose Level:**  It's the amount of sugar (glucose) in your blood. High levels can be an early sign of diabetes. 

---

""")


        st.write(""" 
# **_Heart Disease❤_**

				 
**Age:** This is the patient's age. It's an important factor because heart disease risk often increases with age.

**Sex:** This refers to the patient's gender. It's used in prediction models because heart disease can affect men and women differently.

**CP (Chest Pain):** CP is a feature that describes the type of chest pain a patient experiences. There are typically four types:

0: No chest pain

1: Typical angina (a type of chest discomfort)

2: Atypical angina

3: Non-anginal pain


**Trestbps:** This is the resting blood pressure of the patient. High blood pressure can be a risk factor for heart disease.

**Chol (Cholesterol):** It represents the patient's cholesterol level. High cholesterol can contribute to heart disease.

**FBS (Fasting Blood Sugar):** This indicates the patient's fasting blood sugar level. Elevated sugar levels may be associated with diabetes, a risk factor for heart disease.

**Restecg (Resting ECG):** It describes the results of the patient's resting electrocardiogram. It helps assess heart health.The selection of values 0 to 2 representing "_normal_" , "_abnormality_" and "_left ventricular hypertrophy_".

**Thalach:** This is the maximum heart rate achieved during exercise. A lower maximum heart rate might indicate heart issues.

**Exang (Exercise-Induced Angina):** It tells if the patient experiences angina during exercise, which can be a sign of heart problems.

**Oldpeak:** This is related to changes in the ST segment of the ECG during exercise. It's another indicator of heart health.

**Slope:** It describes the slope of the peak exercise ST segment. It's part of the ECG data and contributes to diagnosis.
The values 0 to 2 representing "_upsloping_" , "_flat_" and "_downsloping_".

**Thal (Thalassemia):** Thalassemia is a blood disorder, and different types of thalassemia can affect the heart. The type of thalassemia, with options "_Normal_" , "Fixed_" , "_Reversible_" and "_Irreversible_" represented by values 0 to 3

**Ca (Number of Major Vessels):** It represents the number of major blood vessels supplying the heart. There are four types of it 
  0: This indicates that there are no major blood vessels with a significant narrowing or obstruction. It suggests a healthier cardiovascular system.

  1: One major blood vessel shows narrowing or obstruction. This might indicate a mild blockage.

  2: Two major blood vessels exhibit narrowing or obstruction. This could imply a moderate level of blockage.

  3: Three major blood vessels have narrowing or obstruction. This suggests a significant level of blockage in multiple vessels.

  4: Four major blood vessels with narrowing or obstruction. This is a substantial indication of blockage, and it typically signifies a higher risk of heart disease..


---

""")


        st.write(""" 
# **_Parkinson's Disease_**

**F0, Fhi, Flo:** These attributes measure the average, maximum, and minimum fundamental frequency (F0) of the voice. 
In PD patients, F0 is typically lower and more variable than in healthy individuals.

**Jitter:** This attribute measures the variation in F0 over time. 
Jitter is typically increased in PD patients.

**Shimmer:** This attribute measures the variation in the amplitude of the voice signal over time. 
Shimmer is also typically increased in PD patients.

**NHR, HNR:** These attributes measure the ratio of noise to tonal components in the voice.
 NHR and HNR are typically increased in PD patients.


In addition to these general voice quality measures, 
there are also a number of more specialized attributes
 that have been shown to be altered in PD patients. 
 
 
 These attributes include:

**RAP, PPQ, DDP:** These attributes measure the variation in F0 over different periods of time. 
RAP, PPQ, and DDP are typically increased in PD patients.

**APQ3, APQ5, APQ, DDA:** These attributes measure the distribution of F0 values. 
APQ3, APQ5, and APQ are typically decreased in PD patients, while DDA is typically increased.

**RPDE, DFA, spread1, spread2, D2, PPE:** These attributes are more complex measures of vocal dynamics and complexity. 
They are often used in research studies, but they are not yet widely used in clinical practice.

It is important to **_note_** that the changes in voice quality seen in PD patients can vary from person to person. 
Some people may have only minor changes, while others may have more severe changes. 
The severity of the voice changes does not necessarily correlate with the severity of the other symptoms of PD.			 

---
---
""")

       

#***********************************************************************
#***********************************************************************




# Diabetes prediction 
if selected == 'Diabetes Disease Prediction': 
	
    if st.button(" Help"):
		
        st.write(""" 
## _**All About Diabetes Diseases **_
---	
---	
""")


        st.write(""" 
# **_Diabtese Disease_**

				 
**Gender:**  This is your biological identification as male , female or other.

**Age:**  Your age, which helps determine your risk of developing diabetes as it often increases with age.

**Hypertension:**  It's high blood pressure, a condition where your blood pushes against the walls of your arteries with too much force.

**Heart Disease:**  This refers to various conditions that affect the heart, which can increase diabetes risk.

**Smoking History:**  Whether or not you have a history of smoking, which can be a risk factor.

**BMI (Body Mass Index):**  This is a measure of your body weight compared to your height. Higher values may indicate a higher risk of diabetes.

**Hemoglobin A1c Level:**  A measure of your average blood sugar levels over several months. High levels suggest a risk of diabetes.

**Blood Glucose Level:**  It's the amount of sugar (glucose) in your blood. High levels can be an early sign of diabetes. 

---

""")


	
    # Making Prediction
    st.title('Diabetes Disease Prediction')

    col1, col2 = st.columns(2)

    with col1:
        gender = st.number_input('Gender (0__F, 1__M, 2__Other)')

    with col2:
        age = st.number_input('How Old (Age)')

    with col1:
        hypertension = st.number_input('Hypertension (0__1)')

    with col2:
        heart_disease = st.number_input('Heart Disease (0__1)')

    with col1:
        smoking_history = st.number_input('Smoking History (0__1)')

    with col2:
        bmi = st.number_input('Body Mass Index (BMI) value')

    with col1:
        HemoglobinA1c_level = st.number_input('HemoglobinA1c (HGI) level')

    with col2:
        blood_glucose_level = st.number_input('Glucose Level')

    prediction_result = ''

    # Creating the button to predict
    if st.button('Predict Result'):
        prediction_result = diabetes_model.predict([[gender, age, hypertension, heart_disease, smoking_history, bmi, HemoglobinA1c_level, blood_glucose_level]])
        print('Predicted Value is = ', prediction_result)

        if prediction_result[0] == 0:
            prediction_result = 'Good news as you are non Diabetic  '
        else:
            prediction_result = 'OH! no, there is sad news as you recognised as diabetic \n\n For further information kindly consult with the doctor'
 
 
 
 
    st.success (prediction_result)			

         

    if st.button('Show Table'):         
    # 1st column: Parameters
     parameters = ["Gender", "Age", "Hypertension", "Heart Disease", "Smoking History", "BMI", "Hemoglobin Level", "Glucose Level"]

	# 2nd column: Normal Ranges 
     normal_ranges = [(0,2) , (18, 80) , (0,0) , (0,0) , (0,0) , (18.5,24.9) , (4.0,5.0 ) , (70,140 )]

	

	# 3rd column: User Input (Let's assume user input is stored in a dictionary)
     user_input = [ gender, age ,  hypertension,  heart_disease,   smoking_history,  bmi,  HemoglobinA1c_level,  blood_glucose_level]
   
	 # 4th column: Check if user input falls within the normal range

     comments = []
     for i, v in enumerate(user_input):
         if normal_ranges[i][0] <= v <= normal_ranges[i][1]:
             comments.append('Normal')
         else:
             comments.append('Not Normal')





     # Create a table to display parameters and normal ranges
     st.table({"Parameters": parameters, "Normal Ranges": normal_ranges , "User Input": user_input , 'Comments': comments })


	
	
	
	
	
	#***********************************************************************
	#***********************************************************************
	
	
	
	
	# Heart disease Prediction Page
if selected == 'Heart Disease Prediction': 
    if st.button(" Help"):
		
        st.write(""" 
## _**All About Heart Disease**_
---	
---	
""")
        st.write(""" 
# **_Heart Disease❤_**

				 
**Age:** This is the patient's age. It's an important factor because heart disease risk often increases with age.

**Sex:** This refers to the patient's gender. It's used in prediction models because heart disease can affect men and women differently.

**CP (Chest Pain):** CP is a feature that describes the type of chest pain a patient experiences. There are typically four types:

0: No chest pain

1: Typical angina (a type of chest discomfort)

2: Atypical angina

3: Non-anginal pain


**Trestbps:** This is the resting blood pressure of the patient. High blood pressure can be a risk factor for heart disease.

**Chol (Cholesterol):** It represents the patient's cholesterol level. High cholesterol can contribute to heart disease.

**FBS (Fasting Blood Sugar):** This indicates the patient's fasting blood sugar level. Elevated sugar levels may be associated with diabetes, a risk factor for heart disease.

**Restecg (Resting ECG):** It describes the results of the patient's resting electrocardiogram. It helps assess heart health.The selection of values 0 to 2 representing "_normal_" , "_abnormality_" and "_left ventricular hypertrophy_".

**Thalach:** This is the maximum heart rate achieved during exercise. A lower maximum heart rate might indicate heart issues.

**Exang (Exercise-Induced Angina):** It tells if the patient experiences angina during exercise, which can be a sign of heart problems.

**Oldpeak:** This is related to changes in the ST segment of the ECG during exercise. It's another indicator of heart health.

**Slope:** It describes the slope of the peak exercise ST segment. It's part of the ECG data and contributes to diagnosis.
The values 0 to 2 representing "_upsloping_" , "_flat_" and "_downsloping_".

**Thal (Thalassemia):** Thalassemia is a blood disorder, and different types of thalassemia can affect the heart. The type of thalassemia, with options "_Normal_" , "Fixed_" , "_Reversible_" and "_Irreversible_" represented by values 0 to 3

**Ca (Number of Major Vessels):** It represents the number of major blood vessels supplying the heart. There are four types of it 
  0: This indicates that there are no major blood vessels with a significant narrowing or obstruction. It suggests a healthier cardiovascular system.

  1: One major blood vessel shows narrowing or obstruction. This might indicate a mild blockage.

  2: Two major blood vessels exhibit narrowing or obstruction. This could imply a moderate level of blockage.

  3: Three major blood vessels have narrowing or obstruction. This suggests a significant level of blockage in multiple vessels.

  4: Four major blood vessels with narrowing or obstruction. This is a substantial indication of blockage, and it typically signifies a higher risk of heart disease..


---

""")


    # Making Prediction
    st.title('Heart Disease Prediction')


   
    col1, col2, col3 = st.columns(3)

	    
    with col1:
        age = st.number_input('Age')
        
    with col2:
        sex = st.number_input('Gender')
    
    with col3:
        cp = st.number_input('Chest pain type 0__3 ')
    
    with col1:
        trestbps = st.number_input('Resting blood pressure (mm Hg)')
    
    with col2:
        chol = st.number_input('Serum cholestoral (mg/dl)')
    
    with col3:
        fbs = st.number_input('Fasting blood sugar(mg/dl) ')
    
    with col1:
        restecg = st.number_input('Rest ECG 0__2 ')
    
    with col2:
        thalach = st.number_input('Maximum heart rate achieved')
		
    with col3:
        exang = st.number_input('Exer induced angina 0__1 (No , Yes )')
    
    with col1:
        oldpeak = st.number_input('Value of oldpeak ')
    
    with col2:
        slope = st.number_input('Slope 0__2' )
		
    with col3:
        ca = st.number_input('No. of major vessels (0__4)')	
    
    with col1:
        thal = st.number_input('Thalassemia 0__3 )')


    prediction_result = ''

    # Creating the button to predict
    if st.button('Predict Result'):
       #prediction_result = heart_model.predict([[0 , 0 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 1 , 2 , 1 , 2]])
     prediction_result = heart_model.predict([[age , sex , cp , trestbps , chol , fbs , restecg , thalach , exang , oldpeak , slope , ca , thal]])
      # print('Predicted Value is = ', prediction_result)
	  
	  
     print('Predicted Value is = ', prediction_result)
	
     if prediction_result[0] == 0:
            prediction_result = 'Good news as you are Healthy person'
     else:
            prediction_result = 'OH! no, there is sad news as you have Heart Problem \n\n For further information kindly consult with the doctor'
            
   
    st.success (prediction_result)	
   
   
   
   # creating table 
   
    if st.button('Show Table'):         
    # 1st column: Parameters
     parameters = [
        "Age", "Sex", "Chest Pain (cp)", "Resting Blood Pressure (tresbps)", "Cholesterol Level (chol)", "Fasting Blood Sugar (FBS)", "Resting Electrocardiogram (restecg)",
        "Maximum Heart Rate (thalach)", "Exercise-Induced Angina (exang)", "ST Depression Induced by Exercise (oldpeak)", "Slope of the Peak Exercise ST Segment (slope)", "No. of Major Vessels Colored by Fluoroscopy (ca)", "Thalassemia (thal)"
    ]

	# 2nd column: Normal Ranges 
     normal_ranges = [
        (18, 80), (0, 1), (0, 3), (80, 130), (126, 200), (0, 1), (0, 2), (100, 166), (0, 1), (0.5, 2.5), (0, 2), (0, 4), (0, 3)
    ]

	

	# 3rd column: User Input 
     user_input1 = [age , sex , cp , trestbps , chol , fbs , restecg , thalach , exang , oldpeak , slope , ca , thal]
   
	 # 4th column: Check if user input falls within the normal range

     comments = []
     for i, v in enumerate(user_input1):
         if normal_ranges[i][0] <= v <= normal_ranges[i][1]:
             comments.append('Normal')
         else:
             comments.append('Not Normal')

   
    # Create a table to display parameters and normal ranges user input and resultant 
     st.table({"Parameters": parameters, "Normal Ranges": normal_ranges , "User Input": user_input1 , 'Comments': comments })

   
	
	#***********************************************************************
	#***********************************************************************
	
	
	
	
# Parkinson's Prediction Page
if selected == 'Parkinson Disease Prediction': 

    if st.button(" Help"):
		
        st.write(""" 
## _**All About Parkinson's Disease**_
---	
---	
""")
        st.write("""
# **_Parkinson's Disease_**

**F0, Fhi, Flo:** These attributes measure the average, maximum, and minimum fundamental frequency (F0) of the voice. 
In PD patients, F0 is typically lower and more variable than in healthy individuals.

**Jitter:** This attribute measures the variation in F0 over time. 
Jitter is typically increased in PD patients.

**Shimmer:** This attribute measures the variation in the amplitude of the voice signal over time. 
Shimmer is also typically increased in PD patients.

**NHR, HNR:** These attributes measure the ratio of noise to tonal components in the voice.
 NHR and HNR are typically increased in PD patients.


In addition to these general voice quality measures, 
there are also a number of more specialized attributes
 that have been shown to be altered in PD patients. 
 
 
 These attributes include:

**RAP, PPQ, DDP:** These attributes measure the variation in F0 over different periods of time. 
RAP, PPQ, and DDP are typically increased in PD patients.

**APQ3, APQ5, APQ, DDA:** These attributes measure the distribution of F0 values. 
APQ3, APQ5, and APQ are typically decreased in PD patients, while DDA is typically increased.

**RPDE, DFA, spread1, spread2, D2, PPE:** These attributes are more complex measures of vocal dynamics and complexity. 
They are often used in research studies, but they are not yet widely used in clinical practice.

It is important to **_note_** that the changes in voice quality seen in PD patients can vary from person to person. 
Some people may have only minor changes, while others may have more severe changes. 
The severity of the voice changes does not necessarily correlate with the severity of the other symptoms of PD.			 

---
---
""")
				 	

    # Making Prediction
    st.title('Parkinson Disease Prediction')

#    MDVP:Fo(Hz)	MDVP:Fhi(Hz)	MDVP:Flo(Hz)	MDVP:Jitter(%)	MDVP:Jitter(Abs)	MDVP:RAP	MDVP:PPQ	Jitter:DDP	MDVP:Shimmer	...	Shimmer:DDA	NHR	HNR	status	RPDE	DFA	spread1	spread2	D2	PPE

    col1, col2, col3, col4, col5 = st.columns(5)  
    
    with col1:
        fo = st.number_input('Fundamental Frequency (fo)')
        
    with col2:
        fhi = st.number_input('High-Frequency (fhi)')
        
    with col3:
        flo = st.number_input('Low-Frequenc (flo)')
        
    with col4:
        Jitter_percent = st.number_input('Jitter Percent)')
        
    with col5:
        Jitter_Abs = st.number_input('Jitter Abs')
        
    with col1:
        RAP = st.number_input('RAP')
        
    with col2:
        PPQ = st.number_input('PPQ')
        
    with col3:
        DDP = st.number_input('DDP')
        
    with col4:
        Shimmer = st.number_input('Shimmer')
        
    with col5:
        Shimmer_dB = st.number_input('Shimmer dB')
        
    with col1:
        APQ3 = st.number_input('APQ3')
        
    with col2:
        APQ5 = st.number_input(' APQ5')
        
    with col3:
        APQ = st.number_input('APQ')
        
    with col4:
        DDA = st.number_input('DDA')
        
    with col5:
        NHR = st.number_input('NHR')
        
    with col1:
        HNR = st.number_input('HNR')
        
    with col2:
        RPDE = st.number_input('RPDE')
        
    with col3:
        DFA = st.number_input('DFA')
        
    with col4:
        spread1 = st.number_input('spread1')
        
    with col5:
        spread2 = st.number_input('spread2')
        
    with col1:
        D2 = st.number_input('D2')
        
    with col2:
        PPE = st.number_input('PPE')
        
    
    
    # code for Prediction
    prediction_result = ''
    
    # creating a button for Prediction    
    if st.button("Predict Result"):
        prediction_result = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])
        
        if prediction_result[0] == 0:
            prediction_result = 'Good news as you are Healthy'
        else:
            prediction_result = 'OH! no, there is sad news as you have Parkinson \n\n For further information kindly consult with the doctor'
            

    st.success (prediction_result)	
	
	  
   
   
   # creating table 
   
    if st.button('Show Table'):         
    # 1st column: Parameters
     parameters = [
    "Fundamental Frequency (fo)", "High-Frequency Component of the Fundamental Frequency (fhi)", "Low-Frequency Component of the Fundamental Frequency(flo)", "Jitter_percent", "Jitter_Abs", "RAP", "PPQ", "DDP",
    "Shimmer", "Shimmer_dB", "APQ3", "APQ5", "APQ", "DDA", "Noise-to-Harmonics Ratio (NHR)", "Harmonics-to-Noise Ratio (HNR)", 
    "Recurrence Period Density Entropy (RPDE)", "Detrended Fluctuation Analysis (DFA)", "spread1", "spread2", "D2", "Pitch Period Entropy (PPE)"
]

	# 2nd column: Normal Ranges 
     normal_ranges = [
	     (120, 140), (40, 60), (80,100), (0.5,1.5), (0.001, 0.02), (150,200), (0.1, 0.2), (0.05, 0.1), (0.5, 1.5), (0, 6), (0.01, 0.02), (0.015, 0.025), (0.1, 0.2), (0.05,0.1), 
	     (-10, 1), (0, 10), (1, 1.5), (1, 1.5), (0.1, 0.2), (0.1, 0.2), (0, 0.1), (1, 1.5)
        
    ]

	

	# 3rd column: User Input 
     user_input2 = [fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]
   
	 # 4th column: Check if user input falls within the normal range

     comments = []
     for i, v in enumerate(user_input2):
         if normal_ranges[i][0] <= v <= normal_ranges[i][1]:
             comments.append('Normal')
         else:
             comments.append('Not Normal')

   
    # Create a table to display parameters and normal ranges user input and resultant 
     st.table({"Parameters": parameters, "Normal Ranges": normal_ranges , "User Input": user_input2 , 'Comments': comments })

   



   
	
	#***********************************************************************
	#***********************************************************************
	
