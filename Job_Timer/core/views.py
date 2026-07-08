from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import WorkSession
import isodate
from django.utils import timezone

# Create your views here.

@csrf_exempt
def home(request):
    if request.method == "POST":
        data = json.loads(request.body)
        print("Post:", request.body)
        if WorkSession.objects.filter(date=timezone.localdate()).exists():
            return JsonResponse({"create": "exists"}, status=409)
        progress_ = isodate.parse_duration(data.get("progress"))
        WorkSession.objects.create(
            progress_bar=data.get("progress_bar"),
            progress=progress_,
        )
        return JsonResponse({"create": True})

    elif request.method == "PATCH":
        print("Patch: ", request.body)
        data = json.loads(request.body)
        progress_ = isodate.parse_duration(data.get("progress"))
        WorkSession.objects.filter(date=timezone.localdate()).update(
            progress_bar=data.get("progress_bar"),
            progress=progress_,
        )
        return JsonResponse({"update": True})

    elif request.method == "GET":
        sessions = WorkSession.objects.all().order_by("-id")
        data_view = []
        for s in sessions:
            data_view.append({
                "progress_bar": s.progress_bar,
                "date": s.date,
                "progress": s.progress,
            })
        return JsonResponse(data_view, safe=False)

    else:
        return JsonResponse({"method": False}, status=405)