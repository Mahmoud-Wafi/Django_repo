import pandas as pd
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import ProductForm

def display_form(request):
    file_path = 'mart/products.csv'
    
    # Initialize products list
    products = []

    try:
        df = pd.read_csv(file_path)
        products = df.to_dict(orient='records')
    except FileNotFoundError:
        # File not found, products list will be empty
        products = []

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            
            # Create a DataFrame with the new data
            new_data = pd.DataFrame([data])
            
            try:
                # Read existing data and concatenate the new data
                df = pd.read_csv(file_path)
                df = pd.concat([df, new_data], ignore_index=True)
            except FileNotFoundError:
                # If file does not exist, use the new data as the file content
                df = new_data

            # Save the updated DataFrame back to the CSV file
            df.to_csv(file_path, index=False)
            
            return redirect('display_form')
        else:
            return HttpResponse("Invalid form data", status=400)
    else:
        form = ProductForm()

    return render(request, 'mart/display_form.html', {'form': form, 'products': products})

def product_detail(request, product_id):
    file_path = 'mart/products.csv'
    try:
        df = pd.read_csv(file_path)
        product = df[df['productID'] == int(product_id)]
        if product.empty:
            return HttpResponse("Product not found", status=404)
        return render(request, 'mart/product_detail.html', {'product': product.to_dict(orient='records')[0]})
    except FileNotFoundError:
        return HttpResponse("Products file not found", status=404)
