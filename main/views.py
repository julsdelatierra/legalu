from django.shortcuts import render_to_response as render
from django.http import HttpResponse as response
from django.template.context import RequestContext as rc
from latex import LatexDocument

def index(req):
    if req.user.is_authenticated():
        return redirect('/home/')
    #login_facebook_url = 'https://graph.facebook.com/oauth/authorize?client_id=%s&redirect_uri=%s&scope=publish_stream,email' % (settings.APP_ID_FACEBOOK, settings.URL+'/login/facebook/')
    args = {
        #'login_facebook_url':login_facebook_url
    }
    return render('index.html', args, context_instance = rc(req))

def about(req):
    args = {}
    return render('about.html', args, context_instance = rc(req))

document = ur'''
\documentclass{article}
\begin{document}
Hola %(first_name)s %(last_name)s.

Naciste el %(birthday)s.

Vives en %(address)s.

No. de document: %(num_document)s.
\end{document}
'''

def new(req):
  args = {}
  return render('new.html', args, context_instance=rc(req))

def save(req):
  json_obj = convert_json(req.POST)
  document_with_content = fill_format(json_obj, document)
  r = LatexDocument(document_with_content)
  pdf = r.as_pdf()
  return response(pdf, mimetype='pdf')

def convert_json(querydict):
  json_obj = {}
  for i in querydict:
    json_obj[i] = querydict[i]
  return json_obj

def fill_format(args, document):
  return document % args
