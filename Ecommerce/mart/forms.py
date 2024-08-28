from django import forms

class ProductForm(forms.Form):
    productID = forms.IntegerField(label='Product ID')
    productName = forms.CharField(label='Product Name', max_length=100)
    price = forms.DecimalField(label='Price', max_digits=10, decimal_places=2)
    stock = forms.IntegerField(label='Stock')
