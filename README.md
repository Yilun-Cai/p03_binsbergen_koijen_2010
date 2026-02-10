# Predictive-Regressions-A-Present-Value-Approach
Full Stack Finance Final Project:

Goals:
- estimate expected returns of the aggregate stock market
- estimate expected dividend frouth rates of the aggregates

How:
 using the aggregates information contained in the history of **price-dividend ratio** and **divident growth rates** to predict future returns and divident growth rates。
- treat conditional expected returns and expected dividend growth rates as latent variables that follow an exogenously specified time-series model
- combine this model with a Campbell and Shiller (1988) present-value model to derive the implied dynamics of the price-dividend ratio.
- using a Kalman filter to construct the likelihood of our model, we estimate the parameters of the model by means of maximum likelihood.

Data specification:
 - consider an annual model to ensure that the dividend growth predictability not simply driven by the seasonality in dividend payments.
 - consider two reinvestment strategy of dividends:
 1. reinvest dividends in a 30-day T-bill, which is **cash-reinvested dividends**.
 2. reinvest dividends in the aggregate stock market, which refers to as **market-reinvested dividends**.

Assumption:
- consider first-order autoregressive processes for expected cash-reinvested dividend growth and returns;