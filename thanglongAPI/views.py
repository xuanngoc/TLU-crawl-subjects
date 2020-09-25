from django.http import HttpResponse

from scraping.management.commands.scrape import Login

def home(request):
    login = Login()
    login.startLogin()
    return HttpResponse(login.getSchedule())