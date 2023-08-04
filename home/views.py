from django.shortcuts import render
from product.models import Product
from feedback.models import Testimonial

from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.


def home(request):
    ''' This function will return the home page content'''
    all_product = Product.objects.all()
    all_testinomial = Testimonial.objects.all()
    context = {
        'all_product': all_product,
        'all_testinomial': all_testinomial
    }
    return render(request, 'pages/index.html', context)


def package_details(request, tour_slug):
    try:
        single_product = Product.objects.get(slug=tour_slug)
        all_product = Product.objects.all()
        material = single_product.material.split(',')
        health = single_product.additional_benefits.split(',')

    except Exception as e:
        raise e

    context = {'single_product': single_product,
               'material': material, "all_product": all_product, "health": health}

    return render(request, 'pages/product_details.html', context)


def quote_submit(request):
    import pandas as pd
    if request.method == 'POST':
        name = request.POST.get('name')
        mobile_number = request.POST.get('mobile_number')
        # Retrieve other form fields
        # ...

        # Append the data to an existing Excel file
        # file_path = 'test.xlsx'
        # with pd.ExcelWriter(file_path, mode='a', engine='openpyxl') as writer:
        #     data.to_excel(writer, index=False, header=not writer.sheets)

        response_data = {
            "status": "success",
            "message": "We have received your information. Our dedicated team will promptly get in touch with you to assist you further. Thank you for choosing our services, and we look forward to providing you with an exceptional experience.",
        }
        return JsonResponse(response_data)


def capture_location(request):
    if request.method == 'GET':
        latitude = request.GET.get('latitude', None)
        longitude = request.GET.get('longitude', None)

        # For testing purposes, print the latitude and longitude
        print(f"Received latitude: {latitude}, longitude: {longitude}")

        return JsonResponse({'message': 'Location captured successfully.'})
    else:
        return JsonResponse({'message': 'Invalid request method.'}, status=400)


def submit_booking(request, slug):
    if request.method == "GET":
        print('submit method called')
        # Get form data from the request
        name = request.GET.get("name")
        email = request.GET.get("email")

        # Perform any additional processing if needed
        # For example, you can save the data in the database here
        # Assuming you have a model named "Booking" to store the data:
        # from .models import Booking
        # booking = Booking(name=name, email=email)
        # booking.save()

        # For demonstration purposes, we'll just return a success response
        response_data = {
            "status": "success",
            "message": "We have received your information. Our dedicated team will promptly get in touch with you to assist you further. Thank you for choosing our services, and we look forward to providing you with an exceptional experience.",
        }
        return JsonResponse(response_data)

    # Handle other HTTP methods if needed (e.g., POST, PUT, DELETE)
    # ...

    # If the request method is not GET or the form submission fails,
    # return an error response
    response_data = {
        "status": "error",
        "message": "Form submission failed.",
    }
    return JsonResponse(response_data, status=400)
