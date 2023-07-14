from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# def get_request_data(key, default=None):
#     output = default
#     if "Content-Type" not in request.headers:
#         output = request.args.get(key, default)
#     else:
#         if "application/x-www-form-urlencoded" in request.headers["Content-Type"]:
#             output = request.form.get(key, default)
#         elif "multipart/form-data" in request.headers["Content-Type"]:
#             output = request.form.get(key, default)
#         elif "application/json" in request.headers["Content-Type"]:
#             if key in request.json:
#                 output = request.json[key]
#         elif "text/plain" in request.headers["Content-Type"]:
#             raw_data = json.loads(request.data)
#             if key in raw_data:
#                 output = raw_data[key]
#         if output is None:
#             output = request.args.get(key, default)
#     return output


def hello_world(request):
    return HttpResponse("Hello World!")

def view_home(request):
    from datetime import datetime
    return render(request, 'index.html', {
        'current_time': str(datetime.now()),
    })

