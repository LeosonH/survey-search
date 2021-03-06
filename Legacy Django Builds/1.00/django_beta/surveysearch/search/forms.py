from django import forms

from search.models import SurveyDetails


class SurveyUploadForm(forms.ModelForm):

    summary = forms.CharField(widget=forms.Textarea)

    class Meta:
        model = SurveyDetails
        fields = ('survey_name',\
        'org_conduct', 'num_participants', 'num_questions', 'data_link', 'doc_link', 'source_link', \
        'summary', 'survey_questions_document')


    def __init__(self, *args, **kwargs):
        super(SurveyUploadForm, self).__init__(*args, **kwargs)
        self.fields['summary'].widget.attrs['cols'] = 40
        self.fields['summary'].widget.attrs['rows'] = 10
        self.fields['survey_name'].label = "Survey Name"
        self.fields['num_participants'].label = "Number of Participants"
        self.fields['org_conduct'].label = "Conducting Organization"
        self.fields['num_questions'].label = "Number of Questions"
        self.fields['doc_link'].label = "Link to Documentation"
        self.fields['source_link'].label = "Link to Source"
        self.fields['survey_questions_document'].widget.attrs['accept'] = ".csv"
        self.fields['summary'].widget.attrs.update({'class': 'form-control'})
        self.fields['survey_name'].widget.attrs.update({'class': 'form-control'})
        self.fields['num_participants'].widget.attrs.update({'class': 'form-control w-25'})
        self.fields['org_conduct'].widget.attrs.update({'class': 'form-control'})
        self.fields['num_questions'].widget.attrs.update({'class': 'form-control w-25'})
        self.fields['doc_link'].widget.attrs.update({'class': 'form-control'})
        self.fields['source_link'].widget.attrs.update({'class': 'form-control'})
        self.fields['data_link'].widget.attrs.update({'class': 'form-control'})