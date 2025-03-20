from django.urls import path
from . import views

urlpatterns = [
    # RiskCategoryLevel1 URLs
    path('riskcategorylevel1/', views.RiskCategoryLevel1ListView.as_view(), name='riskcategorylevel1_list'),
    path('riskcategorylevel1/<int:pk>/', views.RiskCategoryLevel1DetailView.as_view(), name='riskcategorylevel1_detail'),
    path('riskcategorylevel1/create/', views.RiskCategoryLevel1CreateView.as_view(), name='riskcategorylevel1_create'),
    path('riskcategorylevel1/<int:pk>/update/', views.RiskCategoryLevel1UpdateView.as_view(), name='riskcategorylevel1_update'),
    path('riskcategorylevel1/<int:pk>/delete/', views.RiskCategoryLevel1DeleteView.as_view(), name='riskcategorylevel1_delete'),

    # RiskCategoryLevel2 URLs
    path('riskcategorylevel2/', views.RiskCategoryLevel2ListView.as_view(), name='riskcategorylevel2_list'),
    path('riskcategorylevel2/<int:pk>/', views.RiskCategoryLevel2DetailView.as_view(), name='riskcategorylevel2_detail'),
    path('riskcategorylevel2/create/', views.RiskCategoryLevel2CreateView.as_view(), name='riskcategorylevel2_create'),
    path('riskcategorylevel2/<int:pk>/update/', views.RiskCategoryLevel2UpdateView.as_view(), name='riskcategorylevel2_update'),
    path('riskcategorylevel2/<int:pk>/delete/', views.RiskCategoryLevel2DeleteView.as_view(), name='riskcategorylevel2_delete'),

    # Risk URLs
    path('risks/', views.RiskListView.as_view(), name='risk_list'),
    path('risks/<int:pk>/', views.RiskDetailView.as_view(), name='risk_detail'),
    path('risks/create/', views.RiskCreateView.as_view(), name='risk_create'),
    path('risks/<int:pk>/update/', views.RiskUpdateView.as_view(), name='risk_update'),
    path('risks/<int:pk>/delete/', views.RiskDeleteView.as_view(), name='risk_delete'),

    # Asset URLs
    path('assets/', views.AssetListView.as_view(), name='asset_list'),
    path('assets/<int:pk>/', views.AssetDetailView.as_view(), name='asset_detail'),
    path('assets/create/', views.AssetCreateView.as_view(), name='asset_create'),
    path('assets/<int:pk>/update/', views.AssetUpdateView.as_view(), name='asset_update'),
    path('assets/<int:pk>/delete/', views.AssetDeleteView.as_view(), name='asset_delete'),

    # Control URLs
    path('controls/', views.ControlListView.as_view(), name='control_list'),
    path('controls/<int:pk>/', views.ControlDetailView.as_view(), name='control_detail'),
    path('controls/create/', views.ControlCreateView.as_view(), name='control_create'),
    path('controls/<int:pk>/update/', views.ControlUpdateView.as_view(), name='control_update'),
    path('controls/<int:pk>/delete/', views.ControlDeleteView.as_view(), name='control_delete'),

    # MitigationAction URLs
    path('mitigationactions/', views.MitigationActionListView.as_view(), name='mitigationaction_list'),
    path('mitigationactions/<int:pk>/', views.MitigationActionDetailView.as_view(), name='mitigationaction_detail'),
    path('mitigationactions/create/', views.MitigationActionCreateView.as_view(), name='mitigationaction_create'),
    path('mitigationactions/<int:pk>/update/', views.MitigationActionUpdateView.as_view(), name='mitigationaction_update'),
    path('mitigationactions/<int:pk>/delete/', views.MitigationActionDeleteView.as_view(), name='mitigationaction_delete'),

    # ProgressTracking URLs
    path('progresstracking/', views.ProgressTrackingListView.as_view(), name='progresstracking_list'),
    path('progresstracking/<int:pk>/', views.ProgressTrackingDetailView.as_view(), name='progresstracking_detail'),
    path('progresstracking/create/', views.ProgressTrackingCreateView.as_view(), name='progresstracking_create'),
    path('progresstracking/<int:pk>/update/', views.ProgressTrackingUpdateView.as_view(), name='progresstracking_update'),
    path('progresstracking/<int:pk>/delete/', views.ProgressTrackingDeleteView.as_view(), name='progresstracking_delete'),

    path('dashboard/', views.RiskDashboardView.as_view(), name='risk_dashboard'),
]