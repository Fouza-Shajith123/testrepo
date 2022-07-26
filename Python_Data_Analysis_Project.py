{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import matplotlib.pyplot as plt\n",
    "import numpy as np\n",
    "import seaborn as sns\n",
    "from sklearn.pipeline import Pipeline\n",
    "from sklearn.preprocessing import StandardScaler,PolynomialFeatures\n",
    "from sklearn.linear_model import LinearRegression\n",
    "%matplotlib inline"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [],
   "source": [
    "file_name='https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-SkillsNetwork/labs/FinalModule_Coursera/data/kc_house_data_NaN.csv'\n",
    "df=pd.read_csv(file_name)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Question 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "Unnamed: 0         int64\nid                 int64\ndate              object\nprice            float64\nbedrooms         float64\nbathrooms        float64\nsqft_living        int64\nsqft_lot           int64\nfloors           float64\nwaterfront         int64\nview               int64\ncondition          int64\ngrade              int64\nsqft_above         int64\nsqft_basement      int64\nyr_built           int64\nyr_renovated       int64\nzipcode            int64\nlat              float64\nlong             float64\nsqft_living15      int64\nsqft_lot15         int64\ndtype: object"
      ]
     },
     "execution_count": 6,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.dtypes"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n<style scoped>\n    .dataframe tbody tr th:only-of-type {\n        vertical-align: middle;\n    }\n\n    .dataframe tbody tr th {\n        vertical-align: top;\n    }\n\n    .dataframe thead th {\n        text-align: right;\n    }\n</style>\n<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th></th>\n      <th>Unnamed: 0</th>\n      <th>id</th>\n      <th>price</th>\n      <th>bedrooms</th>\n      <th>bathrooms</th>\n      <th>sqft_living</th>\n      <th>sqft_lot</th>\n      <th>floors</th>\n      <th>waterfront</th>\n      <th>view</th>\n      <th>...</th>\n      <th>grade</th>\n      <th>sqft_above</th>\n      <th>sqft_basement</th>\n      <th>yr_built</th>\n      <th>yr_renovated</th>\n      <th>zipcode</th>\n      <th>lat</th>\n      <th>long</th>\n      <th>sqft_living15</th>\n      <th>sqft_lot15</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>count</th>\n      <td>21613.00000</td>\n      <td>2.161300e+04</td>\n      <td>2.161300e+04</td>\n      <td>21600.000000</td>\n      <td>21603.000000</td>\n      <td>21613.000000</td>\n      <td>2.161300e+04</td>\n      <td>21613.000000</td>\n      <td>21613.000000</td>\n      <td>21613.000000</td>\n      <td>...</td>\n      <td>21613.000000</td>\n      <td>21613.000000</td>\n      <td>21613.000000</td>\n      <td>21613.000000</td>\n      <td>21613.000000</td>\n      <td>21613.000000</td>\n      <td>21613.000000</td>\n      <td>21613.000000</td>\n      <td>21613.000000</td>\n      <td>21613.000000</td>\n    </tr>\n    <tr>\n      <th>mean</th>\n      <td>10806.00000</td>\n      <td>4.580302e+09</td>\n      <td>5.400881e+05</td>\n      <td>3.372870</td>\n      <td>2.115736</td>\n      <td>2079.899736</td>\n      <td>1.510697e+04</td>\n      <td>1.494309</td>\n      <td>0.007542</td>\n      <td>0.234303</td>\n      <td>...</td>\n      <td>7.656873</td>\n      <td>1788.390691</td>\n      <td>291.509045</td>\n      <td>1971.005136</td>\n      <td>84.402258</td>\n      <td>98077.939805</td>\n      <td>47.560053</td>\n      <td>-122.213896</td>\n      <td>1986.552492</td>\n      <td>12768.455652</td>\n    </tr>\n    <tr>\n      <th>std</th>\n      <td>6239.28002</td>\n      <td>2.876566e+09</td>\n      <td>3.671272e+05</td>\n      <td>0.926657</td>\n      <td>0.768996</td>\n      <td>918.440897</td>\n      <td>4.142051e+04</td>\n      <td>0.539989</td>\n      <td>0.086517</td>\n      <td>0.766318</td>\n      <td>...</td>\n      <td>1.175459</td>\n      <td>828.090978</td>\n      <td>442.575043</td>\n      <td>29.373411</td>\n      <td>401.679240</td>\n      <td>53.505026</td>\n      <td>0.138564</td>\n      <td>0.140828</td>\n      <td>685.391304</td>\n      <td>27304.179631</td>\n    </tr>\n    <tr>\n      <th>min</th>\n      <td>0.00000</td>\n      <td>1.000102e+06</td>\n      <td>7.500000e+04</td>\n      <td>1.000000</td>\n      <td>0.500000</td>\n      <td>290.000000</td>\n      <td>5.200000e+02</td>\n      <td>1.000000</td>\n      <td>0.000000</td>\n      <td>0.000000</td>\n      <td>...</td>\n      <td>1.000000</td>\n      <td>290.000000</td>\n      <td>0.000000</td>\n      <td>1900.000000</td>\n      <td>0.000000</td>\n      <td>98001.000000</td>\n      <td>47.155900</td>\n      <td>-122.519000</td>\n      <td>399.000000</td>\n      <td>651.000000</td>\n    </tr>\n    <tr>\n      <th>25%</th>\n      <td>5403.00000</td>\n      <td>2.123049e+09</td>\n      <td>3.219500e+05</td>\n      <td>3.000000</td>\n      <td>1.750000</td>\n      <td>1427.000000</td>\n      <td>5.040000e+03</td>\n      <td>1.000000</td>\n      <td>0.000000</td>\n      <td>0.000000</td>\n      <td>...</td>\n      <td>7.000000</td>\n      <td>1190.000000</td>\n      <td>0.000000</td>\n      <td>1951.000000</td>\n      <td>0.000000</td>\n      <td>98033.000000</td>\n      <td>47.471000</td>\n      <td>-122.328000</td>\n      <td>1490.000000</td>\n      <td>5100.000000</td>\n    </tr>\n    <tr>\n      <th>50%</th>\n      <td>10806.00000</td>\n      <td>3.904930e+09</td>\n      <td>4.500000e+05</td>\n      <td>3.000000</td>\n      <td>2.250000</td>\n      <td>1910.000000</td>\n      <td>7.618000e+03</td>\n      <td>1.500000</td>\n      <td>0.000000</td>\n      <td>0.000000</td>\n      <td>...</td>\n      <td>7.000000</td>\n      <td>1560.000000</td>\n      <td>0.000000</td>\n      <td>1975.000000</td>\n      <td>0.000000</td>\n      <td>98065.000000</td>\n      <td>47.571800</td>\n      <td>-122.230000</td>\n      <td>1840.000000</td>\n      <td>7620.000000</td>\n    </tr>\n    <tr>\n      <th>75%</th>\n      <td>16209.00000</td>\n      <td>7.308900e+09</td>\n      <td>6.450000e+05</td>\n      <td>4.000000</td>\n      <td>2.500000</td>\n      <td>2550.000000</td>\n      <td>1.068800e+04</td>\n      <td>2.000000</td>\n      <td>0.000000</td>\n      <td>0.000000</td>\n      <td>...</td>\n      <td>8.000000</td>\n      <td>2210.000000</td>\n      <td>560.000000</td>\n      <td>1997.000000</td>\n      <td>0.000000</td>\n      <td>98118.000000</td>\n      <td>47.678000</td>\n      <td>-122.125000</td>\n      <td>2360.000000</td>\n      <td>10083.000000</td>\n    </tr>\n    <tr>\n      <th>max</th>\n      <td>21612.00000</td>\n      <td>9.900000e+09</td>\n      <td>7.700000e+06</td>\n      <td>33.000000</td>\n      <td>8.000000</td>\n      <td>13540.000000</td>\n      <td>1.651359e+06</td>\n      <td>3.500000</td>\n      <td>1.000000</td>\n      <td>4.000000</td>\n      <td>...</td>\n      <td>13.000000</td>\n      <td>9410.000000</td>\n      <td>4820.000000</td>\n      <td>2015.000000</td>\n      <td>2015.000000</td>\n      <td>98199.000000</td>\n      <td>47.777600</td>\n      <td>-121.315000</td>\n      <td>6210.000000</td>\n      <td>871200.000000</td>\n    </tr>\n  </tbody>\n</table>\n<p>8 rows × 21 columns</p>\n</div>"
      ],
      "text/plain": [
       "        Unnamed: 0            id         price      bedrooms     bathrooms  \\\ncount  21613.00000  2.161300e+04  2.161300e+04  21600.000000  21603.000000   \nmean   10806.00000  4.580302e+09  5.400881e+05      3.372870      2.115736   \nstd     6239.28002  2.876566e+09  3.671272e+05      0.926657      0.768996   \nmin        0.00000  1.000102e+06  7.500000e+04      1.000000      0.500000   \n25%     5403.00000  2.123049e+09  3.219500e+05      3.000000      1.750000   \n50%    10806.00000  3.904930e+09  4.500000e+05      3.000000      2.250000   \n75%    16209.00000  7.308900e+09  6.450000e+05      4.000000      2.500000   \nmax    21612.00000  9.900000e+09  7.700000e+06     33.000000      8.000000   \n\n        sqft_living      sqft_lot        floors    waterfront          view  \\\ncount  21613.000000  2.161300e+04  21613.000000  21613.000000  21613.000000   \nmean    2079.899736  1.510697e+04      1.494309      0.007542      0.234303   \nstd      918.440897  4.142051e+04      0.539989      0.086517      0.766318   \nmin      290.000000  5.200000e+02      1.000000      0.000000      0.000000   \n25%     1427.000000  5.040000e+03      1.000000      0.000000      0.000000   \n50%     1910.000000  7.618000e+03      1.500000      0.000000      0.000000   \n75%     2550.000000  1.068800e+04      2.000000      0.000000      0.000000   \nmax    13540.000000  1.651359e+06      3.500000      1.000000      4.000000   \n\n       ...         grade    sqft_above  sqft_basement      yr_built  \\\ncount  ...  21613.000000  21613.000000   21613.000000  21613.000000   \nmean   ...      7.656873   1788.390691     291.509045   1971.005136   \nstd    ...      1.175459    828.090978     442.575043     29.373411   \nmin    ...      1.000000    290.000000       0.000000   1900.000000   \n25%    ...      7.000000   1190.000000       0.000000   1951.000000   \n50%    ...      7.000000   1560.000000       0.000000   1975.000000   \n75%    ...      8.000000   2210.000000     560.000000   1997.000000   \nmax    ...     13.000000   9410.000000    4820.000000   2015.000000   \n\n       yr_renovated       zipcode           lat          long  sqft_living15  \\\ncount  21613.000000  21613.000000  21613.000000  21613.000000   21613.000000   \nmean      84.402258  98077.939805     47.560053   -122.213896    1986.552492   \nstd      401.679240     53.505026      0.138564      0.140828     685.391304   \nmin        0.000000  98001.000000     47.155900   -122.519000     399.000000   \n25%        0.000000  98033.000000     47.471000   -122.328000    1490.000000   \n50%        0.000000  98065.000000     47.571800   -122.230000    1840.000000   \n75%        0.000000  98118.000000     47.678000   -122.125000    2360.000000   \nmax     2015.000000  98199.000000     47.777600   -121.315000    6210.000000   \n\n          sqft_lot15  \ncount   21613.000000  \nmean    12768.455652  \nstd     27304.179631  \nmin       651.000000  \n25%      5100.000000  \n50%      7620.000000  \n75%     10083.000000  \nmax    871200.000000  \n\n[8 rows x 21 columns]"
      ]
     },
     "execution_count": 7,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.describe()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Question 2"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n<style scoped>\n    .dataframe tbody tr th:only-of-type {\n        vertical-align: middle;\n    }\n\n    .dataframe tbody tr th {\n        vertical-align: top;\n    }\n\n    .dataframe thead th {\n        text-align: right;\n    }\n</style>\n<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th></th>\n      <th>price</th>\n      <th>bedrooms</th>\n      <th>bathrooms</th>\n      <th>sqft_living</th>\n      <th>sqft_lot</th>\n      <th>floors</th>\n      <th>waterfront</th>\n      <th>view</th>\n      <th>condition</th>\n      <th>grade</th>\n      <th>sqft_above</th>\n      <th>sqft_basement</th>\n      <th>yr_built</th>\n      <th>yr_renovated</th>\n      <th>zipcode</th>\n      <th>lat</th>\n      <th>long</th>\n      <th>sqft_living15</th>\n      <th>sqft_lot15</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>count</th>\n      <td>2.161300e+04</td>\n      <td>21600.000000</td>\n      <td>21603.000000</td>\n      <td>21613.000000</td>\n      <td>2.161300e+04</td>\n      <td>21613.000000</td>\n      <td>21613.000000</td>\n      <td>21613.000000</td>\n      <td>21613.000000</td>\n      <td>21613.000000</td>\n      <td>21613.000000</td>\n      <td>21613.000000</td>\n      <td>21613.000000</td>\n      <td>21613.000000</td>\n      <td>21613.000000</td>\n      <td>21613.000000</td>\n      <td>21613.000000</td>\n      <td>21613.000000</td>\n      <td>21613.000000</td>\n    </tr>\n    <tr>\n      <th>mean</th>\n      <td>5.400881e+05</td>\n      <td>3.372870</td>\n      <td>2.115736</td>\n      <td>2079.899736</td>\n      <td>1.510697e+04</td>\n      <td>1.494309</td>\n      <td>0.007542</td>\n      <td>0.234303</td>\n      <td>3.409430</td>\n      <td>7.656873</td>\n      <td>1788.390691</td>\n      <td>291.509045</td>\n      <td>1971.005136</td>\n      <td>84.402258</td>\n      <td>98077.939805</td>\n      <td>47.560053</td>\n      <td>-122.213896</td>\n      <td>1986.552492</td>\n      <td>12768.455652</td>\n    </tr>\n    <tr>\n      <th>std</th>\n      <td>3.671272e+05</td>\n      <td>0.926657</td>\n      <td>0.768996</td>\n      <td>918.440897</td>\n      <td>4.142051e+04</td>\n      <td>0.539989</td>\n      <td>0.086517</td>\n      <td>0.766318</td>\n      <td>0.650743</td>\n      <td>1.175459</td>\n      <td>828.090978</td>\n      <td>442.575043</td>\n      <td>29.373411</td>\n      <td>401.679240</td>\n      <td>53.505026</td>\n      <td>0.138564</td>\n      <td>0.140828</td>\n      <td>685.391304</td>\n      <td>27304.179631</td>\n    </tr>\n    <tr>\n      <th>min</th>\n      <td>7.500000e+04</td>\n      <td>1.000000</td>\n      <td>0.500000</td>\n      <td>290.000000</td>\n      <td>5.200000e+02</td>\n      <td>1.000000</td>\n      <td>0.000000</td>\n      <td>0.000000</td>\n      <td>1.000000</td>\n      <td>1.000000</td>\n      <td>290.000000</td>\n      <td>0.000000</td>\n      <td>1900.000000</td>\n      <td>0.000000</td>\n      <td>98001.000000</td>\n      <td>47.155900</td>\n      <td>-122.519000</td>\n      <td>399.000000</td>\n      <td>651.000000</td>\n    </tr>\n    <tr>\n      <th>25%</th>\n      <td>3.219500e+05</td>\n      <td>3.000000</td>\n      <td>1.750000</td>\n      <td>1427.000000</td>\n      <td>5.040000e+03</td>\n      <td>1.000000</td>\n      <td>0.000000</td>\n      <td>0.000000</td>\n      <td>3.000000</td>\n      <td>7.000000</td>\n      <td>1190.000000</td>\n      <td>0.000000</td>\n      <td>1951.000000</td>\n      <td>0.000000</td>\n      <td>98033.000000</td>\n      <td>47.471000</td>\n      <td>-122.328000</td>\n      <td>1490.000000</td>\n      <td>5100.000000</td>\n    </tr>\n    <tr>\n      <th>50%</th>\n      <td>4.500000e+05</td>\n      <td>3.000000</td>\n      <td>2.250000</td>\n      <td>1910.000000</td>\n      <td>7.618000e+03</td>\n      <td>1.500000</td>\n      <td>0.000000</td>\n      <td>0.000000</td>\n      <td>3.000000</td>\n      <td>7.000000</td>\n      <td>1560.000000</td>\n      <td>0.000000</td>\n      <td>1975.000000</td>\n      <td>0.000000</td>\n      <td>98065.000000</td>\n      <td>47.571800</td>\n      <td>-122.230000</td>\n      <td>1840.000000</td>\n      <td>7620.000000</td>\n    </tr>\n    <tr>\n      <th>75%</th>\n      <td>6.450000e+05</td>\n      <td>4.000000</td>\n      <td>2.500000</td>\n      <td>2550.000000</td>\n      <td>1.068800e+04</td>\n      <td>2.000000</td>\n      <td>0.000000</td>\n      <td>0.000000</td>\n      <td>4.000000</td>\n      <td>8.000000</td>\n      <td>2210.000000</td>\n      <td>560.000000</td>\n      <td>1997.000000</td>\n      <td>0.000000</td>\n      <td>98118.000000</td>\n      <td>47.678000</td>\n      <td>-122.125000</td>\n      <td>2360.000000</td>\n      <td>10083.000000</td>\n    </tr>\n    <tr>\n      <th>max</th>\n      <td>7.700000e+06</td>\n      <td>33.000000</td>\n      <td>8.000000</td>\n      <td>13540.000000</td>\n      <td>1.651359e+06</td>\n      <td>3.500000</td>\n      <td>1.000000</td>\n      <td>4.000000</td>\n      <td>5.000000</td>\n      <td>13.000000</td>\n      <td>9410.000000</td>\n      <td>4820.000000</td>\n      <td>2015.000000</td>\n      <td>2015.000000</td>\n      <td>98199.000000</td>\n      <td>47.777600</td>\n      <td>-121.315000</td>\n      <td>6210.000000</td>\n      <td>871200.000000</td>\n    </tr>\n  </tbody>\n</table>\n</div>"
      ],
      "text/plain": [
       "              price      bedrooms     bathrooms   sqft_living      sqft_lot  \\\ncount  2.161300e+04  21600.000000  21603.000000  21613.000000  2.161300e+04   \nmean   5.400881e+05      3.372870      2.115736   2079.899736  1.510697e+04   \nstd    3.671272e+05      0.926657      0.768996    918.440897  4.142051e+04   \nmin    7.500000e+04      1.000000      0.500000    290.000000  5.200000e+02   \n25%    3.219500e+05      3.000000      1.750000   1427.000000  5.040000e+03   \n50%    4.500000e+05      3.000000      2.250000   1910.000000  7.618000e+03   \n75%    6.450000e+05      4.000000      2.500000   2550.000000  1.068800e+04   \nmax    7.700000e+06     33.000000      8.000000  13540.000000  1.651359e+06   \n\n             floors    waterfront          view     condition         grade  \\\ncount  21613.000000  21613.000000  21613.000000  21613.000000  21613.000000   \nmean       1.494309      0.007542      0.234303      3.409430      7.656873   \nstd        0.539989      0.086517      0.766318      0.650743      1.175459   \nmin        1.000000      0.000000      0.000000      1.000000      1.000000   \n25%        1.000000      0.000000      0.000000      3.000000      7.000000   \n50%        1.500000      0.000000      0.000000      3.000000      7.000000   \n75%        2.000000      0.000000      0.000000      4.000000      8.000000   \nmax        3.500000      1.000000      4.000000      5.000000     13.000000   \n\n         sqft_above  sqft_basement      yr_built  yr_renovated       zipcode  \\\ncount  21613.000000   21613.000000  21613.000000  21613.000000  21613.000000   \nmean    1788.390691     291.509045   1971.005136     84.402258  98077.939805   \nstd      828.090978     442.575043     29.373411    401.679240     53.505026   \nmin      290.000000       0.000000   1900.000000      0.000000  98001.000000   \n25%     1190.000000       0.000000   1951.000000      0.000000  98033.000000   \n50%     1560.000000       0.000000   1975.000000      0.000000  98065.000000   \n75%     2210.000000     560.000000   1997.000000      0.000000  98118.000000   \nmax     9410.000000    4820.000000   2015.000000   2015.000000  98199.000000   \n\n                lat          long  sqft_living15     sqft_lot15  \ncount  21613.000000  21613.000000   21613.000000   21613.000000  \nmean      47.560053   -122.213896    1986.552492   12768.455652  \nstd        0.138564      0.140828     685.391304   27304.179631  \nmin       47.155900   -122.519000     399.000000     651.000000  \n25%       47.471000   -122.328000    1490.000000    5100.000000  \n50%       47.571800   -122.230000    1840.000000    7620.000000  \n75%       47.678000   -122.125000    2360.000000   10083.000000  \nmax       47.777600   -121.315000    6210.000000  871200.000000  "
      ]
     },
     "execution_count": 8,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.drop([\"id\",\"Unnamed: 0\"] , axis = 1, inplace = True)\n",
    "df.describe()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "number of NaN values for the column bedrooms : 13\nnumber of NaN values for the column bathrooms : 10\n"
     ]
    }
   ],
   "source": [
    "print(\"number of NaN values for the column bedrooms :\", df['bedrooms'].isnull().sum())\n",
    "print(\"number of NaN values for the column bathrooms :\", df['bathrooms'].isnull().sum())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "number of NaN values for the column bedrooms : 0\nnumber of NaN values for the column bathrooms : 0\n"
     ]
    }
   ],
   "source": [
    "mean=df['bedrooms'].mean()\n",
    "df['bedrooms'].replace(np.nan,mean, inplace=True)\n",
    "mean=df['bathrooms'].mean()\n",
    "df['bathrooms'].replace(np.nan,mean, inplace=True)\n",
    "print(\"number of NaN values for the column bedrooms :\", df['bedrooms'].isnull().sum())\n",
    "print(\"number of NaN values for the column bathrooms :\", df['bathrooms'].isnull().sum())"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Question 3"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 11,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n<style scoped>\n    .dataframe tbody tr th:only-of-type {\n        vertical-align: middle;\n    }\n\n    .dataframe tbody tr th {\n        vertical-align: top;\n    }\n\n    .dataframe thead th {\n        text-align: right;\n    }\n</style>\n<table border=\"1\" class=\"dataframe\">\n  <thead>\n    <tr style=\"text-align: right;\">\n      <th></th>\n      <th>floors</th>\n    </tr>\n  </thead>\n  <tbody>\n    <tr>\n      <th>1.0</th>\n      <td>10680</td>\n    </tr>\n    <tr>\n      <th>2.0</th>\n      <td>8241</td>\n    </tr>\n    <tr>\n      <th>1.5</th>\n      <td>1910</td>\n    </tr>\n    <tr>\n      <th>3.0</th>\n      <td>613</td>\n    </tr>\n    <tr>\n      <th>2.5</th>\n      <td>161</td>\n    </tr>\n    <tr>\n      <th>3.5</th>\n      <td>8</td>\n    </tr>\n  </tbody>\n</table>\n</div>"
      ],
      "text/plain": [
       "     floors\n1.0   10680\n2.0    8241\n1.5    1910\n3.0     613\n2.5     161\n3.5       8"
      ]
     },
     "execution_count": 11,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df['floors'].value_counts().to_frame()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Question 4"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 12,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='waterfront', ylabel='price'>"
      ]
     },
     "execution_count": 12,
     "metadata": {},
     "output_type": "execute_result"
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
    "sns.boxplot(x=\"waterfront\", y=\"price\", data=df)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Question 5"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 13,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "<AxesSubplot:xlabel='sqft_above', ylabel='price'>"
      ]
     },
     "execution_count": 13,
     "metadata": {},
     "output_type": "execute_result"
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
    "sns.regplot(x=\"sqft_above\", y=\"price\", data=df, ci = None)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "zipcode         -0.053203\nlong             0.021626\ncondition        0.036362\nyr_built         0.054012\nsqft_lot15       0.082447\nsqft_lot         0.089661\nyr_renovated     0.126434\nfloors           0.256794\nwaterfront       0.266369\nlat              0.307003\nbedrooms         0.308797\nsqft_basement    0.323816\nview             0.397293\nbathrooms        0.525738\nsqft_living15    0.585379\nsqft_above       0.605567\ngrade            0.667434\nsqft_living      0.702035\nprice            1.000000\nName: price, dtype: float64"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "df.corr()['price'].sort_values()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 15,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.00046769430149007363"
      ]
     },
     "execution_count": 15,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X = df[['long']]\n",
    "Y = df['price']\n",
    "lm = LinearRegression()\n",
    "lm.fit(X,Y)\n",
    "lm.score(X, Y)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Question 6"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 17,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.4928532179037931"
      ]
     },
     "execution_count": 17,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "lm = LinearRegression()\n",
    "lm\n",
    "\n",
    "X = df[['sqft_living']]\n",
    "Y = df['price']\n",
    "\n",
    "lm.fit(X,Y)\n",
    "\n",
    "lm.score(X,Y)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Question 7"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [],
   "source": [
    "features =[\"floors\", \"waterfront\",\"lat\" ,\"bedrooms\" ,\"sqft_basement\" ,\"view\" ,\"bathrooms\",\"sqft_living15\",\"sqft_above\",\"grade\",\"sqft_living\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 19,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.6576722447699446"
      ]
     },
     "execution_count": 19,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "X2 = df[features]\n",
    "Y2 = df['price']\n",
    "lm.fit(X2,Y2)\n",
    "lm.score(X2,Y2)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 20,
   "metadata": {},
   "outputs": [],
   "source": [
    "Input=[('scale',StandardScaler()),('polynomial', PolynomialFeatures(include_bias=False)),('model',LinearRegression())]"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Question 8"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 21,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.5327430940591443"
      ]
     },
     "execution_count": 21,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pipe=Pipeline(Input)\n",
    "pipe\n",
    "pipe.fit(X,Y)\n",
    "pipe.score(X,Y)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 22,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "done\n"
     ]
    }
   ],
   "source": [
    "from sklearn.model_selection import cross_val_score\n",
    "from sklearn.model_selection import train_test_split\n",
    "print(\"done\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 23,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "number of test samples: 3242\nnumber of training samples: 18371\n"
     ]
    }
   ],
   "source": [
    "features =[\"floors\", \"waterfront\",\"lat\" ,\"bedrooms\" ,\"sqft_basement\" ,\"view\" ,\"bathrooms\",\"sqft_living15\",\"sqft_above\",\"grade\",\"sqft_living\"]    \n",
    "X = df[features]\n",
    "Y = df['price']\n",
    "\n",
    "x_train, x_test, y_train, y_test = train_test_split(X, Y, test_size=0.15, random_state=1)\n",
    "\n",
    "\n",
    "print(\"number of test samples:\", x_test.shape[0])\n",
    "print(\"number of training samples:\",x_train.shape[0])"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Question 9"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [],
   "source": [
    "from sklearn.linear_model import Ridge"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.6478759163939112"
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "RigeModel = Ridge(alpha=0.1) \n",
    "RigeModel.fit(x_train, y_train)\n",
    "RigeModel.score(x_test, y_test)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "#### Question 1"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "0.700274426790608"
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "pr=PolynomialFeatures(degree=2)\n",
    "x_train_pr=pr.fit_transform(x_train[features])\n",
    "x_test_pr=pr.fit_transform(x_test[features])\n",
    "\n",
    "RigeModel = Ridge(alpha=0.1) \n",
    "RigeModel.fit(x_train_pr, y_train)\n",
    "RigeModel.score(x_test_pr, y_test)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    ""
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "name": "python3",
   "display_name": "Python 3.9",
   "language": "python"
  },
  "language_info": {
   "name": "python",
   "version": "3.9.12",
   "mimetype": "text/x-python",
   "codemirror_mode": {
    "name": "ipython",
    "version": 3.0
   },
   "pygments_lexer": "ipython3",
   "nbconvert_exporter": "python",
   "file_extension": ".py"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 0
}