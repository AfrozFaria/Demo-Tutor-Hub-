from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User, Group
from django.contrib.auth import get_user_model
from ad.models import Ad_Student, Ad_Tutor
from ad.forms import Ad_Student_Form, Ad_Tutor_Form
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from home.models import Student, Tutor
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage


@login_required
def view_more(request, pk):
    '''
    This will redirect the url to the view more page
    :type request: HttpResponse
    :param request: Takes the request to show view_more.html
    :param pk: Gets value of id of the selected ad
    '''
    # usr = User.objects.get(username=request.user)
    if request.user.groups.filter(name='student').exists():
        ad = Ad_Tutor.objects.get(id=pk)
    else:
        ad = Ad_Student.objects.get(id=pk)
    # stu_ad = Ad_Student.objects.get(id=pk)
    # ad = Ad_Tutor.objects.get(id=pk)
    return render(request, 'view_more.html', {'ad': ad})
