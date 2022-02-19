# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

# 1. IMPORT DATASET
# Please follow this procedure:
# Import dataset (using the code or from File -> Import dataset -> From Excel)
# 1.a. Remember to turn your data into numeric and that
# the time column is titled "Time" and the data column is titled "Country".
# 1.b. Also, make sure your file is named Country

# 2. Turn data frame in matrix

# Now plot!


# 3. Check for stationarity Is this stationary?
# 3.a. Check ACF and PACF


# 3.b. ANY comments??? Do the ACF and PACF show that the series is stationary or not?

# 3.c. Use the Dickey-Fuller stationarity test
# where the null hypothesis (Ho) is that the series has a unit root (i.e. no stationarity)
# 3.c.1. Load package fUnitRoots from "Tools-Install packages"

# 3.c.2. Perform the adfTest

# 3.c.3. Check P Value.
# Can you reject the null hypothesis? Does the series have a unit root?

# 4. Is the series stationary? If not, then make it stationary!!!
# But how? Create first or second differences of the series
# The procedure is standard now: Create series, check ACF and PACF and ADF test
# 4.a. First differences



# 4.b. Second differences


# 5. BOX-JENKINS PROCEDURE: IDENTIFY, ESTIMATE, CHECK AND FORECAST
# Check ACF and PACF for the rank of AR or MA model
# Estimate the model in mind
# Estimate other models and compare

# INSTALL PACKAGES FOR AUTO.ARIMA


# Suppose you have in mind an AR(1) model

# Suppose you have in mind an AR(2) model

# Suppose you have in mind an ARMA(1,1) model


# Have in mind of what ACF, PACF and ADF showed.
# If the series is not stationary we need to estimate ARIMA models instead.
# Estimate ARIMA models then!



# Auto.arima can give an indication of the best model.
# Remember this is just an indication!!!


# Forecast for the next 10 periods



