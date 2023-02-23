from django.shortcuts import render
from .models import *
#  на шаблоне index.html можно протестить
def index(request):
    bbb = User.objects.all()
    qqq = User.objects.select_related('feedback')

    ttt = Group.objects.all()
    www = Group.objects.select_related('audience')
    rrr = Group.objects.select_related('course')

    context ={'bbb': bbb, 'qqq': qqq, 'www':www, 'rrr': rrr, 'ttt': ttt}



    return render(request, 'lesson/index.html', context)



