# Create your views here.
from django.shortcuts import render

import mail

def home(request):
    return render(request, 'index.html')


def download(request):
    return render(request, 'download.html')


def screenshots(request):
    return render(request, 'screenshots.html')

def contact(request):

    model = {
        'success': False,
        'error': False,
        'name': "",
        'email': "",
        'message': ""
    }

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        if name and email and message:
            mail.send_contact_message(name, email, message)
            model['success'] = True
        else:
            model['error'] = True
            model['name'] = name
            model['email'] = email
            model['message'] = message

    return render(request, 'contact.html', model)

def submitIssue(request):
    model = {
        'success': False,
        'error': False,
        'name': "",
        'email': "",
        'module': "",
        'description': ""
    }

    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        module = request.POST.get('module')
        description = request.POST.get('description')

        if email and description:
            mail.send_issue_message(name, email, module, description)
            model['success'] = True
        else:
            model['error'] = True
            model['name'] = name
            model['email'] = email
            model['module'] = module
            model['description'] = description

    return render(request, 'submitIssue.html', model)

def help(request):
    return render(request, 'help.html')

def getting_started(request):
    return render(request, 'getting-started.html')