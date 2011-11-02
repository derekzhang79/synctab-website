
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.conf import settings
from django.utils.encoding import smart_str
from website.sitemap import WebsiteSitemap

import mail

def sitemap(request):
    page = request.GET.get('p', 1)
    domain = settings.DOMAIN

    sitemap = WebsiteSitemap()
    urls = sitemap.get_urls(domain, page)

    xml = smart_str(loader.render_to_string('sitemap.xml', {'urlset': urls}))
    return HttpResponse(xml, mimetype='application/xml')

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

        # name, email and message are required
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

    return render(request, 'submitIssue.html', model)

def help(request):
    return render(request, 'help.html')

def getting_started(request):
    return render(request, 'getting_started.html')

def how_to_use_android_app(request):
    return render(request, 'how_to_use_android_app.html')

def how_to_use_chrome_ext(request):
    return render(request, 'how_to_use_chrome_ext.html')