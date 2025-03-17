from django.urls import path
from . import views

urlpatterns = [
    # Company URLs
    path('companies/', views.CompanyListView.as_view(), name='company_list'),
    path('companies/<int:pk>/', views.CompanyDetailView.as_view(), name='company_detail'),
    path('companies/create/', views.CompanyCreateView.as_view(), name='company_create'),
    path('companies/<int:pk>/update/', views.CompanyUpdateView.as_view(), name='company_update'),
    path('companies/<int:pk>/delete/', views.CompanyDeleteView.as_view(), name='company_delete'),
    # Department URLs
    path('departments/', views.DepartmentListView.as_view(), name='department_list'),
    path('departments/<int:pk>/', views.DepartmentDetailView.as_view(), name='department_detail'),
    path('departments/create/', views.DepartmentCreateView.as_view(), name='department_create'),
    path('departments/<int:pk>/update/', views.DepartmentUpdateView.as_view(), name='department_update'),
    path('departments/<int:pk>/delete/', views.DepartmentDeleteView.as_view(), name='department_delete'),
    # Position URLs
    path('positions/', views.PositionListView.as_view(), name='position_list'),
    path('positions/<int:pk>/', views.PositionDetailView.as_view(), name='position_detail'),
    path('positions/create/', views.PositionCreateView.as_view(), name='position_create'),
    path('positions/<int:pk>/update/', views.PositionUpdateView.as_view(), name='position_update'),
    path('positions/<int:pk>/delete/', views.PositionDeleteView.as_view(), name='position_delete'),
    # Employee URLs
    path('employees/', views.EmployeeListView.as_view(), name='employee_list'),
    path('employees/<int:pk>/', views.EmployeeDetailView.as_view(), name='employee_detail'),
    path('employees/create/', views.EmployeeCreateView.as_view(), name='employee_create'),
    path('employees/<int:pk>/update/', views.EmployeeUpdateView.as_view(), name='employee_update'),
    path('employees/<int:pk>/delete/', views.EmployeeDeleteView.as_view(), name='employee_delete'),
    # Team URLs
    path('teams/', views.TeamListView.as_view(), name='team_list'),
    path('teams/<int:pk>/', views.TeamDetailView.as_view(), name='team_detail'),
    path('teams/create/', views.TeamCreateView.as_view(), name='team_create'),
    path('teams/<int:pk>/update/', views.TeamUpdateView.as_view(), name='team_update'),
    path('teams/<int:pk>/delete/', views.TeamDeleteView.as_view(), name='team_delete'),
    # EmployeePositionAssignment URLs
    path(
        'employeepositionassignments/',
        views.EmployeePositionAssignmentListView.as_view(),
        name='employeepositionassignment_list',
    ),
    path(
        'employeepositionassignments/<int:pk>/',
        views.EmployeePositionAssignmentDetailView.as_view(),
        name='employeepositionassignment_detail',
    ),
    path(
        'employeepositionassignments/create/',
        views.EmployeePositionAssignmentCreateView.as_view(),
        name='employeepositionassignment_create',
    ),
    path(
        'employeepositionassignments/<int:pk>/update/',
        views.EmployeePositionAssignmentUpdateView.as_view(),
        name='employeepositionassignment_update',
    ),
    path(
        'employeepositionassignments/<int:pk>/delete/',
        views.EmployeePositionAssignmentDeleteView.as_view(),
        name='employeepositionassignment_delete',
    ),
    # TeamMembership URLs
    path('teammemberships/', views.TeamMembershipListView.as_view(), name='teammembership_list'),
    path('teammemberships/<int:pk>/', views.TeamMembershipDetailView.as_view(), name='teammembership_detail'),
    path('teammemberships/create/', views.TeamMembershipCreateView.as_view(), name='teammembership_create'),
    path('teammemberships/<int:pk>/update/', views.TeamMembershipUpdateView.as_view(), name='teammembership_update'),
    path('teammemberships/<int:pk>/delete/', views.TeamMembershipDeleteView.as_view(), name='teammembership_delete'),
    # TeamLeaderAssignment URLs
    path(
        'teamleaderassignments/', views.TeamLeaderAssignmentListView.as_view(), name='teamleaderassignment_list'
    ),
    path(
        'teamleaderassignments/<int:pk>/',
        views.TeamLeaderAssignmentDetailView.as_view(),
        name='teamleaderassignment_detail',
    ),
    path(
        'teamleaderassignments/create/',
        views.TeamLeaderAssignmentCreateView.as_view(),
        name='teamleaderassignment_create',
    ),
    path(
        'teamleaderassignments/<int:pk>/update/',
        views.TeamLeaderAssignmentUpdateView.as_view(),
        name='teamleaderassignment_update',
    ),
    path(
        'teamleaderassignments/<int:pk>/delete/',
        views.TeamLeaderAssignmentDeleteView.as_view(),
        name='teamleaderassignment_delete',
    ),
    path('dashboard/', views.dashboard, name='dashboard'),
]