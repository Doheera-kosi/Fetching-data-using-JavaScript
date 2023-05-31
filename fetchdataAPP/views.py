from django.shortcuts import render
from fetchdataAPP.forms import CommentForm
from .models import UserComments
from django.http import JsonResponse

# Create your views here.

# CREATING VIEW FUNCTION
def form_view(request):
  form = CommentForm()
  
  if request.method == 'POST':
    form = CommentForm(request.POST)