from django import forms
from .models import Risk, Asset, Control, MitigationAction, ProgressTracking, RCSA, Tag
from org.models import Department  # Import Department model
import datetime
from org.models import Position  # Import the Position model


class RiskForm(forms.ModelForm):
    cdtags = forms.CharField(
        max_length=255,
        required=False,
        help_text="Enter tags separated by commas.",
        label="Tags",
    )

    class Meta:
        model = Risk
        fields = ['risk_id', 'risk_name', 'risk_category', 'risk_description', 'potential_impact', 'likelihood_of_occurrence',
                  'inherent_risk_score', 'risk_owner', 'date_identified', 'status', 'relevant_eu_regulations', 'associated_controls', 'associated_mitigation_actions', 'cdtags']
        widgets = {
            'date_identified': forms.DateInput(attrs={'type': 'date'}),
            # Make risk_id readonly
            'risk_id': forms.TextInput(attrs={'readonly': 'readonly'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Set initial value for date_identified to today's date if creating a new risk
        if not self.instance.pk:
            self.fields['date_identified'].initial = datetime.date.today()
            # Generate risk_id
            last_risk = Risk.objects.order_by('-risk_id').first()
            if last_risk:
                # Extract number from 'RISKnnn'
                last_id = int(last_risk.risk_id[4:])
                new_id = last_id + 1
            else:
                new_id = 1
            self.fields['risk_id'].initial = f'RISK{new_id:03}'
            # Make it readonly
            self.fields['risk_id'].widget.attrs['readonly'] = True
        # Populate the cdtags field with comma-separated tag names
        if self.instance.pk:
            self.fields['cdtags'].initial = ", ".join(
                [tag.name for tag in self.instance.tags.all()])

    def clean_cdtags(self):
        """
        Convert the comma-delimited string of tags into a list of Tag objects.
        """
        tag_string = self.cleaned_data['cdtags']
        tag_names = [tag.strip()
                     for tag in tag_string.split(',') if tag.strip()]
        tags = []
        for tag_name in tag_names:
            tag, created = Tag.objects.get_or_create(name=tag_name)
            tags.append(tag)
        return tags

    def save(self, commit=True):
        """
        Save the Risk instance and associate the tags.
        """
        risk = super().save(commit=False)
        if commit:
            risk.save()
        # Save tags after the risk is saved
        if hasattr(self, 'cleaned_data') and 'cdtags' in self.cleaned_data:
            risk.tags.set(self.cleaned_data['cdtags'])
        return risk


class AssetForm(forms.ModelForm):
    class Meta:
        model = Asset
        fields = ['asset_id', 'asset_name', 'asset_type', 'description',
                  'criticality_level', 'owner', 'location']  # Removed associated_controls
        widgets = {
            # Make asset_id readonly
            'asset_id': forms.TextInput(attrs={'readonly': 'readonly'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Generate asset_id
        if not self.instance.pk:
            last_asset = Asset.objects.order_by('-asset_id').first()
            if last_asset:
                # Extract number from 'ASSTnnn'
                last_id = int(last_asset.asset_id[4:])
                new_id = last_id + 1
            else:
                new_id = 1
            self.fields['asset_id'].initial = f'ASST{new_id:03}'
            # Make it readonly
            self.fields['asset_id'].widget.attrs['readonly'] = True


class AssetModalForm(forms.ModelForm):
    asset_id = forms.CharField(
        max_length=50,
        required=False,
        widget=forms.TextInput(attrs={'readonly': 'readonly'}),
        label="Asset ID"
    )

    class Meta:
        model = Asset
        fields = ['asset_id', 'asset_name', 'asset_type', 'description', 'criticality_level', 'owner', 'location']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Generate asset_id if creating a new asset
        if not self.instance.pk:
            last_asset = Asset.objects.order_by('-asset_id').first()
            if last_asset:
                last_id = int(last_asset.asset_id[4:])  # Extract number from 'ASSTnnn'
                new_id = last_id + 1
            else:
                new_id = 1
            self.fields['asset_id'].initial = f'ASST{new_id:03}'

    def save(self, commit=True):
        # Ensure the asset_id is set on the instance
        self.instance.asset_id = self.cleaned_data['asset_id']
        return super().save(commit=commit)


class ControlForm(forms.ModelForm):
    owner = forms.ModelChoiceField(
        queryset=Department.objects.all(),
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Owner"
    )

    class Meta:
        model = Control
        fields = ['control_id', 'control_name', 'control_objective', 'control_description', 'control_type',
                  'implementation_status', 'effectiveness_rating', 'owner']  # Removed associated_assets
        widgets = {
            # Make control_id readonly
            'control_id': forms.TextInput(attrs={'readonly': 'readonly'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Generate control_id
        if not self.instance.pk:
            last_control = Control.objects.order_by('-control_id').first()
            if last_control:
                # Extract number from 'CTRLnnn'
                last_id = int(last_control.control_id[4:])
                new_id = last_id + 1
            else:
                new_id = 1
            self.fields['control_id'].initial = f'CTRL{new_id:03}'
            # Make it readonly
            self.fields['control_id'].widget.attrs['readonly'] = True


class MitigationActionForm(forms.ModelForm):
    class Meta:
        model = MitigationAction
        fields = [
            'mitigation_action_id', 'risk', 'action_description', 'priority',
            'assigned_to', 'target_start_date', 'target_end_date', 'status',
            'estimated_cost', 'actual_cost', 'expected_outcome'
        ]
        widgets = {
            'target_start_date': forms.DateInput(attrs={'type': 'date'}),
            'target_end_date': forms.DateInput(attrs={'type': 'date'}),
            'mitigation_action_id': forms.TextInput(attrs={'readonly': 'readonly'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Generate mitigation_action_id
        if not self.instance.pk:
            last_mitigation_action = MitigationAction.objects.order_by(
                '-mitigation_action_id').first()
            if last_mitigation_action:
                # Extract number from 'MITnnn'
                last_id = int(last_mitigation_action.mitigation_action_id[3:])
                new_id = last_id + 1
            else:
                new_id = 1
            self.fields['mitigation_action_id'].initial = f'MIT{new_id:03}'
            # Make it readonly
            self.fields['mitigation_action_id'].widget.attrs['readonly'] = True


class MitigatingActionForm(forms.ModelForm):
    assigned_to = forms.ModelChoiceField(
        queryset=Position.objects.all(),
        required=False,
        widget=forms.Select(attrs={'class': 'form-control'}),
        label="Assigned To"
    )

    class Meta:
        model = MitigationAction
        fields = ['action_description', 'target_end_date', 'status', 'assigned_to']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Additional initialization logic if needed


class ProgressTrackingForm(forms.ModelForm):
    class Meta:
        model = ProgressTracking
        fields = ['progress_tracking_id', 'mitigation_action', 'date_of_update', 'progress_update', 'percentage_completion',
                  'actual_start_date', 'actual_end_date', 'effectiveness_assessment', 'updated_residual_risk']
        widgets = {
            'date_of_update': forms.DateInput(attrs={'type': 'date'}),
            'actual_start_date': forms.DateInput(attrs={'type': 'date'}),
            'actual_end_date': forms.DateInput(attrs={'type': 'date'}),
            # Make progress_tracking_id readonly
            'progress_tracking_id': forms.TextInput(attrs={'readonly': 'readonly'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Generate progress_tracking_id
        if not self.instance.pk:
            last_progress_tracking = ProgressTracking.objects.order_by(
                '-progress_tracking_id').first()
            if last_progress_tracking:
                # Extract number from 'PROGnnn'
                last_id = int(last_progress_tracking.progress_tracking_id[4:])
                new_id = last_id + 1
            else:
                new_id = 1
            self.fields['progress_tracking_id'].initial = f'PROG{new_id:03}'
            # Make it readonly
            self.fields['progress_tracking_id'].widget.attrs['readonly'] = True


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
            # Make rcsa_id readonly
            'rcsa_id': forms.TextInput(attrs={'readonly': 'readonly'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Generate rcsa_id
        if not self.instance.pk:
            last_rcsa = RCSA.objects.order_by('-rcsa_id').first()
            if last_rcsa:
                # Extract number from 'RCSA001'
                last_id = int(last_rcsa.rcsa_id[4:])
                new_id = last_id + 1
            else:
                new_id = 1
            self.fields['rcsa_id'].initial = f'RCSA{new_id:03}'
            # Make it readonly
            self.fields['rcsa_id'].widget.attrs['readonly'] = True
