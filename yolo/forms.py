from django import forms 




class uploadimage(forms.Form):
    #name = forms.CharField()
    #email= forms.EmailField()
    #text = forms.CharField(widget=forms.Textarea)

    image = forms.FileField()


        