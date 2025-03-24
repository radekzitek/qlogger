from django.db import models
from org.models import Department  # Import the Department model from the org app


class RiskCategoryLevel1(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


class RiskCategoryLevel2(models.Model):
    level1 = models.ForeignKey(
        RiskCategoryLevel1, on_delete=models.CASCADE, related_name='level2_categories')
    name = models.CharField(max_length=255)
    relevant_eu_regulations = models.TextField(blank=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.level1.name} - {self.name}"


class Risk(models.Model):
    risk_id = models.CharField(max_length=50, unique=True)
    risk_name = models.CharField(max_length=255)
    risk_category = models.ForeignKey(
        RiskCategoryLevel2, on_delete=models.SET_NULL, null=True, blank=True)
    risk_description = models.TextField()
    potential_impact = models.TextField()
    likelihood_of_occurrence = models.CharField(
        max_length=20,
        choices=[
            ('Low', 'Low (Unlikely, annual likelihood < 10%)'),
            ('Medium', 'Medium (Possible, annual likelihood 10-50%)'),
            ('High', 'High (Almost Certain, annual likelihood > 50%)'),
        ],
        default='Medium',
    )
    inherent_risk_score = models.CharField(
        max_length=20,
        choices=[
            ('Low', 'Low (Immaterial or Minor)'),
            ('Medium', 'Medium (Moderate)'),
            ('High', 'High (Significant)'),
            ('Critical', 'Critical (Severe)'),
        ],
        default='Medium',
        null=True,
        blank=True
    )
    risk_owner = models.ForeignKey(Department, on_delete=models.SET_NULL,
                                   null=True, blank=True, related_name='owned_risks')  # Add this line
    date_identified = models.DateField()
    status = models.CharField(
        max_length=20,
        choices=[
            ('Open', 'Open'),
            ('Closed', 'Closed'),
            ('Mitigating', 'Mitigating'),
            ('Accepted', 'Accepted'),
        ],
        default='Open',
    )
    relevant_eu_regulations = models.TextField(blank=True)
    associated_assets = models.ManyToManyField(
        'Asset', related_name='risks', blank=True)
    associated_controls = models.ManyToManyField(
        'Control', related_name='risks', blank=True)
    associated_mitigation_actions = models.ManyToManyField(
        # Assuming you'll create a MitigationAction model
        'MitigationAction', related_name='risks', blank=True)

    def __str__(self):
        return self.risk_name


class Asset(models.Model):
    asset_id = models.CharField(max_length=50, unique=True)
    asset_name = models.CharField(max_length=255)
    asset_type = models.CharField(
        max_length=50,
        choices=[
            ('Hardware', 'Hardware'),
            ('Software', 'Software'),
            ('Data', 'Data'),
            ('Service', 'Service'),
        ],
        default='Software',
    )
    description = models.TextField()
    criticality_level = models.CharField(
        max_length=20,
        choices=[
            ('High', 'High'),
            ('Medium', 'Medium'),
            ('Low', 'Low'),
        ],
        default='Medium',
    )
    owner = models.ForeignKey(Department, on_delete=models.SET_NULL,
                              null=True, blank=True, related_name='owned_assets')  # Add this line
    location = models.CharField(max_length=255)

    def __str__(self):
        return self.asset_name


class Control(models.Model):
    control_id = models.CharField(max_length=50, unique=True)
    control_name = models.CharField(max_length=255)
    control_objective = models.TextField()
    control_description = models.TextField()
    control_type = models.CharField(
        max_length=20,
        choices=[
            ('Preventive', 'Preventive'),
            ('Detective', 'Detective'),
            ('Corrective', 'Corrective'),
        ],
        default='Preventive',
    )
    implementation_status = models.CharField(
        max_length=20,
        choices=[
            ('Implemented', 'Implemented'),
            ('Planned', 'Planned'),
            ('Not Implemented', 'Not Implemented'),
        ],
        default='Planned',
    )
    effectiveness_rating = models.CharField(
        max_length=20,
        choices=[
            ('High', 'High'),
            ('Medium', 'Medium'),
            ('Low', 'Low'),
        ],
        default='Medium',
    )
    owner = models.CharField(max_length=255)
    associated_assets = models.ManyToManyField(
        'Asset', related_name='controls', blank=True)

    def __str__(self):
        return self.control_name


class RCSA(models.Model):
    rcsa_id = models.CharField(max_length=50, unique=True)
    assessment_date = models.DateField()
    assessed_by = models.CharField(max_length=255)
    assessment_scope = models.TextField()
    risk_assessed = models.ForeignKey(Risk, on_delete=models.CASCADE)
    control_assessed = models.ForeignKey(Control, on_delete=models.CASCADE)
    inherent_risk_rating = models.CharField(
        max_length=20,
        choices=[
            ('Low', 'Low (Immaterial or Minor)'),
            ('Medium', 'Medium (Moderate)'),
            ('High', 'High (Significant)'),
            ('Critical', 'Critical (Severe)'),
        ],
        default='Medium',
    )
    design_effectiveness = models.CharField(
        max_length=20,
        choices=[
            ('Low', 'Low'),
            ('Medium', 'Medium'),
            ('High', 'High'),
        ],
        default='Medium',
    )
    operating_effectiveness = models.CharField(
        max_length=20,
        choices=[
            ('Low', 'Low'),
            ('Medium', 'Medium'),
            ('High', 'High'),
        ],
        default='Medium',
    )
    residual_risk_rating = models.CharField(
        max_length=20,
        choices=[
            ('Low', 'Low (Immaterial or Minor)'),
            ('Medium', 'Medium (Moderate)'),
            ('High', 'High (Significant)'),
            ('Critical', 'Critical (Severe)'),
        ],
        default='Medium',
    )
    risk_acceptance = models.BooleanField(default=False)
    findings_observations = models.TextField()
    recommendations = models.TextField()
    recommendation_status = models.CharField(
        max_length=20,
        choices=[
            ('Open', 'Open'),
            ('In Progress', 'In Progress'),
            ('Closed', 'Closed'),
        ],
        default='Open',
    )
    due_date_for_recommendations = models.DateField(null=True, blank=True)
    responsibility_for_recommendations = models.CharField(max_length=255)

    def __str__(self):
        return f"RCSA: {self.rcsa_id} - Risk: {self.risk_assessed.risk_name} - Control: {self.control_assessed.control_name}"


class MitigationAction(models.Model):
    mitigation_action_id = models.CharField(max_length=50, unique=True)
    risk = models.ForeignKey(
        Risk, on_delete=models.CASCADE, related_name='mitigation_actions')
    action_description = models.TextField()
    priority = models.CharField(
        max_length=20,
        choices=[
            ('High', 'High'),
            ('Medium', 'Medium'),
            ('Low', 'Low'),
        ],
        default='Medium',
    )
    assigned_to = models.CharField(max_length=255)
    target_start_date = models.DateField()
    target_end_date = models.DateField()
    status = models.CharField(
        max_length=20,
        choices=[
            ('To Do', 'To Do'),
            ('In Progress', 'In Progress'),
            ('On Hold', 'On Hold'),
            ('Completed', 'Completed'),
        ],
        default='To Do',
    )
    estimated_cost = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    actual_cost = models.DecimalField(
        max_digits=10, decimal_places=2, null=True, blank=True)
    expected_outcome = models.TextField()
    date_created = models.DateField(auto_now_add=True)
    created_by = models.CharField(max_length=255)
    date_updated = models.DateField(auto_now=True)
    updated_by = models.CharField(max_length=255)

    def __str__(self):
        return f"Mitigation Action: {self.mitigation_action_id} - Risk: {self.risk.risk_name}"


class ProgressTracking(models.Model):
    progress_tracking_id = models.CharField(max_length=50, unique=True)
    mitigation_action = models.ForeignKey(
        MitigationAction, on_delete=models.CASCADE, related_name='progress_updates')
    date_of_update = models.DateField()
    progress_update = models.TextField()
    percentage_completion = models.IntegerField(default=0)
    actual_start_date = models.DateField(null=True, blank=True)
    actual_end_date = models.DateField(null=True, blank=True)
    effectiveness_assessment = models.TextField(blank=True)
    updated_residual_risk = models.CharField(
        max_length=20,
        choices=[
            ('Low', 'Low (Immaterial or Minor)'),
            ('Medium', 'Medium (Moderate)'),
            ('High', 'High (Significant)'),
            ('Critical', 'Critical (Severe)'),
        ],
        default='Medium',
    )
    updated_by = models.CharField(max_length=255)

    def __str__(self):
        return f"Progress Update: {self.progress_tracking_id} - Mitigation Action: {self.mitigation_action.mitigation_action_id}"
