from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.request import Request
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

# def Testreview(request):
#     from .models import review
#     if request.method == "GET":
#         review2 = review.objects.get(id=2)
#         review_data = {
#             'id': review2.id,
#             'title': review2.slug,
#             # Add other fields you want to include in the JSON representation
#         }
        
#         return JsonResponse(review_data)

@api_view(["GET"])
def testReview(request):
    from .models import review
    from .serializers import reviewSerializer
    post2 = review.objects.get(id=3)

    if request.method == "GET":
        if not (output:=reviewSerializer(post2)):
            return JsonResponse({
                "status": "error",
                "detail": "id not exit"
            })
        return JsonResponse({
            "status": "good",
            "output": output
        })