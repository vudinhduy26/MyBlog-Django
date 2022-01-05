from django.core import paginator
from django.shortcuts import render , redirect
from django.core.paginator import Paginator
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings



from .models import *
from django.core.paginator import Paginator

# Create your views here.

def search_content(request):
    if request.method == "POST":
        search_ct = request.POST['searched']
        #content
        search_content = content_home.objects.filter(title__contains = search_ct)
        paginator = Paginator(search_content,6)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        ####
        #list categories
        content1 = categorie.objects.all().order_by('id')
        paginator = Paginator(content1,5)
        page_number1 = request.GET.get('page')
        page_obj1 = paginator.get_page(page_number1)
        ####
        #list categories
        cate_child = child_cate.objects.filter()
        ####
        return render(request,'home/search_content.html',{
            'searched_ct':search_ct,
            'page_obj':page_obj,
            'page_obj1':page_obj1,
            'cate_childs':cate_child,
            'content1':content1,
            })
    else:
        return render(request,'home/search_content.html')


def index(request):
    #list nav
    content1 = categorie.objects.all().order_by('id')
    ####
    content = content_home.objects.all().order_by('id')
    paginator = Paginator(content,6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    #
    element5 = content_home.objects.all().order_by('id').reverse()[:5]
    #list categories
    cate_child = child_cate.objects.filter()
    #
    #get list content same categorie
    
    #
    paginator = Paginator(content1,5)
    page_number1 = request.GET.get('page')
    page_obj1 = paginator.get_page(page_number1)
    return render(request,'home/index.html',{
        'content':content,
        'page_obj':page_obj,
        'page_obj1':page_obj1,
        'content1':content1,
        'element':element5,
        'cate_childs':cate_child,
    })

def detail_content(request,detail_slug,categories_slug,categories_child_slug):
    select_detail = content_home.objects.get(slug=detail_slug,categories__slug_child=categories_child_slug,categories__categorie_child__slug=categories_slug)
    content1 = categorie.objects.all().order_by('id')
    paginator = Paginator(content1,5)
    page_number1 = request.GET.get('page')
    page_obj1 = paginator.get_page(page_number1)
    #
    element = content_home.objects.all().order_by('id').reverse()[:5]
    #
    cate_child = child_cate.objects.all()
    return render(request,'home/detail_content.html',{
        'select_detail':select_detail,
        'content1':content1,
        'page_obj1':page_obj1,
        'element':element,
        'cate_childs':cate_child,
    })

#list content categories child
def categoriess_content_child(request,categories,categories_child):
    #lay tat cac ca pha tu voi dieu kien 
    categoriess = content_home.objects.filter(categories__categorie_child__slug=categories,categories__slug_child=categories_child)
    paginator = Paginator(categoriess,10)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    #
    element = content_home.objects.all().order_by('id').reverse()[:5]
    #
    cate_child = child_cate.objects.all()
    #
    #list categories
    content1 = categorie.objects.all().order_by('id')
    paginator = Paginator(content1,5)
    page_number1 = request.GET.get('page')
    page_obj1 = paginator.get_page(page_number1)
    return render(request,'home/categories_content_child.html',{
        'categories_childs':categoriess,
        'content1':content1,
        #'categ':cate,
        'page_obj':page_obj,
        'page_obj1':page_obj1,
        'element':element,
        'cate_childs':cate_child,
    })
    

def ContentSamecate(request,slugsame):
    #list same categories
    contentSameSlug = content_home.objects.filter(categories__categorie_child__slug=slugsame)
    paginatoR = Paginator(contentSameSlug,6)
    page_number1 = request.GET.get('page')
    page_obj = paginatoR.get_page(page_number1)

    #list content recommend
    element = content_home.objects.all().order_by('id').reverse()[:5]
    
    #list categories
    content1 = categorie.objects.all().order_by('id')
    paginator = Paginator(content1,5)
    page_number1 = request.GET.get('page')
    page_obj1 = paginator.get_page(page_number1)    
    #list nav
    content1 = categorie.objects.all().order_by('id')
    cate_child = child_cate.objects.all()


    return render(request,'home/categories_content.html',{
        'contentSameSlug':contentSameSlug,
        'page_obj':page_obj,
        'element':element,
        #categories
        'page_obj1':page_obj1,
        'cate_childs':cate_child,
        'content1':content1,
    })


def contact(request):
    content1 = categorie.objects.all().order_by('id')
    paginator = Paginator(content1,5)
    page_number1 = request.GET.get('page')
    page_obj1 = paginator.get_page(page_number1)
    element5 = content_home.objects.all().order_by('id').reverse()[:5]
    #list categories
    cate_child = child_cate.objects.all()
    #list nav
    content1 = categorie.objects.all().order_by('id')

    return render(request,'home/contact.html',{
        'element':element5,
        'page_obj1':page_obj1,
        'cate_childs':cate_child,
        'content1':content1,
    })



def sendMail(request):
    if request.method == 'POST':
        sender = settings.EMAIL_HOST_USER
        receiver = request.POST['receiver']
        subject = request.POST['sub']
        content = request.POST['content']

        mail = send_mail(subject, content, sender, [receiver], fail_silently=False)
        if mail:
            messages.success(request, 'Email has been sent.')
            return redirect('home')
    else:
        return redirect('home')
