from django import forms
from django.contrib.auth.models import User
from tenthoughts.models import SubmitedArticles, Article, Group, UserProf
from django.forms.widgets import TextInput
from datetime import date

class ArticleForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="Please enter the title of the Article")
    url = forms.URLField(max_length=200,
                         help_text="Please enter the URL of the Article",
                         initial='http://',
                         widget=TextInput)
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)


    class Meta:
        model = Article
        exclude = ('submitter', 'submission_date')

        def clean(self):
            cleaned_data = self.cleaned_data
            url = cleaned_data.get('url')

            # If url is not empty and doesn't start with 'http://', prepend 'http://'.
            if url and not url.startswith('http://'):
                url = 'http://' + url
                cleaned_data['url'] = url

            return cleaned_data




class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    password_again = forms.CharField(widget=forms.PasswordInput())
    confirm_email = forms.EmailField(label="Confirm email", required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name')

    #def clean_password_again(self):
        #password1 = self.cleaned_data.get('password1')
        #password2 = self.cleaned_data.get('password_again')

        #if not password2:
            #raise forms.ValidationError("You must confirm your password")
        #if password1 != password2:
            #raise forms.ValidationError("Your passwords do not match")
        
        #return password2



class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProf
        fields = ('picture', ) #'groups')

class GroupSelectForm(forms.Form):
    bschool = forms.ModelChoiceField(queryset=Group.objects.all().order_by('name'), initial=16, label='Business School')
