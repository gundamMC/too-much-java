from django.shortcuts import render


def dropoff(request):
    if 'file' not in request.FILES:
        # no file uploaded, show default page
        return render(request, '../templates/assignment_dropoff.html')
    else:
        f = request.FILES['file'] # here you get the files needed
        print(f.name)
        return render(request, '../templates/assignment_dropoff.html', {'name': f.name})
