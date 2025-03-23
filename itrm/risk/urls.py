from django.urls import path
from .views import (
    RiskCategoryLevel1ListView,
    RiskCategoryLevel1DetailView,
    RiskCategoryLevel1CreateView,
    RiskCategoryLevel1UpdateView,
    RiskCategoryLevel1DeleteView,
    RiskCategoryLevel2ListView,
    RiskCategoryLevel2DetailView,
    RiskCategoryLevel2CreateView,
    RiskCategoryLevel2UpdateView,
    RiskCategoryLevel2DeleteView,
    RiskListView,
    RiskDetailView,
    RiskCreateView,
    RiskUpdateView,
    RiskDeleteView,
    AssetListView,
    AssetDetailView,
    AssetCreateView,
    AssetUpdateView,
    AssetDeleteView,
    AssetCreateAjaxView,
    ControlListView,
    ControlDetailView,
    ControlCreateView,
    ControlUpdateView,
    ControlDeleteView,
    MitigationActionListView,
    MitigationActionDetailView,
    MitigationActionCreateView,
    MitigationActionUpdateView,
    MitigationActionDeleteView,
    ProgressTrackingListView,
    ProgressTrackingDetailView,
    ProgressTrackingCreateView,
    ProgressTrackingUpdateView,
    ProgressTrackingDeleteView,
    RiskDashboardView,
)

urlpatterns = [
    # RiskCategoryLevel1 URLs
    path('riskcategorylevel1/', RiskCategoryLevel1ListView.as_view(), name='riskcategorylevel1_list'),
    path('riskcategorylevel1/<int:pk>/', RiskCategoryLevel1DetailView.as_view(), name='riskcategorylevel1_detail'),
    path('riskcategorylevel1/create/', RiskCategoryLevel1CreateView.as_view(), name='riskcategorylevel1_create'),
    path('riskcategorylevel1/<int:pk>/update/', RiskCategoryLevel1UpdateView.as_view(), name='riskcategorylevel1_update'),
    path('riskcategorylevel1/<int:pk>/delete/', RiskCategoryLevel1DeleteView.as_view(), name='riskcategorylevel1_delete'),

    # RiskCategoryLevel2 URLs
    path('riskcategorylevel2/', RiskCategoryLevel2ListView.as_view(), name='riskcategorylevel2_list'),
    path('riskcategorylevel2/<int:pk>/', RiskCategoryLevel2DetailView.as_view(), name='riskcategorylevel2_detail'),
    path('riskcategorylevel2/create/', RiskCategoryLevel2CreateView.as_view(), name='riskcategorylevel2_create'),
    path('riskcategorylevel2/<int:pk>/update/', RiskCategoryLevel2UpdateView.as_view(), name='riskcategorylevel2_update'),
    path('riskcategorylevel2/<int:pk>/delete/', RiskCategoryLevel2DeleteView.as_view(), name='riskcategorylevel2_delete'),

    # Risk URLs
    path('risks/', RiskListView.as_view(), name='risk_list'),
    path('risks/<int:pk>/', RiskDetailView.as_view(), name='risk_detail'),
    path('risks/create/', RiskCreateView.as_view(), name='risk_create'),
    path('risks/<int:pk>/update/', RiskUpdateView.as_view(), name='risk_update'),
    path('risks/<int:pk>/delete/', RiskDeleteView.as_view(), name='risk_delete'),

    # Asset URLs
    path('assets/', AssetListView.as_view(), name='asset_list'),
    path('assets/<int:pk>/', AssetDetailView.as_view(), name='asset_detail'),
    path('assets/create/', AssetCreateView.as_view(), name='asset_create'),
    path('assets/<int:pk>/update/', AssetUpdateView.as_view(), name='asset_update'),
    path('assets/<int:pk>/delete/', AssetDeleteView.as_view(), name='asset_delete'),
    path('assets/create_ajax/', AssetCreateAjaxView.as_view(), name='asset_create_ajax'),

    # Control URLs
    path('controls/', ControlListView.as_view(), name='control_list'),
    path('controls/<int:pk>/', ControlDetailView.as_view(), name='control_detail'),
    path('controls/create/', ControlCreateView.as_view(), name='control_create'),
    path('controls/<int:pk>/update/', ControlUpdateView.as_view(), name='control_update'),
    path('controls/<int:pk>/delete/', ControlDeleteView.as_view(), name='control_delete'),

    # MitigationAction URLs
    path('mitigationactions/', MitigationActionListView.as_view(), name='mitigationaction_list'),
    path('mitigationactions/<int:pk>/', MitigationActionDetailView.as_view(), name='mitigationaction_detail'),
    path('mitigationactions/create/', MitigationActionCreateView.as_view(), name='mitigationaction_create'),
    path('mitigationactions/<int:pk>/update/', MitigationActionUpdateView.as_view(), name='mitigationaction_update'),
    path('mitigationactions/<int:pk>/delete/', MitigationActionDeleteView.as_view(), name='mitigationaction_delete'),

    # ProgressTracking URLs
    path('progresstracking/', ProgressTrackingListView.as_view(), name='progresstracking_list'),
    path('progresstracking/<int:pk>/', ProgressTrackingDetailView.as_view(), name='progresstracking_detail'),
    path('progresstracking/create/', ProgressTrackingCreateView.as_view(), name='progresstracking_create'),
    path('progresstracking/<int:pk>/update/', ProgressTrackingUpdateView.as_view(), name='progresstracking_update'),
    path('progresstracking/<int:pk>/delete/', ProgressTrackingDeleteView.as_view(), name='progresstracking_delete'),

    path('dashboard/', RiskDashboardView.as_view(), name='risk_dashboard'),
]