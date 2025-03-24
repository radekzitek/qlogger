from django import forms
from .models import Risk, Asset, Control, MitigationAction, ProgressTracking, RCSA
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
        fields = ['asset_id', 'asset_name', 'asset_type', 'description', 'criticality_level', 'owner', 'location'] # Removed associated_controls
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

class AssetModalForm(forms.ModelForm):
    class Meta:
        model = Asset
        fields = ['asset_name', 'asset_type', 'description', 'criticality_level', 'owner', 'location'] # Excluded asset_id and associated_controls
        # No widgets needed here, as we want the default widgets

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
            self.fields['asset_id'] = forms.CharField(initial=f'ASST{new_id:03}', disabled=True, required=False)

class ControlForm(forms.ModelForm):
    class Meta:
        model = Control
        fields = ['control_id', 'control_name', 'control_objective', 'control_description', 'control_type',
                  'implementation_status', 'effectiveness_rating', 'owner'] # Removed associated_assets
        widgets = {
            'control_id': forms.TextInput(attrs={'readonly': 'readonly'}),  # Make control_id readonly
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Generate control_id
        if not self.instance.pk:
            last_control = Control.objects.order_by('-control_id').first()
            if last_control:
                last_id = int(last_control.control_id[4:])  # Extract number from 'CTRLnnn'
                new_id = last_id + 1
            else:
                new_id = 1
            self.fields['control_id'].initial = f'CTRL{new_id:03}'
            self.fields['control_id'].widget.attrs['readonly'] = True  # Make it readonly

class MitigationActionForm(forms.ModelForm):
    class Meta:
        model = MitigationAction
        fields = ['mitigation_action_id', 'risk', 'action_description', 'priority', 'assigned_to', 'target_start_date',
                  'target_end_date', 'status', 'estimated_cost', 'actual_cost', 'expected_outcome']
        widgets = {
            'target_start_date': forms.DateInput(attrs={'type': 'date'}),
            'target_end_date': forms.DateInput(attrs={'type': 'date'}),
            'mitigation_action_id': forms.TextInput(attrs={'readonly': 'readonly'}),  # Make mitigation_action_id readonly
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Generate mitigation_action_id
        if not self.instance.pk:
            last_mitigation_action = MitigationAction.objects.order_by('-mitigation_action_id').first()
            if last_mitigation_action:
                last_id = int(last_mitigation_action.mitigation_action_id[3:])  # Extract number from 'MITnnn'
                new_id = last_id + 1
            else:
                new_id = 1
            self.fields['mitigation_action_id'].initial = f'MIT{new_id:03}'
            self.fields['mitigation_action_id'].widget.attrs['readonly'] = True  # Make it readonly

class ProgressTrackingForm(forms.ModelForm):
    class Meta:
        model = ProgressTracking
        fields = ['progress_tracking_id', 'mitigation_action', 'date_of_update', 'progress_update', 'percentage_completion',
                  'actual_start_date', 'actual_end_date', 'effectiveness_assessment', 'updated_residual_risk']
        widgets = {
            'date_of_update': forms.DateInput(attrs={'type': 'date'}),
            'actual_start_date': forms.DateInput(attrs={'type': 'date'}),
            'actual_end_date': forms.DateInput(attrs={'type': 'date'}),
            'progress_tracking_id': forms.TextInput(attrs={'readonly': 'readonly'}),  # Make progress_tracking_id readonly
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Generate progress_tracking_id
        if not self.instance.pk:
            last_progress_tracking = ProgressTracking.objects.order_by('-progress_tracking_id').first()
            if last_progress_tracking:
                last_id = int(last_progress_tracking.progress_tracking_id[4:])  # Extract number from 'PROGnnn'
                new_id = last_id + 1
            else:
                new_id = 1
            self.fields['progress_tracking_id'].initial = f'PROG{new_id:03}'
            self.fields['progress_tracking_id'].widget.attrs['readonly'] = True  # Make it readonly

class RCSAForm(forms.ModelForm):
    class Meta:
        model = RCSA
        fields = ['rcsa_id', 'assessment_date', 'assessed_by', 'assessment_scope', 'risk_assessed',
                  'control_assessed', 'inherent_risk_rating', 'design_effectiveness',
                  'operating_effectiveness', 'residual_risk_rating', 'risk_acceptance',
                  'findings_observations', 'recommendations', 'recommendation_status',
                  'due_date_for_recommendations', 'responsibility_for_recommendations']
        widgets = {
            'assessment_date': forms.DateInput(attrs={'type': 'date'}),
            'due_date_for_recommendations': forms.DateInput(attrs={'type': 'date'}),
            'rcsa_id': forms.TextInput(attrs={'readonly': 'readonly'}),  # Make rcsa_id readonly
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Generate rcsa_id
        if not self.instance.pk:
            last_rcsa = RCSA.objects.order_by('-rcsa_id').first()
            if last_rcsa:
                last_id = int(last_rcsa.rcsa_id[4:])  # Extract number from 'RCSA001'
                new_id = last_id + 1
            else:
                new_id = 1
            self.fields['rcsa_id'].initial = f'RCSA{new_id:03}'
            self.fields['rcsa_id'].widget.attrs['readonly'] = True  # Make it readonly