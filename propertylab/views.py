from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import get_template
from django.core.mail import send_mail, EmailMultiAlternatives
from django.template.loader import render_to_string
from django.contrib import messages
from django.template import Context
from .forms import WebsiteEnquiryForm

def home_page(request):
 my_title = "hello propertylab..."
 context = {"title": my_title}
 return render(request, "home.html", context)


def enquiry_view(request):
  
	form = WebsiteEnquiryForm(request.POST or None)
	if form.is_valid():
	    print(form.cleaned_data)

	    # merge_data = {
	    #     'ORDERNO': "12345", 'TRACKINGNO': "1Z987"
	    # }
	    # plaintext_context = Context(autoescape=False)  # HTML escaping not appropriate in plaintext
	    # #subject = render_to_string("property_subject.txt", merge_data, plaintext_context)
	    # subject = 'Website enquiry'
	    # text_body = render_to_string("email/enquiry.html", merge_data)
	    
	    # msg = EmailMultiAlternatives(subject=subject, from_email="dhirendra@propertylab.net",
	    #                              to=["dhirendra@propertylab.net"], body=text_body)
	    # msg.attach_alternative(text_body, "text/html")
	    # msg.send()
	    send_mail(
	        'Website enquiry',
	         form.cleaned_data['message'],
	        'dhirendra@propertylab.net',
	        ['dhirendra@propertylab.net'],
	        fail_silently=False,
	    )
	    messages.success(request, 'Email sent successfully.')
	    form = WebsiteEnquiryForm()

	context = {"title": "Sent successfully"}
	return render(request, "home.html", context)
