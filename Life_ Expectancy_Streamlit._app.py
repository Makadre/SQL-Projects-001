{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "ca8a06ca-2120-4dde-8fca-a547ebfbd334",
   "metadata": {},
   "source": [
    "### Project: Life Expectancy (WHO) Prediction with Streamlit\n",
    "We are working with a **World Health Organisation (WHO)** dataset, which contains indicators on global health trends, such as life expectancy, mortality rates, access to sanitation, etc. \n",
    "\n",
    "### Objective\n",
    "- The dataset includes health-related statistics for countries over time (e.g., life expectancy, fertility rates, or other health indicators)\n",
    "- Display visualizations like prediction vs actual values and other charts.\n",
    "- Trains the model and predicts life expectancy using Linear Regression.\n",
    "- Deploy the model using Streamlit to allow the user to input health data (e.g., health expenditure,   mortality rate, etc.) \n",
    "\n",
    "### Steps to build the Project:\n",
    "\n",
    "1. **Obtain the WHO Dataset**.\n",
    "2. **Preprocess and Clean the Data**.\n",
    "3. **Visualize the Data**.\n",
    "4. **Train a Model** to predict life expectancy or health indicator.\n",
    "5. **Deploy the Model using Streamlit**.\n",
    "\n",
    "### Dataset\n",
    "We'll use the Life Expectancy (WHO) n dataset from Kaggle, which contains statistical analysis on factors influencing Life Expectancy.\n",
    "\n",
    "### Dataset URL: https://www.kaggle.com/datasets/kumarajarshi/life-expectancy-who "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "bdeb46c6-f706-43a0-aa55-195283f4cd67",
   "metadata": {},
   "source": [
    "### Load and Preprocess the Data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "310d0466-22e9-4eac-ab4b-ef5a83770d7d",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import streamlit as st\n",
    "from sklearn.model_selection import train_test_split\n",
    "from sklearn.linear_model import LinearRegression\n",
    "from sklearn.metrics import mean_squared_error, r2_score\n",
    "from sklearn.preprocessing import StandardScaler\n",
    "import seaborn as sns\n",
    "import matplotlib.pyplot as plt"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "dc82a97b-de96-41a0-9ebc-a4cc8fbec9b6",
   "metadata": {},
   "source": [
    "# Load life expectancy dataset\n",
    "This function loads the dataset from the provided file path."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "id": "d4ee93b1-fd0a-4226-9af3-20f9dc54b9cb",
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.read_csv(r\"C:\\Users\\Oguntuga\\Downloads\\Life Expectancy Data.csv\")"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8e97c165-8f85-4af9-b31f-f00afdc4cc7e",
   "metadata": {},
   "source": [
    "# Explore data"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "id": "bc686c9a-6a38-4256-94a3-fc1bf55efac6",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "       Country  Year      Status  Life expectancy   Adult Mortality  \\\n",
      "0  Afghanistan  2015  Developing              65.0            263.0   \n",
      "1  Afghanistan  2014  Developing              59.9            271.0   \n",
      "2  Afghanistan  2013  Developing              59.9            268.0   \n",
      "3  Afghanistan  2012  Developing              59.5            272.0   \n",
      "4  Afghanistan  2011  Developing              59.2            275.0   \n",
      "\n",
      "   infant deaths  Alcohol  percentage expenditure  Hepatitis B  Measles   ...  \\\n",
      "0             62     0.01               71.279624         65.0      1154  ...   \n",
      "1             64     0.01               73.523582         62.0       492  ...   \n",
      "2             66     0.01               73.219243         64.0       430  ...   \n",
      "3             69     0.01               78.184215         67.0      2787  ...   \n",
      "4             71     0.01                7.097109         68.0      3013  ...   \n",
      "\n",
      "   Polio  Total expenditure  Diphtheria    HIV/AIDS         GDP  Population  \\\n",
      "0    6.0               8.16         65.0        0.1  584.259210  33736494.0   \n",
      "1   58.0               8.18         62.0        0.1  612.696514    327582.0   \n",
      "2   62.0               8.13         64.0        0.1  631.744976  31731688.0   \n",
      "3   67.0               8.52         67.0        0.1  669.959000   3696958.0   \n",
      "4   68.0               7.87         68.0        0.1   63.537231   2978599.0   \n",
      "\n",
      "    thinness  1-19 years   thinness 5-9 years  \\\n",
      "0                   17.2                 17.3   \n",
      "1                   17.5                 17.5   \n",
      "2                   17.7                 17.7   \n",
      "3                   17.9                 18.0   \n",
      "4                   18.2                 18.2   \n",
      "\n",
      "   Income composition of resources  Schooling  \n",
      "0                            0.479       10.1  \n",
      "1                            0.476       10.0  \n",
      "2                            0.470        9.9  \n",
      "3                            0.463        9.8  \n",
      "4                            0.454        9.5  \n",
      "\n",
      "[5 rows x 22 columns]\n"
     ]
    }
   ],
   "source": [
    "print(df.head())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "id": "6cf9f925-54dc-4bbf-b889-6edfdd405e94",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "RangeIndex: 2938 entries, 0 to 2937\n",
      "Data columns (total 22 columns):\n",
      " #   Column                           Non-None Count  Dtype  \n",
      "---  ------                           --------------  -----  \n",
      " 0   Country                          2938 non-none   object \n",
      " 1   Year                             2938 non-none   int64  \n",
      " 2   Status                           2938 non-none   object \n",
      " 3   Life expectancy                  2928 non-none   float64\n",
      " 4   Adult Mortality                  2928 non-none   float64\n",
      " 5   infant deaths                    2938 non-none   int64  \n",
      " 6   Alcohol                          2744 non-none   float64\n",
      " 7   percentage expenditure           2938 non-none   float64\n",
      " 8   Hepatitis B                      2385 non-none   float64\n",
      " 9   Measles                          2938 non-none   int64  \n",
      " 10   BMI                             2904 non-none   float64\n",
      " 11  under-five deaths                2938 non-none   int64  \n",
      " 12  Polio                            2919 non-none   float64\n",
      " 13  Total expenditure                2712 non-none   float64\n",
      " 14  Diphtheria                       2919 non-none   float64\n",
      " 15   HIV/AIDS                        2938 non-none   float64\n",
      " 16  GDP                              2490 non-none   float64\n",
      " 17  Population                       2286 non-none   float64\n",
      " 18   thinness  1-19 years            2904 non-none   float64\n",
      " 19   thinness 5-9 years              2904 non-none   float64\n",
      " 20  Income composition of resources  2771 non-none   float64\n",
      " 21  Schooling                        2775 non-none   float64\n",
      "dtypes: float64(16), int64(4), object(2)\n",
      "memory usage: 505.1+ KB\n",
      "None\n"
     ]
    }
   ],
   "source": [
    "print(df.info())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 53,
   "id": "95469c10-20e6-4793-9353-3e2c2be384bd",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "              Year  Life expectancy   Adult Mortality  infant deaths  \\\n",
      "count  2938.000000       2928.000000      2928.000000    2938.000000   \n",
      "mean   2007.518720         69.224932       164.796448      30.303948   \n",
      "std       4.613841          9.523867       124.292079     117.926501   \n",
      "min    2000.000000         36.300000         1.000000       0.000000   \n",
      "25%    2004.000000         63.100000        74.000000       0.000000   \n",
      "50%    2008.000000         72.100000       144.000000       3.000000   \n",
      "75%    2012.000000         75.700000       228.000000      22.000000   \n",
      "max    2015.000000         89.000000       723.000000    1800.000000   \n",
      "\n",
      "           Alcohol  percentage expenditure  Hepatitis B       Measles   \\\n",
      "count  2744.000000             2938.000000  2385.000000    2938.000000   \n",
      "mean      4.602861              738.251295    80.940461    2419.592240   \n",
      "std       4.052413             1987.914858    25.070016   11467.272489   \n",
      "min       0.010000                0.000000     1.000000       0.000000   \n",
      "25%       0.877500                4.685343    77.000000       0.000000   \n",
      "50%       3.755000               64.912906    92.000000      17.000000   \n",
      "75%       7.702500              441.534144    97.000000     360.250000   \n",
      "max      17.870000            19479.911610    99.000000  212183.000000   \n",
      "\n",
      "              BMI   under-five deaths         Polio  Total expenditure  \\\n",
      "count  2904.000000         2938.000000  2919.000000         2712.00000   \n",
      "mean     38.321247           42.035739    82.550188            5.93819   \n",
      "std      20.044034          160.445548    23.428046            2.49832   \n",
      "min       1.000000            0.000000     3.000000            0.37000   \n",
      "25%      19.300000            0.000000    78.000000            4.26000   \n",
      "50%      43.500000            4.000000    93.000000            5.75500   \n",
      "75%      56.200000           28.000000    97.000000            7.49250   \n",
      "max      87.300000         2500.000000    99.000000           17.60000   \n",
      "\n",
      "       Diphtheria      HIV/AIDS            GDP    Population  \\\n",
      "count  2919.000000  2938.000000    2490.000000  2.286000e+03   \n",
      "mean     82.324084     1.742103    7483.158469  1.275338e+07   \n",
      "std      23.716912     5.077785   14270.169342  6.101210e+07   \n",
      "min       2.000000     0.100000       1.681350  3.400000e+01   \n",
      "25%      78.000000     0.100000     463.935626  1.957932e+05   \n",
      "50%      93.000000     0.100000    1766.947595  1.386542e+06   \n",
      "75%      97.000000     0.800000    5910.806335  7.420359e+06   \n",
      "max      99.000000    50.600000  119172.741800  1.293859e+09   \n",
      "\n",
      "        thinness  1-19 years   thinness 5-9 years  \\\n",
      "count            2904.000000          2904.000000   \n",
      "mean                4.839704             4.870317   \n",
      "std                 4.420195             4.508882   \n",
      "min                 0.100000             0.100000   \n",
      "25%                 1.600000             1.500000   \n",
      "50%                 3.300000             3.300000   \n",
      "75%                 7.200000             7.200000   \n",
      "max                27.700000            28.600000   \n",
      "\n",
      "       Income composition of resources    Schooling  \n",
      "count                      2771.000000  2775.000000  \n",
      "mean                          0.627551    11.992793  \n",
      "std                           0.210904     3.358920  \n",
      "min                           0.000000     0.000000  \n",
      "25%                           0.493000    10.100000  \n",
      "50%                           0.677000    12.300000  \n",
      "75%                           0.779000    14.300000  \n",
      "max                           0.948000    20.700000  \n"
     ]
    }
   ],
   "source": [
    "#### Summary Statistics\n",
    "print(df.describe())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4ec40bc7-d4c5-4a08-b6cd-0eefbe24ffb1",
   "metadata": {},
   "source": [
    "# Preprocess the dataset\n",
    "This function preprocesses the dataset by dropping missing values\n",
    "and separating the target and feature variables."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "id": "17cd0ec8-f708-4a12-95b6-ce34b3c7ea88",
   "metadata": {},
   "outputs": [],
   "source": [
    "def preprocess_data(df):\n",
    "    \n",
    "    # Check if necessary columns exist in the dataframe\n",
    "    if 'Life Expectancy' not in df.columns:\n",
    "        st.error(\"Dataset does not contain 'Life Expectancy' column.\")\n",
    "        return None, None  # Return None if the column is missing\n",
    "    \n",
    "    # Drop rows with missing target values (Life Expectancy)\n",
    "    df = df.dropna(subset=['Life Expectancy'])  \n",
    "    # Drop rows with missing feature values\n",
    "    df = df.dropna()\n",
    "    \n",
    "    # Convert 'Country' to category type (if necessary)\n",
    "    if 'Country' in df.columns:\n",
    "        df.loc[:, 'Country'] = df['Country'].astype('category')\n",
    "    \n",
    "    # Drop non-relevant columns like 'Country' and 'Year' (we assume 'Country' is categorical)\n",
    "    if 'Country' in df.columns:\n",
    "        df = df.drop(columns=['Country', 'Year'], errors='ignore')  # Use errors='ignore' to avoid KeyError if 'Country' or 'Year' is missing\n",
    "    \n",
    "    # Separate the target variable and features\n",
    "    X = df.drop(columns='Life Expectancy')\n",
    "    y = df['Life Expectancy']\n",
    "    \n",
    "    # Ensure X and y are not empty\n",
    "    if X.empty or y.empty:\n",
    "        st.error(\"Dataframe preprocessing failed: Empty feature or target.\")\n",
    "        return None, None\n",
    "    \n",
    "    return X, y\n",
    "    "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "id": "5b55bfea-6802-4e86-8b17-9d382f2a225d",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Index(['Country', 'Year', 'Status', 'Life expectancy ', 'Adult Mortality',\n",
      "       'infant deaths', 'Alcohol', 'percentage expenditure', 'Hepatitis B',\n",
      "       'Measles ', ' BMI ', 'under-five deaths ', 'Polio', 'Total expenditure',\n",
      "       'Diphtheria ', ' HIV/AIDS', 'GDP', 'Population',\n",
      "       ' thinness  1-19 years', ' thinness 5-9 years',\n",
      "       'Income composition of resources', 'Schooling'],\n",
      "      dtype='object')\n"
     ]
    }
   ],
   "source": [
    "print(df.columns)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c35cfa76-c735-4712-afde-91596e05a805",
   "metadata": {},
   "source": [
    "# Train a Linear Regression model\n",
    "This function trains the model using linear regression."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 74,
   "id": "45ccb4a1-9cab-4ec2-90f4-b446ed7bca34",
   "metadata": {},
   "outputs": [],
   "source": [
    "def train_model(X_train, y_train):\n",
    "    model = LinearRegression()\n",
    "    model.fit(X_train, y_train)\n",
    "    return model"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4ca13a3a-5b32-4651-80f2-5b5b562aa84e",
   "metadata": {},
   "source": [
    "# Evaluate the model\n",
    "This function evaluates the trained model and returns the Mean Squared Error and R-squared value."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 77,
   "id": "fb359db9-41e2-45f8-b5c3-905729a18e9e",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "def evaluate_model(model, X_test, y_test):\n",
    "    y_pred = model.predict(X_test)\n",
    "    mse = mean_squared_error(y_test, y_pred)\n",
    "    r2 = r2_score(y_test, y_pred)\n",
    "    return mse, r2, y_pred\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 79,
   "id": "a4083a0d-974c-4ae7-9ea1-9fdfdd12697b",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<bound method DataFrame.mean of           Country  Year      Status  Life expectancy   Adult Mortality  \\\n",
      "0     Afghanistan  2015  Developing              65.0            263.0   \n",
      "1     Afghanistan  2014  Developing              59.9            271.0   \n",
      "2     Afghanistan  2013  Developing              59.9            268.0   \n",
      "3     Afghanistan  2012  Developing              59.5            272.0   \n",
      "4     Afghanistan  2011  Developing              59.2            275.0   \n",
      "...           ...   ...         ...               ...              ...   \n",
      "2933     Zimbabwe  2004  Developing              44.3            723.0   \n",
      "2934     Zimbabwe  2003  Developing              44.5            715.0   \n",
      "2935     Zimbabwe  2002  Developing              44.8             73.0   \n",
      "2936     Zimbabwe  2001  Developing              45.3            686.0   \n",
      "2937     Zimbabwe  2000  Developing              46.0            665.0   \n",
      "\n",
      "      infant deaths  Alcohol  percentage expenditure  Hepatitis B  Measles   \\\n",
      "0                62     0.01               71.279624         65.0      1154   \n",
      "1                64     0.01               73.523582         62.0       492   \n",
      "2                66     0.01               73.219243         64.0       430   \n",
      "3                69     0.01               78.184215         67.0      2787   \n",
      "4                71     0.01                7.097109         68.0      3013   \n",
      "...             ...      ...                     ...          ...       ...   \n",
      "2933             27     4.36                0.000000         68.0        31   \n",
      "2934             26     4.06                0.000000          7.0       998   \n",
      "2935             25     4.43                0.000000         73.0       304   \n",
      "2936             25     1.72                0.000000         76.0       529   \n",
      "2937             24     1.68                0.000000         79.0      1483   \n",
      "\n",
      "      ...  Polio  Total expenditure  Diphtheria    HIV/AIDS         GDP  \\\n",
      "0     ...    6.0               8.16         65.0        0.1  584.259210   \n",
      "1     ...   58.0               8.18         62.0        0.1  612.696514   \n",
      "2     ...   62.0               8.13         64.0        0.1  631.744976   \n",
      "3     ...   67.0               8.52         67.0        0.1  669.959000   \n",
      "4     ...   68.0               7.87         68.0        0.1   63.537231   \n",
      "...   ...    ...                ...          ...        ...         ...   \n",
      "2933  ...   67.0               7.13         65.0       33.6  454.366654   \n",
      "2934  ...    7.0               6.52         68.0       36.7  453.351155   \n",
      "2935  ...   73.0               6.53         71.0       39.8   57.348340   \n",
      "2936  ...   76.0               6.16         75.0       42.1  548.587312   \n",
      "2937  ...   78.0               7.10         78.0       43.5  547.358878   \n",
      "\n",
      "      Population   thinness  1-19 years   thinness 5-9 years  \\\n",
      "0     33736494.0                   17.2                 17.3   \n",
      "1       327582.0                   17.5                 17.5   \n",
      "2     31731688.0                   17.7                 17.7   \n",
      "3      3696958.0                   17.9                 18.0   \n",
      "4      2978599.0                   18.2                 18.2   \n",
      "...          ...                    ...                  ...   \n",
      "2933  12777511.0                    9.4                  9.4   \n",
      "2934  12633897.0                    9.8                  9.9   \n",
      "2935    125525.0                    1.2                  1.3   \n",
      "2936  12366165.0                    1.6                  1.7   \n",
      "2937  12222251.0                   11.0                 11.2   \n",
      "\n",
      "      Income composition of resources  Schooling  \n",
      "0                               0.479       10.1  \n",
      "1                               0.476       10.0  \n",
      "2                               0.470        9.9  \n",
      "3                               0.463        9.8  \n",
      "4                               0.454        9.5  \n",
      "...                               ...        ...  \n",
      "2933                            0.407        9.2  \n",
      "2934                            0.418        9.5  \n",
      "2935                            0.427       10.0  \n",
      "2936                            0.427        9.8  \n",
      "2937                            0.434        9.8  \n",
      "\n",
      "[2938 rows x 22 columns]>\n"
     ]
    }
   ],
   "source": [
    "print(df.mean)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "399d678f-2f19-4fec-a520-822da40cc621",
   "metadata": {},
   "source": [
    "# Feature scaling for model input\n",
    "This function scales the features using StandardScaler.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 84,
   "id": "f8c9d5fb-3224-483c-a577-9005618d6a1c",
   "metadata": {},
   "outputs": [],
   "source": [
    "def scale_features(X_train, X_test):\n",
    "    scaler = StandardScaler()\n",
    "    X_train_scaled = scaler.fit_transform(X_train)\n",
    "    X_test_scaled = scaler.transform(X_test)\n",
    "    return X_train_scaled, X_test_scaled, scaler"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ac0b6b54-ea96-4d13-89a9-d507c4e51cec",
   "metadata": {},
   "source": [
    "# Streamlit interface\n",
    "The main function that runs the Streamlit app."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 94,
   "id": "6d8ae8a8-0e06-4d00-8edd-100c075d649a",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Streamlit interface\n",
    "def main():\n",
    "\n",
    "    st.title('WHO Life Expectancy Prediction')\n",
    "\n",
    "    # Load the dataset (change the file path as needed)\n",
    "    df = pd.read_csv(r\"C:\\Users\\Oguntuga\\Downloads\\Life Expectancy Data.csv\")\n",
    "    \n",
    "    st.write(\"Dataset Preview:\")\n",
    "    st.write(df.head())\n",
    "\n",
    "    # Visualize correlation matrix (Only numeric columns)\n",
    "    st.subheader('Correlation Matrix')\n",
    "\n",
    "    # Select only numeric columns for correlation matrix\n",
    "    numeric_cols = df.select_dtypes(include=[np.number])  # Select only numeric columns\n",
    "    corr = numeric_cols.corr()  # Calculate correlation matrix on numeric columns\n",
    "    \n",
    "    fig, ax = plt.subplots(figsize=(10, 8))\n",
    "    sns.heatmap(corr, annot=True, cmap='coolwarm', ax=ax)\n",
    "    st.pyplot(fig)\n",
    "\n",
    "    # Preprocess the data\n",
    "    X, y = preprocess_data(df)\n",
    "    if X is None or y is None:  # Check if preprocessing returned None\n",
    "        return  # Exit the function if preprocessing failed\n",
    "\n",
    "    # Train-Test Split\n",
    "    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)\n",
    "\n",
    "    # Feature Scaling\n",
    "    X_train_scaled, X_test_scaled, scaler = scale_features(X_train, X_test)\n",
    "\n",
    "    # Train model\n",
    "    model = train_model(X_train_scaled, y_train)\n",
    "\n",
    "    # Evaluate model\n",
    "    mse, r2, y_pred = evaluate_model(model, X_test_scaled, y_test)\n",
    "    st.write(f'Mean Squared Error: {mse:.2f}')\n",
    "    st.write(f'R²: {r2:.2f}')\n",
    "\n",
    "    # Plot True vs Predicted Life Expectancy\n",
    "    st.subheader('True vs Predicted Life Expectancy')\n",
    "    fig, ax = plt.subplots()\n",
    "    ax.scatter(y_test, y_pred, color='blue')\n",
    "    ax.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()], color='red', linestyle='--')\n",
    "    ax.set_xlabel('True Life Expectancy')\n",
    "    ax.set_ylabel('Predicted Life Expectancy')\n",
    "    st.pyplot(fig)\n",
    "\n",
    "    # User input for new data prediction\n",
    "    st.sidebar.header(\"Enter health data for prediction\")\n",
    "    \n",
    "    # Sample input fields\n",
    "    health_expenditure = st.sidebar.slider('Health Expenditure', 0, 5000, 100)\n",
    "    mortality_rate = st.sidebar.slider('Mortality Rate', 0.0, 20.0, 5.0)\n",
    "\n",
    "    # Prepare input data for prediction\n",
    "    user_data = np.array([[health_expenditure, mortality_rate]])\n",
    "    user_data_scaled = scaler.transform(user_data)\n",
    "    \n",
    "    # Predict life expectancy\n",
    "    predicted_life_expectancy = model.predict(user_data_scaled)\n",
    "    st.write(f'Predicted Life Expectancy: {predicted_life_expectancy[0]:.2f}')\n",
    "\n",
    "# Run the Streamlit app\n",
    "if __name__ == '__main__':\n",
    "    main()\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": None,
   "id": "3af4fb84-8389-41c4-9330-e310f6cea062",
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
   "version": "3.12.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
