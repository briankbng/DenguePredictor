# Imports all the necessary 3rd parties packages

# External package imports.
# =============================================================================
import os
import time
import datetime
import logging

import pandas as pd
from bokeh.embed import components

from flask import Flask, render_template, request, jsonify, flash, redirect, url_for
from flask_bootstrap import Bootstrap
from flask_wtf import Form

logging.basicConfig(level=logging.INFO)

# Internal package imports.
# =============================================================================
# Imports the Data paths.
from definitions import MODEL_DT_REGRESSOR, MODEL_LT_GBM_MAY, MODEL_PKL, FORECAST_WEATHER_CSV, ACTUAL_DATA_CSV
# Imports the functions/class for Predictions and Visualization
from models.predict_model import CaseReasoner
from visualization.generate_graph import GenerateGraph

# FLASK application setup
# =============================================================================
app = Flask(__name__)
app.secret_key = 'SHH!'
Bootstrap(app)

# Main Body
# =============================================================================

# Utilities
def createDengueCasesPlot(From='2020-01-01', to='2020-05-01'):
    
        predict_cases = list()

        # Converts date string to python datetime.
        startDate = datetime.datetime.strptime(From, '%Y-%m-%d')
        endDate = datetime.datetime.strptime(to, '%Y-%m-%d')

        next_day = startDate
        # Iterate from start date to end date and predict the dengue cases
        # base on the known forecast weather data.
        # Note: Should the prediction use the weather forecast data of 1 week ago?
        while True:
            if next_day > endDate:
                break

            dateStr = next_day.strftime("%Y-%m-%d")

            predict_case = dict()
            value = []

            if dateStr in FORECAST_WEATHER.keys():
                value = FORECAST_WEATHER[dateStr]

                weatherInfo = [ value[0], value[1], value[2], value[3], value[4], value[5],
                                value[6], value[7], value[8], value[9], value[10], value[11],
                                value[12], value[13], value[14], value[15], value[16], value[17],
                                value[18], value[19], value[20], value[21], value[22], value[23],
                                value[24], value[25], value[26], value[27], value[28], value[29],
                                value[30], value[31], value[32], value[33], value[34], value[35],
                                value[36], value[37], value[38], value[39], value[40], value[41],
                                value[42], value[43], value[44], value[45], value[46], value[47],
                                value[48], value[49], value[50], value[51], value[52], value[53],
                                value[54]
                            ]

                num_cases = int(reasoner.predict(weatherInfo))

                predict_case['date'] = dateStr
                predict_case['cases'] = num_cases

                predict_cases.append(predict_case)

            next_day += datetime.timedelta(days=1)       

        # Converts the predicted cases from Dict to Pandas dataframe
        predict_cases_df = pd.DataFrame.from_dict(predict_cases)
         
        # To show longer date ranges, it is best to hide weather conditions
        p = plotGraph.generateGraphForActualAndPredictedDengueCases(
                From,               # startDate YYYY-MM-DD
                to,                 # endDate YYYY-MM-DD
                predict_cases_df,   # List of Predicted Cases
                bool(True))         # Hide weather conditions

        script, div =  components(p) 
        return script, div, predict_cases



