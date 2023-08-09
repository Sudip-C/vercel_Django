from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
# Create your views here.

data={}

def Home(request):
    return HttpResponse("Welcome!")

def create_item(request):
    if request.method == "POST" :
        name = request.POST.get('name')
        age= request.POST.get('age')
        city = request.POST.get('city')

        new_item = {
            'name': name,
            'age' : age,
            'city' :city,
        }

        item_id = len(data)+1
        data[item_id]= new_item
        return JsonResponse(new_item, status=201)
    return render(request, 'crud_app/create_item.html')

def read_items(request):
    # TODO: Your code here
    return render(request, 'crud_app/read_items.html', {'items': data})

def update_item(request):
    if request.method == 'POST':
        key = request.POST.get('key')
        new_value = request.POST.get('new_value')

        if key in data:
            data[key] = new_value
            return JsonResponse({'message': 'Item updated successfully'})
        else:
            return JsonResponse({'error':'Key not found'},status=404)
    return render(request, 'crud_app/update_item.html')

def delete_item(request):
    if request.method == "POST":
        key = request.POST.get('key')

        if key in data:
            del data[key]
            return JsonResponse({'message' : "item deleted successfuly!"})
    return render(request, 'crud_app/delete_item.html')