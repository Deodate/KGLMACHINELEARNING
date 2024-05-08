from django.shortcuts import render
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

def index(request):
    return render(request, 'index.html')
def predict(request):
    return render(request, 'predict.html')

def result(request):
    return render(request, "predict.html")