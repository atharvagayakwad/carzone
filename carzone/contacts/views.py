from django.shortcuts import redirect, render

from contacts.models import ContactModel
from django.contrib import messages
from django.core.mail import send_mail
from django.contrib.auth.models import User
# Create your views here.


def inquiry(request):
    if request.method == 'POST':
        car_id = request.POST['car_id']
        car_title = request.POST['car_title']
        user_id = request.POST['user_id']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        city = request.POST['city']
        state = request.POST['state']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        # check if user has already made a request
        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = ContactModel.objects.all().filter(car_id=car_id, user_id=user_id)
            if has_contacted:
                messages.error(
                    request, "You have already made an inquiry about this car. Please wait until we get back to you")
                return redirect('/cars/' + car_id)

        contact = ContactModel(car_id=car_id, car_title=car_title, user_id=user_id, first_name=first_name,
                               last_name=last_name, city=city, state=state, email=email, phone=phone, message=message)

        # getting email of super user 
        admin_info = User.objects.get(is_superuser=True)
        admin_email_id = admin_info.email

        send_mail(
            'New Car Inquiry',
            'You have a new inquiry for the car ' + car_title + '. Please login to your admin panel for more info',
            'atharvag3011@gmail.com',
            [admin_email_id],
            fail_silently=False,
        )

        contact.save()
        messages.success(
            request, 'Your request has been submitted, we will get back to you shortly.')
        return redirect('/cars/'+car_id)
