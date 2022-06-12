from .helper_functions import main
from django.shortcuts import render
from .models import Data

def index(request):
    main()
    return render(request, 'index.html', context={"data_lst": Data.objects.all()})
