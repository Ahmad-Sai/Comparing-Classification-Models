{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "1231c2da",
   "metadata": {},
   "source": [
    "## Comparing classification models"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3c667a04",
   "metadata": {},
   "source": [
    " #### Necessary Libraries and Functions needed to create models and plots. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "id": "7d7278a3",
   "metadata": {},
   "outputs": [],
   "source": [
    "import sklearn\n",
    "import itertools\n",
    "import numpy as np\n",
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "from xgboost import XGBClassifier\n",
    "from sklearn.svm import LinearSVC\n",
    "from matplotlib import pyplot as plt\n",
    "from sklearn.metrics import accuracy_score\n",
    "from sklearn.tree import DecisionTreeClassifier\n",
    "from sklearn.linear_model import LogisticRegression\n",
    "from sklearn.model_selection import train_test_split"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "bca0dea7",
   "metadata": {},
   "source": [
    "#### Read in the data from .csv file and display the first few rows. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "id": "e3b34096",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Pregnancies</th>\n",
       "      <th>Glucose</th>\n",
       "      <th>BloodPressure</th>\n",
       "      <th>SkinThickness</th>\n",
       "      <th>Insulin</th>\n",
       "      <th>BMI</th>\n",
       "      <th>DiabetesPedigreeFunction</th>\n",
       "      <th>Age</th>\n",
       "      <th>Outcome</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>2</td>\n",
       "      <td>138</td>\n",
       "      <td>62</td>\n",
       "      <td>35</td>\n",
       "      <td>0</td>\n",
       "      <td>33.6</td>\n",
       "      <td>0.127</td>\n",
       "      <td>47</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>0</td>\n",
       "      <td>84</td>\n",
       "      <td>82</td>\n",
       "      <td>31</td>\n",
       "      <td>125</td>\n",
       "      <td>38.2</td>\n",
       "      <td>0.233</td>\n",
       "      <td>23</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>0</td>\n",
       "      <td>145</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>0</td>\n",
       "      <td>44.2</td>\n",
       "      <td>0.630</td>\n",
       "      <td>31</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>0</td>\n",
       "      <td>135</td>\n",
       "      <td>68</td>\n",
       "      <td>42</td>\n",
       "      <td>250</td>\n",
       "      <td>42.3</td>\n",
       "      <td>0.365</td>\n",
       "      <td>24</td>\n",
       "      <td>1</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>1</td>\n",
       "      <td>139</td>\n",
       "      <td>62</td>\n",
       "      <td>41</td>\n",
       "      <td>480</td>\n",
       "      <td>40.7</td>\n",
       "      <td>0.536</td>\n",
       "      <td>21</td>\n",
       "      <td>0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Pregnancies  Glucose  BloodPressure  SkinThickness  Insulin   BMI  \\\n",
       "0            2      138             62             35        0  33.6   \n",
       "1            0       84             82             31      125  38.2   \n",
       "2            0      145              0              0        0  44.2   \n",
       "3            0      135             68             42      250  42.3   \n",
       "4            1      139             62             41      480  40.7   \n",
       "\n",
       "   DiabetesPedigreeFunction  Age  Outcome  \n",
       "0                     0.127   47        1  \n",
       "1                     0.233   23        0  \n",
       "2                     0.630   31        1  \n",
       "3                     0.365   24        1  \n",
       "4                     0.536   21        0  "
      ]
     },
     "execution_count": 37,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df = pd.read_csv(\"diabetes-dataset.csv\")\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f01c3743",
   "metadata": {},
   "source": [
    "#### Before cleaning, the dataset has 9 columns and 2000 rows"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "id": "b1d6504e",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(2000, 9)"
      ]
     },
     "execution_count": 38,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.shape"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f7765547",
   "metadata": {},
   "source": [
    "#### Cleaning dataset and remove anomolies"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "id": "8cb318b5",
   "metadata": {},
   "outputs": [],
   "source": [
    "df = df[df.BloodPressure != 0]\n",
    "df = df[df.Glucose != 0]\n",
    "df = df[df.Insulin != 0]\n",
    "df = df[df.SkinThickness != 0]\n",
    "df = df[df.BMI != 0]"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d4464989",
   "metadata": {},
   "source": [
    "#### After cleaning, the dataset now only has 1035 rows remain"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "id": "32f39b8f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "(1035, 9)"
      ]
     },
     "execution_count": 40,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.shape"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0467cb84",
   "metadata": {},
   "source": [
    "#### Now I will group the entries in the dataset by age group (group 1: 20-30, group 2: 30-40, group 3: 40-50,...)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "id": "28cd7124",
   "metadata": {},
   "outputs": [],
   "source": [
    "age_group1 = 0\n",
    "age_group2 = 0\n",
    "age_group3 = 0\n",
    "age_group4 = 0\n",
    "age_group5 = 0\n",
    "age_group6 = 0\n",
    "age_group7 = 0\n",
    "\n",
    "for age, count in dict(df['Age'].value_counts()).items():\n",
    "    if(age <= 30):\n",
    "        age_group1 += count\n",
    "    elif(age <= 40):\n",
    "        age_group2 += count\n",
    "    elif(age <= 50):\n",
    "        age_group3 += count\n",
    "    elif(age <= 60):\n",
    "        age_group4 += count\n",
    "    elif(age <= 70):\n",
    "        age_group5 += count\n",
    "    elif(age <= 80):\n",
    "        age_group6 += count\n",
    "    elif(age > 80):\n",
    "        age_group7 += count "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d383b420",
   "metadata": {},
   "source": [
    "#### Now I will graph the number of people in each age group"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "b3251036",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "x_axis = ['20-30', '30-40', '40-50','50-60','60-70','70-80','80+']\n",
    "y_axis = [age_group1, age_group2, age_group3, age_group4, age_group5, age_group6, age_group7]\n",
    "plt.bar(x_axis, y_axis)\n",
    "plt.title('Entries per Age Groups')\n",
    "plt.ylabel('Num. Entries')\n",
    "plt.xlabel('Age Group')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "37c37269",
   "metadata": {},
   "source": [
    "#### Looks like a large precentage of people in the dataset fall within the 20-30 age range. Now lets' see how many diabetics are in each age group"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "id": "2e605b2a",
   "metadata": {},
   "outputs": [],
   "source": [
    "age_group_diabetes1 = 0\n",
    "age_group_diabetes2 = 0\n",
    "age_group_diabetes3 = 0\n",
    "age_group_diabetes4 = 0\n",
    "age_group_diabetes5 = 0\n",
    "age_group_diabetes6 = 0\n",
    "age_group_diabetes7 = 0\n",
    "\n",
    "\n",
    "for row in range(len(df)):\n",
    "    age = df.iloc[row]['Age']\n",
    "    outcome = df.iloc[row]['Outcome']\n",
    "    if(age <= 30 and outcome):\n",
    "        age_group_diabetes1 += 1\n",
    "    elif(age <= 40 and outcome):\n",
    "        age_group_diabetes2 += 1\n",
    "    elif(age <= 50 and outcome):\n",
    "        age_group_diabetes3 += 1\n",
    "    elif(age <= 60 and outcome):\n",
    "        age_group_diabetes4 += 1\n",
    "    elif(age <= 70 and outcome):\n",
    "        age_group_diabetes5 += 1\n",
    "    elif(age <= 80 and outcome):\n",
    "        age_group_diabetes6 += 1\n",
    "    elif(age > 80 and outcome):\n",
    "        age_group_diabetes7 += 1"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "dc0de432",
   "metadata": {},
   "source": [
    "#### Create the plot"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "id": "926252d7",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "x_axis = ['20-30', '30-40', '40-50','50-60','60-70','70-80','80+']\n",
    "y_axis = [age_group_diabetes1, age_group_diabetes2, age_group_diabetes3, age_group_diabetes4, age_group_diabetes5, age_group_diabetes6, age_group_diabetes7]\n",
    "plt.bar(x_axis, y_axis)\n",
    "plt.title('Diabetics Per Age Group')\n",
    "plt.ylabel('Num. Diabetics')\n",
    "plt.xlabel('Age Group')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3b405497",
   "metadata": {},
   "source": [
    "#### Seems like most diabetics fall within the age range  20-30. This is to be expected as there are more entries for people who fall within this age range. Now let's see the percent of people in each age group that have diabetes."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "id": "af70b78f",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "C:\\Users\\Ahmad\\AppData\\Local\\Temp\\ipykernel_13744\\1691609417.py:4: RuntimeWarning: invalid value encountered in true_divide\n",
      "  percents = np.divide(diabetics,ages)\n"
     ]
    },
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 432x288 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "diabetics = np.asarray([age_group_diabetes1, age_group_diabetes2, age_group_diabetes3, age_group_diabetes4, age_group_diabetes5, age_group_diabetes6, age_group_diabetes7])\n",
    "ages =  np.asarray([age_group1, age_group2, age_group3, age_group4, age_group5, age_group6, age_group7])\n",
    "\n",
    "percents = np.divide(diabetics,ages)\n",
    "\n",
    "x_axis = ['20-30', '30-40', '40-50','50-60','60-70','70-80','80+']\n",
    "y_axis = percents*100\n",
    "plt.bar(x_axis, y_axis)\n",
    "plt.title('Percent of Diabetics Per Age Group')\n",
    "plt.ylabel('Percent %')\n",
    "plt.xlabel('Age Group')\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "bff17420",
   "metadata": {},
   "source": [
    "#### Display the spread of data using the .std() function. Because all the values of the standard deviation of each column are high, it means that the data is less reliable."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "0514bbae",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Pregnancies                   3.167531\n",
       "Glucose                      30.653888\n",
       "BloodPressure                12.336324\n",
       "SkinThickness                10.558989\n",
       "Insulin                     111.489069\n",
       "BMI                           7.097899\n",
       "DiabetesPedigreeFunction      0.332292\n",
       "Age                          10.047212\n",
       "Outcome                       0.468827\n",
       "dtype: float64"
      ]
     },
     "execution_count": 5,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.std()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f063e684",
   "metadata": {},
   "source": [
    "#### Normalize data for consistency. Each column is normalized based on the largest value in that column such that every entry in the column falls in the range [0,1] "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "0171f8b0",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Pregnancies</th>\n",
       "      <th>Glucose</th>\n",
       "      <th>BloodPressure</th>\n",
       "      <th>SkinThickness</th>\n",
       "      <th>Insulin</th>\n",
       "      <th>BMI</th>\n",
       "      <th>DiabetesPedigreeFunction</th>\n",
       "      <th>Age</th>\n",
       "      <th>Outcome</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.424242</td>\n",
       "      <td>0.745455</td>\n",
       "      <td>0.492063</td>\n",
       "      <td>0.168011</td>\n",
       "      <td>0.569300</td>\n",
       "      <td>0.096281</td>\n",
       "      <td>0.283951</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.681818</td>\n",
       "      <td>0.618182</td>\n",
       "      <td>0.666667</td>\n",
       "      <td>0.336022</td>\n",
       "      <td>0.630402</td>\n",
       "      <td>0.150826</td>\n",
       "      <td>0.296296</td>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>0.058824</td>\n",
       "      <td>0.702020</td>\n",
       "      <td>0.563636</td>\n",
       "      <td>0.650794</td>\n",
       "      <td>0.645161</td>\n",
       "      <td>0.606557</td>\n",
       "      <td>0.221488</td>\n",
       "      <td>0.259259</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.873737</td>\n",
       "      <td>0.709091</td>\n",
       "      <td>0.507937</td>\n",
       "      <td>0.356183</td>\n",
       "      <td>0.692996</td>\n",
       "      <td>0.478926</td>\n",
       "      <td>0.716049</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>8</th>\n",
       "      <td>0.117647</td>\n",
       "      <td>0.419192</td>\n",
       "      <td>0.590909</td>\n",
       "      <td>0.444444</td>\n",
       "      <td>0.088710</td>\n",
       "      <td>0.548435</td>\n",
       "      <td>0.259917</td>\n",
       "      <td>0.296296</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "   Pregnancies   Glucose  BloodPressure  SkinThickness   Insulin       BMI  \\\n",
       "1     0.000000  0.424242       0.745455       0.492063  0.168011  0.569300   \n",
       "3     0.000000  0.681818       0.618182       0.666667  0.336022  0.630402   \n",
       "4     0.058824  0.702020       0.563636       0.650794  0.645161  0.606557   \n",
       "5     0.000000  0.873737       0.709091       0.507937  0.356183  0.692996   \n",
       "8     0.117647  0.419192       0.590909       0.444444  0.088710  0.548435   \n",
       "\n",
       "   DiabetesPedigreeFunction       Age  Outcome  \n",
       "1                  0.096281  0.283951      0.0  \n",
       "3                  0.150826  0.296296      1.0  \n",
       "4                  0.221488  0.259259      0.0  \n",
       "5                  0.478926  0.716049      0.0  \n",
       "8                  0.259917  0.296296      0.0  "
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "for column in df.columns:\n",
    "    df[column] = df[column]  / df[column].abs().max()\n",
    "\n",
    "df.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9594e0dd",
   "metadata": {},
   "source": [
    "#### Shuffle the data 100 times. Excessive, but done to avoid inequalities found in data when entries were first recorded, it also helps spread the data so that there isn't data disparity."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "665eaa3d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Pregnancies</th>\n",
       "      <th>Glucose</th>\n",
       "      <th>BloodPressure</th>\n",
       "      <th>SkinThickness</th>\n",
       "      <th>Insulin</th>\n",
       "      <th>BMI</th>\n",
       "      <th>DiabetesPedigreeFunction</th>\n",
       "      <th>Age</th>\n",
       "      <th>Outcome</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>1487</th>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.681818</td>\n",
       "      <td>0.854545</td>\n",
       "      <td>0.730159</td>\n",
       "      <td>0.194892</td>\n",
       "      <td>0.605067</td>\n",
       "      <td>0.117355</td>\n",
       "      <td>0.320988</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>228</th>\n",
       "      <td>0.235294</td>\n",
       "      <td>0.994949</td>\n",
       "      <td>0.636364</td>\n",
       "      <td>0.619048</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.546945</td>\n",
       "      <td>0.962397</td>\n",
       "      <td>0.382716</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1700</th>\n",
       "      <td>0.411765</td>\n",
       "      <td>0.848485</td>\n",
       "      <td>0.800000</td>\n",
       "      <td>0.666667</td>\n",
       "      <td>0.431452</td>\n",
       "      <td>0.569300</td>\n",
       "      <td>0.325207</td>\n",
       "      <td>0.493827</td>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>165</th>\n",
       "      <td>0.352941</td>\n",
       "      <td>0.525253</td>\n",
       "      <td>0.672727</td>\n",
       "      <td>0.285714</td>\n",
       "      <td>0.209677</td>\n",
       "      <td>0.445604</td>\n",
       "      <td>0.298347</td>\n",
       "      <td>0.506173</td>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>414</th>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.696970</td>\n",
       "      <td>0.545455</td>\n",
       "      <td>0.555556</td>\n",
       "      <td>0.224462</td>\n",
       "      <td>0.515648</td>\n",
       "      <td>0.220661</td>\n",
       "      <td>0.259259</td>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "      Pregnancies   Glucose  BloodPressure  SkinThickness   Insulin       BMI  \\\n",
       "1487     0.000000  0.681818       0.854545       0.730159  0.194892  0.605067   \n",
       "228      0.235294  0.994949       0.636364       0.619048  1.000000  0.546945   \n",
       "1700     0.411765  0.848485       0.800000       0.666667  0.431452  0.569300   \n",
       "165      0.352941  0.525253       0.672727       0.285714  0.209677  0.445604   \n",
       "414      0.000000  0.696970       0.545455       0.555556  0.224462  0.515648   \n",
       "\n",
       "      DiabetesPedigreeFunction       Age  Outcome  \n",
       "1487                  0.117355  0.320988      0.0  \n",
       "228                   0.962397  0.382716      0.0  \n",
       "1700                  0.325207  0.493827      1.0  \n",
       "165                   0.298347  0.506173      1.0  \n",
       "414                   0.220661  0.259259      1.0  "
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "for i in range(100):\n",
    "    df = df.sample(frac=1)\n",
    "    \n",
    "df.head()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "46cd741c",
   "metadata": {},
   "source": [
    "#### Display the spread of data using the .std() function after shuffling. Because all the values of the standard deviation of each column are low, it means that the data is more reliable."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "c2df701f",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Pregnancies                 0.186325\n",
       "Glucose                     0.154818\n",
       "BloodPressure               0.112148\n",
       "SkinThickness               0.167603\n",
       "Insulin                     0.149851\n",
       "BMI                         0.105781\n",
       "DiabetesPedigreeFunction    0.137311\n",
       "Age                         0.124040\n",
       "Outcome                     0.468827\n",
       "dtype: float64"
      ]
     },
     "execution_count": 9,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.std()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "dd25c31f",
   "metadata": {},
   "source": [
    "#### Split data into 80% for training set, and 20% for testing set. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "14380645",
   "metadata": {},
   "outputs": [],
   "source": [
    "training_data, testing_data = train_test_split(df, train_size=0.8, test_size=0.2, random_state=42)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "id": "a6c9a96d",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Pregnancies</th>\n",
       "      <th>Glucose</th>\n",
       "      <th>BloodPressure</th>\n",
       "      <th>SkinThickness</th>\n",
       "      <th>Insulin</th>\n",
       "      <th>BMI</th>\n",
       "      <th>DiabetesPedigreeFunction</th>\n",
       "      <th>Age</th>\n",
       "      <th>Outcome</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>442</th>\n",
       "      <td>0.235294</td>\n",
       "      <td>0.590909</td>\n",
       "      <td>0.581818</td>\n",
       "      <td>0.428571</td>\n",
       "      <td>0.161290</td>\n",
       "      <td>0.494784</td>\n",
       "      <td>0.095041</td>\n",
       "      <td>0.296296</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>544</th>\n",
       "      <td>0.058824</td>\n",
       "      <td>0.444444</td>\n",
       "      <td>0.709091</td>\n",
       "      <td>0.460317</td>\n",
       "      <td>0.102151</td>\n",
       "      <td>0.476900</td>\n",
       "      <td>0.150826</td>\n",
       "      <td>0.358025</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1685</th>\n",
       "      <td>0.058824</td>\n",
       "      <td>0.404040</td>\n",
       "      <td>0.672727</td>\n",
       "      <td>0.174603</td>\n",
       "      <td>0.080645</td>\n",
       "      <td>0.447094</td>\n",
       "      <td>0.217769</td>\n",
       "      <td>0.271605</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1189</th>\n",
       "      <td>0.117647</td>\n",
       "      <td>0.878788</td>\n",
       "      <td>0.800000</td>\n",
       "      <td>0.587302</td>\n",
       "      <td>0.161290</td>\n",
       "      <td>0.663189</td>\n",
       "      <td>0.266942</td>\n",
       "      <td>0.296296</td>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>445</th>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.909091</td>\n",
       "      <td>0.709091</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.018817</td>\n",
       "      <td>0.885246</td>\n",
       "      <td>1.000000</td>\n",
       "      <td>0.308642</td>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>777</th>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.691919</td>\n",
       "      <td>0.618182</td>\n",
       "      <td>0.222222</td>\n",
       "      <td>0.198925</td>\n",
       "      <td>0.369598</td>\n",
       "      <td>0.059091</td>\n",
       "      <td>0.259259</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>127</th>\n",
       "      <td>0.058824</td>\n",
       "      <td>0.595960</td>\n",
       "      <td>0.527273</td>\n",
       "      <td>0.571429</td>\n",
       "      <td>0.126344</td>\n",
       "      <td>0.496274</td>\n",
       "      <td>0.107851</td>\n",
       "      <td>0.283951</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1190</th>\n",
       "      <td>0.117647</td>\n",
       "      <td>0.535354</td>\n",
       "      <td>0.509091</td>\n",
       "      <td>0.428571</td>\n",
       "      <td>0.221774</td>\n",
       "      <td>0.432191</td>\n",
       "      <td>0.176033</td>\n",
       "      <td>0.271605</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1120</th>\n",
       "      <td>0.529412</td>\n",
       "      <td>0.732323</td>\n",
       "      <td>0.727273</td>\n",
       "      <td>0.730159</td>\n",
       "      <td>0.174731</td>\n",
       "      <td>0.564829</td>\n",
       "      <td>0.263223</td>\n",
       "      <td>0.493827</td>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>125</th>\n",
       "      <td>0.058824</td>\n",
       "      <td>0.444444</td>\n",
       "      <td>0.272727</td>\n",
       "      <td>0.666667</td>\n",
       "      <td>0.133065</td>\n",
       "      <td>0.819672</td>\n",
       "      <td>0.204959</td>\n",
       "      <td>0.320988</td>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>828 rows × 9 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "      Pregnancies   Glucose  BloodPressure  SkinThickness   Insulin       BMI  \\\n",
       "442      0.235294  0.590909       0.581818       0.428571  0.161290  0.494784   \n",
       "544      0.058824  0.444444       0.709091       0.460317  0.102151  0.476900   \n",
       "1685     0.058824  0.404040       0.672727       0.174603  0.080645  0.447094   \n",
       "1189     0.117647  0.878788       0.800000       0.587302  0.161290  0.663189   \n",
       "445      0.000000  0.909091       0.709091       1.000000  0.018817  0.885246   \n",
       "...           ...       ...            ...            ...       ...       ...   \n",
       "777      0.000000  0.691919       0.618182       0.222222  0.198925  0.369598   \n",
       "127      0.058824  0.595960       0.527273       0.571429  0.126344  0.496274   \n",
       "1190     0.117647  0.535354       0.509091       0.428571  0.221774  0.432191   \n",
       "1120     0.529412  0.732323       0.727273       0.730159  0.174731  0.564829   \n",
       "125      0.058824  0.444444       0.272727       0.666667  0.133065  0.819672   \n",
       "\n",
       "      DiabetesPedigreeFunction       Age  Outcome  \n",
       "442                   0.095041  0.296296      0.0  \n",
       "544                   0.150826  0.358025      0.0  \n",
       "1685                  0.217769  0.271605      0.0  \n",
       "1189                  0.266942  0.296296      1.0  \n",
       "445                   1.000000  0.308642      1.0  \n",
       "...                        ...       ...      ...  \n",
       "777                   0.059091  0.259259      0.0  \n",
       "127                   0.107851  0.283951      0.0  \n",
       "1190                  0.176033  0.271605      0.0  \n",
       "1120                  0.263223  0.493827      1.0  \n",
       "125                   0.204959  0.320988      1.0  \n",
       "\n",
       "[828 rows x 9 columns]"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "training_data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "id": "0dde6456",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>Pregnancies</th>\n",
       "      <th>Glucose</th>\n",
       "      <th>BloodPressure</th>\n",
       "      <th>SkinThickness</th>\n",
       "      <th>Insulin</th>\n",
       "      <th>BMI</th>\n",
       "      <th>DiabetesPedigreeFunction</th>\n",
       "      <th>Age</th>\n",
       "      <th>Outcome</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>1278</th>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.818182</td>\n",
       "      <td>0.690909</td>\n",
       "      <td>0.888889</td>\n",
       "      <td>0.134409</td>\n",
       "      <td>0.792846</td>\n",
       "      <td>0.313636</td>\n",
       "      <td>0.308642</td>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>313</th>\n",
       "      <td>0.176471</td>\n",
       "      <td>0.570707</td>\n",
       "      <td>0.454545</td>\n",
       "      <td>0.158730</td>\n",
       "      <td>0.114247</td>\n",
       "      <td>0.439642</td>\n",
       "      <td>0.258678</td>\n",
       "      <td>0.308642</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1582</th>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.686869</td>\n",
       "      <td>0.672727</td>\n",
       "      <td>0.777778</td>\n",
       "      <td>0.295699</td>\n",
       "      <td>0.299553</td>\n",
       "      <td>0.338843</td>\n",
       "      <td>0.543210</td>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1892</th>\n",
       "      <td>0.294118</td>\n",
       "      <td>0.702020</td>\n",
       "      <td>0.581818</td>\n",
       "      <td>0.555556</td>\n",
       "      <td>0.188172</td>\n",
       "      <td>0.426230</td>\n",
       "      <td>0.169835</td>\n",
       "      <td>0.320988</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1549</th>\n",
       "      <td>0.117647</td>\n",
       "      <td>0.419192</td>\n",
       "      <td>0.590909</td>\n",
       "      <td>0.444444</td>\n",
       "      <td>0.088710</td>\n",
       "      <td>0.548435</td>\n",
       "      <td>0.259917</td>\n",
       "      <td>0.296296</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>...</th>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "      <td>...</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1193</th>\n",
       "      <td>0.000000</td>\n",
       "      <td>0.636364</td>\n",
       "      <td>0.781818</td>\n",
       "      <td>0.428571</td>\n",
       "      <td>0.161290</td>\n",
       "      <td>0.408346</td>\n",
       "      <td>0.212810</td>\n",
       "      <td>0.259259</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1733</th>\n",
       "      <td>0.117647</td>\n",
       "      <td>0.792929</td>\n",
       "      <td>0.672727</td>\n",
       "      <td>0.555556</td>\n",
       "      <td>0.591398</td>\n",
       "      <td>0.587183</td>\n",
       "      <td>0.055372</td>\n",
       "      <td>0.370370</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>421</th>\n",
       "      <td>0.117647</td>\n",
       "      <td>0.474747</td>\n",
       "      <td>0.618182</td>\n",
       "      <td>0.285714</td>\n",
       "      <td>0.102151</td>\n",
       "      <td>0.387481</td>\n",
       "      <td>0.231818</td>\n",
       "      <td>0.259259</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>956</th>\n",
       "      <td>0.058824</td>\n",
       "      <td>0.702020</td>\n",
       "      <td>0.563636</td>\n",
       "      <td>0.650794</td>\n",
       "      <td>0.645161</td>\n",
       "      <td>0.606557</td>\n",
       "      <td>0.221488</td>\n",
       "      <td>0.259259</td>\n",
       "      <td>0.0</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>309</th>\n",
       "      <td>0.117647</td>\n",
       "      <td>0.626263</td>\n",
       "      <td>0.618182</td>\n",
       "      <td>0.444444</td>\n",
       "      <td>0.275538</td>\n",
       "      <td>0.490313</td>\n",
       "      <td>0.361570</td>\n",
       "      <td>0.370370</td>\n",
       "      <td>1.0</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "<p>207 rows × 9 columns</p>\n",
       "</div>"
      ],
      "text/plain": [
       "      Pregnancies   Glucose  BloodPressure  SkinThickness   Insulin       BMI  \\\n",
       "1278     0.000000  0.818182       0.690909       0.888889  0.134409  0.792846   \n",
       "313      0.176471  0.570707       0.454545       0.158730  0.114247  0.439642   \n",
       "1582     0.000000  0.686869       0.672727       0.777778  0.295699  0.299553   \n",
       "1892     0.294118  0.702020       0.581818       0.555556  0.188172  0.426230   \n",
       "1549     0.117647  0.419192       0.590909       0.444444  0.088710  0.548435   \n",
       "...           ...       ...            ...            ...       ...       ...   \n",
       "1193     0.000000  0.636364       0.781818       0.428571  0.161290  0.408346   \n",
       "1733     0.117647  0.792929       0.672727       0.555556  0.591398  0.587183   \n",
       "421      0.117647  0.474747       0.618182       0.285714  0.102151  0.387481   \n",
       "956      0.058824  0.702020       0.563636       0.650794  0.645161  0.606557   \n",
       "309      0.117647  0.626263       0.618182       0.444444  0.275538  0.490313   \n",
       "\n",
       "      DiabetesPedigreeFunction       Age  Outcome  \n",
       "1278                  0.313636  0.308642      1.0  \n",
       "313                   0.258678  0.308642      0.0  \n",
       "1582                  0.338843  0.543210      1.0  \n",
       "1892                  0.169835  0.320988      0.0  \n",
       "1549                  0.259917  0.296296      0.0  \n",
       "...                        ...       ...      ...  \n",
       "1193                  0.212810  0.259259      0.0  \n",
       "1733                  0.055372  0.370370      0.0  \n",
       "421                   0.231818  0.259259      0.0  \n",
       "956                   0.221488  0.259259      0.0  \n",
       "309                   0.361570  0.370370      1.0  \n",
       "\n",
       "[207 rows x 9 columns]"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "testing_data"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "363baff5",
   "metadata": {},
   "source": [
    "#### Set the training data to be all the input columns of the dataset, columns 1 to 8, and the training dataset to be the last column (9)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "id": "460c97f7",
   "metadata": {},
   "outputs": [],
   "source": [
    "x_train = training_data[training_data.columns[:-1]]\n",
    "y_train = training_data[training_data.columns[-1]]"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1999d0df",
   "metadata": {},
   "source": [
    "#### Set the testing data to be all the input columns of the dataset, columns 1 to 8, and the testing dataset to be the last column (9)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "id": "d010f2a5",
   "metadata": {},
   "outputs": [],
   "source": [
    "x_test = testing_data[testing_data.columns[:-1]]\n",
    "y_test = testing_data[testing_data.columns[-1]]"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "72dd8fb2",
   "metadata": {},
   "source": [
    "#### Build Logistic Regression Model, train the model and show the accuracy of it. This will be the default model as it is built on all the input columns."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "0d23a550",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Accuracy: 73.91%\n"
     ]
    }
   ],
   "source": [
    "model = LogisticRegression(solver='liblinear')\n",
    "model.fit(x_train, y_train)\n",
    "\n",
    "\n",
    "model_accuracy = model.score(x_test, y_test) * 100.0\n",
    "print(\"Accuracy: %.2f%%\" % model_accuracy) # accuracy of the model"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "cb0b8472",
   "metadata": {},
   "source": [
    "#### The default model seems to have a 73.91% accuracy rate at predicting whether a person has diabetes or not. This is quite accurate but let's see if we can do better. From researching the leading causes of diabetes I will create a model that only takes in attributes that have the most impact on determining whether the person has diabetes or not. Based on my findings from doing some research, my new modified model will include the attributes: 'Glucose', 'BloodPressure', 'Insulin', 'BMI', 'DiabetesPedigreeFunction', 'Age'."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 16,
   "id": "6d22b374",
   "metadata": {},
   "outputs": [],
   "source": [
    "x_train_2 = training_data.iloc[:, [1,2,4,5,6,7]]\n",
    "y_train_2 = training_data[training_data.columns[-1]]\n",
    "\n",
    "x_test_2 = testing_data.iloc[:, [1,2,4,5,6,7]]\n",
    "y_test_2 = testing_data[testing_data.columns[-1]]"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1e91bdc0",
   "metadata": {},
   "source": [
    "#### Build the new logistic regression model based on the research done, train it and show its accuracy. This will be the modified model as it is built on input columns that seem to have the most impact on a person's diabetic nature."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "f2182f92",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Accuracy: 72.95%\n"
     ]
    }
   ],
   "source": [
    "modified_model = LogisticRegression()\n",
    "modified_model.fit(x_train_2, y_train_2)\n",
    "\n",
    "modified_model_accuracy = modified_model.score(x_test_2, y_test_2) * 100.0\n",
    "print(\"Accuracy: %.2f%%\" % modified_model_accuracy) # accuracy of the model"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "20fb2fb1",
   "metadata": {},
   "source": [
    "#### The modified model seems to have 72.95% accuracy, which unfortunately is worse than before. It seems like the model performs worse with less input. Now, let us see if we can build a different kind of model that is more accurate than logistic regression. The first model I will build will be Xgboost. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "id": "9d4a9b4c",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "XGBClassifier(base_score=0.5, booster='gbtree', callbacks=None,\n",
       "              colsample_bylevel=1, colsample_bynode=1, colsample_bytree=1,\n",
       "              early_stopping_rounds=None, enable_categorical=False,\n",
       "              eval_metric=None, feature_types=None, gamma=0, gpu_id=-1,\n",
       "              grow_policy='depthwise', importance_type=None,\n",
       "              interaction_constraints='', learning_rate=0.300000012,\n",
       "              max_bin=256, max_cat_threshold=64, max_cat_to_onehot=4,\n",
       "              max_delta_step=0, max_depth=6, max_leaves=0, min_child_weight=1,\n",
       "              missing=nan, monotone_constraints='()', n_estimators=100,\n",
       "              n_jobs=0, num_parallel_tree=1, predictor='auto', random_state=0, ...)"
      ]
     },
     "execution_count": 18,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "model_xg = XGBClassifier()\n",
    "model_xg.fit(x_train, y_train)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "6db7de06",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Accuracy: 95.65%\n"
     ]
    }
   ],
   "source": [
    "# make predictions for test data\n",
    "y_pred = model_xg.predict(x_test)\n",
    "predictions = [round(value) for value in y_pred]\n",
    "\n",
    "model_xg_accuracy = accuracy_score(y_test, predictions) * 100.0\n",
    "print(\"Accuracy: %.2f%%\" % model_xg_accuracy)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c27c0aa6",
   "metadata": {},
   "source": [
    "#### Incredible! The Xgboost model has a prediction accuracy of 95.65%. Now let's how Xgboost performs compared to a Decision Tree model. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "id": "c87d1c1d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Accuracy: 95.17%\n"
     ]
    }
   ],
   "source": [
    "model_dct = DecisionTreeClassifier()\n",
    "model_dct.fit(x_train, y_train)\n",
    "model_dct_accuracy = model_dct.score(x_test, y_test) * 100.0\n",
    "\n",
    "\n",
    "print(\"Accuracy: %.2f%%\" % (model_dct_accuracy)) # accuracy of the model"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "56be3dff",
   "metadata": {},
   "source": [
    "#### The Decision Tree model has a prediction accuracy of 95.17%, which is fantastic. The Xgboost model still outperformed the Decision Tree model, but both are incredibly accurate. Now let's compare these models to a new modeling called Support Vector Machine (SVM)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "id": "d90d7340",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Accuracy: 76.33%\n"
     ]
    }
   ],
   "source": [
    "model_svm=LinearSVC()\n",
    "model_svm.fit(x_train, y_train)\n",
    "model_svm_accuracy = model_svm.score(x_test, y_test)* 100.0\n",
    "\n",
    "\n",
    "print(\"Accuracy: %.2f%%\" % (model_svm_accuracy)) # accuracy of the model"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "21bc9c6f",
   "metadata": {},
   "source": [
    "#### Looks like the Support Vector Machine (SVM) model has a 76.33% accuracy for predicting whether a person is diabetic or not. Now lets visually compare the accuracies of the model by using a bar plot."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "id": "d4444f96",
   "metadata": {
    "scrolled": false
   },
   "outputs": [
    {
     "data": {
      "image/png": "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\n",
      "text/plain": [
       "<Figure size 1440x720 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "model_accuracies = { 'Modified Logistic Regression': modified_model_accuracy, 'Default Logistic Regression': model_accuracy, 'Support Vector Machine (SVM)': model_svm_accuracy, 'Decision Tree': model_dct_accuracy, 'XgBoost':model_xg_accuracy}\n",
    "\n",
    "model_used = list(model_accuracies.keys())\n",
    "accuracy_attained = list(model_accuracies.values())\n",
    "  \n",
    "fig = plt.figure(figsize = (20, 10))\n",
    " \n",
    "# creating the bar plot\n",
    "plt.bar(model_used, accuracy_attained,color ='blue',\n",
    "        width = 0.9)\n",
    "plt.xticks(fontsize=12)\n",
    "plt.yticks(np.arange(0, 105, 5), fontsize=12)\n",
    "\n",
    "plt.xlabel(\"Model Used\", fontsize=15)\n",
    "plt.ylabel(\"Accuracy %\", fontsize=15)\n",
    "plt.title(\"Accuracy % of different Binary Classification Models\", fontsize=20)\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "084f4387",
   "metadata": {},
   "source": [
    "#### As we can clearly see, Xgboost and Decision Tree were the most accurate, Support Vector Machine (SVM) coming in next, and the Logistic Regression models coming in at the end"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "31c20852",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.12"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
