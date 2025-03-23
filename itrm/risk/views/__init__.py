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
    ControlCreateAjaxView,
    MitigationActionCreateAjaxView,
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
)
from .mitigationaction_views import (
    MitigationActionListView,
    MitigationActionDetailView,
    MitigationActionCreateView,
    MitigationActionUpdateView,
    MitigationActionDeleteView,
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