from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import os
import pickle
from sklearn.neighbors import KNeighborsClassifier

dir = os.path.dirname(__file__)
model_path = os.path.join(dir, "model.pkl")
with open(model_path, "rb") as f:
    model = pickle.load(f)

@csrf_exempt
def predict(request):
    if request.method == "POST":
        try:
            sl = float(request.POST.get("sl"))
            sw = float(request.POST.get("sw"))
            pl = float(request.POST.get("pl"))
            pw = float(request.POST.get("pw"))
            
            parameters = [[sl, sw, pl, pw]]
            prediction = model.predict(parameters)[0]
            classes = ["setosa", "versicolor", "virginica"]
            prediction_class = classes[prediction]
            
            return JsonResponse({"prediction": prediction_class})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=400)
    return JsonResponse({"error": "Invalid request method"}, status=405)
