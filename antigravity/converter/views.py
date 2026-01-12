from django.shortcuts import render
from .forms import LogInputForm

def index(request):
    result = None
    if request.method == 'POST':
        form = LogInputForm(request.POST, request.FILES)
        if form.is_valid():
            # Get the input text
            log_text = form.cleaned_data.get('log_text')
            # Get the uploaded file (if provided)
            log_file = form.cleaned_data.get('log_file')
            
            # For now, just print it to console to verify
            if log_text:
                print(f"User Input Text: {log_text}")
                # Placeholder for conversion logic
                result = f"Received {len(log_text)} characters of text."
            
            if log_file:
                # Handle file reading if needed
                content = log_file.read().decode('utf-8')
                print(f"User Input File content: {content[:100]}...")
                
    else:
        form = LogInputForm()

    context = {
        'form': form,
        'result': result
    }
    return render(request, 'index.html', context)
