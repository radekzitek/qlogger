from .riskcategorylevel1_views import (
    RiskCategoryLevel1ListView,
    RiskCategoryLevel1DetailView,
    RiskCategoryLevel1CreateView,
    RiskCategoryLevel1UpdateView,
    RiskCategoryLevel1DeleteView,
)
from .riskcategorylevel2_views import (
    RiskCategoryLevel2ListView,
    RiskCategoryLevel2DetailView,
    RiskCategoryLevel2CreateView,
    RiskCategoryLevel2UpdateView,
    RiskCategoryLevel2DeleteView,
)
from .risk_views import (
    RiskListView,
    RiskDetailView,
    RiskCreateView,
    RiskUpdateView,
    RiskDeleteView,
)
from .asset_views import (
    AssetListView,
    AssetDetailView,
    AssetCreateView,
    AssetUpdateView,
    AssetDeleteView,
    AssetCreateAjaxView,
)
from .control_views import (
    ControlListView,
    ControlDetailView,
    ControlCreateView,
    ControlUpdateView,
    ControlDeleteView,
    ControlCreateAjaxView,
)
from .mitigationaction_views import (
    MitigationActionListView,
    MitigationActionDetailView,
    MitigationActionCreateView,
    MitigationActionUpdateView,
    MitigationActionDeleteView,
    MitigationActionCreateAjaxView,
)
from .progresstracking_views import (
    ProgressTrackingListView,
    ProgressTrackingDetailView,
    ProgressTrackingCreateView,
    ProgressTrackingUpdateView,
    ProgressTrackingDeleteView,
)
from .dashboard_views import (
    RiskDashboardView,
)
from .rcsa_views import (
    RCSAListView,
    RCSADetailView,
    RCSACreateView,
    RCSAUpdateView,
    RCSADeleteView,
)
