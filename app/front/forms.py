from django import forms

#     authors         = models.CharField(max_length=80)
#     year            = models.CharField(max_length=4)
#     edition         = models.CharField(max_length=10)
#     volume          = models.CharField(max_length=10)
#     no_of_pages     = models.CharField(max_length=20)
#     publisher       = models.CharField(max_length=20)
#     city            = models.CharField(max_length=15)
#     title           = models.CharField(max_length=30)
#     journal         = models.CharField(max_length=200)
#     bookTitle       = models.CharField(max_length=200)
#     referenceType 

class ReferenceForm(forms.Form):
    author = forms.CharField(
        label = "Author(s) of the reference",
    )

    year = forms.CharField(
        label = "Reference year",
        widget=forms.TextInput(attrs={'placeholder': '2022'})
    )

    edition = forms.CharField(
        label = "Edition",
    )

    volume = forms.IntegerField(
        label = "Volume",
    )