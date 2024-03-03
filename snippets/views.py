from django.shortcuts import render
from django.http import HttpResponse

def top(request):
    return HttpResponse('Hello, Django!')

def snippet_new(request):
    return HttpResponse('スニペットの新規作成')

def snippet_edit(request, snippet_id):
    return HttpResponse(f'スニペットの編集')

def snippet_detail(request, snippet_id):
    return HttpResponse(f'スニペットの詳細閲覧')
# Create your views here.
