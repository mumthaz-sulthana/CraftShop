from django import forms

from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User

from shop.models import UserProfile, Product, Category

class SignUpForm(UserCreationForm):
    
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))
    
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={"class": "form-control"}))

    class Meta:
        
        model = User
        
        fields = ["username", "email", "password1", "password2"]
        
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
        }
        
class SignInForm(forms.ModelForm):
    
    class Meta:
        
        model = User
        
        fields = ["username", "password"]
        
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control"}),
            "password": forms.PasswordInput(attrs={"class": "form-control"}),
        }
        
class UserProfileForm(forms.ModelForm):
    
    class Meta:
        
        model = UserProfile
        
        fields = ["bio", "profile_pic"]
        
        widgets = {
            "bio": forms.TextInput(attrs={"class": "w-full border p-2 my-3"}),
            "profile_pic": forms.FileInput(attrs={"class": "w-full p-2 my-3"}),
        }

class ProductForm(forms.ModelForm):
    
    class Meta:
        
        model = Product
        
        exclude = ["created_date", "updated_date", "is_active", "owner"]
        
        widgets = {
            "name": forms.TextInput(attrs={"class": "w-full p-3 border mb-3"}),
            "description": forms.Textarea(attrs={"class": "w-full p-3 border mb-3", "rows": 5}),
            "category_object": forms.Select(attrs={"class": "w-full p-3 border mb-3"}),
            "price": forms.NumberInput(attrs={"class": "w-full p-3 border mb-3"}),
            "stock": forms.NumberInput(attrs={"class": "w-full p-3 border mb-3"}),
            "image": forms.FileInput(attrs={"class": "w-full p-3 border mb-3"}),
        }
        
class CategoryForm(forms.ModelForm):
    
    class Meta:
        
        model = Category
        
        fields = ["title"]
        
        widgets = {
            "title": forms.TextInput(attrs={"class": "w-full p-3 border mb-3"}),
        }