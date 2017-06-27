from datetime import date
from django.shortcuts import render,redirect
from booktest.models import BookInfo, HeroInfo


# 查询所有图书和英雄，并显示的视图函数
def index(request):
    books=BookInfo.objects.all()
    heros=HeroInfo.objects.all()
    return render(request,'booktest/index.html',{'books':books,'heros':heros})

# 新增图书视图视图函数
def addBook(request):
    book=BookInfo()
    book.btitle='晓可自传'
    book.bpub_date=date(2017,6,27)
    book.save()
    # return HttpResponse('ok')
    # 重定向跳转到首页
    return redirect('/index/')

# 根据图书id删除一本书的视图函数
def delBook(request,bid):
    # 查询出图书
    b=BookInfo.objects.get(id=int(bid))
    b.delete()
    return redirect('/index/')




