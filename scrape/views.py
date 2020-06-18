from django.shortcuts import render,redirect,HttpResponse
from google_play_scraper import app
from django.shortcuts import redirect
from django.contrib import messages
from django.conf import settings
import json



# com.google.android.gm.lite
def home(request):
    url='home.html'
    result=''
    context={}
    if(request.method=='POST'):
        app_id = request.POST['appid']

        try:

            result = app(
                app_id = app_id ,
                lang = 'en' ,  # defaults to 'en'
                country = 'us'  # defaults to 'us'
            )
            request.session['result'] = result
            return redirect('/result')
        except:
            messages.error(request , "Invalid Id . Please check")





    return render(request,url)


def result(request) :
    url = 'result.html'
    title='Scrap Results'
    heading='Scraping Results'
    result= request.session.get('result')
    print(type(result))

    return render(request , url,{'result': result,'title':title,'heading':heading})

def handler404(request,exception=None):
    context = {"project_name":settings.PROJECT_NAME}
    return redirect('')
# def handler500(request,exception):
#     context = {"project_name":settings.PROJECT_NAME}
#     return render('500.html')
