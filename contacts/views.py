from django.shortcuts import redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact

def contact(request):
    if request.method == 'POST':
       listing = request.POST['listing']
       listing_id = request.POST['listing_id']
       user_id = request.POST['user_id']
       realtor_email = request.POST['realtor_email']
       realtor_name = request.POST['realtor_name']
       name = request.POST['name']
       email = request.POST['email']
       phone = request.POST['phone']
       message = request.POST['message']

       if request.user.is_authenticated:
           user_id = request.user.id
           has_sent_inquiry = Contact.objects.all().filter(user_id=user_id, listing_id=listing_id)
           if has_sent_inquiry:
               messages.error(request, 'You have already inquired about this listing')
               return redirect('/listings/{}'.format(listing_id))


       contact = Contact(listing=listing, listing_id=listing_id, user_id=user_id, name=name, email=email, phone=phone, message=message)
       contact.save()

    #    send_mail(
    #        'Property Listing Inquiry({})'.format(listing),
    #        'There is an inquiry about {}'.format(listing),
    #        'dummy@gmail.com',
    #        [realtor_email],
    #        fail_silently=False
    #    )

       messages.success(request, 'Your inquiry was saved and an email was sent to {}'.format(realtor_name))

    return redirect('/listings/{}'.format(listing_id))