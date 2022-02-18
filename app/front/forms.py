from django import forms

class ReferenceForm(forms.Form):
    authors = forms.CharField(
        label = "Author(s) of the reference",
        help_text="Comma-delimited names with space-separated initials first (no ANDs). e.g. \"A. N. Other, B.-C. Person Jr., Ch. Someone-Someone, N. M. L. Haw Haw\""
    )

    title = forms.CharField(
        label = "Title",
        help_text="Best-effort UTF-8 encoded plaintext version of title. No HTML tags, markdown or LaTeX."
    )

    titlehtml = forms.CharField(
        label = "Title html",
        help_text="Valid HTML version of title. Don't wrap with <p> or other tags."
    )

    titlelatex = forms.CharField(
        label = "Title latex",
        help_text="LaTeX version of title. Don't escape backslashes (\) but do use valid LaTeX for accented and similar characers."
    )

    journal = forms.CharField(
        label = "Journal",
        help_text=""
    )

    volume = forms.CharField(
        label = "Volume",
        help_text=""
    )

    pagestart = forms.CharField(
        label = "Page start",
        help_text=""
    )

    pageend = forms.CharField(
        label = "Page end",
        help_text=""
    )

    articlenumber = forms.CharField(
        label = "Article number",
        help_text=""
    )

    year = forms.CharField(
        label = "Year",
        widget=forms.TextInput(attrs={'placeholder': '2022'})
    )

    note = forms.CharField(
        label = "Note",
    )

    notehtml = forms.CharField(
        label = "Note html",
    )

    notelatex = forms.CharField(
        label = "Note latex",
    )

    doi = forms.CharField(
        label = "Doi",
    )

    bibcode = forms.CharField(
        label = "Bibcode",
    )

    url = forms.CharField(
        label = "Url",
        help_text="If not provided, this will be automatically constructed as https://dx.doi.org/<DOI> if possible."
    )

    bibtex = forms.IntegerField(
        label = "Bibtex",
    )