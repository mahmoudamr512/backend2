from typing import Dict, List, TypeVar, Generic, Optional, Any

from pydantic import BaseModel, Field

from all_types.response_dtypes import LyrInfoInCtlgSave

U = TypeVar("U")


class ReqModel(BaseModel, Generic[U]):
    message: str
    request_info: Dict
    request_body: U

class boxmapProperties(BaseModel):
    name: str
    rating: float
    address: str
    phone: str
    website: str
    business_status: str
    user_ratings_total: int


class ReqSavePrdcerLyer(BaseModel):
    prdcer_layer_name: str
    prdcer_lyr_id: str
    bknd_dataset_id: str
    points_color: str
    layer_legend: str
    layer_description: str
    user_id: str


class ReqSavePrdcerCtlg(BaseModel):
    prdcer_ctlg_name: str
    subscription_price: str
    ctlg_description: str
    total_records: int
    lyrs: List[LyrInfoInCtlgSave] = Field(..., description="list of layer objects.")
    user_id: str
    thumbnail_url: str


class ZoneLayerInfo(BaseModel):
    lyr_id: str
    property_key: str


# Request models
class ReqLocation(BaseModel):
    lat: float
    lng: float
    radius: int
    excludedTypes: list[str]
    includedTypes: list[str]
    page_token: Optional[str] = ""
    text_search: Optional[str] = ""


class ReqCatalogId(BaseModel):
    catalogue_dataset_id: str


class ReqUserId(BaseModel):
    user_id: str


class ReqPrdcerLyrMapData(BaseModel):
    prdcer_lyr_id: str
    user_id: str


class ReqFetchDataset(BaseModel):
    dataset_country: str
    dataset_city: str
    excludedTypes: list[str]
    includedTypes: list[str]
    action: Optional[str] = ""
    page_token: Optional[str] = ""
    search_type: Optional[str] = "default"
    text_search: Optional[str] = ""
    user_id: str


# class ReqApplyZoneLayers(BaseModel):
#     user_id: str
#     lyrs: List[str]
#     lyrs_as_zone: List[Dict[str, str]]


class ReqCreateUserProfile(BaseModel):
    username: str
    email: str
    password: str


class ReqFetchCtlgLyrs(BaseModel):
    prdcer_ctlg_id: str
    as_layers: bool
    user_id: str


class ReqUserLogin(BaseModel):
    email: str
    password: str


class ReqUserProfile(BaseModel):
    user_id: str


class ReqResetPassword(BaseModel):
    email: str


class ReqConfirmReset(BaseModel):
    oob_code: str
    new_password: str


class ReqChangePassword(BaseModel):
    user_id: str
    email: str
    password: str
    new_password: str

class ReqChangeEmail(BaseModel):
    user_id: str
    current_email: str
    new_email: str
    password: str

class ReqAddPaymentMethod(BaseModel):
    user_id: str
    payment_type: str  # e.g., "credit_card", "paypal", "bank_account"
    payment_details: Dict[str, Any]  # This will contain the specific details for each payment type

class ReqCostEstimate(BaseModel):
    included_categories: List[str]
    excluded_categories: List[str]
    city_name: str
    country: str

class ReqRealEstate(BaseModel):
    country_name:str
    city_name: str
    excludedTypes: list[str]
    includedTypes: list[str]
    page_token: Optional[str] = ""
    text_search: Optional[str] = ""



class ReqGradientColorBasedOnZone(ReqPrdcerLyrMapData):
    color_grid_choice:list[str]
    change_lyr_id:str
    based_on_lyr_id:str
    radius_offset: float
    color_based_on: str


## Added it for Refresh token
class ReqRefreshToken(BaseModel):
    grant_type:str
    refresh_token:str

class ReqGetPaymentMethods(BaseModel):
    user_id: str