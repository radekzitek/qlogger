from django import forms
from .models import Risk, Asset, Control, MitigationAction
from org.models import Department  # Import Department model
import datetime

class RiskForm(forms.ModelForm):
    inherent_risk_score = forms.ChoiceField(
        choices=[(i, str(i)) for i in range(6)],  # 0 to 5
        label="Inherent Risk Score",
        required=False,  # Or True, depending on your requirements
    )

    class Meta:
        model = Risk
        fields = ['risk_id', 'risk_name', 'risk_category', 'risk_description', 'potential_impact', 'likelihood_of_occurrence',
                  'inherent_risk_score', 'risk_owner', 'date_identified', 'status', 'relevant_eu_regulations', 'associated_controls', 'associated_mitigation_actions'] # Removed associated_assets
        widgets = {
            'date_identified': forms.DateInput(attrs={'type': 'date'}),
            'risk_id': forms.TextInput(attrs={'readonly': 'readonly'}),  # Make risk_id readonly
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set initial value for date_identified to today's date if creating a new risk
        if not self.instance.pk:
            self.fields['date_identified'].initial = datetime.date.today()
            # Generate risk_id
            last_risk = Risk.objects.order_by('-risk_id').first()
            if last_risk:
                last_id = int(last_risk.risk_id[4:])  # Extract number from 'RISKnnn'
                new_id = last_id + 1
            else:
                new_id = 1
            self.fields['risk_id'].initial = f'RISK{new_id:03}'
            self.fields['risk_id'].widget.attrs['readonly'] = True  # Make it readonly

    def clean_inherent_risk_score(self):
        score = self.cleaned_data['inherent_risk_score']
        if score == '':
            return None  # Or a default value if appropriate
        return int(score)

class AssetForm(forms.ModelForm):
    class Meta:
        model = Asset
        fields = ['asset_id', 'asset_name', 'asset_type', 'description', 'criticality_level', 'owner', 'location', 'associated_risks', 'associated_controls']
        widgets = {
            'asset_id': forms.TextInput(attrs={'readonly': 'readonly'}),  # Make asset_id readonly
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Generate asset_id
        if not self.instance.pk:
            last_asset = Asset.objects.order_by('-asset_id').first()
            if last_asset:
                last_id = int(last_asset.asset_id[4:])  # Extract number from 'ASSTnnn'
                new_id = last_id + 1
            else:
                new_id = 1
            self.fields['asset_id'].initial = f'ASST{new_id:03}'
            self.fields['asset_id'].widget.attrs['readonly'] = True  # Make it readonly

class AssetModalForm(forms.Form):
    asset_id = forms.CharField(disabled=True, required=False, label="Asset ID")
    asset_name = forms.CharField(max_length=255, label="Asset Name")
    asset_type = forms.CharField(max_length=255, label="Asset Type")
    description = forms.CharField(widget=forms.Textarea, required=False, label="Description")
    criticality_level = forms.CharField(max_length=255, label="Criticality Level")
    owner = forms.ModelChoiceField(queryset=Department.objects.all(), label="Owner")
    location = forms.CharField(max_length=255, required=False, label="Location")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Generate asset_id
        if not 'instance' in kwargs or not kwargs['instance']:
            last_asset = Asset.objects.order_by('-asset_id').first()
            if last_asset:
                last_id = int(last_asset.asset_id[4:])  # Extract number from 'ASSTnnn'
                new_id = last_id + 1
            else:
                new_id = 1
            self.fields['asset_id'].initial = f'ASST{new_id:03}'

    def save(self):
        asset = Asset(
            asset_id=self.fields['asset_id'].initial,
            asset_name=self.cleaned_data['asset_name'],
            asset_type=self.cleaned_data['asset_type'],
            description=self.cleaned_data['description'],
            criticality_level=self.cleaned_data['criticality_level'],
            owner=self.cleaned_data['owner'],
            location=self.cleaned_data['location'],
        )
        asset.save()
        return asset