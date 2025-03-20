from django.contrib import admin
from .models import Company, Department, Position, Employee, Team, EmployeePositionAssignment, TeamMembership, TeamLeaderAssignment

# Register your models here.
admin.site.register(Company)
admin.site.register(Department)
admin.site.register(Position)
admin.site.register(Employee)
admin.site.register(Team)
admin.site.register(EmployeePositionAssignment)
admin.site.register(TeamMembership)
admin.site.register(TeamLeaderAssignment)