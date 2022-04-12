#   Copyright 2020 Frances M. Skinner, Christian Hill
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

from cProfile import label
from django import forms
from .models import GeographicDiv, Reference, TaxonAuthorLkp, TaxonomicUnit, Kingdom, Expert, TaxonAuthorLkp
from django_select2.forms import Select2MultipleWidget, ModelSelect2MultipleWidget

class RefForm(forms.ModelForm):
    class Meta:
        model = Reference
        exclude = ['ris', 'citeproc_json', 'visible']

    def clean_doi(self):
        doi = self.cleaned_data['doi']
        try:
            ref = Reference.objects.get(doi=doi)
            if ref.pk != self.instance.pk:
                raise forms.ValidationError('A reference with this DOI exists'
                             'in the database already')
        except Reference.MultipleObjectsReturned:
            # Hmmm... there are already multiple entries with this DOI in the
            # database. TODO deal with this case
            pass
        except Reference.DoesNotExist:
            # Good: a reference with this DOI is not in the DB already
            pass

        return self.cleaned_data['doi']

class TaxonForm(forms.ModelForm):
    template_name = 'add-taxon.html'

    kingdom_name = forms.ModelChoiceField(queryset=Kingdom.objects.all())
    rank_name = forms.CharField(widget=forms.Select(choices=[]), label="New taxon's parent")

    taxonnomic_types = forms.CharField(widget=forms.Select(choices=[]), label="Rank of the new taxon")

    # reference = forms.ModelChoiceField(queryset=Reference.objects.all(), label="References where the taxon is mentioned", empty_label="Please choose reference for this taxon")
    # https://stackoverflow.com/a/8538923
    references = forms.ModelMultipleChoiceField(
        queryset=Reference.objects.filter(visible=1),
        widget=Select2MultipleWidget,
    )

    geographic_div = forms.ModelMultipleChoiceField(
        queryset=GeographicDiv.objects.all(),
        widget=Select2MultipleWidget,
        label='Geographic location',
        required=False
    )

    expert = forms.ModelMultipleChoiceField(
        queryset=Expert.objects.all(),
        widget=Select2MultipleWidget,
        label= 'Experts',
        required=False
    )

    author = forms.ModelChoiceField(
    queryset=TaxonAuthorLkp.objects.all(),
    required=False
    )


    # Maybe multiplechoicefield from this advice: https://stackoverflow.com/a/56823482

    # FIX: In order to query database and set an author for new unit, add a suitable field 
    # other later deemed necessary fields can also be added here

    class Meta:
        model = TaxonomicUnit
        fields = ['kingdom_name' , 'taxonnomic_types', 'rank_name', 'unit_name1', 'unit_name2', 'unit_name3', 'unit_name4', 'references', 'geographic_div', 'expert', 'author']
        exclude = ['unnamed_taxon_ind']

class ExpertForm(forms.ModelForm):
    template_name = 'add-expert.html'

    geographic_div = forms.ModelMultipleChoiceField(
        queryset=GeographicDiv.objects.all(),
        widget=Select2MultipleWidget,
    )

    class Meta:
        model = Expert
        fields = ['expert', 'geographic_div']

class AuthorForm(forms.ModelForm):
    template_name = 'add-author.html'

    kingdom = forms.ModelChoiceField(queryset=Kingdom.objects.all())

    class Meta:
        model = TaxonAuthorLkp
        fields = ['taxon_author', 'kingdom']

    # Prevent blank or duplicate authors
    def clean_taxon_author(self):
        taxon_author = self.cleaned_data['taxon_author']
        if taxon_author is None or taxon_author.strip() == '':
            raise forms.ValidationError('Taxon author cannot be left blank')
        try:
            author = TaxonAuthorLkp.objects.get(taxon_author=taxon_author)
            if author is not None:
                raise forms.ValidationError('An author with the name '\
                             + taxon_author + ' already exists in the database')
        except TaxonAuthorLkp.DoesNotExist:
            # Good: an author with this name is not in the DB already
            pass

        return self.cleaned_data['taxon_author']

