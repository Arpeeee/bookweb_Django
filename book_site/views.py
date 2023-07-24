from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import datetime

# Create your views here.


def get_request_data(key, default=None):
    from rest_framework.request import Request as request
    import json

    output = default
    if "Content-Type" not in request.headers:
        output = request.GET.get(key, default)
    else:
        if "application/x-www-form-urlencoded" in request.headers["Content-Type"]:
            output = request.data.get(key, default)
        elif "multipart/form-data" in request.headers["Content-Type"]:
            output = request.data.get(key, default)
        elif "application/json" in request.headers["Content-Type"]:
            if key in request.json:
                output = request.json[key]
        elif "text/plain" in request.headers["Content-Type"]:
            raw_data = json.loads(request.data)
            if key in raw_data:
                output = raw_data[key]
        if output is None:
            output = request.GET.get(key, default)
    return output


def hello_world(request):
    return HttpResponse("Hello World!")


def view_home(request):
    from datetime import datetime

    return render(
        request,
        "index.html",
        {
            "current_time": str(datetime.now()),
        },
    )


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
def api_Review(request):
    from .models import review

    post2 = review.objects.all()

    if request.method == "GET":
        if not (output := [row.list for row in post2]):
            return Response({"status": "error", "detail": "id not exit"})
        return Response({"status": "good", "output": output})


@api_view(["POST"])
def login(request):
    from .models import UserAccount, User
    from django.contrib.auth.hashers import make_password, check_password

    timestamp = datetime.now()
    # 因為用其他方法會出錯，所以不用判斷request method
    if not (email := request.POST["email"]):
        return JsonResponse(
            {"Status": "error", "Detail": "no email", "timestamp": timestamp}
        )
    if not (passowrd := request.POST["password"]):
        return JsonResponse(
            {"Status": "error", "Detail": "no password", "timestamp": timestamp}
        )
    try:
        UserAccount.objects.get(email=email)
        if check_password(passowrd, UserAccount.objects.get(email=email).password):
            try:
                username = UserAccount.objects.get(email=email).worker.name
                userrank = UserAccount.objects.get(email=email).worker.rank.rank
                return JsonResponse(
                    {"user": username, "userrank": userrank, "timestamp": timestamp}
                )
            except:
                pass
        else:
            return JsonResponse(
                {"Status": "error", "Detail": "wrong password", "timestamp": timestamp}
            )
    except:
        return JsonResponse(
            {"Status": "error", "Detail": "wrong email", "timestamp": timestamp}
        )

        # if not check_password(passowrd,UserAccount.objects.get(email=email).password):
