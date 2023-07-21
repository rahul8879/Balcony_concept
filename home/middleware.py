# myapp/middleware.py
import time


class RequestLoggerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        # Record the start time when the request is received
        start_time = time.time()
        # Log IP address, user-agent, and referral source
        ip_address = request.META.get('REMOTE_ADDR')
        user_agent = request.META.get('HTTP_USER_AGENT')
        referral_source = request.META.get('HTTP_REFERER')

        # Log or process the information as needed (e.g., save to the database)
        # ...
        # Print the information to the console
        print(f"IP Address: {ip_address}")
        print(f"User-Agent: {user_agent}")
        print(f"Referral Source: {referral_source}")

        # Calculate the time spent on the page
        end_time = time.time()
        time_spent = end_time - start_time
        print(f"Response time : {time_spent} seconds")

        response = self.get_response(request)
        return response
