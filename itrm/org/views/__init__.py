from .company_views import (
    CompanyListView,
    CompanyDetailView,
    CompanyCreateView,
    CompanyUpdateView,
    CompanyDeleteView,
)
from .department_views import (
    DepartmentListView,
    DepartmentDetailView,
    DepartmentCreateView,
    DepartmentUpdateView,
    DepartmentDeleteView,
)  
from .position_views import (
    PositionListView,
    PositionDetailView,
    PositionCreateView,
    PositionUpdateView,
    PositionDeleteView,
)
from .employee_views import (
    EmployeeListView,
    EmployeeDetailView,
    EmployeeCreateView,
    EmployeeCreateAndAssignView,
    EmployeeUpdateView,
    EmployeeDeleteView,
)
from .team_views import (
    TeamListView,
    TeamDetailView,
    TeamCreateView,
    TeamUpdateView,
    TeamDeleteView,
)
from .employeepositionassignment_views import (
    EmployeePositionAssignmentListView,
    EmployeePositionAssignmentDetailView,
    EmployeePositionAssignmentCreateView,
    EmployeePositionAssignmentUpdateView,
    EmployeePositionAssignmentDeleteView,
)
from .teammembership_views import (
    TeamMembershipListView,
    TeamMembershipDetailView,
    TeamMembershipCreateView,
    TeamMembershipUpdateView,
    TeamMembershipDeleteView,
)
from .teamleaderassignment_views import (
    TeamLeaderAssignmentListView,
    TeamLeaderAssignmentDetailView,
    TeamLeaderAssignmentCreateView,
    TeamLeaderAssignmentUpdateView,
    TeamLeaderAssignmentDeleteView,
)
from .views import (
    dashboard,
    organization_view,
)