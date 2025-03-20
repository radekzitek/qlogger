from django.db import models


class BaseModel(models.Model):
    """
    Abstract base model to include common fields for auditing and status tracking.
    """
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True


class Company(BaseModel):
    """
    Represents a company.
    """
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    top_level_department = models.ForeignKey(
        'Department', on_delete=models.SET_NULL, null=True, blank=True, related_name='top_level_companies')

    def __str__(self):
        return self.name


class Department(BaseModel):
    """
    Represents a department within a company.
    """
    company = models.ForeignKey(
        'Company', on_delete=models.CASCADE, related_name='departments')
    name = models.CharField(max_length=255)
    parent_department = models.ForeignKey(
        'self', on_delete=models.SET_NULL, null=True, blank=True, related_name='sub_departments')
    manager_position = models.ForeignKey(
        'Position', on_delete=models.SET_NULL, null=True, blank=True, related_name='managed_departments')

    def __str__(self):
        return self.name


class Position(BaseModel):
    """
    Represents a position within a department.
    """
    department = models.ForeignKey(
        'Department', on_delete=models.CASCADE, related_name='positions')
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class Employee(BaseModel):
    """
    Represents an employee within the company.
    """
    company = models.ForeignKey(
        'Company', on_delete=models.CASCADE, related_name='employees')
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    user_name = models.CharField(max_length=64)
    password = models.CharField(max_length=128)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    positions = models.ManyToManyField(
        'Position', through='EmployeePositionAssignment', related_name='employees')
    teams = models.ManyToManyField(
        'Team', through='TeamMembership', related_name='members')

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


class Team(BaseModel):
    """
    Represents a team within the company.
    """
    company = models.ForeignKey(
        'Company', on_delete=models.CASCADE, related_name='teams')
    name = models.CharField(max_length=255)
    leaders = models.ManyToManyField(
        'Employee', through='TeamLeaderAssignment', related_name='led_teams')

    def __str__(self):
        return self.name


class EmployeePositionAssignment(BaseModel):
    """
    Through model for the many-to-many relationship between Employee and Position.
    Stores the assignment date.
    """
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE)
    position = models.ForeignKey('Position', on_delete=models.CASCADE)
    assigned_date = models.DateField()

    class Meta:
        unique_together = ('employee', 'position')


class TeamMembership(BaseModel):
    """
    Through model for the many-to-many relationship between Employee and Team.
    Stores the date when an employee joined the team.
    """
    employee = models.ForeignKey('Employee', on_delete=models.CASCADE)
    team = models.ForeignKey('Team', on_delete=models.CASCADE)
    joined_date = models.DateField()

    class Meta:
        unique_together = ('employee', 'team')


class TeamLeaderAssignment(BaseModel):
    """
    Through model for the many-to-many relationship between Team and Employee (leader).
    Stores the date when an employee was assigned as a leader to the team.
    """
    team = models.ForeignKey('Team', on_delete=models.CASCADE)
    leader = models.ForeignKey('Employee', on_delete=models.CASCADE)
    assigned_date = models.DateField()

    class Meta:
        unique_together = ('team', 'leader')
