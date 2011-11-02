from django.shortcuts import render

import mail

def home(request):
    return render(request, 'mobile/index.html')


def download(request):
    return render(request, 'mobile/download.html')


def screenshots(request):
    return render(request, 'mobile/screenshots.html')


def help(request):
    return render(request, 'mobile/help.html')


def getting_started(request):
    return render(request, 'mobile/getting_started.html')


def how_to_use_android_app(request):
    return render(request, 'mobile/how_to_use_android_app.html')


def how_to_use_chrome_ext(request):
    return render(request, 'mobile/how_to_use_chrome_ext.html')


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

        # name, email and message are required
        if name and email and message:
            mail.send_contact_message(name, email, message)
            model['success'] = True
        else:
            model['error'] = True
            model['name'] = name
            model['email'] = email
            model['message'] = message

    return render(request, 'mobile/contact.html', model)


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

        # only mail and description are required
        if email and description:
            mail.send_issue_message(name, email, module, description)
            model['success'] = True
        else:
            model['error'] = True
            model['name'] = name
            model['email'] = email
            model['module'] = module
            model['description'] = description

    return render(request, 'mobile/submitIssue.html', model)
