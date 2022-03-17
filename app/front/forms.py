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

from django import forms
from .models import Reference, TaxonomicUnit, Kingdom

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

class NameForm(forms.ModelForm):
    template_name = 'add_name.html'

    kingdom_name = forms.ModelChoiceField(queryset=Kingdom.objects.all())
    rank_name = forms.CharField(widget=forms.Select(choices=[]), label="Rank of new taxon's parent")

    taxonnomic_types = forms.CharField(widget=forms.Select(choices=[]), label="Rank of the new taxon")
    
    # FIX: In order to query database and set an author for new unit, add a suitable field 
    # other later deemed necessary fields can also be added here

    class Meta:
        model = TaxonomicUnit
        fields = ['kingdom_name' , 'taxonnomic_types', 'rank_name', 'unit_name1', 'unit_name2', 'unit_name3', 'unit_name4']
        exclude = ['unnamed_taxon_ind']
