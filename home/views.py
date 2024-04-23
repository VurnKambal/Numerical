from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_protect
from .forms import DatasetUploadForm
import pandas as pd

@csrf_protect
def home(request):
    context = {}
    if request.method == "POST":
        try:
            form = DatasetUploadForm(request.POST, request.FILES)
            context['form'] = form

            print(request.FILES)
            if form.is_valid():
                cleaned_data = form.cleaned_data['dataset']
                print(cleaned_data)
                df = pd.read_csv(cleaned_data) 
                html = df.to_html(header=False, index=False)
                text_file = open("templates/table.html", "w")
                text_file.write(html)
                text_file.close()

                datasetUploaded = True  # Set datasetUploaded to True if form submitted
                
            else:
                datasetUploaded = False  # Set datasetUploaded to False otherwise

                return HttpResponse("Form is not valid")
            
        except Exception as e:
            return HttpResponse("Error uploading file: " + str(e))
    else:
        form = DatasetUploadForm()

        datasetUploaded = False
        df = None

    context = {
        'form': form,
        'datasetUploaded': datasetUploaded,
        'df': df
    }  
    return render(request, 'home.html', context)

        
def about(request):
    return render(request, 'about.html')
# end
    