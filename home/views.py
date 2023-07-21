from django.shortcuts import render
from product.models import Product
from feedback.models import Testimonial

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
               'material': material, "all_product": all_product,"health":health}

    return render(request, 'pages/product_details.html', context)


def quote_submit(request):
    import pandas as pd
    if request.method == 'POST':
        name = request.POST.get('name')
        mobile_number = request.POST.get('mobile_number')
        # Retrieve other form fields
        # ...

        # Create a pandas DataFrame with the collected data
        data = pd.DataFrame({
            'Name': [name],
            'Mobile Number': [mobile_number],
            # Other fields
            # ...
        })

        # Append the data to an existing Excel file
        # file_path = 'test.xlsx'
        # with pd.ExcelWriter(file_path, mode='a', engine='openpyxl') as writer:
        #     data.to_excel(writer, index=False, header=not writer.sheets)

        return HttpResponse('Thank you for your submission!')

    return HttpResponseBadRequest('Invalid request method.')


def capture_location(request):
    if request.method == 'GET':
        latitude = request.GET.get('latitude', None)
        longitude = request.GET.get('longitude', None)

        # For testing purposes, print the latitude and longitude
        print(f"Received latitude: {latitude}, longitude: {longitude}")

        return JsonResponse({'message': 'Location captured successfully.'})
    else:
        return JsonResponse({'message': 'Invalid request method.'}, status=400)
