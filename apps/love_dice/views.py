from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .models import *
from .forms import *



def index(request):
    return render(request, '01_pages/index.html')


def edit_memo(request, item_id):
    instance_to_edit = get_object_or_404(Memo, pk=item_id)
    if request.method == 'POST':
        form = MemoForm(request.POST, instance=instance_to_edit)
        if form.is_valid():
            form.save()
            return redirect('memos')
    else:
        form = MemoForm(instance=item)
    return render(request, '01_pages/edit_memo.html', {'form': form})


def delete_memo(request, item_id):
    item = get_object_or_404(Memo, pk=item_id)
    if request.method == 'POST':
        item.delete()
        return redirect('memos')
    return render(request, '01_pages/delete_memo.html', {'item': item})


def create_memo(request):
    if request.method == 'POST':
        form = MemoForm(request.POST)  # request.POSTでformの内容を辞書形式で取得
        if form.is_valid():  # tableのフィールド定義に従っているかどうかをチェック
            form.save()  # dbに保存
            return redirect('memos')
    else:
        form = MemoForm()
    return render(request, '01_pages/create_memo.html', {'form': form})


def memos(request):
    context = {}
    context['memos'] = Memo.objects.all()
    return render(request, '01_pages/memos.html', context)