def getForeCastedWeather():

   # Define the path to the forecasted weather data.
    forecastWeatherDataCsv = FORECAST_WEATHER_CSV

    # Read from forecast weather data (csv format) as Pandas DataFrame object
    df = pd.read_csv(forecastWeatherDataCsv, header=0, parse_dates=['date'])

    # Converts the data frame to list
    weather = df.values.tolist()
    # print(df)
    # print(weather)
    # Creates a dictionary
    dayWeatherInfo = dict()

    # Iterates through the list of forecasted weather data and store it in dictionary.
    # date is the key and the weather data as list of values
    for timeStamp,mean_temp,max_temp,min_temp,humidity,mean_rain_fall,mean_wind,\
        MA5_mean_temp,MA5_max_temp,MA5_min_temp,MA5_humidity,MA5_mean_rain_fall,\
        MA5_mean_wind,MA10_mean_temp,MA10_max_temp,MA10_min_temp,MA10_humidity,\
        MA10_mean_rain_fall,MA10_mean_wind,MA15_mean_temp,MA15_max_temp,MA15_min_temp,\
        MA15_humidity,MA15_mean_rain_fall,MA15_mean_wind,MA20_mean_temp,MA20_max_temp,\
        MA20_min_temp,MA20_humidity,MA20_mean_rain_fall,MA20_mean_wind,LA5_mean_temp,\
        LA5_max_temp,LA5_min_temp,LA5_humidity,LA5_mean_rain_fall,LA5_mean_wind,\
        LA8_mean_temp,LA8_max_temp,LA8_min_temp,LA8_humidity,LA8_mean_rain_fall,\
        LA8_mean_wind,LA12_mean_temp,LA12_max_temp,LA12_min_temp,LA12_humidity,\
        LA12_mean_rain_fall,LA12_mean_wind,LA15_mean_temp,LA15_max_temp,LA15_min_temp,\
        LA15_humidity,LA15_mean_rain_fall,LA15_mean_wind,ln_cases in weather:
        
        # Converts from pandas timestamp to python datetime
        dateTimeObj = timeStamp.to_pydatetime()
        # Converts to date string
        dateStr = dateTimeObj.strftime("%Y-%m-%d")
        
        # Stores the weather data into the dictionary
        dayWeatherInfo[dateStr] = [mean_temp,max_temp,min_temp,humidity,mean_rain_fall,\
                                    mean_wind,MA5_mean_temp,MA5_max_temp,MA5_min_temp,\
                                    MA5_humidity,MA5_mean_rain_fall,MA5_mean_wind,MA10_mean_temp,\
                                    MA10_max_temp,MA10_min_temp,MA10_humidity,MA10_mean_rain_fall,\
                                    MA10_mean_wind,MA15_mean_temp,MA15_max_temp,MA15_min_temp,MA15_humidity,\
                                    MA15_mean_rain_fall,MA15_mean_wind,MA20_mean_temp,MA20_max_temp,\
                                    MA20_min_temp,MA20_humidity,MA20_mean_rain_fall,MA20_mean_wind,\
                                    LA5_mean_temp,LA5_max_temp,LA5_min_temp,LA5_humidity,LA5_mean_rain_fall,\
                                    LA5_mean_wind,LA8_mean_temp,LA8_max_temp,LA8_min_temp,LA8_humidity,\
                                    LA8_mean_rain_fall,LA8_mean_wind,LA12_mean_temp,LA12_max_temp,LA12_min_temp,\
                                    LA12_humidity,LA12_mean_rain_fall,LA12_mean_wind,LA15_mean_temp,LA15_max_temp,\
                                    LA15_min_temp,LA15_humidity,LA15_mean_rain_fall,LA15_mean_wind,ln_cases]

    return dayWeatherInfo


# FLASK web routes.

@app.after_request
def add_headers(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = "Content-Type, Access-Control-Allow-Headers, Authorization, X-Requested-With"
    response.headers['Access-Control-Allow-Methods']=  "POST, GET, PUT, DELETE, OPTIONS"
    return response

@app.route('/')
def index():

    # script, div, predict_cases = createDengueCasesPlot()

    # forecastWeatherData = []
    # dayWeatherData = dict()

    # for key, value in FORECAST_WEATHER.items():
    #     dayWeatherData['date'] = key
    #     dayWeatherData['mean_temp'] = value[0]
    #     dayWeatherData['max_temp'] = value[1]
    #     dayWeatherData['min_temp'] = value[2]
    #     dayWeatherData['humidity'] = value[3]
    #     dayWeatherData['mean_rain_fall'] = value[4]
    #     dayWeatherData['mean_wind'] = value[5]
    #     forecastWeatherData.append(dayWeatherData)

    return render_template('index.html')

@app.route("/range",methods=["POST","GET"])
def range(): 
 
    # predict_cases = list()

    print(request.method)

    if request.method == 'POST':
        From = request.form['From']
        to = request.form['to']
        print(From)
        print(to)

        script, div, predict_cases = createDengueCasesPlot(From=From, to=to)

        return jsonify({'htmlresponse': render_template('response.html', predict_cases=predict_cases, the_div=div, the_script=script)})
 
if __name__ == "__main__":
   
    # Set the prediction model to use.
    predict_model = MODEL_LT_GBM_MAY
    
    # Get the forecasted weather data.
    FORECAST_WEATHER = getForeCastedWeather()

    # Creates the dengue case resoner object and assign the predict model to it.
    reasoner = CaseReasoner(predict_model)

    # Creates the GenerateGraph object and assign the actual data csv to it.
    plotGraph = GenerateGraph(ACTUAL_DATA_CSV)

    # Start the FLASK application
    app.run(debug=False, host='0.0.0.0', port=8888)

