from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *

def chat_view(request):
    chat_group = get_object_or_404(ChatGroup, group_name="number1")
    chat_messages = chat_group.chat_messages.all()[:30]
    form = ChatmessageCreateForm()
    if request.htmx:
        form = ChatmessageCreateForm(request.POST)
        if form.is_valid:
            message = form.save(commit=False)
            message.author = request.user
            message.group = chat_group
            message.save()
            context = {
                'message' : message,
                'user' : request.user
            }
            return render(request, 'partials/chat_message_p.html', context)
    return render(request, 'chat.html', {'chat_messages':chat_messages,'form':form})

