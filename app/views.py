# from django.shortcuts import render
# import requests

# # Create your views here.
# def index(request):
#      city=request.GET.get('city')
#      api_key="e601ad48ae344f6f7bd97024b87ebe6c"
#      api_url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
#      print(api_url)
#      api=requests.get(api_url).json()
#      temperature=api['main']['temp']
#      city=api['name']

#      return render(request,'index.html',{'temperature':temperature,'city':city})

from django.shortcuts import render
import requests

# Create your views here.
def index(request):
  city=request.GET.get('city')
  api_key="b9ff926d294018fecfe1d396f20bd2f5"
  api_url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
  print(api_url)
  api=requests.get(api_url).json()
  temperature=api['main']['temp']
  city=api['name']
  
  return render(request,'index.html',{'temperature':temperature,'city':city})