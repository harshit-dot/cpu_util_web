from django.shortcuts import render, redirect
from django.contrib import messages
import re
import smtplib
import matplotlib.pyplot as plt
from datetime import datetime
import numpy as np
from matplotlib.backends.backend_pdf import PdfPages
import csv
import os
import paramiko
import time

# Create your views here.

def main(request):
    return render(request, 'app/index.html')


def download(request):
    if request.method == 'POST':
        email = request.POST['email']
        ip_address = request.POST['ip_address']
        start_time = request.POST['start_time']
        end_time = request.POST['end_time']
        username = request.POST['username']
        password = request.POST['password']
        gap = request.POST['gap']
        if int(gap) <= 0:
            messages.error(request, "Gap in between two snapshots should greater than 0")
            return redirect('/')

    return render(request, 'app/index.html')

