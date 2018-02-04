class LogMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        print("Before middleware")
        response = self.get_response(request)
        print("After middleware")

        return response
