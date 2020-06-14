from django.shortcuts import render,redirect,HttpResponse
from google_play_scraper import app
import json



# com.google.android.gm.lite
def home(request):
    url='home.html'
    result=''
    if(request.method=='POST'):
        app_id = request.POST['appid']
        result = app(
            app_id = app_id ,
            lang = 'en' ,  # defaults to 'en'
            country = 'us'  # defaults to 'us'
        )
        print(type(result))



        request.session['result'] = result
        return redirect('/result')



    return render(request,url)


def result(request) :
    url = 'result.html'
    title='Scrape Results'
    heading='Scrape Results'
    result= request.session.get('result')
    print(type(result))

    return render(request , url,{'result': result,'title':title,'heading':heading})
