from django.shortcuts import render
from bs4 import BeautifulSoup
import requests

# Create your views here.
def home(request):
  return render(request, 'home.html')

def result(request):
  URL = 'https://search.naver.com/search.naver?where=news&sm=tab_jum&query='
  query = request.GET.get('search_term', '')
  fullURL = URL + query
  html = requests.get(fullURL).text
  soup = BeautifulSoup(html, 'html.parser')
  news_title = soup.find_all(class_='_sp_each_title')
  title_array = []
  for title in news_title:
    title_array.append({'url': title.get('href'), 'title': title.get('title')})

  return render(request, 'result.html', {'objects': title_array})