from django import forms

class ExcelFileForm(forms.Form):
    excel_file = forms.FileField(label='Select an Excel file')
