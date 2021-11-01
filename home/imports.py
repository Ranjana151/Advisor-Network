from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth import login, logout, authenticate
from django.core.exceptions import ValidationError
import django.dispatch
from rest_framework.decorators import api_view
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status
from rest_framework.response import Response
from django.utils import timezone
from django.core.mail import send_mail
import random
import uuid
import requests
from .models import *
import uuid
# from .signals import *
# from .decorators import *

from .encode  import encode_auth_token
from .decode import decode_auth_token
from .utils import permission_check

import datetime
import json
import time
