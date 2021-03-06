from web_site.models import Blog, CodeGist, Tweet
from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class CustomAuthenticateForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget = forms.TextInput(attrs={'placeholder' : 'Github ID', 'class' : "form-control"})
        self.fields['password'].widget = forms.TextInput(attrs={'placeholder' : 'password', 'type' : 'password', "class" : "form-control"})

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User 
        fields = ['first_name', "last_name", 'username', 'email', 'password1', 'password2']
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["first_name"].widget = forms.TextInput(attrs={"placeholder" : "First Name", "class" : "form-control"})
        self.fields["last_name"].widget = forms.TextInput(attrs={"placeholder" : "Last Name", "class" : "form-control"})
        self.fields['username'].widget = forms.TextInput(attrs={'placeholder' : 'Github ID', "class" : "form-control"})
        self.fields['email'].widget = forms.EmailInput(attrs={'placeholder' : 'Email', "class" : "form-control"})
        self.fields['password1'].widget = forms.TextInput(attrs={'placeholder' : 'Password', 'type' : 'password', "class" : "form-control"})
        self.fields['password2'].widget = forms.TextInput(attrs={'placeholder' : 'Confirm Password', 'type' : 'password', "class" : "form-control"})


class BlogForm(forms.ModelForm):
    class Meta:
        model = Blog
        fields = ("title", "description", "content")
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["title"].widget = forms.TextInput(attrs={"placeholder" : "Enter a title for your article", "class" : "form-control"})
        self.fields["description"].widget = forms.TextInput(attrs={"placeholder" : "Description", "class" : "form-control"})
        self.fields["content"].widget = forms.Textarea(attrs={"placeholder" : "Enter your article content here! type markdown", "class" : "form-control"})


class CodeGistForm(forms.ModelForm):
    class Meta:
        model = CodeGist
        fields = ( "language", "analogy", "code_snippet", "difficulty", "topic",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["topic"].widget = forms.TextInput(attrs={"placeholder" : "Enter the topic", "class" : "form-control"})
        self.fields["analogy"].widget = forms.Textarea(attrs={"placeholder" : "Describe your code!! (You can type markup)", "class" : "form-control"})
        self.fields["code_snippet"].widget = forms.Textarea(attrs={"placeholder" : "Enter your code here!!", "class" : "form-control"})


class TweetCreationForm(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ("content",)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields["content"].widget = forms.Textarea(attrs={'placeholder' : "Enter your post content here!(Supports markdown)", "class" : "form-control", "style" : "max-height: 15vh;" })