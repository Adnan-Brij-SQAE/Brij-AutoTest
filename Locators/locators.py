# Login Page Locators
USERNAME_INPUT = { '#float-input'}
PASSWORD_INPUT = {'#float-input1'}
USERNAME_SIGNIN = {"//span[@class='p-button-label']"}
LOGIN_BUTTON = {"//span[normalize-space()='Sign In']"}
analytics_general_dashboard = {"//h1[normalize-space()='Analytics > General']"}
toast_message = {"css selector" : "//div[contains(@class, 'toast-message-class')]"}

# Dashboard Page Locators

SCANS_CLICKS = {"//*[@id='mainContent']/div[2]/div/app-dashboard/div/div[1]/div[3]/div/app-analytics-card[1]/div[1]/div[1]"}
REGISTRATIONS = {"//*[@id='mainContent']/div[2]/div/app-dashboard/div/div[1]/div[3]/div/app-analytics-card[2]/div[1]/div[1]"}
ENGAGEMENTS = {"//*[@id='mainContent']/div[2]/div/app-dashboard/div/div[1]/div[3]/div/app-analytics-card[3]/div[1]/div[1]"}
WEBSITE_VISITS = {"//*[@id='mainContent']/div[2]/div/app-dashboard/div/div[1]/div[3]/div/app-analytics-card[4]/div[1]/div[1]"}
REVENUE = {"//*[@id='mainContent']/div[2]/div/app-dashboard/div/div[1]/div[3]/div/app-analytics-card[5]/div[1]/div[1]"}
DATE_RANGE = { "//input[@placeholder='Select Custom Date']"}
DATE_RANGE_TODAY = { "//button[normalize-space()='Today']"}
DATE_RANGE_YESTERDAY = { "//button[normalize-space()='Yesterday']"}
DATE_RANGE_LAST7 = { "//button[normalize-space()='Last 7 Days']"}
DATE_RANGE_LAST30 = { "//button[normalize-space()='Last 30 Days']"}
DATE_RANGE_THIS_MONTH = { "//button[normalize-space()='This Month']"}
DATE_RANGE_LAST_MONTH = { "//button[normalize-space()='Last Month']"}
EXPORT_BUTTON = { "//button[normalize-space()='Export Selection']"}
TODAY_FILTER = {"//div[normalize-space()='Day']"}
THIS_WEEK_FILTER = {"//div[normalize-space()='Week']"}
THIS_MONTH_FILTER = {"//div[normalize-space()='Month']"}
THIS_YEAR_FILTER = {"//div[normalize-space()='Year']"}
ALL_TIME_FILTER = {"//div[@class='filter-box mr-0']"}
FILTERED_RESULTS = {"//div[@class='filter-box mr-0 active-filter']"}
NOTIFICATION_ICON = {".notification"}
TEST_RESULT_NOTIFICATION = {"xpath":"//div[@class='notification']"}
NOTIFICATION_ICON_2 = {"xpath":"//div[@class='notification notification-hover']"}
LOGOUT_BUTTON = "//img[@alt='logout']"
SCANS_CLICKS_EYE = {"//body/app-root/app-brand-main[@class='ng-star-inserted']/div[@class='adminDashboardContainerWrapper']/div[@id='adminDashboardContainer']/div[@id='mainContent']/div/div[@class='ng-star-inserted']/app-dashboard[@class='ng-star-inserted']/div[@class='overview-container overflow']/div[@class='type-container']/div[1]/div[2]"}
REGISTRATIONS_EYE = {"//img[@alt='//body/app-root/app-brand-main[@class='ng-star-inserted']/div[@class='adminDashboardContainerWrapper']/div[@id='adminDashboardContainer']/div[@id='mainContent']/div/div[@class='ng-star-inserted']/app-dashboard[@class='ng-star-inserted']/div[@class='overview-container overflow']/div[@class='type-container']/div[1]/div[2]"}
ENGAGEMENTS_EYE = {"//body/app-root/app-brand-main[@class='ng-star-inserted']/div[@class='adminDashboardContainerWrapper']/div[@id='adminDashboardContainer']/div[@id='mainContent']/div/div[@class='ng-star-inserted']/app-dashboard[@class='ng-star-inserted']/div[@class='overview-container overflow']/div[@class='type-container']/div[1]/div[2]"}
WEBSITE_VISITS_EYE = {"//body/app-root/app-brand-main[@class='ng-star-inserted']/div[@class='adminDashboardContainerWrapper']/div[@id='adminDashboardContainer']/div[@id='mainContent']/div/div[@class='ng-star-inserted']/app-dashboard[@class='ng-star-inserted']/div[@class='overview-container overflow']/div[@class='type-container']/div[1]/div[2]"}
REVENUE_EYE = {"//body/app-root/app-brand-main[@class='ng-star-inserted']/div[@class='adminDashboardContainerWrapper']/div[@id='adminDashboardContainer']/div[@id='mainContent']/div/div[@class='ng-star-inserted']/app-dashboard[@class='ng-star-inserted']/div[@class='overview-container overflow']/div[@class='type-container']/div[5]/div[1]"}
ANALYTICS_GENERAL_EXPORT= {"//*[@id='mainContent']/div[2]/div/app-dashboard/div/div[1]/div[1]/div[2]/app-table-overlay/p-overlaypanel/div/div/div[2]/span"}
ANALYTICS_GENERAL_EXPORT_3DOT= {"//span[@class='dots-menu']"}
ANALYTICS_START_DATE = {"//span[@class='ng-tns-c3241611875-7 p-datepicker p-component p-inputwrapper p-focus']//input[@id='templatedisplay']"}
ANALYTICS_END_DATE = {"//span[@class='ng-tns-c3241611875-8 p-datepicker p-component p-inputwrapper p-inputwrapper-filled p-focus']//input[@id='templatedisplay']"}


# Analytics>rebate  Elements
analytics_rebate_dashboard = {"//h1[normalize-space()='Analytics > Rebates']"}
LEFT_PANEL = {"xpath" : "//span[normalize-space()='Analytics']"}
REBATE_OPTION = {"xpath" : "//*[@id='adminDashboardContainer']/nav/ul[1]/li[2]/ul/li[2]"}
EXPERIENCE_FILTER = { "//div[contains(text(),'All Experiences')]"}
DROPDOWN_ALL_EXPERIENCE = { "//label[normalize-space()='All Experiences']"}
DROPDOWN_SELECT_ALL = { "//label[normalize-space()='Select All']"}
EXPERIENCE_FILTER_SEARCH = {"xpath":"//input[@placeholder='Search...']"}
EXPERIENCE_FILTER_SEARCH_OPTION= {"xpath":"//li[@id='pn_id_9_1']//div[@class='flex w-full items-center ng-star-inserted']"}
EXPERIENCE_FILTER_SEARCH_OPTION2 = {"xpath":"//div[@title='Test']"}
EXPERIENCE_FILTER_SEARCH_CROSS = {"xpath":"//span[@class='p-button-icon pi pi-times']"}
VARIANT_FILTER_SEARCH_CROSS = {"xpath":"//span[@class='p-button-icon pi pi-times']"}
VARIANT_LIST_CHECKBOX1 = {"xpath":"//p-checkbox[@class='ng-pristine ng-valid ng-touched']//div[@class='p-checkbox-box']"}
VARIANT_FILTER_SEARCH = {"xpath":"//input[@placeholder='Search...']"}
DROPDOWN_ALL_VARIANT = { "//label[normalize-space()='All Variants']"}
VARIANT_FILTER_SEARCH_OPTION= {"xpath":"//li[@id='pn_id_12_1']//div[@class='flex w-full items-center ng-star-inserted']"}
VARIANT_FILTER_SEARCH_OPTION2= {"xpath":"//div[contains(text(),'test')]"}
VARIANT_FILTER_SEARCH_SAll= {"xpath":"//label[normalize-space()='Select All']"}
VARIANT_FILTER_SEARCH_AllV = {"xpath":"//label[normalize-space()='All Variants']"}
REBATE_EXPERIENCE_FILTER = {"xpath" : "//div[contains(text(),'All Experiences')]"}
REBATE_VARIANT_FILTER= {"css selector" :".p-multiselect-trigger-icon.ng-tns-c93-23.pi.pi-chevron-down"}
VARIANT_FILTER = {"//div[contains(text(),'All Variants')]"}
DATE_RANGE_FILTER = {"id":  '//input[@placeholder="Select Custom Date"]'}
RECEIPT_INSIGHTS_RETAILERS = {"//div[text()='Retailers']"}
RECEIPT_INSIGHTS_LOCATIONS = {"//div[text()='Locations']"}
RETAILER_METRIC = {"//table//td[text()='WALL-MART-SUPERSTORE']/following-sibling::td"}
CONVERSION_FUNNEL_SCANS_CLICKS = {"//span[normalize-space()='Scans/Clicks']"}
CONVERSION_FUNNEL_INITIATIONS = {"//span[normalize-space()='Initiations']"}
CONVERSION_FUNNEL_SUBMISSIONS = {"//span[normalize-space()='Submissions']"}
CONVERSION_FUNNEL_APPROVALS = {"//span[normalize-space()='Approvals']"}
CONVERSION_FUNNEL_PAYOUTS = {"//span[normalize-space()='Payouts']"}
REBATE_DASHBOARD = {"xpath" : "//*[@id='mainContent']/div[1]/div[1]/h1"}
REBATE_EXPORT = {"xpath":"//button[normalize-space()='Export Selection']"}
DROPDOWN_FILTER = { "//div[@class='filter-button']"}
DROPDOWN_FILTER_CATEGORY = { "//span[@class='filter-name']"}
DROPDOWN_CATEGORY = { "//div[contains(text(),'All Categories')]"}
CATEGORY_FILTER_SEARCH = {"xpath":"//input[@placeholder='Search...']"}
DROPDOWN_ALL_CATEGORY = { "//label[normalize-space()='All Categories']"}
CATEGORY_FILTER_SEARCH_CROSS = {"xpath":"//span[@class='p-button-icon pi pi-times']"}

###Customer Registration###
CUSTOMER_OPTION = {"css selector", "body > app-root:nth-child(1) > app-brand-main:nth-child(4) > div:nth-child(1) > div:nth-child(1) > nav:nth-child(1) > ul:nth-child(1) > li:nth-child(4) > span:nth-child(2)"}
REGISTRATION_OPTION = {"xpath", "//span[normalize-space()='Registrations']"}
CUSTOMER_LOGOUT_BUTTON = {"//img[@alt='logout']"}
CUSTOMER_REGISTRATION_TITLE = {"//h1[normalize-space()='Customers > Registrations']"}
CUSTOMER_COUNT = { "//h6[normalize-space()='Total Registrations']"}
CUSTOMER_EXPERIENCE_FILTER = {"(//div[@class='p-multiselect-label-container'])[1]"}
CUSTOMER_FILTER_SEARCH = {"//input[@placeholder='Search...']"}
CUSTOMER_FILTER_OPTION = {"//div[@title='Test']"}
CUSTOMER_FILTER_CROSS = {"xpath":"//span[@class='p-button-icon pi pi-times']"}
CUSTOMER_VARIANT_FILTER = {"//div[contains(text(),'All Variants')]"}
CUSTOMER_REGISTRATION_STATUS = {"//div[contains(text(),'All Registration Statuses')]"}
CUSTOMER_SOURCE = {"//div[contains(text(),'All Customer Sources')]"}
CUSTOMER_SEARCH_BAR = {"//input[@placeholder='Search Items...']"}
CUSTOMER_SWITCHER_BUTTON = {"//button[@class='p-ripple p-togglebutton p-component']"}
CUSTOMER_FIELDS_BUTTON = { "(//button[normalize-space()='Fields'])[1]"}
CUSTOMER_UNSELECT_ALL_CHECKBOX = {"xpath" : "//p-checkbox[@class='ng-valid ng-dirty ng-touched']//div[@class='p-checkbox-box']"}
CUSTOMER_SELECT_ALL_CHECKBOX = {"(//div[@class='p-checkbox-box'])[4]"}
CUSTOMER_CUSTOMER_NAME_HEADING = { "#firstName"}
CUSTOMER_REGISTRATION_CUSTOMER_HEADING = {"css selector":"#email1"}
CUSTOMER_REGISTRATION_REG_DATE = {"css selector":"#prodRegDate"}
CUSTOMER_REGISTRATION_PURCHASE_DATE = {"css selector":"#prodPurchased"}
CUSTOMER_REGISTRATION_REG_STATUS = {"css selector":"#warrantyStatus"}
CUSTOMER_REGISTRATION_LOCATION = {"css selector":"#productLocation"}
CUSTOMER_ICON = {"(//img[@class='user-image'])[1]"}
CUSTOMER_POPUP_CUSTOMER_DETAIL = {"xpath":"//div[contains(text(),'Customer Details')]"}
CUSTOMER_POPUP_ENGAGEMENT_DETAIL = {"xpath":"//div[contains(text(),'Engagement Details')]"}
CUSTOMER_POPUP_REGISTRATION = {"xpath":"//div[contains(text(),'Registrations')]"}
CUSTOMER_POPUP_CLOSE  = {"xpath":"//timesicon[@class='p-component p-iconwrapper ng-tns-c787154972-127 ng-star-inserted']//*[name()='svg']"}
Customer_Expander = { "//body[1]/app-root[1]/app-brand-main[1]/div[1]/div[1]/div[2]/div[2]/div[1]/app-users-listing[1]/p-table[1]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[2]/img[2]"}
CUSTOMER_REGISTRATION_ICON = { "img[class='cursor-pointer arrow-btn img-border ng-star-inserted']"}
CUSTOMER_RESET_GOOGLE_PERMISSION = {"//button[normalize-space()='Reset Google Sheet']"}
CUSTOMER_VIEW_IN_GOOGLE_SHEET = { "//button[normalize-space()='View in Google Sheet']"}
CUSTOMER_EXPORT_BUTTON = {"xpath" : "//button[normalize-space()='Export CSV']"}
CUSTOMER_EXPORT_CANCEL = {"xpath":"//span[normalize-space()='Cancel']"}
CUSTOMER_EXPORT_CLOSE = {"xpath":"(//*[name()='svg'][@class='p-icon'])[1]"}
CUSTOMER_EXPORT_EXPORT = {"xpath":"//span[normalize-space()='Export']"}
CUSTOMER_REGISTRATION_COUNT = {"xpath":"//h6[normalize-space()='Total Registrations']"}
REGISTRATION_STATUS_ACTIVE= {"xpath":"//div[@title='Active']"}
REGISTRATION_STATUS_PENDING= {"xpath":"//div[@title='Pending']"}
REGISTRATION_STATUS_INCOMPLETE= {"xpath":"//div[@title='Incomplete']"}
REGISTRATION_STATUS_DENIED= {"xpath":"//div[@title='Denied']"}
REGISTRATION_STATUS_EXPIRED= {"xpath":"//div[@title='Expired']"}
REGISTRATION_STATUS_ALL= {"xpath":"//label[normalize-space()='All Registration Statuses']"}
REGISTRATION_CUSTOMER_SOURCE_ALL = {"xpath":"//label[normalize-space()='All Customer Sources']"}
REGISTRATION_CUSTOMER_SOURCE_BRIJ = {"xpath":"//div[@title='Brij']"}
REGISTRATION_CUSTOMER_SOURCE_OTHERS = {"xpath":"//div[@title='Other']"}
CUSTOMER_ROWPERPAGE_OPTION = {"xpath":"//div[@aria-label='dropdown trigger']"}
CUSTOMER_ROWPERPAGE_20 = {"xpath":"//span[@class='ng-star-inserted'][normalize-space()='20']"}
CUSTOMER_ROWPERPAGE_100 = {"xpath":"//span[normalize-space()='100']"}
CUSTOMER_ROWPERPAGE_1000 = {"xpath":"//span[normalize-space()='1000']"}

###REGISTRATION ###

REGISTRATION_SEARCH_BAR = {"css selector" : " input[placeholder='Search Items...']"}
REGISTRATION_ICON = {"xpath":"//tbody/tr[1]"}
REGISTRATION_KEBAB_MENU = {"xpath":"(//app-row-options)[1]"}
REGISTRATION_EDIT_REG = {"xpath":"//div[@class='custom-listing-field edit-registration ng-star-inserted']"}
REGISTRATION_ARCHIVE = {"xpath":"//div[@class='custom-listing-field red ng-star-inserted']"}
REGISTRATION_RESTORE = {"xpath":"//span[@class='text']"}
REGISTRATION_RESTORE_CONFIRM = {"xpath":"//span[normalize-space()='Restore']"}
REGISTRATION_ARCHIVE_CONFIRM = {"xpath":"//span[normalize-space()='Archive']"}
REGISTRATION_STATUS_DROPDOWN = {"xpath":"//div[contains(text(),'All Registration Statuses')]"}
REGISTRATION_STATUS_DROPDOWN_CLOSE = {"xpath":"//div[contains(text(),'All Registration Statuses')]"}
REGISTRATION_STATUS_DROPDOWN_ARCHIVE = {"xpath":"(//div[@class='p-checkbox p-component'])[1]"}
REGISTRATION_SWITCHER_BUTTON = {"css selector" : ".div[class='p-ripple p-element p-button p-component ng-star-inserted']"}
REGISTRATION_FIELDS_BUTTON = {"css selector" : ".p-element.p-ripple.p-button-outlined.brand-fields-btn.ml-12.p-button.p-component"}
REGISTRATION_SELECT_ALL_CHECKBOX = {"css selector" :  "p-checkbox[name='tableHeaderCheckbox'] div[class='p-checkbox-box']"}
REGISTRATION_CUSTOMER_NAME_HEADING = {"css selector" :  "#email1"}
REGISTRATION_REG_DATE_HEADING = {"css selector" :  "#prodRegDate"}
REGISTRATION_PURCHASE_DATE_HEADING = {"css selector" :  "#prodPurchased"}
REGISTRATION_REG_STATUS_HEADING = {"css selector" :  "#warrantyStatus"}
REGISTRATION_LOCATION_HEADING = {"css selector" :  "#productLocation"}
REGISTRATION_REGISTRATION_DETAIL = {"xpath":"//div[@class='ng-tns-c4084589801-323'][normalize-space()='Registration Details']"}
REGISTRATION_POPUP_CUSTOMER_DETAIL = {"xpath":"//div[contains(text(),'Customer Details')]"}
REGISTRATION_POPUP_PENCIL_ICON = {"css selector":"img[src='assets/svgs/pencil-dark.svg']"}
REGISTRATION_POPUP_PENCIL_ICON2 = {"xpath":"//span[@class='purchase-edit flex ng-tns-c4084589801-309 ng-star-inserted']"}
REGISTRATION_POPUP_WARRANTY_NUM = {"xpath":"//input[@class='enabled-input ng-tns-c4084589801-1075 ng-pristine ng-valid ng-touched']"}
REGISTRATION_POPUP_WARRANTY_NUM1 = {"css selector":".enabled-input.ng-tns-c4084589801-323.ng-valid.ng-dirty.ng-touched"}
REGISTRATION_POPUP_WARRANTY_DUR = {"xpath":"//*[@id='pn_id_109']"}
REGISTRATION_POPUP_WARRANTY_MON = {"xpath":"//span[normalize-space()='Months']"}
REGISTRATION_POPUP_SERIAL_NUM = {"xpath":"//div[@class='field flex-50 ng-tns-c4084589801-315 ng-star-inserted']//input[@type='text']"}
REGISTRATION_POPUP_CLOSE = {"xpath":"//img[@alt='close']"}
REGISTRATION_POPUP_FORM = {"xpath":"//div[contains(text(),'Forms ')]"}
REGISTRATION_POPUP_STATUS = {"xpath":"//div[@class='ng-tns-c4084589801-32'][normalize-space()='Status']"}
REGISTRATION_REGISTRATION_ICON = {"css selector" : "body > app-root:nth-child(1) > app-brand-main:nth-child(4) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(2) > div:nth-child(1) > app-users-listing:nth-child(2) > p-table:nth-child(2) > div:nth-child(1) > div:nth-child(1) > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(2) > img:nth-child(1)"}
REGISTRATION_RESET_GOOGLE_PERMISSION = {"css selector" : "//span[normalize-space()='Reset Google Sheet']"}
REGISTRATION_VIEW_IN_GOOGLE_SHEET = {"css selector" :  "button[label='View in Google Sheet']"}
REGISTRATION_EXPORT_BUTTON = {"css selector" : "button[label='Export CSV']"}



### CUSTOMER REBATES   ###
CUSTOMER_REBATE_TITLE = {"//h1[normalize-space()='Customers > Rebates']"}
CUSTOMER_COUNT_REBATE = {"css selector" : "div[class='content-space-between'] div[class='ng-star-inserted']"}
REBATE_PAGE_EXPERIENCE_FILTER = {"xpath" :  "//div[contains(text(),'All Experiences')]"}
REBATE_EXPERIENCE_FILTER_SEARCH = {"xpath" :  "//input[@placeholder='Search...']"}
REBATE_EXPERIENCE_FILTER_CLOSE = {"xpath":"//span[@class='p-button-icon pi pi-times']"}
CUSTOMER_REBATE_STATUS_FILTER = {"xpath" :  "//div[contains(text(),'All Rebate Statuses')]"}
REBATE_FILTER_PAID = {"xpath":"//div[@title='Paid']"}
REBATE_SEARCH_BAR = {"css selector" :  "input[placeholder='Search Items...']"}
CUSTOMER_SWITCHER_BUTTON_REBATE ={"css selector" : ".p-ripple.p-element.p-button.p-component.ng-star-inserted.p-highlight"}
CUSTOMER_REBATE_FIELDS_BUTTON = {"css selector" :  "button[type='button'] span[class='p-button-label']"}
CUSTOMER_REBATE_SELECT_ALL_CHECKBOX = {"css selector" :  "p-checkbox[name='tableHeaderCheckbox'] div[class='p-checkbox-box']"}
CUSTOMER_REBATE_CUSTOMER_NAME_HEADING = {"css selector" :  "#firstName"}
REBATE_POPUP_CUSTOMER_DETAIL = {"xpath":"//div[contains(text(),'Customer Details')]"}
REBATE_POPUP_REBATE_DETAIL = {"xpath":"//div[contains(text(),'Rebate Details:')]"}
REBATE_POPUP_RECEIPT_DETAIL = {"xpath":"//div[contains(text(),'Receipt Details:')]"}
REBATE_POPUP_CLOSE = {"xpath":"//img[@alt='close']"}
CUSTOMER_REBATE_ICON = {"css selector" : "body > app-root:nth-child(1) > app-brand-main:nth-child(4) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(2) > div:nth-child(1) > app-users-listing:nth-child(2) > p-table:nth-child(2) > div:nth-child(1) > div:nth-child(1) > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(3) > app-user-avatar:nth-child(1) > div:nth-child(1) > img:nth-child(1)"}
Customer_REBATE_Expander = {"css selector" :  "img[class='cursor-pointer arrow-btn img-border ng-star-inserted']"}
CUSTOMER_IN_REBATE_ICON = {"css selector" :  "body > app-root:nth-child(1) > app-brand-main:nth-child(4) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(2) > div:nth-child(1) > app-users-listing:nth-child(2) > p-table:nth-child(2) > div:nth-child(1) > div:nth-child(1) > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(2) > td:nth-child(1) > p-table:nth-child(1) > div:nth-child(1) > div:nth-child(1) > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(3) > img:nth-child(1)"}
CUSTOMER_REBATE_EXPORT_BUTTON = {"xpath" : "//span[normalize-space()='Export CSV']"}

### REBATES ###
REBATE_PAGE_OPTION = {"xpath" : "//li[@class='pl-0 is-active']//span[contains(text(),'Rebates')]"}
REBATE_REBATE_SEARCH_BAR = {"css selector" : " input[placeholder='Search Items...']"}
REBATE_SWITCHER_BUTTON = {"xpath" :"//button[@class='p-ripple p-togglebutton p-component']"}
REBATE_FIELDS_BUTTON = {"xpath" :  "//button[normalize-space()='Fields']"}
REBATE_SELECT_ALL_CHECKBOX = {"xpath" :  "//input[@id='tableHeaderCheckbox']"}
REBATE_CUSTOMER_NAME_HEADING = {"xpath" :  "//th[normalize-space()='Customer']"}
REBATE_REBATE_DATE_HEADING = {"xpath" :  "//th[normalize-space()='Rebate Date']"}
REBATE_REG_STATUS_HEADING = {"xpath" :  "//th[normalize-space()='Rebate Status']"}
REBATE_ICON = {"xpath" :  "//tbody/tr[2]"}
REBATE_EXPORT_BUTTON = {"xpath" : "//button[normalize-space()='Export CSV']"}
REBATE_LIST_KEBAB_MENU = {"xpath" : "//body[1]/app-root[1]/app-brand-main[1]/div[1]/div[1]/div[2]/div[2]/div[1]/app-rebate-listing[1]/p-table[1]/div[1]/div[1]/table[1]/tbody[1]/tr[2]/td[11]/app-row-options[1]/div[1]/img[1]"}
REBATE_LIST_EDIT = {"xpath" : "//div[@class='custom-listing-field edit-registration ng-star-inserted']"}



### AB899 MODULE ##
MODULE_ICON_LEFTPANEL = {"xpath":"(//li[@class='has-subnav ng-star-inserted'])[3]"}
MODULE_ICON_LEFTPANEL2 = {"xpath":"//span[normalize-space()='Modules']"}
MODULE_ARROW_LEFTPANEL = {"xpath":"//img[@class='module-image']"}
AB899_TITLE = {"xpath":"//h1[normalize-space()='AB 899']"}
AB899_TABLE_LIST_OPTION = {"xpath":"//tbody/tr[1]"}
AB899_OPTION = {"xpath":"////div[@id='adminDashboardContainer']/nav/ul/li[2]"}
AB899_FIELD_BUTTON = {"xpath":"//button[normalize-space()='Fields']"}
AB899_SEARCH = {"xpath":"//input[@placeholder='Search Items...']"}
AB899_ALL_CHECK = {"xpath":"//*[@id='selectAllCol']/app-checkbox/div/p-checkbox/div"}
AB899_ALL_UNCHECK = {"xpath":"//input[@id='tableHeaderCheckbox']"}
AB899_NEW_MODULE = {"xpath":"//button[normalize-space()='New AB 899 Module']"}
AB899_DIALOG = {"xpath":"//div[@role='dialog']"}
AB899_POPUP_MODULE_NAME= {"xpath":"//input[@placeholder='Enter module name...']"}
AB899_POPUP_CTA = {"xpath":"//input[@placeholder='Enter call to action...']"}
AB899_POPUP_EDITOR = {"xpath":"//div[@class='fr-element fr-view default-styles-1']//p"}
AB899_POPUP_ASETTING = {"css selector":".p-element.advanced-setting-icon.ng-tns-c202-12"}
AB899_POPUP_SAVE_BUTTON = {"xpath":"//button[normalize-space()='Save']"}
AB899_LIST = {"xpath":"//tbody/tr[1]"}
AB899_FIELD_MODULE_NAME ={"xpath":"//*[@id='mainContent']/div[2]/div/app-ab899-module-listing/div/app-table-search-filter/div/div/div[1]/div/div/div/div[1]/app-checkbox/div/p-checkbox/div"}
AB899_FIELD_WHERE_USED = {"xpath":"//*[@id='mainContent']/div[2]/div/app-ab899-module-listing/div/app-table-search-filter/div/div/div[1]/div/div/div/div[2]/app-checkbox/div/p-checkbox/div"}
AB899_FIELD_CALL_TO_ACTION = {"xpath":"//*[@id='mainContent']/div[2]/div/app-ab899-module-listing/div/app-table-search-filter/div/div/div[1]/div/div/div/div[3]/app-checkbox/div/p-checkbox/div"}
AB899_ADD_EDIT_MODULE = {"xpath":"//span[@class='p-dialog-title align']"}
AB899_MODULE_HEADING ={"xpath":"//th[@id='moduleName']"}
AB899_WHERE_USED = {"xpath":"//th[@id='whereUsed']"}
AB899_CALL_TO_ACTION = {"xpath":"//th[@id='callToAction']"}
Ab899_COUNT = {"xpath","//h6[normalize-space()='Total AB 899 Modules']"}
AB899_CHECKBOX_LIST = {"xpath":"(//div[@class='p-checkbox p-component'])[2]"}
AB899_DELETE_BUTTON = {"xpath":"//button[normalize-space()='Delete']"}
AB899_CONFIRM_DELETE_BUTTON = {"xpath":"//span[normalize-space()='Delete']"}
AB899_CONFIRM_DELETE_toast = {"xpath":"//div[@class='ng-tns-c3499315822-33 p-toast-detail']"}
AB899_POPUP_CLOSE = {"xpath":"//button[@class='p-dialog-header-icon p-dialog-header-maximize p-link ng-star-inserted']"}
AB899_ROWPERPAGE_OPTION = {"xpath":"//div[@aria-label='dropdown trigger']"}
AB899_ROWPERPAGE_20 = {"xpath":"//span[@class='ng-star-inserted'][normalize-space()='20']"}
AB899_ROWPERPAGE_100 = {"xpath":"//span[normalize-space()='100']"}
AB899_ROWPERPAGE_1000 = {"xpath":"//span[normalize-space()='1000']"}
AB899_AS = {"xpath":"//img[@alt='advance settings icon']"}
AB899_DUPLICATE = {"xpath":"//img[@alt='Copy Module']"}
AB899_AS_SAVE = {"xpath":"/html/body/p-dynamicdialog/div/div/div[2]/app-module-edit-popup/app-ab899-module-edit/form/div/div[1]/div[2]/div[1]/div/div[1]/div[2]/app-p-button/button"}
AB899_AS_BACK = {"xpath":"//label[normalize-space()='Advanced Settings']"}
AB899_AS_HEAVY_METALS = {"xpath":"//label[normalize-space()='Show Heavy Metals Results']"}
AB899_AS_HM_HIDE_TEST_DATE = {"xpath":"//*[@id='style-1']/div[1]/div/div[2]/div/div[1]/app-ab899-results-interface/div/div/div[1]/app-checkbox/div/label"}
AB899_AS_HM_EXPIRY_DATE = {"xpath":"//*[@id='style-1']/div[1]/div/div[2]/div/div[1]/app-ab899-results-interface/div/div/div[2]/app-checkbox/div/label"}
AB899_AS_HM_HIDE_NULL = {"xpath":"//*[@id='style-1']/div[1]/div/div[2]/div/div[1]/app-ab899-results-interface/div/div/div[3]/app-checkbox/div/label"}
AB899_AS_HM_POST_30DAYS = {"xpath":"//*[@id='style-1']/div[1]/div/div[2]/div/div[1]/app-ab899-results-interface/div/div/div[4]/app-checkbox/div/label"}
AB899_AS_HM_OVERRIDE_NONNUMERIC = {"xpath":"//*[@id='style-1']/div[1]/div/div[2]/div/div[1]/app-ab899-results-interface/div/div/div[5]/app-checkbox/div/label"}
AB899_AS_HM_OVERRIDE_NONNUMERIC_ARSENIC = {"xpath":"//*[@id='style-1']/div[1]/div/div[2]/div/div[1]/app-ab899-results-interface/div/div/div[5]/div/div/div[1]/app-checkbox/div/label"}
AB899_AS_HM_OVERRIDE_NONNUMERIC_ARSENIC_TEXT = {"xpath":"//*[@id='style-1']/div[1]/div/div[2]/div/div[1]/app-ab899-results-interface/div/div/div[5]/div/div/div[1]/div/input"}
AB899_AS_HM_OVERRIDE_NONNUMERIC_CADMIUM = {"xpath":"//*[@id='style-1']/div[1]/div/div[2]/div/div[1]/app-ab899-results-interface/div/div/div[5]/div/div/div[2]/app-checkbox/div/label"}
AB899_AS_HM_OVERRIDE_NONNUMERIC_CADMIUM_TEXT = {"xpath":"//*[@id='style-1']/div[1]/div/div[2]/div/div[1]/app-ab899-results-interface/div/div/div[5]/div/div/div[2]/div/input"}
AB899_AS_HM_OVERRIDE_NONNUMERIC_lEAD = {"xpath":"//*[@id='style-1']/div[1]/div/div[2]/div/div[1]/app-ab899-results-interface/div/div/div[5]/div/div/div[3]/app-checkbox/div/label"}
AB899_AS_HM_OVERRIDE_NONNUMERIC_lEAD_TEXT = {"xpath":"//*[@id='style-1']/div[1]/div/div[2]/div/div[1]/app-ab899-results-interface/div/div/div[5]/div/div/div[3]/div/input"}
AB899_AS_HM_OVERRIDE_NONNUMERIC_MERCURY = {"xpath":"//*[@id='style-1']/div[1]/div/div[2]/div/div[1]/app-ab899-results-interface/div/div/div[5]/div/div/div[4]/app-checkbox/div/label"}
AB899_AS_HM_OVERRIDE_NONNUMERIC_MERCURY_TEXT = {"xpath":"/html/body/p-dynamicdialog/div/div/div[2]/app-module-edit-popup/app-ab899-module-edit/form/div/div[1]/div[2]/div[1]/div/div[2]/div/div[1]/app-ab899-results-interface/div/div/div[5]/div/div/div[4]/div/input"}
AB899_AS_HM_SHOW_EDUCATIONAL = {"xpath":"//*[@id='style-1']/div[1]/div/div[2]/div/div[1]/app-ab899-results-interface/div/div/div[6]/app-checkbox/div/label"}
AB899_AS_HM_SHOW_EDUCATIONAL_TEXT = {"xpath":"//*[@id='style-1']/div[1]/div/div[2]/div/div[1]/app-ab899-results-interface/div/div/div[6]/div/app-editor/div/div[2]/div/p"}
AB899_AS_HM_SHOW_INFO = {"xpath":"//*[@id='style-1']/div[1]/div/div[2]/div/div[1]/app-ab899-results-interface/div/div/div[7]/app-checkbox/div/label"}
AB899_AS_HM_SHOW_INFO_LABEL = {"xpath":"//*[@id='style-1']/div[1]/div/div[2]/div/div[1]/app-ab899-results-interface/div/div/div[7]/div/input"}
AB899_AS_HM_SHOW_INFO_TEXT = {"xpath":"//*[@id='style-1']/div[1]/div/div[2]/div/div[1]/app-ab899-results-interface/div/div/div[7]/div/app-editor/div/div[2]/div"}
AB899_AS_HM_INCLUDE_LINK = {"xpath":"//*[@id='style-1']/div[1]/div/div[2]/div/div[1]/app-ab899-results-interface/div/div/div[8]/app-checkbox/div/label"}
AB899_AS_HM_INCLUDE_LINK_TEXT = {"xpath":"//*[@id='style-1']/div[1]/div/div[2]/div/div[1]/app-ab899-results-interface/div/div/div[8]/div/input"}
AB899_AS_HM_BELOW_THRESHOLD = {"xpath":"//*[@id='style-1']/div[1]/div/div[2]/div/div[1]/app-ab899-results-interface/div/div/div[9]/app-checkbox/div/label"}
AB899_AS_HM_BELOW_THRESHOLD_ARSENIC = {"xpath":"//*[@id='style-1']/div[1]/div/div[2]/div/div[1]/app-ab899-results-interface/div/div/div[9]/div/div/div[1]/app-checkbox/div/label"}
AB899_AS_HM_BELOW_THRESHOLD_ARSENIC_TEXT = {"xpath":"//*[@id='style-1']/div[1]/div/div[2]/div/div[1]/app-ab899-results-interface/div/div/div[9]/div/div/div[1]/div/input[1]"}
AB899_AS_HM_BELOW_THRESHOLD_ARSENIC_VALUE = {"xpath":"//*[@id='style-1']/div[1]/div/div[2]/div/div[1]/app-ab899-results-interface/div/div/div[9]/div/div/div[1]/div/input[2]"}
AB899_AS_HM_BELOW_THRESHOLD_CADMIUM = {"xpath":"//*[@id='style-1']/div[1]/div/div[2]/div/div[1]/app-ab899-results-interface/div/div/div[9]/div/div/div[2]/app-checkbox/div/label"}
AB899_AS_HM_BELOW_THRESHOLD_CADMIUM_TEXT = {"xpath":"//*[@id='style-1']/div[1]/div/div[2]/div/div[1]/app-ab899-results-interface/div/div/div[9]/div/div/div[2]/div/input[1]"}
AB899_AS_HM_BELOW_THRESHOLD_CADMIUM_VALUE = {"xpath":"//*[@id='style-1']/div[1]/div/div[2]/div/div[1]/app-ab899-results-interface/div/div/div[9]/div/div/div[2]/div/input[2]"}
AB899_AS_HM_BELOW_THRESHOLD_LEAD = {"xpath":"//*[@id='style-1']/div[1]/div/div[2]/div/div[1]/app-ab899-results-interface/div/div/div[9]/div/div/div[3]/app-checkbox/div/label"}
AB899_AS_HM_BELOW_THRESHOLD_LEAD_TEXT = {"xpath":"//*[@id='style-1']/div[1]/div/div[2]/div/div[1]/app-ab899-results-interface/div/div/div[9]/div/div/div[3]/div/input[1]"}
AB899_AS_HM_BELOW_THRESHOLD_LEAD_VALUE = {"xpath":"//*[@id='style-1']/div[1]/div/div[2]/div/div[1]/app-ab899-results-interface/div/div/div[9]/div/div/div[3]/div/input[2]"}
AB899_AS_HM_BELOW_THRESHOLD_MERCURY = {"xpath":"//*[@id='style-1']/div[1]/div/div[2]/div/div[1]/app-ab899-results-interface/div/div/div[9]/div/div/div[4]/app-checkbox/div/label"}
AB899_AS_HM_BELOW_THRESHOLD_MERCURY_TEXT = {"xpath":"//*[@id='style-1']/div[1]/div/div[2]/div/div[1]/app-ab899-results-interface/div/div/div[9]/div/div/div[4]/div/input[1]"}
AB899_AS_HM_BELOW_THRESHOLD_MERCURY_VALUE = {"xpath":"//*[@id='style-1']/div[1]/div/div[2]/div/div[1]/app-ab899-results-interface/div/div/div[9]/div/div/div[4]/div/input[2]"}
AB899_AS_HM_STANDARD_LIMIT = {"xpath":"//*[@id='style-1']/div[1]/div/div[2]/div/div[1]/app-ab899-results-interface/div/div/div[10]/app-checkbox/div/label"}
AB899_AS_HM_STANDARD_LIMIT_ARSENIC = {"xpath":"//*[@id='style-1']/div[1]/div/div[2]/div/div[1]/app-ab899-results-interface/div/div/div[10]/div/div[1]/div[1]/app-checkbox/div/label"}
AB899_AS_HM_STANDARD_LIMIT_ARSENIC_LIMIT = {"xpath":"//*[@id='style-1']/div[1]/div/div[2]/div/div[1]/app-ab899-results-interface/div/div/div[10]/div/div[1]/div[1]/div/input"}
AB899_AS_HM_STANDARD_LIMIT_CADMIUM = {"xpath":"//*[@id='style-1']/div[1]/div/div[2]/div/div[1]/app-ab899-results-interface/div/div/div[10]/div/div[1]/div[2]/app-checkbox/div/label"}
AB899_AS_HM_STANDARD_LIMIT_CADMIUM_LIMIT = {"xpath":"//*[@id='style-1']/div[1]/div/div[2]/div/div[1]/app-ab899-results-interface/div/div/div[10]/div/div[1]/div[2]/div/input"}
AB899_AS_HM_STANDARD_LIMIT_LEAD = {"xpath":"//*[@id='style-1']/div[1]/div/div[2]/div/div[1]/app-ab899-results-interface/div/div/div[10]/div/div[1]/div[3]/app-checkbox/div/label"}
AB899_AS_HM_STANDARD_LIMIT_LEAD_LIMIT = {"xpath":"//*[@id='style-1']/div[1]/div/div[2]/div/div[1]/app-ab899-results-interface/div/div/div[10]/div/div[1]/div[3]/div/input"}
AB899_AS_HM_STANDARD_LIMIT_MERCURY = {"xpath":"//*[@id='style-1']/div[1]/div/div[2]/div/div[1]/app-ab899-results-interface/div/div/div[10]/div/div[1]/div[4]/app-checkbox/div/label"}
AB899_AS_HM_STANDARD_LIMIT_MERCURY_LIMIT = {"xpath":"//*[@id='style-1']/div[1]/div/div[2]/div/div[1]/app-ab899-results-interface/div/div/div[10]/div/div[1]/div[4]/div/input"}
AB899_AS_HM_STANDARD_LIMIT_ALERT = {"xpath":"//*[@id='style-1']/div[1]/div/div[2]/div/div[1]/app-ab899-results-interface/div/div/div[10]/div/div[2]/app-checkbox/div/label"}
AB899_AS_HM_STANDARD_LIMIT_ALERT_TEXT = {"xpath":"//*[@id='style-1']/div[1]/div/div[2]/div/div[1]/app-ab899-results-interface/div/div/div[10]/div/div[2]/div/textarea"}
AB899_AS_PLASTICIZERS = {"xpath":"//label[normalize-space()='Show Plasticizers Results']"}
AB899_AS_PS_HIDE_TEST_DATE = {"xpath":"//*[@id='style-1']/div[1]/div/div[2]/div/div[3]/app-ab899-results-interface/div/div/div[1]/app-checkbox/div/label"}
AB899_AS_PS_EXPIRY_DATE = {"xpath":"//*[@id='style-1']/div[1]/div/div[2]/div/div[3]/app-ab899-results-interface/div/div/div[2]/app-checkbox/div/label"}
AB899_AS_PS_HIDE_RESULT = {"xpath":"//*[@id='style-1']/div[1]/div/div[2]/div/div[2]/app-ab899-results-interface/div/div/div[4]/app-checkbox/div/label"}
AB899_AS_PS_HIDE_NULL = {"xpath":"//*[@id='style-1']/div[1]/div/div[2]/div/div[3]/app-ab899-results-interface/div/div/div[3]/app-checkbox/div/label"}
AB899_AS_PS_POST_30DAYS = {"xpath":"//*[@id='style-1']/div[1]/div/div[2]/div/div[3]/app-ab899-results-interface/div/div/div[4]/app-checkbox/div/label"}
AB899_AS_PS_OVERRIDE_NONNUMERIC = {"xpath":"//*[@id='style-1']/div[1]/div/div[2]/div/div[3]/app-ab899-results-interface/div/div/div[5]/app-checkbox/div/label"}
AB899_AS_PS_OVERRIDE_NONNUMERIC_BPA = {"xpath":"//label[normalize-space()='BPA (ppb)']"}
AB899_AS_PS_OVERRIDE_NONNUMERIC_BPA_TEXT = {"xpath":"//*[@id='style-1']/div[1]/div/div[2]/div/div[3]/app-ab899-results-interface/div/div/div[5]/div/div/div[1]/div/input"}
AB899_AS_PS_OVERRIDE_NONNUMERIC_BPS = {"xpath":"//label[normalize-space()='BPS (ppb)']"}
AB899_AS_PS_OVERRIDE_NONNUMERIC_BPS_TEXT = {"xpath":"//*[@id='style-1']/div[1]/div/div[2]/div/div[3]/app-ab899-results-interface/div/div/div[5]/div/div/div[2]/div/input"}
AB899_AS_PS_SHOW_EDUCATIONAL = {"xpath":"//*[@id='style-1']/div[1]/div/div[2]/div/div[3]/app-ab899-results-interface/div/div/div[6]/app-checkbox/div/label"}
AB899_AS_PS_SHOW_EDUCATIONAL_TEXT = {"xpath":"//*[@id='style-1']/div[1]/div/div[2]/div/div[3]/app-ab899-results-interface/div/div/div[6]/div/app-editor/div/div[2]/div/p"}
AB899_AS_PS_SHOW_INFO = {"xpath":"//*[@id='style-1']/div[1]/div/div[2]/div/div[3]/app-ab899-results-interface/div/div/div[7]/app-checkbox/div/label"}
AB899_AS_PS_SHOW_INFO_LABEL = {"xpath":"//*[@id='style-1']/div[1]/div/div[2]/div/div[2]/app-ab899-results-interface/div/div/div[7]/div/input"}
AB899_AS_PS_SHOW_INFO_TEXT = {"xpath":"//*[@id='style-1']/div[1]/div/div[2]/div/div[3]/app-ab899-results-interface/div/div/div[7]/div/app-editor/div/div[2]/div/p"}
AB899_AS_PS_INCLUDE_LINK = {"xpath":"//*[@id='style-1']/div[1]/div/div[2]/div/div[3]/app-ab899-results-interface/div/div/div[8]/app-checkbox/div/label"}
AB899_AS_PS_INCLUDE_LINK_TEXT = {"xpath":"//*[@id='style-1']/div[1]/div/div[2]/div/div[3]/app-ab899-results-interface/div/div/div[8]/div/input"}
AB899_AS_PS_BELOW_THRESHOLD = {"xpath":"//*[@id='style-1']/div[1]/div/div[2]/div/div[3]/app-ab899-results-interface/div/div/div[9]/app-checkbox/div/label"}
AB899_AS_PS_BELOW_THRESHOLD_BPA = {"xpath":"//*[@id='style-1']/div[1]/div/div[2]/div/div[3]/app-ab899-results-interface/div/div/div[9]/div/div/div[1]/app-checkbox/div/label"}
AB899_AS_PS_BELOW_THRESHOLD_BPA_TEXT = {"xpath":"//*[@id='style-1']/div[1]/div/div[2]/div/div[3]/app-ab899-results-interface/div/div/div[9]/div/div/div[1]/div/input[1]"}
AB899_AS_PS_BELOW_THRESHOLD_BPA_VALUE = {"xpath":"//*[@id='style-1']/div[1]/div/div[2]/div/div[3]/app-ab899-results-interface/div/div/div[9]/div/div/div[1]/div/input[2]"}
AB899_AS_PS_BELOW_THRESHOLD_BPS = {"xpath":"//*[@id='style-1']/div[1]/div/div[2]/div/div[3]/app-ab899-results-interface/div/div/div[9]/div/div/div[2]/app-checkbox/div/label"}
AB899_AS_PS_BELOW_THRESHOLD_BPS_TEXT = {"xpath":"//*[@id='style-1']/div[1]/div/div[2]/div/div[3]/app-ab899-results-interface/div/div/div[9]/div/div/div[2]/div/input[1]"}
AB899_AS_PS_BELOW_THRESHOLD_BPS_VALUE = {"xpath":"//*[@id='style-1']/div[1]/div/div[2]/div/div[3]/app-ab899-results-interface/div/div/div[9]/div/div/div[2]/div/input[2]"}
AB899_AS_PS_STANDARD_LIMIT = {"xpath":"//*[@id='style-1']/div[1]/div/div[2]/div/div[3]/app-ab899-results-interface/div/div/div[10]/app-checkbox/div/label"}
AB899_AS_PS_STANDARD_LIMIT_BPA = {"xpath":"//*[@id='style-1']/div[1]/div/div[2]/div/div[3]/app-ab899-results-interface/div/div/div[10]/div/div[1]/div[1]/app-checkbox/div/label"}
AB899_AS_PS_STANDARD_LIMIT_BPA_LIMIT = {"xpath":"//*[@id='style-1']/div[1]/div/div[2]/div/div[3]/app-ab899-results-interface/div/div/div[10]/div/div[1]/div[1]/div/input"}
AB899_AS_PS_STANDARD_LIMIT_BPS = {"xpath":"//*[@id='style-1']/div[1]/div/div[2]/div/div[3]/app-ab899-results-interface/div/div/div[10]/div/div[1]/div[2]/app-checkbox/div/label"}
AB899_AS_PS_STANDARD_LIMIT_BPS_LIMIT = {"xpath":"//*[@id='style-1']/div[1]/div/div[2]/div/div[3]/app-ab899-results-interface/div/div/div[10]/div/div[1]/div[2]/div/input"}
AB899_AS_PS_STANDARD_LIMIT_ALERT = {"xpath":"//*[@id='style-1']/div[1]/div/div[2]/div/div[3]/app-ab899-results-interface/div/div/div[10]/div/div[2]/app-checkbox/div/label"}
AB899_AS_PS_STANDARD_LIMIT_ALERT_text = {"xpath":"//*[@id='style-1']/div[1]/div/div[2]/div/div[3]/app-ab899-results-interface/div/div/div[10]/div/div[2]/div/textarea"}
AB899_AS_PESTICIDE_GLYPHOSATE = {"xpath":"//label[normalize-space()='Show Pesticides & Glyphosate Results']"}
AB899_AS_PnG_HIDE_TEST_DATE = {"xpath":"//*[@id='style-1']/div[1]/div/div[2]/div/div[2]/app-ab899-results-interface/div/div/div[1]/app-checkbox/div/label"}
AB899_AS_PnG_EXPIRY_DATE = {"xpath":"//*[@id='style-1']/div[1]/div/div[2]/div/div[2]/app-ab899-results-interface/div/div/div[2]/app-checkbox/div/label"}
AB899_AS_PnG_HIDE_RESULT = {"xpath":"//*[@id='style-1']/div[1]/div/div[2]/div/div[2]/app-ab899-results-interface/div/div/div[4]/app-checkbox/div/label"}
AB899_AS_PnG_HIDE_NULL = {"xpath":"//*[@id='style-1']/div[1]/div/div[2]/div/div[2]/app-ab899-results-interface/div/div/div[3]/app-checkbox/div/label"}
AB899_AS_PnG_POST_30DAYS = {"xpath":"//*[@id='style-1']/div[1]/div/div[2]/div/div[2]/app-ab899-results-interface/div/div/div[4]/app-checkbox/div/label"}
AB899_AS_PnG_OVERRIDE_NONNUMERIC = {"xpath":"//*[@id='style-1']/div[1]/div/div[2]/div/div[2]/app-ab899-results-interface/div/div/div[5]/app-checkbox/div/label"}
AB899_AS_PnG_OVERRIDE_NONNUMERIC_PESTICIDES = {"xpath":"//*[@id='style-1']/div[1]/div/div[2]/div/div[2]/app-ab899-results-interface/div/div/div[5]/div/div/div[1]/app-checkbox/div/label"}
AB899_AS_PnG_OVERRIDE_NONNUMERIC_PESTICIDES_TEXT = {"xpath":"//*[@id='style-1']/div[1]/div/div[2]/div/div[2]/app-ab899-results-interface/div/div/div[5]/div/div/div[1]/div/input"}
AB899_AS_PnG_OVERRIDE_NONNUMERIC_GLYPHOSATE = {"xpath":"//*[@id='style-1']/div[1]/div/div[2]/div/div[2]/app-ab899-results-interface/div/div/div[5]/div/div/div[2]/app-checkbox/div/label"}
AB899_AS_PnG_OVERRIDE_NONNUMERIC_GLYPHOSATE_TEXT = {"xpath":"//*[@id='style-1']/div[1]/div/div[2]/div/div[2]/app-ab899-results-interface/div/div/div[5]/div/div/div[2]/div/input"}
AB899_AS_PnG_SHOW_EDUCATIONAL = {"xpath":"//*[@id='style-1']/div[1]/div/div[2]/div/div[2]/app-ab899-results-interface/div/div/div[6]/app-checkbox/div/label"}
AB899_AS_PnG_SHOW_EDUCATIONAL_TEXT = {"xpath":"//*[@id='style-1']/div[1]/div/div[2]/div/div[2]/app-ab899-results-interface/div/div/div[6]/div/app-editor/div/div[2]/div"}
AB899_AS_PnG_SHOW_INFO = {"xpath":"//*[@id='style-1']/div[1]/div/div[2]/div/div[2]/app-ab899-results-interface/div/div/div[7]/app-checkbox/div/label"}
AB899_AS_PnG_SHOW_INFO_LABEL = {"xpath":"//*[@id='style-1']/div[1]/div/div[2]/div/div[2]/app-ab899-results-interface/div/div/div[7]/div/input"}
AB899_AS_PnG_SHOW_INFO_TEXT = {"xpath":"//*[@id='style-1']/div[1]/div/div[2]/div/div[2]/app-ab899-results-interface/div/div/div[7]/div/app-editor/div/div[2]/div/p"}
AB899_AS_PnG_INCLUDE_LINK = {"xpath":"//*[@id='style-1']/div[1]/div/div[2]/div/div[2]/app-ab899-results-interface/div/div/div[8]/app-checkbox/div/label"}
AB899_AS_PnG_INCLUDE_LINK_TEXT = {"xpath":"//*[@id='style-1']/div[1]/div/div[2]/div/div[2]/app-ab899-results-interface/div/div/div[8]/div/input"}
AB899_AS_PnG_BELOW_THRESHOLD = {"xpath":"//*[@id='style-1']/div[1]/div/div[2]/div/div[2]/app-ab899-results-interface/div/div/div[9]/app-checkbox/div/label"}
AB899_AS_PnG_BELOW_THRESHOLD_PESTICIDES = {"xpath":"//*[@id='style-1']/div[1]/div/div[2]/div/div[2]/app-ab899-results-interface/div/div/div[9]/div/div/div[1]/app-checkbox/div/label"}
AB899_AS_PnG_BELOW_THRESHOLD_PESTICIDES_TEXT = {"xpath":"//*[@id='style-1']/div[1]/div/div[2]/div/div[2]/app-ab899-results-interface/div/div/div[9]/div/div/div[1]/div/input[1]"}
AB899_AS_PnG_BELOW_THRESHOLD_PESTICIDES_VALUE = {"xpath":"//*[@id='style-1']/div[1]/div/div[2]/div/div[2]/app-ab899-results-interface/div/div/div[9]/div/div/div[1]/div/input[2]"}
AB899_AS_PnG_BELOW_THRESHOLD_GLYPHOSATE = {"xpath":"//*[@id='style-1']/div[1]/div/div[2]/div/div[2]/app-ab899-results-interface/div/div/div[9]/div/div/div[2]/app-checkbox/div/label"}
AB899_AS_PnG_BELOW_THRESHOLD_GLYPHOSATE_TEXT = {"xpath":"//*[@id='style-1']/div[1]/div/div[2]/div/div[2]/app-ab899-results-interface/div/div/div[9]/div/div/div[2]/div/input[1]"}
AB899_AS_PnG_BELOW_THRESHOLD_GLYPHOSATE_VALUE = {"xpath":"//*[@id='style-1']/div[1]/div/div[2]/div/div[2]/app-ab899-results-interface/div/div/div[9]/div/div/div[2]/div/input[2]"}
AB899_AS_PnG_STANDARD_LIMIT = {"xpath":"//*[@id='style-1']/div[1]/div/div[2]/div/div[2]/app-ab899-results-interface/div/div/div[10]/app-checkbox/div/label"}
AB899_AS_PnG_STANDARD_LIMIT_PESTICIDES = {"xpath":"//*[@id='style-1']/div[1]/div/div[2]/div/div[2]/app-ab899-results-interface/div/div/div[10]/div/div[1]/div[1]/app-checkbox/div/label"}
AB899_AS_PnG_STANDARD_LIMIT_PESTICIDES_LIMIT = {"xpath":"//*[@id='style-1']/div[1]/div/div[2]/div/div[2]/app-ab899-results-interface/div/div/div[10]/div/div[1]/div[1]/div/input"}
AB899_AS_PnG_STANDARD_LIMIT_GLYPHOSATE = {"xpath":"//*[@id='style-1']/div[1]/div/div[2]/div/div[2]/app-ab899-results-interface/div/div/div[10]/div/div[1]/div[2]/app-checkbox/div/label"}
AB899_AS_PnG_STANDARD_LIMIT_GLYPHOSATE_LIMIT = {"xpath":"//*[@id='style-1']/div[1]/div/div[2]/div/div[2]/app-ab899-results-interface/div/div/div[10]/div/div[1]/div[2]/div/input"}
AB899_AS_PnG_STANDARD_LIMIT_ALERT = {"xpath":"//*[@id='style-1']/div[1]/div/div[2]/div/div[2]/app-ab899-results-interface/div/div/div[10]/div/div[2]/app-checkbox/div/label"}
AB899_AS_PnG_STANDARD_LIMIT_ALERT_text = {"xpath":"//*[@id='style-1']/div[1]/div/div[2]/div/div[2]/app-ab899-results-interface/div/div/div[10]/div/div[2]/div/textarea"}
AB899_AS_CUSTOMIZE_SEARCH_INSTRUCTION = {"xpath":"//*[@id='style-1']/div[1]/div/div[2]/div/div[4]/app-checkbox/div/label"}
AB899_AS_CUSTOMIZE_SEARCH_INSTRUCTION_TEXT = {"xpath":"//*[@id='style-1']/div[1]/div/div[2]/div/div[4]/div/textarea"}
AB899_AS_CUSTOMIZE_SEARCH_DISCLAIMER = {"xpath":"//*[@id='style-1']/div[1]/div/div[2]/div/div[5]/app-checkbox/div/label"}
AB899_AS_CUSTOMIZE_SEARCH_DISCLAIMER_TEXT = {"xpath":"//*[@id='style-1']/div[1]/div/div[2]/div/div[5]/div/app-editor/div/div[2]/div/p"}
AB899_AS_CUSTOMIZE_NORESULT = {"xpath":"//*[@id='style-1']/div[1]/div/div[2]/div/div[6]/app-checkbox/div/label"}
AB899_AS_CUSTOMIZE_NORESULT_TEXT = {"xpath":"//*[@id='style-1']/div[1]/div/div[2]/div/div[6]/div/textarea"}
AB899_AS_SEARCHBY_PRODUCT = {"xpath":"//label[normalize-space()='Enable Search by Product']"}
AB899_AS_SEARCHBY_PRODUCT_byUPC = {"xpath":"//label[normalize-space()='Search by UPC']"}
AB899_AS_SEARCHBY_PRODUCT_byNAME = {"xpath":"//label[normalize-space()='Search by Product Name']"}
AB899_AS_SEARCHBY_PRODUCT_IGNORE_SPECIAL = {"xpath":"//*[@id='style-1']/div[1]/div/div[2]/div/div[7]/div/div[3]/app-checkbox/div/label"}
AB899_AS_SEARCHBY_PRODUCT_REQUIRED = {"xpath":"//*[@id='style-1']/div[1]/div/div[2]/div/div[7]/div/div[4]/app-checkbox/div/label"}
AB899_AS_SEARCHBY_LOTNO = {"xpath":"//label[normalize-space()='Enable Search by Lot Number']"}
AB899_AS_SEARCHBY_LOTNO_IGNORE = {"xpath":"//*[@id='style-1']/div[1]/div/div[2]/div/div[8]/div/div[1]/app-checkbox/div/label"}
AB899_AS_SEARCHBY_LOTNO_REQUIRED = {"xpath":"//*[@id='style-1']/div[1]/div/div[2]/div/div[8]/div/div[2]/app-checkbox/div/label"}
AB899_AS_CUSTOMIZE_BUTTON = {"xpath":"//label[normalize-space()='Customize Button Colors']"}


### CUSTOM MODULE ##
CUSTOM_OPTION = {"xpath":"//h1[normalize-space()='Custom']"}
CUSTOM_TITLE = {"xpath":"//h1[normalize-space()='Custom']"}
CUSTOM_SEARCH = {"xpath":"//input[@placeholder='Search Items...']"}
CUSTOM_NEW_MODULE = {"xpath":"//button[normalize-space()='New Custom Module']"}
CUSTOM_DIALOG = {"xpath":"//span[@class='p-dialog-title align']"}
CUSTOM_POPUP_DUPLICATE= {"xpath":"//*[@id='style-1']/div/div[1]/div[2]/div/span"}
CUSTOM_POPUP_MODULE_NAME= {"xpath":"//input[@placeholder='Enter module name...']"}
CUSTOM_POPUP_CTA = {"xpath":"//input[@placeholder='Enter call to action...']"}
CUSTOM_POPUP_EDITOR = {"xpath":"//*[@id='style-1']/div/div[3]/app-form-control/div/app-editor/div/div[2]/div/p"}
CUSTOM_POPUP_ASETTING = {"css selector":".p-element.advanced-setting-icon.ng-tns-c202-12"}
CUSTOM_POPUP_SAVE_BUTTON = {"xpath":"//button[normalize-space()='Save']"}
CUSTOM_ECLIPSE = {"xpath":"//body[1]/app-root[1]/app-brand-main[1]/div[1]/div[1]/div[2]/div[2]/div[1]/app-custom-listing[1]/p-table[1]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[7]/app-row-options[1]/div[1]"}
CUSTOM_ECLIPSE_EDIT = {"xpath":"//div[contains(text(),'Edit Custom Module')]"}
CUSTOM_ECLIPSE_DELETE = {"xpath":"//div[contains(text(),'Delete Custom Module')]"}
CUSTOM_DELETE_ALL = {"xpath":"//button[normalize-space()='Delete']"}
CUSTOM_DELETE_CANCEL = {"xpath":"//span[normalize-space()='Cancel']"}
CUSTOM_DELETE_CONFIRM = {"xpath":"//span[normalize-space()='Delete']"}
CUSTOM_LIST = {"xpath":"//tbody/tr[2]/td[1]"}
CUSTOM_ADD_EDIT_MODULE = {"xpath":"//span[@class='p-dialog-title align']"}
CUSTOM_MODULE_HEADING ={"xpath":"//th[@id='moduleName']"}
CUSTOM_WHERE_USED = {"xpath":"//th[@id='whereUsed']"}
CUSTOM_CALL_TO_ACTION = {"xpath":"//th[@id='callToAction']"}
CUSTOM_FIELD_MODULE_NAME ={"xpath":"//*[@id='mainContent']/div[2]/div/app-custom-listing/div/app-table-search-filter/div/div/div[1]/div/div/div/div[1]/app-checkbox/div/p-checkbox/div"}
CUSTOM_FIELD_WHERE_USED = {"xpath":"//*[@id='mainContent']/div[2]/div/app-custom-listing/div/app-table-search-filter/div/div/div[1]/div/div/div/div[2]/app-checkbox/div/p-checkbox/div"}
CUSTOM_FIELD_CALL_TO_ACTION = {"xpath":"//*[@id='mainContent']/div[2]/div/app-custom-listing/div/app-table-search-filter/div/div/div[1]/div/div/div/div[3]/app-checkbox/div/p-checkbox/div"}
CUSTOM_COUNT = {"xpath","//h6[normalize-space()='Total AB 899 Modules']"}
CUSTOM_CHECKBOX_LIST = {"xpath":"//app-checkbox[@class='ng-untouched ng-pristine ng-valid ng-star-inserted']//div[@class='p-checkbox-box']"}
CUSTOM_DELETE_BUTTON = {"xpath":"//button[normalize-space()='Delete']"}
CUSTOM_CONFIRM_DELETE_BUTTON = {"xpath":"//span[normalize-space()='Delete']"}
CUSTOM_CONFIRM_DELETE_toast = {"xpath":"//div[@class='ng-tns-c3499315822-92 p-toast-detail']"}
CUSTOM_POPUP_CLOSE = {"xpath":"//span[@class='p-dialog-header-close-icon pi pi-times']"}
CUSTOM_ROWPERPAGE_OPTION = {"xpath":"//div[@aria-label='dropdown trigger']"}
CUSTOM_ROWPERPAGE_20 = {"xpath":"//span[@class='ng-star-inserted'][normalize-space()='20']"}
CUSTOM_ROWPERPAGE_100 = {"xpath":"//span[normalize-space()='100']"}
CUSTOM_ROWPERPAGE_1000 = {"xpath":"//span[normalize-space()='1000']"}
CUSTOM_FIELD_BUTTON = {"xpath":"//button[normalize-space()='Fields']"}
CUSTOM_ALL_CHECK = {"xpath":"//*[@id='selectAllCol']/app-checkbox/div/p-checkbox/div"}
CUSTOM_ALL_UNCHECK = {"xpath":"//input[@id='tableHeaderCheckbox']"}


### DOCUMENT MODULE ##
DOCUMENT_OPTION = {"xpath":"//h1[normalize-space()='Document']"}
DOCUMENT_SEARCH = {"xpath":"//input[@placeholder='Search Items...']"}
DOCUMENT_NEW_MODULE = {"xpath":"//button[normalize-space()='New Document Module']"}
DOCUMENT_DIALOG = {"xpath":"//div[@role='dialog']"}
DOCUMENT_POPUP_MODULE_NAME= {"xpath":"//input[@placeholder='Enter module name...']"}
DOCUMENT_POPUP_CTA = {"xpath":"//input[@placeholder='Enter call to action...']"}
DOCUMENT_POPUP_UPLOAD = {"xpath":"//label[normalize-space()='Click or Drag File Here']"}
DOCUMENT_POPUP_ASETTING = {"css selector":".p-element.advanced-setting-icon.ng-tns-c202-12"}
DOCUMENT_POPUP_SAVE_BUTTON = {"css selector":"p-button[type='button']"}
DOCUMENT_LIST = {"xpath":"//td[@class='bold ng-star-inserted'][normalize-space()='release test']"}
DOCUMENT_ADD_EDIT_MODULE = {"xpath":"//span[@class='p-dialog-title align']"}
DOCUMENT_MODULE_HEADING ={"xpath":"//th[@id='moduleName']"}
DOCUMENT_WHERE_USED = {"xpath":"//th[@id='whereUsed']"}
DOCUMENT_CALL_TO_ACTION = {"xpath":"//th[@id='callToAction']"}
DOCUMENT_COUNT = {"xpath","//h6[normalize-space()='Total AB 899 Modules']"}
DOCUMENT_CHECKBOX_LIST = {"xpath":"//p-checkbox[@class='ng-pristine ng-valid ng-touched']//div[@class='p-checkbox p-component']"}
DOCUMENT_DELETE_BUTTON = {"xpath":"//button[normalize-space()='Delete']"}
DOCUMENT_CONFIRM_DELETE_BUTTON = {"xpath":"//span[normalize-space()='Delete']"}
DOCUMENT_CONFIRM_DELETE_toast = {"xpath":"//div[@class='ng-tns-c3499315822-19 p-toast-message-text ng-star-inserted']"}
DOCUMENT_SELECT_ALL_CHECKBOXES = {"//input[@id='tableHeaderCheckbox']"}
DOCUMENT_FIELD_BUTTON = {"//button[normalize-space()='Fields']"}
DOCUMENT_POPUP_CLOSE = {"xpath":"//span[@class='p-dialog-header-close-icon pi pi-times']"}
DOCUMENT_ROWPERPAGE_OPTION = {"xpath":"//div[@aria-label='dropdown trigger']"}
DOCUMENT_ROWPERPAGE_20 = {"xpath":"//span[@class='ng-star-inserted'][normalize-space()='20']"}
DOCUMENT_ROWPERPAGE_100 = {"xpath":"//span[normalize-space()='100']"}
DOCUMENT_ROWPERPAGE_1000 = {"xpath":"//span[normalize-space()='1000']"}

### FORM MODULE ##
FORM_OPTION = {"xpath":"//div[@id='adminDashboardContainer']/nav/ul/li[2]"}
FORM_TITLE = {"xpath":"//h1[normalize-space()='Form & Survey']"}
FORM_SEARCH = {"xpath":"//input[@placeholder='Search Items...']"}
FORM_NEW_MODULE = {"xpath":"//button[normalize-space()='New Form & Survey Module']"}
FORM_DIALOG = {"xpath":"//div[@role='dialog']"}
FORM_POPUP_MODULE_NAME= {"xpath":"//input[@placeholder='Enter module name...']"}
FORM_POPUP_CTA = {"xpath":"//input[@placeholder='Enter call to action...']"}
FORM_POPUP_EDITOR = {"xpath":"//app-editor[@formcontrolname='startScreenContent']//div[@class='fr-wrapper']"}
FORM_SELECT_ALL = {"xpath":"//input[@id='tableHeaderCheckbox']"}
FORM_POPUP_ASETTING = {"xpath":"//img[@alt='advance settings icon']"}
FORM_POPUP_ASETTING_lIMIT = {"xpath":"//label[normalize-space()='Limit One Submission Per Customer']"}
FORM_POPUP_ASETTING_CCM = {"xpath":"//label[normalize-space()='Customize Confirmation Message']"}
FORM_POPUP_ASETTING_CCM_TEXT = {"xpath":"//textarea[@placeholder='Enter confirmation message...']"}
FORM_POPUP_ASETTING_CC = {"xpath":"//label[normalize-space()='Customize Button Colors']"}
FORM_POPUP_ASETTING_BACK = {"xpath":"//label[normalize-space()='Advanced Settings']"}
FORM_POPUP_SAVE_BUTTON = {"xpath":"//button[normalize-space()='Save']"}
FORM_LIST = {"xpath":"//td[contains(text(),'Auto')]"}
FORM_ADD_EDIT_MODULE = {"xpath":"//span[@class='p-dialog-title align']"}
FORM_MODULE_HEADING ={"xpath":"//th[@id='moduleName']"}
FORM_TEXTFIELD_BUTTON = {"xpath":"//button[normalize-space()='Text Field']"}
FORM_TEXTFIELD_TITLE = {"xpath":"//input[@id='text0']"}
FORM_TEXTFIELD_SUBTEXT = {"xpath":"//input[@placeholder='Enter subtext']"}
FORM_DROPDOWN = {"xpath":"//button[normalize-space()='Dropdown']"}
FORM_DROPDOWN_TITLE = {"xpath":"//input[@id='drop-down1']"}
FORM_DROPDOWN_SUBTEXT = {"xpath":"//input[@placeholder='Enter subtext']"}
FORM_DROPDOWN_CHOICE_1 = {"xpath":"//input[@id='drop-down10']"}
FORM_DROPDOWN_CHOICE_2 = {"xpath":"//input[@id='drop-down11']"}
FORM_DROPDOWN_ADDCHOICE = {"xpath":"//button[normalize-space()='Add Choice']"}
FORM_MULTICHOICE = {"xpath":"//button[normalize-space()='Multiple Choice']"}
FORM_MULTICHOICE_TITLE = {"xpath":"//input[@id='multiple-choice2']"}
FORM_MULTICHOICE_SUBTEXT = {"xpath":"//input[@placeholder='Enter subtext']"}
FORM_MULTICHOICE_CHOICE_1 = {"xpath":"//input[@id='multiple-choice20']"}
FORM_MULTICHOICE_CHOICE_2 = {"xpath":"//input[@id='multiple-choice21']"}
FORM_MULTICHOICE_ADDCHOICE = {"xpath":"//img[@alt='Add option icon']"}
FORM_KEBAB_ICON = {"xpath":"(//img[@class='three-dots-icon pointer ng-tns-c761393940-266'])[3]"}
FORM_KEBAB_ICON_REMOVE = {"xpath":"//li[@class='ng-tns-c761393940-266']"}
FORM_FIELD = {"xpath":"//button[normalize-space()='Fields']"}
FORM_WHERE_USED = {"xpath":"//th[@id='whereUsed']"}
FORM_UPLOAD_FILE = {"xpath":"//button[normalize-space()='File Upload']"}
FORM_UPLOAD_FILE_TITLE = {"xpath":"//input[@id='file-upload4']"}
FORM_UPLOAD_FILE_SUB_TEXT = {"xpath":"//input[@placeholder='Enter subtext']"}
FORM_CALL_TO_ACTION = {"xpath":"//th[@id='callToAction']"}
FORM_COUNT = {"xpath","//h6[normalize-space()='Total Form & Survey Modules']"}
FORM_CHECKBOX_LIST = {"xpath":"//p-checkbox[@class='ng-pristine ng-valid ng-touched']//div[@class='p-checkbox p-component']"}
FORM_DELETE_BUTTON = {"xpath":"//button[normalize-space()='Delete']"}
FORM_CONFIRM_DELETE_BUTTON = {"xpath":"//span[normalize-space()='Delete']"}
FORM_CONFIRM_DELETE_toast = {"xpath":"//div[@class='ng-tns-c3499315822-19 p-toast-message-text ng-star-inserted']"}
FORM_POPUP_CLOSE = {"xpath":"//span[@class='p-dialog-header-close-icon pi pi-times']"}

FORM_ROWPERPAGE_OPTION = {"xpath":"//"}
FORM_ROWPERPAGE_20 = {"xpath":"//span[@class='ng-star-inserted'][normalize-space()='20']"}
FORM_ROWPERPAGE_100 = {"xpath":"//span[normalize-space()='100']"}
FORM_ROWPERPAGE_1000 = {"xpath":"//span[normalize-space()='1000']"}
FORM_LIST_ECLIPSE = {"xpath":"//body[1]/app-root[1]/app-brand-main[1]/div[1]/div[1]/div[2]/div[2]/div[1]/app-form-listing[1]/p-table[1]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[7]/app-row-options[1]/div[1]"}
FORM_LIST_ECLIPSE_EDIT = {"xpath":"//div[contains(text(),'Edit & Survey Module')]"}



### IFRAME MODULE ##
IFRAME_OPTION = {"xpath":"////div[@id='adminDashboardContainer']/nav/ul/li[2]"}
IFRAME_SEARCH = {"xpath":"//input[@placeholder='Search Items...']"}
IFRAME_NEW_MODULE = {"xpath":"//span[normalize-space()='New AB 899 Module']"}
IFRAME_DIALOG = {"xpath":"//div[@role='dialog']"}
IFRAME_POPUP_MODULE_NAME= {"xpath":"//input[@placeholder='Enter module name...']"}
IFRAME_POPUP_CTA = {"xpath":"//input[@placeholder='Enter call to action...']"}
IFRAME_POPUP_EDITOR = {"xpath":"//app-editor[@IFRAMEcontrolname='preLookup']//br"}
IFRAME_POPUP_ASETTING = {"css selector":".p-element.advanced-setting-icon.ng-tns-c202-12"}
IFRAME_POPUP_SAVE_BUTTON = {"css selector":"p-button[type='button']"}
IFRAME_LIST = {"xpath":"//td[@class='bold ng-star-inserted'][normalize-space()='release test']"}
IFRAME_ADD_EDIT_MODULE = {"xpath":"//span[@class='p-dialog-title align']"}
IFRAME_MODULE_HEADING ={"xpath":"//th[@id='moduleName']"}
IFRAME_WHERE_USED = {"xpath":"//th[@id='whereUsed']"}
IFRAME_CALL_TO_ACTION = {"xpath":"//th[@id='callToAction']"}
IFRAME_COUNT = {"xpath","//h6[normalize-space()='Total AB 899 Modules']"}
IFRAME_CHECKBOX_LIST = {"xpath":"//p-checkbox[@class='ng-pristine ng-valid ng-touched']//div[@class='p-checkbox p-component']"}
IFRAME_DELETE_BUTTON = {"xpath":"//button[normalize-space()='Delete']"}
IFRAME_CONFIRM_DELETE_BUTTON = {"xpath":"//span[normalize-space()='Delete']"}
IFRAME_CONFIRM_DELETE_toast = {"xpath":"//div[@class='ng-tns-c3499315822-19 p-toast-message-text ng-star-inserted']"}

### LINK MODULE ##
LINK_OPTION = {"xpath":"////div[@id='adminDashboardContainer']/nav/ul/li[2]"}
LINK_TITLE = {"xpath":"//h1[normalize-space()='Link']"}
LINK_FIELD = {"xpath":"//button[normalize-space()='Fields']"}
LINK_SELECT_ALL = {"xpath":"//input[@id='tableHeaderCheckbox']"}
LINK_DESTINATION_URL ={"xpath":"(//th[@id='destinationUrl'])[1]"}
LINK_CUSTOM_URL = {"xpath":"//th[normalize-space()='Custom URL']//p-sorticon"}
LINK_POPUP_DESTINATION_URL = {"xpath":"(//div[@aria-label='dropdown trigger'])[2]"}
LINK_POPUP_WEBSITEHOME = {"xpath":"//span[normalize-space()='Website Homepage']"}
LINK_POPUP_PRODUCTPAGE = {"xpath":"//span[normalize-space()='Product Page']"}
LINK_POPUP_CUSTOM ={"xpath":"//span[normalize-space()='Custom URL']"}
LINK_SEARCH = {"xpath":"//input[@placeholder='Search Items...']"}
LINK_NEW_MODULE = {"xpath":"//button[normalize-space()='New Link Module']"}
LINK_DUPLICATE = {"xpath":"//img[@alt='Copy Module']"}
LINK_DIALOG = {"xpath":"//div[@role='dialog']"}
LINK_POPUP_MODULE_NAME= {"xpath":"//input[@placeholder='Enter module name...']"}
LINK_POPUP_CTA = {"xpath":"//input[@placeholder='Enter call to action...']"}
LINK_POPUP_EDITOR = {"xpath":"//app-editor[@LINKcontrolname='preLookup']//br"}
LINK_POPUP_ASETTING = {"xpath":"//img[@alt='advance settings icon']"}
LINK_POPUP_ADD_SUFIX = {"xpath":"//label[normalize-space()='Add Custom URL Suffix']"}
LINK_POPUP_SUFIX_INSERT = {"xpath":"//input[@placeholder='Enter here..']"}
LINK_POPUP_SAVE_BUTTON = {"xpath":"//button[normalize-space()='Save']"}
LINK_POPUP_ADD_SAVE = {"xpath":"//div[@class='form-header has-single-action ng-tns-c816701541-466']//button[@type='button'][normalize-space()='Save']"}
LINK_POPUP_ADV_BACK = {"xpath":"//label[normalize-space()='Advanced Settings']"}
LINK_PREVIEW_LINKBTN = {"xpath":"/html[1]/body[1]/div[1]/div[1]/div[1]/div[1]/main[1]/div[1]/div[2]/div[1]/div[2]/div[1]/div[3]/div[1]/button[1]"}
LINK_LIST = {"xpath":"//td[contains(text(),'Auto')]"}
LINK_LIST_ECLIPSE = {"xpath":"//tbody/tr[1]/td[8]/app-row-options[1]/div[1]/img[1]"}
LINK_LIST_ECLIPSE_EDIT = {"xpath":"//div[contains(text(),'Edit Module')]"}
LINK_ADD_EDIT_MODULE = {"xpath":"//span[@class='p-dialog-title align']"}
LINK_MODULE_HEADING ={"xpath":"//th[@id='moduleName ']"}
LINK_WHERE_USED = {"xpath":"//th[@id='whereUsed']"}
LINK_CALL_TO_ACTION = {"xpath":"//th[@id='callToAction']"}
LINK_COUNT = {"xpath","//h6[normalize-space()='Total AB 899 Modules']"}
LINK_CHECKBOX_LIST = {"xpath":"//p-checkbox[@class='ng-pristine ng-valid ng-touched']//div[@class='p-checkbox p-component']"}
LINK_DELETE_BUTTON = {"xpath":"//button[normalize-space()='Delete']"}
LINK_CONFIRM_DELETE_BUTTON = {"xpath":"//span[normalize-space()='Delete']"}
LINK_CONFIRM_DELETE_toast = {"xpath":"//div[@class='ng-tns-c3499315822-19 p-toast-message-text ng-star-inserted']"}
LINK_POPUP_CLOSE = {"xpath":"//div[@class='p-dialog-header-icons ng-tns-c26-25']"}
LINK_ROWPERPAGE_OPTION = {"xpath":"//div[@aria-label='dropdown trigger']"}
LINK_ROWPERPAGE_20 = {"xpath":"//span[@class='ng-star-inserted'][normalize-space()='20']"}
LINK_ROWPERPAGE_100 = {"xpath":"//span[normalize-space()='100']"}
LINK_ROWPERPAGE_1000 = {"xpath":"//span[normalize-space()='1000']"}

### REBATE_CAMPAIGN MODULE ##
REBATE_CAMPAIGN_OPTION = {"xpath":"//*[@id='adminDashboardContainer']/nav/ul[1]/li[5]/ul/li[10]/span"}
REBATE_CAMPAIGN_SEARCH = {"xpath":"//input[@placeholder='Search Items...']"}
REBATE_CAMPAIGN_NEW_MODULE = {"xpath":"//button[normalize-space()='New Rebate Campaign']"}
REBATE_CAMPAIGN_LOGOUT_BUTTON= {"xpath":"//img[@alt='logout']"}
REBATE_CAMPAIGN_POPUP_MODULE_NAME= {"xpath":"//input[@placeholder='Enter module name...']"}
REBATE_CAMPAIGN_POPUP_CTA = {"xpath":"//input[@placeholder='Enter call to action...']"}
REBATE_CAMPAIGN_POPUP_EDITOR = {"xpath":"//app-editor[@REBATE_CAMPAIGNcontrolname='preLookup']//br"}
REBATE_CAMPAIGN_POPUP_ADVANCE_SETTING = {"css selector":".p-element.advanced-setting-icon.ng-tns-c202-12"}
REBATE_CAMPAIGN_POPUP_SAVE_BUTTON = {"css selector":"p-button[type='button']"}
REBATE_CAMPAIGN_LIST = {"xpath":"//td[@class='bold ng-star-inserted'][normalize-space()='release test']"}
REBATE_CAMPAIGN_ADD_EDIT_MODULE = {"xpath":"//span[@class='p-dialog-title align']"}
REBATE_CAMPAIGN_CAMPAIGN_HEADING ={"xpath":"//th[@id='moduleName ']"}
REBATE_CAMPAIGN_WHERE_USED = {"xpath":"//th[@id='whereUsed']"}
REBATE_CAMPAIGN_PHONE = {"xpath":"//th[@id='phoneNumber']"}
REBATE_CAMPAIGN_COUNT = {"xpath","//h6[normalize-space()='Total AB 899 Modules']"}
REBATE_CAMPAIGN_ALL_CHECKBOX = {"xpath":"//*[@id='selectAllCol']/app-checkbox/div/p-checkbox/div"}
REBATE_CAMPAIGN_DELETE_BUTTON = {"xpath":"//button[normalize-space()='Delete']"}
REBATE_CAMPAIGN_CONFIRM_DELETE_BUTTON = {"xpath":"//span[normalize-space()='Delete']"}
REBATE_CAMPAIGN_CONFIRM_DELETE_toast = {"xpath":"//div[@class='ng-tns-c3499315822-19 p-toast-message-text ng-star-inserted']"}
REBATE_CAMPAIGN_ROWPERPAGE_OPTION = {"xpath":"//div[@aria-label='dropdown trigger']"}
REBATE_CAMPAIGN_ROWPERPAGE_20 = {"xpath":"//span[@class='ng-star-inserted'][normalize-space()='20']"}
REBATE_CAMPAIGN_ROWPERPAGE_100 = {"xpath":"//span[normalize-space()='100']"}
REBATE_CAMPAIGN_ROWPERPAGE_1000 = {"xpath":"//span[normalize-space()='1000']"}
REBATE_CAMPAIGN_EDIT = {"xpath":"//div[@class='text']"}
REBATE_CAMPAIGN_DUPLICATE = {"xpath":"//img[@alt='Copy Module']"}
REBATE_CAMPAIGN_FIELD = {"xpath":"//button[normalize-space()='Fields']"}
REBATE_CAMPAIGN_NUMBER = {"/html/body/p-dynamicdialog/div/div/div[2]/app-module-edit-popup/app-sms-modules-edit/form/div/div[1]/div[2]/div/div[2]/app-form-control/div/app-dropdown/div/p-select/span/span"}
REBATE_CAMPAIGN_NUMBER_none = {"//span[@class='w-full max-w-full whitespace-nowrap text-ellipsis overflow-hidden']"}
REBATE_CAMPAIGN_GRACE = {"//input[@placeholder='Enter grace period...']"}
REBATE_CAMPAIGN_REBATE_TERM = {"/html/body/p-dynamicdialog/div/div/div[2]/app-module-edit-popup/app-sms-modules-edit/form/div/div[1]/div[2]/div/div[5]/app-form-control/div/app-dropdown/div/p-select"}
REBATE_CAMPAIGN_REBATE_TERM_alternate = {"body > p-dynamicdialog:nth-child(10) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > app-module-edit-popup:nth-child(1) > app-sms-modules-edit:nth-child(3) > form:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(6) > app-form-control:nth-child(2) > div:nth-child(1) > app-dropdown:nth-child(1) > div:nth-child(1) > p-select:nth-child(1) > span:nth-child(1) > span:nth-child(1)"}
REBATE_CAMPAIGN_REBATE_TERM_BUYX_GETCASH = {"//span[normalize-space()='Buy X Get Y Cash Back']"}
REBATE_CAMPAIGN_REBATE_TERM_CUSTOM = {""}
REBATE_CAMPAIGN_BUYX_GETY_QUANTITY = {"//input[@class='p-inputtext p-component register-modal-input ng-tns-c1952139658-372 ng-pristine ng-valid p-filled ng-touched']"}
REBATE_CAMPAIGN_BUYX_GETY_QUANTITY2= {"//*[@id='style-1']/div/div[5]/div/div[1]/div/input"}
REBATE_CAMPAIGN_BUYX_GETY_PAYOUT = {"//input[@class='p-inputtext p-component register-modal-input rebate-amount-input ng-tns-c1952139658-372 ng-pristine ng-valid ng-touched']"}
REBATE_CAMPAIGN_BUYX_GETY_PRODUCTNAME = {"//input[@formcontrolname='requiredProduct']"}
REBATE_CAMPAIGN_BUYX_GETY_PAYOUT_PLUS = {"//*[@id='style-1']/div/div[5]/div/div[2]/div/div/span[2]/img"}
REBATE_CAMPAIGN_BUYX_GETY_MAX = {"/html/body/p-dynamicdialog/div/div/div[2]/app-module-edit-popup/app-sms-modules-edit/form/div/div[1]/div[2]/div/div[7]/div/input"}
REBATE_CAMPAIGN_BUYX_GETY_MAX_plus = {"xpath":"/html/body/p-dynamicdialog/div/div/div[2]/app-module-edit-popup/app-sms-modules-edit/form/div/div[1]/div[2]/div/div[7]/div/div/span[2]"}
REBATE_CAMPAIGN_REBATE_TERM_BUYX_GETY = {"//span[normalize-space()='Buy X Get Y Free']"}
REBATE_CAMPAIGN_REBATE_TERM_BUYX_GETY_MIN = {"//input[@class='p-inputtext p-component register-modal-input ng-tns-c1952139658-375 ng-pristine ng-valid p-filled ng-touched']"}
REBATE_CAMPAIGN_REBATE_TERM_BUYX_GETY_MAX = {"//input[@class='p-inputtext p-component register-modal-input ng-tns-c1952139658-375 ng-pristine ng-valid p-filled ng-touched']"}
REBATE_CAMPAIGN_REBATE_TERM_BUYX_GETY_GET_BACK = {"//div[@class='flex gap-5 ng-tns-c1952139658-375 ng-star-inserted']//div[1]//div[1]//input[1]"}
REBATE_CAMPAIGN_REBATE_TERM_BUYX_GETY_REQUIRED_PRODUCT = {"//input[@formcontrolname='requiredProduct']"}
REBATE_CAMPAIGN_REBATE_TERM_BUYX_GETY_REBATE_AMOUNT = {"//input[@class='p-inputtext p-component register-modal-input rebate-amount-input ng-tns-c1952139658-375 ng-pristine ng-valid ng-touched']"}
REBATE_CAMPAIGN_REBATE_TERM_BUYX_GETY_REGENERATE = {"(//span[@class='regenerate-section ng-tns-c1952139658-375'][normalize-space()='Regenerate Text'])[1]"}
REBATE_CAMPAIGN_SAVE = {"//button[normalize-space()='Save']"}
REBATE_CAMPAIGN_CLOSE = {"//span[@class='p-dialog-header-close-icon pi pi-times']"}
REBATE_CAMPAIGN_AS = {"/html/body/p-dynamicdialog/div/div/div[2]/app-module-edit-popup/app-sms-modules-edit/form/div/div[1]/div[1]/div/app-p-button[1]/button/img"}
REBATE_CAMPAIGN_AS_alternate = {"img[alt='advance settings icon']"}
REBATE_CAMPAIGN_AS_REMINDER = {"//label[normalize-space()='Enable Reminder Messages']"}
REBATE_CAMPAIGN_AS_CUSTOMIZE_AI = {"//label[normalize-space()='Customize AI Settings']"}
REBATE_CAMPAIGN_AS_CUSTOMIZE_AI_OPTION = {"(//span[@aria-label='Select an option'])[1]"}
REBATE_CAMPAIGN_AS_CUSTOMIZE_AI_TEXT = {"//span[normalize-space()='Validate receipt / On text message']"}
REBATE_CAMPAIGN_AS_CUSTOMIZE_AI_TEXT2 = {"//div[@title='Validate receipt / On text message']"}
REBATE_CAMPAIGN_AS_CUSTOMIZE_AI_RECEIPT = {"//span[normalize-space()='Validate receipt / On invalid receipt']"}
REBATE_CAMPAIGN_AS_CUSTOMIZE_AI_RECEIPT2 = {"//div[@title='Validate receipt / On invalid receipt']"}
REBATE_CAMPAIGN_AS_CUSTOMIZE_AI_ERROR = {"//span[normalize-space()='Validate receipt / On error']"}
REBATE_CAMPAIGN_AS_CUSTOMIZE_AI_ERROR2 = {"//div[@title='Validate receipt / On error']"}
REBATE_CAMPAIGN_AS_CUSTOMIZE_AI_VALID_RECEIPT = {"//span[normalize-space()='Validate receipt / On valid receipt']"}
REBATE_CAMPAIGN_AS_CUSTOMIZE_AI_VALID_RECEIPT2 = {"//div[@title='Validate receipt / On valid receipt']"}
REBATE_CAMPAIGN_AS_APPROVAL = {"//label[normalize-space()='Rebate Auto-Approval']"}
REBATE_CAMPAIGN_AS_VERIFICATION_CRITERIA = {"//span[contains(text(),'Select Verification Criteria')]"}
REBATE_CAMPAIGN_AS_VERIFICATION_CRITERIA_NEW = {"//span[@class='w-full max-w-full whitespace-nowrap text-ellipsis overflow-hidden text-primary']"}
REBATE_CAMPAIGN_AS_VERIFICATION_CRITERIA_NAME = {"//input[@placeholder='Enter name...']"}
REBATE_CAMPAIGN_AS_VERIFICATION_CRITERIA_RETAILER = {"//label[normalize-space()='Verify Retailers']"}
REBATE_CAMPAIGN_AS_VERIFICATION_CRITERIA_INCLUDE_RETAILER = {"//label[normalize-space()='Include Retailers from Experience']"}
REBATE_CAMPAIGN_AS_VERIFICATION_CRITERIA_ENTER_RETAILER = {"//input[@placeholder='Enter Retailers...']"}
REBATE_CAMPAIGN_AS_VERIFICATION_CRITERIA_RETAILER_ADD = {"//img[@alt='white-plus.svg']"}
REBATE_CAMPAIGN_AS_VERIFICATION_CRITERIA_LINE_ITEM = {"//label[normalize-space()='Verify Line Items']"}
REBATE_CAMPAIGN_AS_VERIFICATION_CRITERIA_LINE_TEM_NAME = {"//input[@placeholder='Enter Line Item name...']"}
REBATE_CAMPAIGN_AS_VERIFICATION_CRITERIA_LINE_TEM_NAME_ADD = {"//img[@class='ng-tns-c787443071-61']"}
REBATE_CAMPAIGN_AS_AUTO_RECEIPT = {"//label[normalize-space()='Rebate Auto-Approval']"}
REBATE_CAMPAIGN_AS_VERIFICATION_CRITERIA_LINE_ITEM_ADD= {"//img[@class='ng-tns-c787443071-61']"}
REBATE_CAMPAIGN_AS_VERIFICATION_CRITERIA_LINE_ITEM_PRICE = {"//label[normalize-space()='Verify Purchase Price']"}
REBATE_CAMPAIGN_AS_VERIFICATION_CRITERIA_LINE_ITEM_PRICE_min = {"//div[@class='p-field-checkbox modal-checkbox my-20 ng-tns-c1842535111-228 ng-valid ng-touched ng-dirty']//div[@class='verify-product-container indent-left-7 mt-6 ng-tns-c1842535111-228 ng-trigger ng-trigger-openClose ng-star-inserted']//div[1]//div[1]//input[1]"}
REBATE_CAMPAIGN_AS_VERIFICATION_CRITERIA_LINE_ITEM_PRICE_max = {"//label[normalize-space()='Verify Purchase Price']"}
REBATE_CAMPAIGN_AS_VERIFICATION_CRITERIA_LINE_ITEM_QUANTITY = {"//label[normalize-space()='Verify Quantity']"}
REBATE_CAMPAIGN_AS_VERIFICATION_CRITERIA_LINE_ITEM_NEW = {"//div[@class='line-item-btn ng-tns-c1842535111-53']"}
REBATE_CAMPAIGN_AS_VERIFICATION_CRITERIA_LINE_ITEM_DELETE = {"//span[@class='delete-btn ng-tns-c1842535111-53']"}
REBATE_CAMPAIGN_AS_VERIFICATION_CRITERIA_PURCHASE_DATE = {"//label[normalize-space()='Verify Purchase Date']"}
REBATE_CAMPAIGN_AS_VERIFICATION_CRITERIA_UNIQUENESS = {"//label[normalize-space()='Verify Uniqueness']"}
REBATE_CAMPAIGN_AS_VERIFICATION_CRITERIA_SAVE = {"//app-p-button[@class='ng-tns-c1842535111-53']//button[@type='button'][normalize-space()='Save']"}
REBATE_CAMPAIGN_AS_VERIFICATION_CRITERIA_BACK  = {"//button[@type='button']//label[contains(text(),'Verification Criteria')]"}
REBATE_CAMPAIGN_AS_SAVE = {"(//button[@type='button'][normalize-space()='Save'])[2]"}
REBATE_CAMPAIGN_AS_BACK = {"//label[normalize-space()='Advanced Settings']"}
REBATE_CAMPAIGN_BACK = {"//label[normalize-space()='Rebate Campaign']"}
REBATE_CAMPAIGN_SAVE_CHANGES = {"//button[normalize-space()='Save']"}
REBATE_CAMPAIGN_DISCARD = {"(//span[normalize-space()='DON'T SAVE'])[1]"}


### REBATE_SIGNUP MODULE ##
REBATE_SIGNUP_OPTION = {"xpath":"//span[normalize-space()='Rebate Signup Page']"}
REBATE_SIGNUP_SEARCH = {"xpath":"//input[@placeholder='Search Items...']"}
REBATE_SIGNUP_KEBAB = {"xpath":"//img[@class='menu-icon options-menu-icon']"}
REBATE_SIGNUP_DELETE = {"xpath":"//div[contains(text(),'Delete Module')]"}
REBATE_SIGNUP_DELETE_CONFIRM = {"xpath":"//span[normalize-space()='Delete']"}
REBATE_SIGNUP_DELETE_ALL = {"xpath":"//button[normalize-space()='Delete']"}
REBATE_SIGNUP_NEW_MODULE = {"xpath":"//button[normalize-space()='New Rebate Signup Page']"}
REBATE_SIGNUP_DIALOG = {"xpath":"//div[@role='dialog']"}
REBATE_SIGNUP_POPUP_MODULE_NAME= {"xpath":"//input[@placeholder='Enter module name...']"}
REBATE_SIGNUP_POPUP_CTA = {"xpath":"//input[@placeholder='Enter call to action...']"}
REBATE_SIGNUP_POPUP_EDITOR = {"xpath":"//app-editor[@REBATE_SIGNUPcontrolname='preLookup']//br"}
REBATE_SIGNUP_POPUP_ASETTING = {"css selector":".p-element.advanced-setting-icon.ng-tns-c202-12"}
REBATE_SIGNUP_POPUP_SAVE_BUTTON = {"css selector":"body > p-dynamicdialog:nth-child(10) > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > app-module-edit-popup:nth-child(1) > app-sms-modules-edit:nth-child(3) > form:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > app-p-button:nth-child(2) > button:nth-child(1)"}
REBATE_SIGNUP_LIST = {"xpath":"//td[@class='bold ng-star-inserted'][normalize-space()='release test']"}
REBATE_SIGNUP_ADD_EDIT_MODULE = {"xpath":"//span[@class='p-dialog-title align']"}
REBATE_SIGNUP_SIGNUP_HEADING ={"xpath":"//th[@id='moduleName ']"}
REBATE_SIGNUP_WHERE_USED = {"xpath":"//th[@id='whereUsed']"}
REBATE_SIGNUP_CALL_TO_ACTION = {"xpath":"//th[@id='callToAction']"}
REBATE_SIGNUP_COUNT = {"xpath","//h6[normalize-space()='Total AB 899 Modules']"}
REBATE_SIGNUP_CHECKBOX_LIST = {"xpath":"//p-checkbox[@class='ng-pristine ng-valid ng-touched']//div[@class='p-checkbox p-component']"}
REBATE_SIGNUP_DELETE_BUTTON = {"xpath":"//button[normalize-space()='Delete']"}
REBATE_SIGNUP_CONFIRM_DELETE_BUTTON = {"xpath":"//span[normalize-space()='Delete']"}
REBATE_SIGNUP_CONFIRM_DELETE_toast = {"xpath":"//div[@class='ng-tns-c3499315822-19 p-toast-message-text ng-star-inserted']"}
REBATE_NEW_SIGNUP = {"//span[@class='w-full max-w-full whitespace-nowrap text-ellipsis overflow-hidden text-primary']"}
REBATE_SIGNUP_NAME = {"//input[@placeholder='Enter module name...']"}
REBATE_SIGNUP_SHOW_BACKGROUND = {"//img[@class='long-answer-icon ng-tns-c1952139658-368']"}
REBATE_SIGNUP_SHOW_INSTRUCTION = {"//label[normalize-space()='Show Instructions']"}
REBATE_SIGNUP_CARD_TITLE = {"//input[@placeholder='Enter title here...']"}
REBATE_SIGNUP_ADD_STEP = {"//div[contains(@class, 'add-step-btn')]/span[text()='Add Step']"}
REBATE_SIGNUP_ADD_STEPP = {"name": "Add Step"}
REBATE_SIGNUP_REMOVE_STEP = {"//div[@class='instruction-messages ng-tns-c1952139658-42 ng-untouched ng-pristine ng-invalid ng-star-inserted']//span[@class='remove-step ng-tns-c1952139658-42'][normalize-space()='Remove Step']"}
REBATE_SIGNUP_REMOVE_STEPP = {"name": "Remove Step"}
REBATE_SIGNUP_DESCRIPTION = {"(//p)[2]"}
REBATE_SIGNUP_SMS_MARKETING = {"//label[normalize-space()='SMS Marketing Consent']"}
REBATE_SIGNUP_SMS_CONSENT = {"//p[contains(text(),'By entering your phone number or by sending us a t')]"}
REBATE_SIGNUP_CUSTOM_CTA = {"//label[normalize-space()='Customize Button CTA']"}
REBATE_SIGNUP_AS = {"//img[@alt='advance settings icon']"}
REBATE_SIGNUP_AS_DISABLE_OPTION = {"//label[normalize-space()='Disable ``Text to Opt-In`` on Mobile']"}
REBATE_SIGNUP_AS_DIM_BACKGROUND = {"//label[normalize-space()='Dim Background']"}
REBATE_SIGNUP_AS_SOCIAL_MEDIA = {"//label[normalize-space()='Social Media Icons']"}
REBATE_SIGNUP_AS_SEND_USER = {"//label[normalize-space()='Send Mobile Users Directly to Messaging App']"}
REBATE_SIGNUP_AS_LEGAL_TEXT = {"//label[normalize-space()='Customize legal text']"}
REBATE_SIGNUP_AS_LEGAL_TEXT_CONSENT = {"(//p[contains(text(),'By entering your phone number or by sending us a t')])[1]"}
REBATE_SIGNUP_SAVE = {"//button[normalize-space()='Save']"}
REBATE_SIGNUP_SAVE1 = {"class name": "primary small undefined p-button p-component"}
REBATE_SIGNUP_AS_BACK = {"//label[normalize-space()='Advanced Settings']"}
REBATE_SIGNUP_BACK = {"(//label[contains(text(),'Rebate Signup Page')])[2]"}
REBATE_SIGNUP_BACK2 = {"//button[@type='button']//label[contains(text(),'Rebate Signup Page')]"}
REBATE_SIGNUP_ROWPERPAGE_OPTION = {"xpath":"//div[@aria-label='dropdown trigger']"}
REBATE_SIGNUP_ROWPERPAGE_20 = {"xpath":"//span[@class='ng-star-inserted'][normalize-space()='20']"}
REBATE_SIGNUP_ROWPERPAGE_100 = {"xpath":"//span[normalize-space()='100']"}
REBATE_SIGNUP_ROWPERPAGE_1000 = {"xpath":"//span[normalize-space()='1000']"}
REBATE_SIGNUP_EDIT = {"xpath":"//div[@class='text']"}
REBATE_SIGNUP_DUPLICATE = {"xpath":"//img[@alt='Copy Module']"}
REBATE_SIGNUP_LOGOUT_BUTTON = {"xpath":"//img[@alt='logout']"}
REBATE_SIGNUP_FIELD = {"xpath":"//button[normalize-space()='Fields']"}

### REGISTRATION MODULE ##
REGISTRATION_MODULE_OPTION = "//span[normalize-space()='Registration']"
REGISTRATION_NOTIFICATION_ICON = "//div[@class='notification']"
REGISTRATION_SEARCH = "//input[@placeholder='Search Items...']"
REGISTRATION_FIRST_ROW = "//tbody/tr[1]"
REGISTRATION_FIELD_BUTTON = "//button[normalize-space()='Fields']"
REGISTRATION_FIELD_CONFIGURATION = "//*[@id='mainContent']/div[2]/div/app-registration-listing/div/app-table-search-filter/div/div/div[1]/div/div/div/div[1]/app-checkbox/div/p-checkbox"
REGISTRATION_FIELD_WHERE_USED = "//*[@id='mainContent']/div[2]/div/app-registration-listing/div/app-table-search-filter/div/div/div[1]/div/div/div/div[2]/app-checkbox"
REGISTRATION_ALL_CHECKBOX = "//*[@id='selectAllCol']/app-checkbox/div/p-checkbox"
REGISTRATION_NEW_MODULE = "//button[normalize-space()='New Registration Module']"
REGISTRATION_POPUP_MODULE_NAME= "//input[@placeholder='Enter module name...']"
REGISTRATION_POPUP_CTA = "//input[@placeholder='Enter call to action...']"
REGISTRATION_POPUP_EDITOR = "//app-editor[@REGISTRATIONcontrolname='preLookup']//br"
REGISTRATION_POPUP_ASETTING = "/html/body/p-dynamicdialog/div/div/div[2]/app-module-edit-popup/app-registration-edit/form/div/div[1]/div[1]/div/app-p-button[1]/button"
REGISTRATION_POPUP_SAVE_BUTTON = "/html/body/p-dynamicdialog/div/div/div[2]/app-module-edit-popup/app-registration-edit/form/div/div[1]/div[1]/div/app-p-button[2]/button"
REGISTRATION_LIST = "/html/body/app-root/app-brand-main/div/div/div[2]/div[2]/div/app-registration-listing/p-table/div/div/table/tbody/tr[1]/td[2]"
REGISTRATION_LIST_KEBAB = "/html/body/app-root/app-brand-main/div/div/div[2]/div[2]/div/app-registration-listing/p-table/div/div/table/tbody/tr[1]/td[6]/app-row-options/div"
REGISTRATION_EDIT_OPTION = "/html/body/div[4]/div/div[2]/div"
REGISTRATION_DELETE_OPTION = "//div[contains(text(),'Delete Module')]"
REGISTRATION_DUPLICATE =  "//*[@id='style-1']/div/div[1]/div[2]/div/span/img"
REGISTRATION_POPUP_CROSS = "/html/body/p-dynamicdialog/div/div/div[2]/app-module-edit-popup/div[1]/div/button/span"
REGISTRATION_ADD_EDIT_MODULE = "//span[@class='p-dialog-title align']"
REGISTRATION_CONFIGURATION_HEADING ="//th[@id='configName']"
REGISTRATION_WHERE_USED = "//th[@id='whereUsed']"
REGISTRATION_COUNT = "//h6[normalize-space()='Total Registration Modules']"
REGISTRATION_CHECKBOX_LIST = "//p-checkbox[@class='ng-pristine ng-valid ng-touched']//div[@class='p-checkbox p-component']"
REGISTRATION_DELETE_BUTTON = "//button[normalize-space()='Delete']"
REGISTRATION_CONFIRM_DELETE_BUTTON = "//span[normalize-space()='Delete']"
REGISTRATION_AS_MULTIPLE_TEXT = "//input[@placeholder='Call to Action']"
REGISTRATION_CONFIRM_DELETE_toast = "//div[@class='ng-tns-c3499315822-19 p-toast-message-text ng-star-inserted']"
REGISTRATION_AS_CUSTOM_CONFIRM_TEXT = "//textarea[@placeholder='Enter confirmation message...']"
REGISTRATION_AS_MARKETING = "//label[normalize-space()='Email Marketing Consent']"
REGISTRATION_AS_MARKETING_CONSENT = "//p[contains(text(),'Sign me up for marketing emails from SQAE Test mod')]"
REGISTRATION_AS_MARKETING_REQUIRED = "//label[normalize-space()='Make Required']"
REGISTRATION_AS_MARKETING_DEFAULT = "//*[@id='style-11']/div/div[2]/div[3]/div[2]/div[2]/app-checkbox/div/p-checkbox/div"
REGISTRATION_AS_TERM = "//label[normalize-space()='Terms & Privacy Consent']"
REGISTRATION_AS_TERM_CONSENT = "//p[contains(text(),'I confirm that i have read and agree to')]"
REGISTRATION_AS_TERM_REQUIRED = "//app-checkbox[@name='Make_Required']//p-checkbox[@class='ng-valid ng-dirty ng-touched']"
REGISTRATION_AS_TERM_DEFAULT = "//app-checkbox[@name='Checked_by_Default']//p-checkbox[@class='ng-valid ng-dirty ng-touched']"
REGISTRATION_AS_PROFILE = "//label[normalize-space()='Ask to Complete Profile']"
REGISTRATION_AS_PROFILE_NAME = "//label[normalize-space()='Name']"
REGISTRATION_AS_PROFILE_PHONE = "//label[normalize-space()='Phone Number']"
REGISTRATION_AS_PROFILE_PHONE_CONSENT = "//label[normalize-space()='SMS Marketing Consent']"
REGISTRATION_AS_PROFILE_PHONE_CONSENT_TEXT = "//p[contains(text(),'By signing up you agree to receive recurring autom')]"
REGISTRATION_AS_PROFILE_PHONE_DEFAULT = "//label[normalize-space()='Require Consent']"
REGISTRATION_AS_PROFILE_PHONE_REQUIRED = "//label[@for='I983MK']"
REGISTRATION_AS_GOOGLE_SIGNUP = "//label[normalize-space()='Hide Google Signup Option']"
REGISTRATION_All_DELETE = "//button[normalize-space()='Delete']"
REGISTRATION_AS_PURCHASE = "//label[normalize-space()='Require Purchase Details']"
REGISTRATION_AS_PURCHASE_TEXT = "//textarea[@placeholder='Please add purchase details to complete registration.']"
REGISTRATION_AS_PURCHASE_NAME = "//body[1]/p-dynamicdialog[1]/div[1]/div[1]/div[1]/app-products-edit-popup[1]/div[2]/div[2]/div[1]/app-registration-edit[1]/form[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[8]/div[2]/div[1]/app-checkbox[1]/div[1]/p-checkbox[1]"
REGISTRATION_AS_PURCHASE_PHONE = "//app-checkbox[@name='purchaseTemplate.phoneNo']//p-checkbox[@class='ng-untouched ng-pristine ng-valid']"
REGISTRATION_AS_PURCHASE_PHONE_CONSENT = "//*[@id='style-11']/div/div[2]/div[8]/div[3]/div/div/div/app-checkbox/div/label"
REGISTRATION_AS_PURCHASE_PHONE_CONSENT_TEXT = "//p[contains(text(),'Sign up for texts. By checking this box, I agree t')]"
REGISTRATION_AS_PURCHASE_PHONE_REQUIRED = "//label[@for='66UHC6']"
REGISTRATION_AS_PURCHASE_PHONE_DEFAULT = "//label[@for='IUA95T']"
REGISTRATION_AS_PURCHASE_NAME1 = "//*[@id='style-11']/div/div[2]/div[8]/div[2]/div/app-checkbox/div/label"
REGISTRATION_AS_PURCHASE_PDATE = "//label[normalize-space()='Purchase Date']"
REGISTRATION_AS_PURCHASE_PDATE_DYNAMIC = "/html/body/p-dynamicdialog/div/div/div[2]/app-module-edit-popup/app-registration-edit/form/div/div[1]/div[2]/div[1]/div/div[2]/div[8]/div[4]/div/div/app-date-validations/form/div[1]/app-checkbox/div/label"
REGISTRATION_AS_PURCHASE_PDATE_DYNAMIC_BEFORE = "//input[@name='daysBeforeCurrentDate']"
REGISTRATION_AS_PURCHASE_PDATE_DYNAMIC_AFTER = "//input[@name='daysAfterCurrentDate']"
REGISTRATION_AS_PURCHASE_PDATE_FIXED = "//label[normalize-space()='Fixed Date Window']"
REGISTRATION_AS_PURCHASE_QUANTITY = "//label[normalize-space()='Quantity']"
REGISTRATION_AS_PURCHASE_PLACE_PURCHASE = "//label[normalize-space()='Place of Purchase']"
REGISTRATION_AS_PURCHASE_PLACE_RETAIL_CHANNEL = "/html/body/p-dynamicdialog/div/div/div[2]/app-module-edit-popup/app-registration-edit/form/div/div[1]/div[2]/div[1]/div/div[2]/div[8]/div[6]/div/div/div/app-retail-channel-dropdown/div/app-multiselect/div/p-multiselect/div[2]"
REGISTRATION_AS_PURCHASE_PLACE_RETAIL_CHANNEL_ALL = "//label[normalize-space()='All Channels']"
REGISTRATION_AS_PURCHASE_PLACE_RETAIL_CHANNEL_NEW = "//label[normalize-space()='New Channel']"
REGISTRATION_AS_PURCHASE_PLACE_RETAIL_CHANNEL_NEW_NAME = "//input[@id='name']"
REGISTRATION_AS_PURCHASE_PLACE_RETAIL_CHANNEL_NEW_NAME_SAVE = "//button[@class='full-width full-width-button medium primary p-button p-component']"
REGISTRATION_AS_PURCHASE_PLACE_RETAIL_CHANNEL_OPTION = "//img[@class='close-icon']"
REGISTRATION_AS_PURCHASE_SERIAL_NUM = "//label[normalize-space()='Serial Number']"
REGISTRATION_AS_PURCHASE_PROOF = "//label[normalize-space()='Proof of Purchase (Receipt Upload)']"
REGISTRATION_AS_PURCHASE_PROOF_TEXT = "//input[@placeholder='Call to Action...']"
REGISTRATION_AS_REQUIRED_APPROVAL = "//label[normalize-space()='Require Approval']"
REGISTRATION_AS_VERIFICATION_CRITERIA = "//span[contains(text(),'Select Verification Criteria')]"
AS_VERIFICATION_CRITERIA_OPTION = "//span[normalize-space()='Test Criteria']"
REGISTRATION_AS_VERIFICATION_CRITERIA_NEW = "//span[@class='w-full max-w-full whitespace-nowrap text-ellipsis overflow-hidden text-primary']"
REGISTRATION_AS_VERIFICATION_CRITERIA_NAME = "//input[@placeholder='Enter name...']"
REGISTRATION_AS_VERIFICATION_CRITERIA_RETAILER = "//label[normalize-space()='Verify Retailers']"
REGISTRATION_AS_VERIFICATION_CRITERIA_INCLUDE_RETAILER = "//label[normalize-space()='Include Retailers from Experience']"
REGISTRATION_AS_VERIFICATION_CRITERIA_ENTER_RETAILER = "//input[@placeholder='Enter Retailers...']"
REGISTRATION_AS_VERIFICATION_CRITERIA_RETAILER_ADD = "//img[@alt='white-plus.svg']"
REGISTRATION_AS_VERIFICATION_CRITERIA_LINE_ITEM = "//label[normalize-space()='Verify Line Items']"
REGISTRATION_AS_VERIFICATION_CRITERIA_LINE_TEM_NAME = "//input[@placeholder='Enter Line Item name...']"
REGISTRATION_AS_VERIFICATION_CRITERIA_LINE_TEM_NAME_ADD = "//img[@class='ng-tns-c787443071-61']"
REGISTRATION_AS_VERIFICATION_CRITERIA_LINE_ITEM_PRICE = "//label[normalize-space()='Verify Purchase Price']"
REGISTRATION_AS_VERIFICATION_CRITERIA_LINE_ITEM_PRICE_min = "//div[@class='p-field-checkbox modal-checkbox my-20 ng-tns-c1842535111-228 ng-valid ng-touched ng-dirty']//div[@class='verify-product-container indent-left-7 mt-6 ng-tns-c1842535111-228 ng-trigger ng-trigger-openClose ng-star-inserted']//div[1]//div[1]//input[1]"
REGISTRATION_AS_VERIFICATION_CRITERIA_LINE_ITEM_PRICE_max = "//label[normalize-space()='Verify Purchase Price']"
REGISTRATION_AS_VERIFICATION_CRITERIA_LINE_ITEM_QUANTITY = "//label[normalize-space()='Verify Quantity']"
REGISTRATION_AS_VERIFICATION_CRITERIA_LINE_ITEM_NEW = "//div[@class='line-item-btn ng-tns-c1842535111-53']"
REGISTRATION_AS_VERIFICATION_CRITERIA_LINE_ITEM_DELETE = "//span[@class='delete-btn ng-tns-c1842535111-53']"
REGISTRATION_AS_VERIFICATION_CRITERIA_PURCHASE_DATE = "//label[normalize-space()='Verify Purchase Date']"
REGISTRATION_AS_VERIFICATION_CRITERIA_UNIQUENESS = "//label[normalize-space()='Verify Uniqueness']"
REGISTRATION_AS_VERIFICATION_CRITERIA_SAVE = "//app-p-button[@class='ng-tns-c1842535111-53']//button[@type='button'][normalize-space()='Save']"
REGISTRATION_AS_VERIFICATION_CRITERIA_BACK = "//button[@type='button']//label[contains(text(),'Verification Criteria')]"
REGISTRATION_AS_SAVE = "/html/body/p-dynamicdialog/div/div/div/app-products-edit-popup/div[2]/div[2]/div[1]/app-registration-edit/form/div/div/div/div[1]/div/div[1]/div[2]/app-p-button/button"
REGISTRATION_AS_SAVE_CONFIRM = "//span[normalize-space()='Save']"
REGISTRATION_AS_back = "//label[normalize-space()='Advanced Settings']"
REGISTRATION_SAVE = "//button[normalize-space()='Save']"
REGISTRATION_NAME = "//input[@placeholder='Enter module name...']"
REGISTRATION_CTA = "//div[@title='Register']"
REGISTRATION_CTA_REGISTER = "//span[@class='w-full max-w-full whitespace-nowrap text-ellipsis overflow-hidden'][normalize-space()='Register']"
REGISTRATION_CTA_ACTIVATE = "//span[normalize-space()='Activate']"
REGISTRATION_CTAa = "//div[@title='Activate']"
REGISTRATION_CTA_SIGNUP = "//span[normalize-space()='Sign Up']"
REGISTRATION_CTAs = "//div[@title='Sign Up']"
REGISTRATION_CTA_DONATE = "//span[normalize-space()='Donate']"
REGISTRATION_CTAd = "//div[@title='Donate']"
REGISTRATION_CTA_CUSTOM = "//span[@class='w-full max-w-full whitespace-nowrap text-ellipsis overflow-hidden'][normalize-space()='Custom']"
REGISTRATION_CTA_INPUT = "//input[@placeholder='Enter Custom Call to Action']"
REGISTRATION_DESCRIPTION = "(//p)[2]"
REGISTRATION_FORM = "//span[contains(text(),'Select a Module')]"
REGISTRATION_FORM_SEARCH = "//input[@placeholder='Search...']"
REGISTRATION_FORM_SEARCH_OPTION = "//span[@class='w-full max-w-full whitespace-nowrap text-ellipsis overflow-hidden']"
REGISTRATION_MODULE_FORM_SEARCH = "//input[@placeholder='Search...']"
REGISTRATION_MODULE_FORM_SEARCH_OPTION = "//span[contains(text(),'Registration form')]"
REGISTRATION_AS = "//img[@alt='advance settings icon']"
REGISTRATION_AS_SHOW_OTHER = "//label[normalize-space()='Show other modules after Registration']"
REGISTRATION_AS_MULTIPLE = "//label[normalize-space()='Enable Multiple Registrations']"
REGISTRATION_AS_CUSTOM_CONFIRM = "//label[normalize-space()='Customize Confirmation Message']"
REBATE_CAMPAIGN_KEBAB = "//img[@class='menu-icon options-menu-icon']"
REBATE_CAMPAIGN_DELETE = "//div[contains(text(),'Delete Module')]"
REBATE_CAMPAIGN_DELETE_CONFIRM = "//span[normalize-space()='Delete']"
REBATE_CAMPAIGN_DELETE_ALL = "//button[normalize-space()='Delete']"

### REVIEW MODULE ##
REVIEW_OPTION = {"xpath":"////div[@id='adminDashboardContainer']/nav/ul/li[2]"}
REVIEW_SEARCH = {"xpath":"//input[@placeholder='Search Items...']"}
REVIEW_NEW_MODULE = {"xpath":"//span[normalize-space()='New AB 899 Module']"}
REVIEW_DIALOG = {"xpath":"//div[@role='dialog']"}
REVIEW_POPUP_MODULE_NAME= {"xpath":"//input[@placeholder='Enter module name...']"}
REVIEW_POPUP_CTA = {"xpath":"//input[@placeholder='Enter call to action...']"}
REVIEW_POPUP_EDITOR = {"xpath":"//app-editor[@REVIEWcontrolname='preLookup']//br"}
REVIEW_POPUP_ASETTING = {"css selector":".p-element.advanced-setting-icon.ng-tns-c202-12"}
REVIEW_POPUP_SAVE_BUTTON = {"css selector":"p-button[type='button']"}
REVIEW_LIST = {"xpath":"//td[@class='bold ng-star-inserted'][normalize-space()='release test']"}
REVIEW_ADD_EDIT_MODULE = {"xpath":"//span[@class='p-dialog-title align']"}
REVIEW_MODULE_HEADING ={"xpath":"//th[@id='moduleName']"}
REVIEW_WHERE_USED = {"xpath":"//th[@id='whereUsed']"}
REVIEW_CALL_TO_ACTION = {"xpath":"//th[@id='callToAction']"}
REVIEW_COUNT = {"xpath","//h6[normalize-space()='Total AB 899 Modules']"}
REVIEW_CHECKBOX_LIST = {"xpath":"//p-checkbox[@class='ng-pristine ng-valid ng-touched']//div[@class='p-checkbox p-component']"}
REVIEW_DELETE_BUTTON = {"xpath":"//button[normalize-space()='Delete']"}
REVIEW_CONFIRM_DELETE_BUTTON = {"xpath":"//span[normalize-space()='Delete']"}
REVIEW_CONFIRM_DELETE_toast = {"xpath":"//div[@class='ng-tns-c3499315822-19 p-toast-message-text ng-star-inserted']"}

### SWEEPSTAKES MODULE ##
## SWEEPSTAKES MODULE ##
SWEEPSTAKES_OPTION = "//*[@id='adminDashboardContainer']/nav/ul[1]/li[5]/ul/li[11]/span"
SWEEPSTAKES_TITLE = "//h1[normalize-space()='Sweepstakes']"
SWEEPSTAKES_SEARCH = "//input[@placeholder='Search Items...']"
SWEEPSTAKES_NEW_MODULE = "//button[normalize-space()='New Sweepstakes']"
SWEEPSTAKES_DIALOG = "//div[@role='dialog']"
SWEEPSTAKES_POPUP_MODULE_NAME= "//input[@placeholder='Enter module name...']"
SWEEPSTAKES_POPUP_CTA = "//input[@placeholder='Enter call to action...']"
SWEEPSTAKES_POPUP_EDITOR = "//*[@id='style-1']/div/div[4]/app-form-control/div/app-editor/div/div[2]/div/p"
SWEEPSTAKES_POPUP_ASETTING = ".p-element.advanced-setting-icon.ng-tns-c202-12"
SWEEPSTAKES_POPUP_SAVE_BUTTON = "/html/body/p-dynamicdialog/div/div/div[2]/app-module-edit-popup/app-sweepstakes-edit/form/div/div[1]/div[1]/div/app-p-button[2]/button"
SWEEPSTAKES_LIST = "/html/body/app-root/app-brand-main/div/div/div[2]/div[2]/div/app-sweepstakes-listing/p-table/div/div/table/tbody/tr[1]/td[2]"
SWEEPSTAKES_KEBAB_MENU = "/html/body/app-root/app-brand-main/div/div/div[2]/div[2]/div/app-sweepstakes-listing/p-table/div/div/table/tbody/tr/td[7]/app-row-options/div/img"
SWEEPSTAKES_ADD_EDIT_MODULE = "//span[@class='p-dialog-title align']"
SWEEPSTAKES_EDIT_MODULE = "//div[contains(text(),'Edit Module')]"
SWEEPSTAKES_MODULE_HEADING ="//*[@id='warrantyName']"
SWEEPSTAKES_WHERE_USED = "//th[@id='whereUsed']"
SWEEPSTAKES_CALL_TO_ACTION = "//th[@id='callToAction']"
SWEEPSTAKES_COUNT = "xpath","//h6[normalize-space()='Total AB 899 Modules']"
SWEEPSTAKES_CHECKBOX_LIST = "//p-checkbox[@class='ng-pristine ng-valid ng-touched']//div[@class='p-checkbox p-component']"
SWEEPSTAKES_DELETE_BUTTON = "//div[contains(text(),'Delete Module')]"
SWEEPSTAKES_DELETEALL_BUTTON = "//button[normalize-space()='Delete']"
SWEEPSTAKES_CONFIRM_DELETE_BUTTON = "/html/body/app-root/app-brand-main/div/app-confirmdialog/div/div/div/div[4]/p-button[2]/button/span"
SWEEPSTAKES_CONFIRM_DELETE_toast = "//div[@class='ng-tns-c3499315822-19 p-toast-message-text ng-star-inserted']"
SWEEPSTAKES_FIELD_BUTTON = "//button[normalize-space()='Fields']"
SWEEPSTAKES_SELECT_ALL_CHECKBOXES = "//*[@id='selectAllCol']/app-checkbox/div"
SWEEPSTAKES_ROWPERPAGE_OPTION = "/html/body/app-root/app-brand-main/div/div/div[2]/div[2]/div/app-sweepstakes-listing/p-table/div/p-paginator/div/p-select/div/chevrondownicon"
SWEEPSTAKES_ROWPERPAGE_20 = "//span[@class='ng-star-inserted'][normalize-space()='20']"
SWEEPSTAKES_ROWPERPAGE_100 = "//span[normalize-space()='100']"
SWEEPSTAKES_ROWPERPAGE_1000 = "//span[normalize-space()='1000']"
SWEEPSTAKES_POPUP_CLOSE = "//span[@class='p-dialog-header-close-icon pi pi-times']"
SWEEPSTAKES_FIELD_SWEEPSTAKES_NAME  = "//*[@id='mainContent']/div[2]/div/app-sweepstakes-listing/div/app-table-search-filter/div/div/div[1]/div/div/div/div[1]/app-checkbox/div/p-checkbox"
SWEEPSTAKES_FIELD_WHERE_USED = "//*[@id='mainContent']/div[2]/div/app-sweepstakes-listing/div/app-table-search-filter/div/div/div[1]/div/div/div/div[2]/app-checkbox/div/p-checkbox"
SWEEPSTAKES_FIELD_SWEEPSTAKES_DURATION = "//*[@id='mainContent']/div[2]/div/app-sweepstakes-listing/div/app-table-search-filter/div/div/div[1]/div/div/div/div[3]/app-checkbox/div/p-checkbox"
SWEEPSTAKES_FIELD_CTA = "//*[@id='mainContent']/div[2]/div/app-sweepstakes-listing/div/app-table-search-filter/div/div/div[1]/div/div/div/div[4]/app-checkbox/div/p-checkbox"
SWEEPSTAKES_POPUP_DUPLICATE  = "//*[@id='style-1']/div/div[1]/div[2]/div/span"


### VIDEO MODULE ##
VIDEO_OPTION = {"xpath":"//span[normalize-space()='Video']"}
VIDEO_HEADING = {"xpath":"//h1[normalize-space()='Video']"}
VIDEO_NOTIFICATION_ICON = {"xpath":"//*[@id='mainContent']/div[1]/div[3]/div/div[1]"}
VIDEO_LOGOUT_BUTTON = {"xpath":"//*[@id='mainContent']/div[1]/div[3]/div/div[2]/img"}
VIDEO_SEARCH = {"xpath":"//input[@placeholder='Search Items...']"}
VIDEO_FIELDS_BUTTON = {"xpath":"//button[normalize-space()='Fields']"}
VIDEO_NEW_MODULE = {"xpath":"//button[normalize-space()='New Video Module']"}
VIDEO_DIALOG = {"xpath":"//div[@role='dialog']"}
VIDEO_FIELD_MODULE_NAME = {"xpath":"/html/body/app-root/app-brand-main/div/div/div[2]/div[2]/div/app-video-listing/div/app-table-search-filter/div/div/div[1]/div/div/div/div[1]/app-checkbox/div/p-checkbox/div/input"}
VIDEO_FIELD_WHERE_USED = {"xpath":"/html/body/app-root/app-brand-main/div/div/div[2]/div[2]/div/app-video-listing/div/app-table-search-filter/div/div/div[1]/div/div/div/div[2]/app-checkbox/div/p-checkbox/div/input"}
VIDEO_FIELD_FILE_NAME = {"xpath":"/html/body/app-root/app-brand-main/div/div/div[2]/div[2]/div/app-video-listing/div/app-table-search-filter/div/div/div[1]/div/div/div/div[4]/app-checkbox/div/p-checkbox/div/input"}
VIDEO_FIELD_CTA = {"xpath":"/html/body/app-root/app-brand-main/div/div/div[2]/div[2]/div/app-video-listing/div/app-table-search-filter/div/div/div[1]/div/div/div/div[3]/app-checkbox/div/p-checkbox/div/input/div[@role='dialog']"}
# VIDEO_ALL_CHECKBOX
# VIDEO_FILE_NAME


VIDEO_POPUP_MODULE_NAME= {"xpath":"//input[@placeholder='Enter module name...']"}
VIDEO_POPUP_CTA = {"xpath":"//input[@placeholder='Enter call to action...']"}
VIDEO_POPUP_EDITOR = {"xpath":"//app-editor[@VIDEOcontrolname='preLookup']//br"}
VIDEO_POPUP_ASETTING = {"css selector":".p-element.advanced-setting-icon.ng-tns-c202-12"}
VIDEO_POPUP_SAVE_BUTTON = {"css selector":"p-button[type='button']"}
VIDEO_LIST = {"xpath":"//td[@class='bold ng-star-inserted'][normalize-space()='release test']"}
VIDEO_ADD_EDIT_MODULE = {"xpath":"//span[@class='p-dialog-title align']"}
VIDEO_MODULE_HEADING ={"xpath":"//th[@id='moduleName']"}
VIDEO_WHERE_USED = {"xpath":"//th[@id='whereUsed']"}
VIDEO_CALL_TO_ACTION = {"xpath":"//th[@id='callToAction']"}
VIDEO_COUNT = {"xpath","//h6[normalize-space()='Total AB 899 Modules']"}
VIDEO_CHECKBOX_LIST = {"xpath":"//p-checkbox[@class='ng-pristine ng-valid ng-touched']//div[@class='p-checkbox p-component']"}
VIDEO_DELETE_BUTTON = {"xpath":"//button[normalize-space()='Delete']"}
VIDEO_CONFIRM_DELETE_BUTTON = {"xpath":"//span[normalize-space()='Delete']"}
VIDEO_CONFIRM_DELETE_toast = {"xpath":"//div[@class='ng-tns-c3499315822-19 p-toast-message-text ng-star-inserted']"}

### WARRANTY MODULE ##

WARRANTY_OPTION = {"xpath":"//span[normalize-space()='Warranty']"}
WARRANTY_TITLE = {"xpath":"//h1[normalize-space()='Warranty']"}
WARRANTY_LOGOUT_BUTTON = {"xpath":"//*[@id='mainContent']/div[1]/div[3]/div/div[2]/img"}
Warranty_NOTIFICATION_ICON = {"//*[@id='mainContent']/div[1]/div[3]/div/div[1]"}
WARRANTY_SEARCH = {"xpath":"//input[@placeholder='Search Items...']"}
WARRANTY_NEW_MODULE = {"xpath":"//button[normalize-space()='New Warranty Module']"}
WARRANTY_DIALOG = {"xpath":"//div[@role='dialog']"}
WARRANTY_POPUP_MODULE_NAME= {"xpath":"//*[@id='style-1']/div/div[1]/div[1]/app-form-control/div/input"}
WARRANTY_POPUP_CTA = {"xpath":"//input[@placeholder='Enter call to action...']"}
WARRANTY_DURATION_DAYS = {"xpath":"/html/body/p-dynamicdialog/div/div/div[2]/app-module-edit-popup/app-warranty-edit/form/div/div[1]/div[2]/div/div[3]/div/app-form-control[1]/div/input"}
WARRANTY_DURATION_TYPE = {"xpath":"/html/body/p-dynamicdialog/div/div/div[2]/app-module-edit-popup/app-warranty-edit/form/div/div[1]/div[2]/div/div[3]/div/app-form-control[2]/div/app-dropdown/div/p-select/span/div"}
WARRANTY_DURATION_TYPE_DAYS = {"xpath":"//span[contains(text(),'Days')]"}
WARRANTY_DURATION_TYPE_YEARS= {"xpath":"//span[normalize-space()='Years']"}
WARRANTY_DURATION_TYPE_MONTHS= {"xpath":"//span[normalize-space()='Months']"}
WARRANTY_DURATION_TYPE_LIFETIME= {"xpath":"//span[normalize-space()='Years']"}
WARRANTY_POPUP_IMAGE_EDITOR = {"xpath":"//*[@id='style-1']/div/div[4]/app-form-control/div/app-editor/div/div[2]/div/p"}
WARRANTY_POPUP_IMAGE_EDITOR1 = {"xpath":"//div[@class='fr-buttons fr-tabs']//button[@id='imageManager-2']//*[name()='svg']//*[name()='path' and contains(@d,'M20,6h-7l-')]"}
WARRANTY_POPUP_IMAGE_EDITOR2 = {"xpath":"//div[@class='fr-image-container fr-image-0']//*[name()='svg']"}
WARRANTY_LIST_KEBAB = {"xpath":"/html/body/app-root/app-brand-main/div/div/div[2]/div[2]/div/app-warranty-listing/p-table/div/div/table/tbody/tr[1]/td[8]/app-row-options/div"}
WARRANTY_EDIT_OPTION = {"xpath":"//div[contains(text(),'Edit Module')]"}
WARRANTY_INCLUDE_CLAIM = {"xpath":"/html/body/p-dynamicdialog/div/div/div[2]/app-module-edit-popup/app-warranty-edit/form/div/div[1]/div[2]/div/div[5]/div/app-checkbox/div/label"}
WARRANTY_CLAIM_TEXT = {"xpath":"/html/body/p-dynamicdialog/div/div/div[2]/app-module-edit-popup/app-warranty-edit/form/div/div[1]/div[2]/div/div[5]/div[2]/app-form-control[1]/div/input"}
WARRANTY_CLAIM_LINK = {"xpath":"/html/body/p-dynamicdialog/div/div/div[2]/app-module-edit-popup/app-warranty-edit/form/div/div[1]/div[2]/div/div[5]/div[2]/app-form-control[2]/div/input"}
WARRANTY_MULLBERY_CHECK = {"xpath":"/html/body/p-dynamicdialog/div/div/div[2]/app-module-edit-popup/app-warranty-edit/form/div/div[1]/div[2]/div/div[6]/div[1]/app-checkbox/div/label"}
WARRANTY_HEADER_TEXT = {"xpath":"//*[@id='style-1']/div/div[6]/div[2]/app-form-control[1]/div/input"}
WARRANTY_TEXT_BODY  = {"xpath":"//*[@id='style-1']/div/div[6]/div[2]/app-form-control[2]/div/textarea"}
WARRANTY_EXTENTION_CTA = {"xpath":"//*[@id='style-1']/div/div[6]/div[2]/app-form-control[3]/div/input"}
WARRANTY_AS_SHOW_STATUS  = {"xpath":"//*[@id='style-1']/div[1]/div/div[2]/div/div[1]/app-checkbox/div/label"}
WARRANTY_AS_DURATION_SCREEN = {"xpath":"//*[@id='style-1']/div[1]/div/div[2]/div/div[2]/app-checkbox/div/label"}
WARRANTY_AS_CUSTOMIZE_STATE = {"xpath":"//*[@id='style-1']/div[1]/div/div[2]/div/div[3]/app-checkbox/div/label"}
WARRANTY_AS_CUSTOMIZE_STATE_PENDING = {"xpath":"//*[@id='style-1']/div[1]/div/div[2]/div/div[3]/div/div[1]/textarea"}
WARRANTY_AS_CUSTOMIZE_STATE_DENIED = {"xpath":"//*[@id='style-1']/div[1]/div/div[2]/div/div[3]/div/div[2]/textarea"}
WARRANTY_AS_CUSTOMIZE_POST_CTA = {"xpath":"//*[@id='style-1']/div[1]/div/div[2]/div/div[4]/app-checkbox/div/label"}
WARRANTY_AS_CUSTOMIZE_POST_CTA_TEXT = {"xpath":"//*[@id='style-1']/div[1]/div/div[2]/div/div[4]/div/textarea"}
WARRANTY_AS_CUSTOMIZE_COLOUR = {"xpath":"//*[@id='style-1']/div[1]/div/div[2]/div/div[5]/app-modules-theme-selector/div/div/app-checkbox/div/label"}
WARRANTY_AS = {"xpath":"/html/body/p-dynamicdialog/div/div/div[2]/app-module-edit-popup/app-warranty-edit/form/div/div[1]/div[1]/div/app-p-button[1]/button/img"}
WARRANTY_AS_BACK = {"xpath":"//*[@id='style-1']/div[1]/div/div[1]/div[1]/app-p-button/button/label"}
WARRANTY_AS_SAVE = {"xpath":"//*[@id='style-1']/div[1]/div/div[1]/div[2]/app-p-button/button"}
WARRANTY_POPUP_SAVE_BUTTON = {"xpath":"/html/body/p-dynamicdialog/div/div/div[2]/app-module-edit-popup/app-warranty-edit/form/div/div[1]/div[1]/div/app-p-button[2]/button"}
WARRANTY_POPUP_DUPLICATE = {"xpath":"//*[@id='style-1']/div/div[1]/div[2]/div/span/img"}
WARRANTY_POPUP_CROSS = {"xpath":"/html/body/p-dynamicdialog/div/div/div[2]/app-module-edit-popup/div[1]/div/button/span"}
WARRANTY_AS_SAVE_BUTTON = {"css selector":"p-button[type='button']"}
WARRANTY_LIST = {"xpath":"/html/body/app-root/app-brand-main/div/div/div[2]/div[2]/div/app-warranty-listing/p-table/div/div/table/tbody/tr[1]/td[1]"}
WARRANTY_ADD_EDIT_MODULE = {"xpath":"//span[@class='p-dialog-title align']"}
WARRANTY_WARRANTY_NAME ={"xpath":"//th[@id='warrantyName']"}
WARRANTY_WHERE_USED = {"xpath":"//th[@id='whereUsed']"}
WARRANTY_DURATION = {"xpath":"//th[@id='warrantyDuration']"}
WARRANTY_CALL_TO_ACTION = {"xpath":"//th[@id='callToAction']"}
WARRANTY_COUNT = {"xpath","//h6[normalize-space()='Total AB 899 Modules']"}
WARRANTY_CHECKBOX_LIST = {"xpath":"//p-checkbox[@class='ng-pristine ng-valid ng-touched']//div[@class='p-checkbox p-component']"}
WARRANTY_DELETE_BUTTON = {"xpath":"//div[contains(text(),'Delete Module')]"}
WARRANTY_DELETEALL_BUTTON = {"xpath":"//*[@id='mainContent']/div[2]/div/app-warranty-listing/div/div/div[1]/div/app-p-button/button"}
WARRANTY_CONFIRM_DELETE_BUTTON = {"xpath":"//span[normalize-space()='Delete']"}
WARRANTY_CONFIRM_DELETE_toast = {"xpath":"//div[@class='ng-tns-c3499315822-19 p-toast-message-text ng-star-inserted']"}
WARRANTY_FIELD_BUTTON = {"xpath":"//*[@id='mainContent']/div[2]/div/app-warranty-listing/div/app-table-search-filter/div/div/div[1]/app-p-button/button"}
WARRANTY_FIELD_WARRANTY_NAME = {"xpath":"//*[@id='mainContent']/div[2]/div/app-warranty-listing/div/app-table-search-filter/div/div/div[1]/div/div/div/div[1]/app-checkbox/div/p-checkbox/div"}
WARRANTY_FIELD_WHERE_USED = {"xpath":"//*[@id='mainContent']/div[2]/div/app-warranty-listing/div/app-table-search-filter/div/div/div[1]/div/div/div/div[2]/app-checkbox/div/p-checkbox/div"}
WARRANTY_FIELD_WARRANTY_DURATION = {"xpath":"//*[@id='mainContent']/div[2]/div/app-warranty-listing/div/app-table-search-filter/div/div/div[1]/div/div/div/div[3]/app-checkbox/div/p-checkbox/div"}
WARRANTY_FIELD_CTA = {"xpath":"//*[@id='mainContent']/div[2]/div/app-warranty-listing/div/app-table-search-filter/div/div/div[1]/div/div/div/div[4]/app-checkbox/div/p-checkbox/div"}
WARRANTY_SELECT_ALL_CHECKBOXES = {"xpath":"/html/body/app-root/app-brand-main/div/div/div[2]/div[2]/div/app-warranty-listing/p-table/div/div/table/thead/tr/th[1]/app-checkbox/div/p-checkbox/div/input"}
WARRANTY_TABLE_LIST = {"css selector":"tbody tr:nth-child(1)"}
WARRANTY_ROWPERPAGE_OPTION = {"xpath":"/html/body/app-root/app-brand-main/div/div/div[2]/div[2]/div/app-warranty-listing/p-table/div/p-paginator/div/p-select/div/chevrondownicon"}
WARRANTY_ROWPERPAGE_20 = {"xpath":"//span[normalize-space()='20']"}
WARRANTY_ROWPERPAGE_100 = {"xpath":"//span[normalize-space()='100']"}
WARRANTY_ROWPERPAGE_1000 = {"xpath":"//span[normalize-space()='1000']"}
WARRANTY_POPUP_CLOSE = {"xpath":"//span[@class='p-dialog-header-close-icon pi pi-times']"}


###SEARIALIZED_CODE ###
SEARIALIZED_CODE_OPTION = {"xpath", "//span[normalize-space()='Serialized Codes']"}
SEARIALIZED_CODE_TITLE = {"//h1[normalize-space()='SEARIALIZED_CODEs > SEARIALIZED_CODEs']"}
SEARIALIZED_CODE_COUNT = { "//h6[normalize-space()='Total Active Codes']"}
SEARIALIZED_CODE_EXPERIENCE_FILTER_SEARIALIZED_CODE = { "//div[@class='p-multiselect-label ng-tns-c93-176']"}
SEARIALIZED_CODE_VARIANT_FILTER_SEARIALIZED_CODE = { ".p-multiselect-label.ng-tns-c93-177"}
SEARIALIZED_CODE_SEARIALIZED_CODE_STATUS = { ".p-multiselect-label.ng-tns-c93-178"}
SEARIALIZED_CODE_SOURCE = { "//div[@class='p-element p-multiselect-label-container ng-tns-c93-11']"}
SEARIALIZED_CODE_SEARCH_BAR = {" input[placeholder='Search Items...']"}
SEARIALIZED_CODE_FIELDS_BUTTON = { "//button[normalize-space()='Fields']"}
SEARIALIZED_CODE_UNSELECT_ALL_CHECKBOXES = {"xpath" : "//p-checkbox[@class='ng-pristine ng-valid ng-touched']//div[@class='p-checkbox p-component']"}
SEARIALIZED_CODE_SELECT_ALL_CHECKBOX = {"class name":  "p-checkbox-input"}
SEARIALIZED_CODE_BRIJ_HEADING = { "//th[@id='brijCodeId']"}
SEARIALIZED_CODE_CODE_HEADING = { "//th[@id='codeType']"}
SEARIALIZED_CODE_SERIAL_HEADING = { "//th[@id='serialNo']"}
SEARIALIZED_CODE_LOT_HEADING = { "//th[@id='lotNo']"}
SEARIALIZED_CODE_OWNER_HEADING = { "//th[@id='owner']"}
SEARIALIZED_CODE_ICON = { "//tbody/tr[1]/td[4]/span[1]"}
SEARIALIZED_CODE_Expander = { "img[class='cursor-pointer arrow-btn img-border ng-star-inserted']"}
SEARIALIZED_COD_ICON = { "img[class='cursor-pointer arrow-btn img-border ng-star-inserted']"}
SEARIALIZED_CODE_RESET_GOOGLE_PERMISSION = {"//span[normalize-space()='Reset Google Sheet']"}
SEARIALIZED_CODE_VIEW_IN_GOOGLE_SHEET = { "button[label='View in Google Sheet']"}
SEARIALIZED_CODE_EXPORT_BUTTON = {"css selector" : "button[label='Export CSV']"}
SEARIALIZED_CODE_KEBAB = {"xpath" : "//tbody/tr[1]/td[11]/app-row-options[1]/div[1]/img[1]"}
SERIALIZED_Activate= {"xpath":"//span[normalize-space()='Activate']"}
SERIALIZED_Deactivate= {"xpath":"//span[normalize-space()='Deactivate']"}
SERIALIZED_Delete= {"xpath":"//span[normalize-space()='Delete']"}
SERIALIZED_REGISTRATION_STATUS = {"//div[contains(text(),'All Registration Statuses')]"}
SERIALIZED_REGISTRATION_STATUS_ACTIVE= {"xpath":"//div[@title='Active']"}
SERIALIZED_REGISTRATION_STATUS_PENDING= {"xpath":"//div[@title='Pending']"}
SERIALIZED_REGISTRATION_STATUS_INCOMPLETE= {"xpath":"//div[@title='Incomplete']"}
SERIALIZED_REGISTRATION_STATUS_DENIED= {"xpath":"//div[@title='Denied']"}
SERIALIZED_REGISTRATION_STATUS_EXPIRED= {"xpath":"//div[@title='Expired']"}
SERIALIZED_REGISTRATION_STATUS_ALL= {"xpath":"//label[normalize-space()='All Registration Statuses']"}
SERIALIZED_REGISTRATION_STATUS_APPROVED= {"xpath":"//div[@title='Approved']"}
SERIALIZED_REGISTRATION_STATUS_INACTIVE= {"xpath":"//div[@title='Inactive']"}
SERIALIZED_REGISTRATION_STATUS_UNREGISTERED= {"xpath":"//div[@title='Unregistered']"}
SEARIALIZED_ROWPERPAGE_OPTION = {"xpath":"//div[@aria-label='dropdown trigger']"}
SEARIALIZED_ROWPERPAGE_20 = {"xpath":"//span[@class='ng-star-inserted'][normalize-space()='20']"}
SEARIALIZED_ROWPERPAGE_100 = {"xpath":"//span[normalize-space()='100']"}
SEARIALIZED_ROWPERPAGE_1000 = {"xpath":"//span[normalize-space()='1000']"}
SEARIALIZED_EXPORT_BUTTON = {"xpath":"//button[normalize-space()='Export']"}
SEARIALIZED_EXPORT_CANCEL = {"xpath":"//span[normalize-space()='Cancel']"}
SEARIALIZED_EXPORT_CLOSE = {"xpath":"/html/body/app-root/app-brand-main/div/app-confirmdialog/div/div/div/div[2]/div/p-button/button/timesicon/svg"}
SEARIALIZED_EXPORT_EXPORT = {"xpath":"//span[normalize-space()='Export']"}
SERIALIZED_DELETE_CONFIRM = {"xpath":"//span[normalize-space()='Delete']"}

###TEST_RESULT ###
TEST_RESULT_OPTION = {"css selector", ".has-subnav.orders.ng-star-inserted.is-active"}
TEST_RESULT_TITLE = {"//h1[normalize-space()='Test Results']"}
TEST_RESULT_COUNT = { "//*[@id='mainContent']/div[2]/div/app-test-result-listing/div[1]/div/div[3]/h2"}
TEST_RESULT_TEST_PANEL_FILTER = {"//div[contains(text(),'All Testing Panels')]"}
TEST_RESULT_TEST_PANEL_FILTER_SEARCH = {"xpath":"//input[@placeholder='Search...']"}
TEST_RESULT_TEST_PANEL_FILTER_CROSS = {"xpath":"//input[@placeholder='Search...']"}
TEST_RESULT_TEST_PANEL_FILTER_HEAVY = {"xpath":"//div[@title='Heavy Metals']"}
TEST_RESULT_TEST_PANEL_FILTER_PESTICIDES = {"xpath":"//div[@title='Pesticides and Glyphosate']"}
TEST_RESULT_TEST_PANEL_FILTER_PLASTICISER = {"xpath":"//div[@title='Plasticizers']"}
TEST_RESULT_TEST_LAB_FILTER = { "//p-multiselect[@id='pn_id_30']//div[@class='p-multiselect-label-container']"}
TEST_RESULT_TEST_LAB_FILTER_OPTION = {"xpath":"//li[@id='pn_id_30_1']//div[@class='flex w-full items-center ng-star-inserted']"}
TEST_RESULT_TEST_RESULT_STATUS = { ".p-multiselect-label.ng-tns-c93-178"}
TEST_RESULT_SOURCE = { "//div[@class='p-element p-multiselect-label-container ng-tns-c93-11']"}
TEST_RESULT_SEARCH_BAR = {" input[placeholder='Search Items...']"}
TEST_RESULT_SWITCHER_BUTTON = {".p-ripple.p-element.p-button.p-component.ng-star-inserted.p-highlight"}
TEST_RESULT_FIELDS_BUTTON = { "//button[normalize-space()='Fields']"}
TEST_RESULT_UNSELECT_ALL_CHECKBOXES = {"xpath" : "//p-checkbox[@name='tableHeaderCheckbox']//span[@class='p-checkbox-icon pi pi-check']"}
TEST_RESULT_SELECT_ALL_CHECKBOX = { "//*[@id='selectAllCol']/app-checkbox/div/p-checkbox"}
TEST_RESULT_LOT_NO = { "//th[@id='lotNo']"}
TEST_RESULT_TEST_DATE = { "//th[normalize-space()='Testing Date']//p-sorticon//sortalticon"}
TEST_RESULT_EXPIRATION_DATE= { "//body//app-root//th[5]"}
TEST_RESULT_TEST_ID = { "//th[@id='testId']"}
TEST_RESULT_KEBAB_MENU = {"xpath":"//body[1]/app-root[1]/app-brand-main[1]/div[1]/div[1]/div[2]/div[2]/div[1]/app-test-result-listing[1]/p-table[1]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[9]/app-row-options[1]/div[1]"}
TEST_RESULT_EDIT  = {"xpath":"//div[contains(text(),'Edit Test Result')]"}
TEST_RESULT_DELETE_RESULT = {"xpath":"//div[contains(text(),'Delete Test Result')]"}
TEST_RESULT_NEW_TEST  = {"xpath":"//button[normalize-space()='New Test Result']"}
TEST_RESULT_CROSS  = {"xpath":"//span[@class='p-dialog-header-close-icon pi pi-times']"}
TEST_RESULT_POPUP_TESTING_PANEL  = {"xpath":"(//div[@class='p-multiselect-label-container'])[3]"}
TEST_RESULT_POPUP_TESTING_PANEL_edit  = {"xpath":"/html[1]/body[1]/p-dynamicdialog[1]/div[1]/div[1]/div[1]/app-test-result-edit[1]/div[1]/div[2]/div[2]/app-dropdown[1]/div[1]/span[1]/*[name()='svg']-icon[1]/*[name()=''][undefined"}
TEST_RESULT_POPUP_TESTING_PANEL1 = {"css selector":"body > p-dynamicdialog:nth-child(11) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > app-test-result-edit:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > app-multiselect:nth-child(2) > div:nth-child(1) > p-multiselect:nth-child(2) > div:nth-child(2)"}
TEST_RESULT_POPUP_ALL_PANEL  = {"xpath":"//label[normalize-space()='All Testing Panels']"}
TEST_RESULT_POPUP_HEAVY_METAL  = {"xpath":"//div[@title='Heavy Metals']"}
TEST_RESULT_POPUP_PESTICIDES  = {"xpath":"//div[@title='Pesticides and Glyphosate']"}
TEST_RESULT_POPUP_PLASTICISERS  = {"xpath":"//div[@title='Plasticizers']"}
TEST_RESULT_POPUP_TP_CANCEL  = {"xpath":"//span[@class='p-button-icon pi pi-times']"}
TEST_RESULT_POPUP_TP_ALL  = {"xpath":"//p-multiselect[@id='pn_id_41']//div[@class='p-multiselect-label'][normalize-space()='All Testing Panels']"}
TEST_RESULT_POPUP_TESTLAB  = {"xpath":"/html/body/p-dynamicdialog/div/div/div/app-test-result-edit/div/div[2]/div[2]/app-dropdown/div/p-select"}
TEST_RESULT_POPUP_TESTLAB_name = {"xpath":"//span[@class='edit-role-name-icon ng-star-inserted']"}
TEST_RESULT_POPUP_TESTLAB_1 = {"xpath":"//div[@title='Auto test lab']"}
TEST_RESULT_POPUP_TESTLAB_SLAB = {"xpath":"/html/body/p-dynamicdialog/div/div/div/app-test-result-edit/div/div[2]/div[2]/app-dropdown/div/p-select/span/div"}
TEST_RESULT_POPUP_TESTLAB_edit = {"xpath":"//span[@class='edit-role-name-icon ng-star-inserted']"}
TEST_RESULT_POPUP_NEWLAB = {"xpath":"//span[@class='w-full max-w-full whitespace-nowrap text-ellipsis overflow-hidden text-primary']"}
TEST_RESULT_POPUP_NEWLAB_NAME = {"xpath":"//input[@id='name']"}
TEST_RESULT_POPUP_NEWLAB_SAVE = {"xpath":"//button[@class='full-width full-width-button medium primary p-button p-component']"}
TEST_RESULT_POPUP_FIRSTLAB  = {"xpath":"//li[@id='pn_id_19_1']"}
TEST_RESULT_POPUP_LAB_EDIT = {"xpath":"//li[@id='pn_id_19_1']//span[@class='edit-icon bg-"}
TEST_RESULT_POPUP_LAB_NAME_FIELD = {"xpath":"//input[@id='name']"}
TEST_RESULT_POPUP_LAB_NAME_SAVE = {"xpath":"//button[@class='full-width full-width-button medium primary p-button p-component']"}
TEST_RESULT_POPUP_LAB_NAME_SAVE1 = {"xpath":"//*[@id='pc235']/div/app-testing-lab-edit/div/form/div/div[2]/app-p-button[2]/button"}
TEST_RESULT_POPUP_LAB_NAME_DELETE = {"xpath":"//button[normalize-space()='Remove']"}
TEST_RESULT_POPUP_LAB_NAME_DELETE_CONFIRM = {"xpath":"//button[normalize-space()='Remove']"}
TEST_RESULT_POPUP_LAB_NAME_DELETE_CANCEL = {"xpath":"//button[normalize-space()='Cancel']"}
TEST_RESULT_POPUP_LAB_CROSS = {"xpath":"//span[@class='p-button-icon pi pi-times']"}
TEST_RESULT_POPUP_LAB_SEARCH = {"xpath":"//input[@placeholder='Search...']"}
TEST_RESULT_POPUP_APPLY_ALL_LOT = {"xpath":"//label[normalize-space()='Apply to all Lots']"}
TEST_RESULT_POPUP_LOT_NO = {"xpath":"//input[@formcontrolname='lotNo']"}
TEST_RESULT_POPUP_TESTID = {"xpath":"//input[@formcontrolname='testId']"}
TEST_RESULT_POPUP_SAMPLE_ID = {"xpath":"//input[@formcontrolname='sampleId']"}
TEST_RESULT_POPUP_ORDER_ID = {"xpath":"//input[@formcontrolname='orderId']"}
TEST_RESULT_POPUP_TESTDATE = {"xpath":"//span[@class='ng-tns-c2456691946-314 p-datepicker p-component p-inputwrapper p-inputwrapper-filled p-focus']"}
TEST_RESULT_POPUP_TDCALENDAR = {"xpath":"//td[@aria-label='3']"}
TEST_RESULT_POPUP_EXPIRYDATE = {"xpath":"//span[@class='ng-tns-c2456691946-315 p-datepicker p-component p-inputwrapper p-focus']//input[@id='templatedisplay']"}
TEST_RESULT_POPUP_EDCALENDAR = {"xpath":"//span[@class='p-ripple ng-tns-c2456691946-315 p-datepicker-day ng-star-inserted'][normalize-space()='28']"}
TEST_RESULT_POPUP_PRODUCT = {"xpath":"//span[@aria-label='Click to select']"}
TEST_RESULT_POPUP_PRODUCT_selected = {"xpath":"/html/body/p-dynamicdialog/div/div/div/app-test-result-edit/div/div[2]/div[7]/app-form-control/div/app-dropdown/div/p-select/span/div/div"}
TEST_RESULT_POPUP_PRODUCT1 = {"css selector":"div[class='country-item country-item-value ng-star-inserted'] div:nth-child(1)"}
TEST_RESULT_POPUP_NEW_PRODUCT = {"xpath":"//span[@class='w-full max-w-full whitespace-nowrap text-ellipsis overflow-hidden text-primary']"}
TEST_RESULT_POPUP_SEARCH_PRODUCT = {"xpath":"//input[@placeholder='Search...']"}
TEST_RESULT_POPUP_SELECT_FIRST_PRODUCT = {"xpath":"//span[@class='sub-label ng-star-inserted']"}
TEST_RESULT_POPUP_SELECT_FIRST_PRODUCT1 = {"xpath":"//span[normalize-space()='Auto test product 12 digit']"}
TEST_RESULT_POPUP_SELECT_PRODUCT = {"xpath":"//li[@id='pn_id_100_11']//span[@class='ellipsis2']"}
TEST_RESULT_POPUP_EDIT_PRODUCT = {"css selector":"li[id='pn_id_125_11'] span[class='edit-icon-container ml-auto ng-star-inserted']"}
TEST_RESULT_POPUP_PRODUCTNAME = {"xpath":"//input[@id='name']"}
TEST_RESULT_POPUP_UPC = {"xpath":"//input[@id='upc']"}
TEST_RESULT_POPUP_PRODUCT_SAVE = {"xpath":"//button[@class='full-width full-width-button medium primary p-button p-component']"}
TEST_RESULT_POPUP_PRODUCT_CANCEL = {"xpath":"//img[@class='close-icon']"}
TEST_RESULT_POPUP_SUBCOMPONENT = {"xpath":"//p-multiselect[@id='pn_id_112']//div[@class='p-multiselect-label-container']"}
TEST_RESULT_POPUP_SUBCOMPONENT_LIST = {"xpath":"//div[@class='flex gap-//app-checkbox[@class='ng-untouched ng-pristine ng-valid']"}
TEST_RESULT_POPUP_SUB_CROSS = {"xpath":"//span[@class='p-button-icon pi pi-times']"}
TEST_RESULT_POPUP_ARSENIC = {"xpath":"/html/body/p-dynamicdialog/div/div/div/app-test-result-edit/div/div[2]/div[8]/div/div[1]/input"}
TEST_RESULT_POPUP_CADMIUM = {"xpath":"(//input[@placeholder='Enter here...'])[6]"}
TEST_RESULT_POPUP_LEAD = {"xpath":"(//input[@placeholder='Enter here...'])[7]"}
TEST_RESULT_POPUP_MERCURY = {"xpath":"(//input[@placeholder='Enter here...'])[8]"}
TEST_RESULT_POPUP_PESTICIDE = {"xpath":"(//input[@placeholder='Enter here...'])[9]"}
TEST_RESULT_POPUP_GLYPHOSATE = {"xpath":"(//input[@placeholder='Enter here...'])[10]"}
TEST_RESULT_POPUP_BPA = {"xpath":"(//input[@placeholder='Enter here...'])[11]"}
TEST_RESULT_POPUP_BPS = {"xpath":"//*[@id='pc471'']/div/app-test-result-edit/div/div[2]/div[9]/div/div[2]/input"}
TEST_RESULT_POPUP_TEST_RESULT_UPLOAD = {"xpath":"//div[@class='csv-upload-container']"}
TEST_RESULT_POPUP_SAVE = {"xpath":"//button[normalize-space()='Save']"}
TEST_RESULT_POPUP_CROSS_ICON = {"xpath":"//span[@class='p-dialog-header-close-icon pi pi-times']"}
TEST_RESULT_EXPORT = {"xpath":"//button[normalize-space()='Export']"}
TEST_RESULT_EXPORT_CONFIRM = {"xpath":"//span[normalize-space()='Export']"}
TEST_RESULT_IMPORT_BTN = {"xpath":"//button[normalize-space()='Import']"}
TEST_RESULT_DOWNLOAD_TEMPLATE = {"xpath":"//span[normalize-space()='Download Template']"}
TEST_RESULT_IMPORT_CROSS = {"xpath":"//img[@class='close-icon p-6']"}
TEST_RESULT_IMPORT_SHEET_OPTION = {"xpath":"//span[@class='upload-text']"}
TEST_RESULT_IMPORT_SHEET = {"xpath":"//span[normalize-space()='Upload']"}
TEST_RESULT_IMPORT_CANCEL = {"xpath":"//img[@class='close-icon p-6']"}
TEST_RESULT_UPLOAD_FILE = {"xpath":"//div[@class='csv-upload-container']"}
TEST_RESULT_UPDATE_FILE= {"xpath":"//span[normalize-space()='Update']"}
TEST_RESULT_UPLOAD_FILE_REMOVE = {"xpath":"//span[normalize-space()='Remove']"}
TEST_RESULT_ROW_PER_PAGE = {"//div[@aria-label='dropdown trigger']"}
TEST_RESULT_ROWS_20 = { "//span[@class='ng-star-inserted'][normalize-space()='20']"}
TEST_RESULT_ROWS_100 = { "//span[normalize-space()='100']"}
TEST_RESULT_ROWS_1000 = { "//span[normalize-space()='1000']"}
TEST_RESULT_ARROW_NEXT = {"xpath" : "//button[@aria-label='Next Page']"}
TEST_RESULT_ARROW_PREVIOUS = {"xpath" : "//button[@aria-label='Previous Page']"}
TEST_RESULT_LIST_VERIFY_TESTRESULT = {"xpath":"//span[normalize-space()='Auto test product 12 digit']"}

### AUTOMATION ###
AUTOMATION_OPTION = {"xpath" : "//span[normalize-space()='Automations']"}
AUTOMATION_TITLE = {"xpath" : "//h1[normalize-space()='Automations']"}
AUTOMATION_NOTIFICATION_BUTTON = {"xpath" : "//div[@class='notification']"}
AUTOMATION_LOGOUT_BUTTON = {"xpath" : "//img[@alt='logout']"}
AUTOMATION_SEARCH_BAR = {"xpath" : "//input[@placeholder='Search Items...']"}
AUTOMATION_FIELD_BUTTON = {"xpath" : "//button[normalize-space()='Fields']"}
AUTOMATION_ALL_CHECKBOXES = {"xpath" : "//p-checkbox[@class='ng-pristine ng-valid ng-touched']"}
AUTOMATION_CHECKBOX = {"xpath" : "//td[@class='center']//p-checkbox[@class='ng-pristine ng-valid ng-touched']//div[@class='p-checkbox-box']"}
AUTOMATION_LIST_ROW1 = {"xpath" : "//tbody/tr[1]"}
AUTOMATION_LIST_ECLIPSE = {"xpath" : "//body[1]/app-root[1]/app-brand-main[1]/div[1]/div[1]/div[2]/div[2]/div[1]/app-automations-listing[1]/p-table[1]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[8]/app-row-options[1]/div[1]/img[1]"}
AUTOMATION_ECLIPSE_DELETE = {"xpath" : "//div[contains(text(),'Delete')]"}
AUTOMATION_ECLIPSE_PAUSE = {"xpath" : "//div[contains(text(),'Pause')]"}
AUTOMATION_TABLE_HEADER = {"xpath":"//th[@id='integrationProvider']"}
AUTOMATION_ECLIPSE_ACTIVATE = {"xpath" : "//div[contains(text(),'Activate')]"}
AUTOMATION_DELETE_ALL = {"xpath" : "//button[normalize-space()='Delete']"}
AUTOMATION_DELETE_CONFIRMATION = {"xpath" : "//span[normalize-space()='Yes']"}
AUTOMATION_DELETE_CROSS = {"xpath" : "//timesicon[@class='p-component p-iconwrapper ng-tns-c787154972-3 ng-star-inserted']//*[name()='svg']"}
AUTOMATION_DELETE_CANCEL = {"xpath" : "//span[normalize-space()='No']"}
AUTOMATION_NEW_AUTOMATION = {"xpath" : "//button[normalize-space()='New Automation']"}
AUTOMATION_POPUP_INTEGRATION = {"xpath" : "(//button[normalize-space()='Integration'])[1]"}
AUTOMATION_POPUP_AUTHENTICATION = {"xpath" : "(//button[normalize-space()='Authentication'])[1]"}
AUTOMATION_POPUP_ACTION = {"xpath" : "(//button[normalize-space()='Action'])[1]"}
AUTOMATION_POPUP_FILTER = {"xpath" : "(//button[normalize-space()='Filters'])[1]"}
AUTOMATION_POPUP_TRIGGER_PROPERTIES = {"xpath" : "//button[@id='pn_id_23_header_action']"}
AUTOMATION_POPUP_CONFIGURATION = {"xpath" : "(//button[normalize-space()='Configuration'])[1]"}
AUTOMATION_POPUP_AUTOMATION_NAME = {"xpath" : "//input[@placeholder='Enter here...']"}
AUTOMATION_POPUP_AUTOMATION_TYPE_KLAVIYO = {"xpath" : "//div[contains(text(),'Klaviyo')]"}
AUTOMATION_POPUP_AUTOMATION_TYPE_WEBHOOK = {"xpath" : "//div[contains(text(),'Webhook')]"}
AUTOMATION_POPUP_AUTOMATION_TYPE_MULBERRY = {"xpath" : "//div[contains(text(),'Mulberry')]"}
AUTOMATION_POPUP_NEXT_BUTTON = {"xpath" : "//span[normalize-space()='Next']"}
AUTOMATION_POPUP_BACK_BUTTON = {"xpath" : "//span[normalize-space()='Back']"}
AUTOMATION_POPUP_AUTHENTICATION_OPTION = {"xpath" : "//span[contains(text(),'Select an option')]"}
AUTOMATION_POPUP_AUTHENTICATION_NEW = {"xpath" : "//div[@title='New Authentication']"}
AUTOMATION_POPUP_AUTHENTICATION_NEW_NAME = {"xpath" : "//input[@name='name']"}
AUTOMATION_POPUP_AUTHENTICATION_NEW_AUTHENTICATION_TYPE = {"xpath" : "//div[@title='apiKey']"}
AUTOMATION_POPUP_AUTHENTICATION_NEW_AUTHENTICATION_TYPE_OPTION = {"xpath" : "//span[@class='w-full max-w-full whitespace-nowrap text-ellipsis overflow-hidden']"}
AUTOMATION_POPUP_AUTHENTICATION_NEW_AUTHENTICATION_API_KEY = {"xpath" : "//input[@placeholder='pk_1234567890']"}
AUTOMATION_POPUP_AUTHENTICATION_NEW_AUTHENTICATION_SAVE = {"xpath" : "//button[normalize-space()='Save']"}
AUTOMATION_POPUP_AUTHENTICATION_NEW_AUTHENTICATION_REMOVE = {"xpath" : "//span[normalize-space()='Remove']"}
AUTOMATION_POPUP_ACTION_NAME = {"xpath" : "//div[@title='Brij -> Klaviyo Integration']"}
AUTOMATION_POPUP_ACTION_VERSION = {"xpath" : "//div[@title='V1']"}
AUTOMATION_POPUP_FILTER_EXPERIENCE_TEST = {"xpath" : "//div[@title='Test (Q071)']"}
AUTOMATION_POPUP_FILTER_EXPERIENCE_TEST1 = {"xpath" : "//div[@title='Testing (72A0)']"}
AUTOMATION_POPUP_FILTER_EXPERIENCE_DROPDOWN = {"xpath" : "//div[@class='p-multiselect-label']"}
AUTOMATION_POPUP_FILTER_EXPERIENCE_DROPDOWN_SEARCH = {"xpath" : "//input[@placeholder='Search...']"}
AUTOMATION_POPUP_FILTER_EXPERIENCE_DROPDOWN_SEARCH_CROSS = {"xpath" : "//span[@class='p-button-icon pi pi-times']"}
AUTOMATION_POPUP_FILTER_EXPERIENCE_DROPDOWN_SEARCH_OPTION = {"xpath" : ""}
AUTOMATION_POPUP_FILTER_EXPERIENCE_DROPDOWN_SEARCH_SELECT_ALL = {"xpath" : "//label[normalize-space()='Select All']"}
AUTOMATION_POPUP_FILTER_EXPERIENCE_DROPDOWN_SEARCH_ALL_EXPERIENCE = {"xpath" : "//label[normalize-space()='All Experiences']"}
AUTOMATION_POPUP_TRIGGERS_PROPERTIES_REGISTRATION_INITIATION_EVENT = {"xpath" : "//div[@class='main ng-tns-c2347749340-94']//div[1]//div[1]//img[1]"}
AUTOMATION_POPUP_TRIGGERS_PROPERTIES_REGISTRATION_INITIATION_EVENT_CHECKBOX = {"xpath" : "//span[normalize-space()='Registration Initiation Event']"}
AUTOMATION_POPUP_TRIGGERS_PROPERTIES_REGISTRATION_SUBMISSION_EVENT = {"xpath" : ""}
AUTOMATION_POPUP_TRIGGERS_PROPERTIES_REGISTRATION_SUBMISSION_EVENT_CHECKBOX = {"xpath" : "//span[normalize-space()='Registration Submission Event']"}
AUTOMATION_POPUP_TRIGGERS_PROPERTIES_REGISTRATION_APPROVAL_EVENT = {"xpath" : ""}
AUTOMATION_POPUP_TRIGGERS_PROPERTIES_REGISTRATION_APPROVAL_EVENT_CHECKBOX = {"xpath" : "//span[normalize-space()='Registration Approval Event']"}
AUTOMATION_POPUP_TRIGGERS_PROPERTIES_REGISTRATION_DENIAL_EVENT = {"xpath" : ""}
AUTOMATION_POPUP_TRIGGERS_PROPERTIES_REGISTRATION_DENIAL_EVENT_CHECKBOX = {"xpath" : "//span[normalize-space()='Registration Denial Event']"}
AUTOMATION_POPUP_TRIGGERS_PROPERTIES_FORM_SUBMISSION_EVENT = {"xpath" : ""}
AUTOMATION_POPUP_TRIGGERS_PROPERTIES_FORM_SUBMISSION_EVENT_CHECKBOX = {"xpath" : "//span[normalize-space()='Form Submission Event']"}
AUTOMATION_POPUP_TRIGGERS_PROPERTIES_REVIEW_SUBMISSION_EVENT = {"xpath" : ""}
AUTOMATION_POPUP_TRIGGERS_PROPERTIES_REVIEW_SUBMISSION_EVENT_CHECKBOX = {"xpath" : "//span[normalize-space()='Review Submission Event']"}
AUTOMATION_POPUP_CONFIGURATION_ADDUSERTOLIST_DROPDOWN = {"xpath" : "//span[contains(@class, 'p-select-label ng-star-inserted')]/div[contains(@class, 'ng-star-inserted') and text()=' No ']"}
AUTOMATION_POPUP_CONFIGURATION_ADDUSERTOLIST_DROPDOWN_YES = {"xpath" : "//span[@class='w-full max-w-full whitespace-nowrap text-ellipsis overflow-hidden'][normalize-space()='Yes']"}
AUTOMATION_POPUP_CONFIGURATION_ADDUSERTOLIST_DROPDOWN_NO = {"xpath" : "//span[@class='w-full max-w-full whitespace-nowrap text-ellipsis overflow-hidden'][normalize-space()='No']"}
AUTOMATION_POPUP_CONFIGURATION_ADDUSERTOLIST_KLAVIYO = {"class" : "p-inputtext p-component register-modal-input ng-pristine ng-valid ng-star-inserted ng-touched"}
AUTOMATION_POPUP_CONFIGURATION_SMS_SINGLEOPTIN = {"xpath" : "//p-select[@id='pn_id_126']//span[@aria-label='No']"}
AUTOMATION_POPUP_CONFIGURATION_SMS_SINGLEOPTIN_YES = {"xpath" : "//span[@class='w-full max-w-full whitespace-nowrap text-ellipsis overflow-hidden'][normalize-space()='Yes']"}
AUTOMATION_POPUP_CONFIGURATION_SMS_SINGLEOPTIN_NO = {"xpath" : "//span[@class='w-full max-w-full whitespace-nowrap text-ellipsis overflow-hidden'][normalize-space()='No']"}
AUTOMATION_POPUP_CONFIGURATION_CONSENTING_SMS = {"xpath" : "//p-select[@id='pn_id_128']"}
AUTOMATION_POPUP_CONFIGURATION_CONSENTING_SMS_YES = {"xpath" : "//span[@class='w-full max-w-full whitespace-nowrap text-ellipsis overflow-hidden'][normalize-space()='Yes']"}
AUTOMATION_POPUP_CONFIGURATION_CONSENTING_SMS_NO = {"xpath" : "//span[@class='w-full max-w-full whitespace-nowrap text-ellipsis overflow-hidden'][normalize-space()='No']"}
AUTOMATION_POPUP_CONFIGURATION_CONSENTING_SMS_INPUT = {"xpath" : "(//input[@placeholder='abc123'])[2]"}
AUTOMATION_POPUP_CONFIGURATION_ADD_FORMDATA = {"xpath" : "//p-select[@id='pn_id_130']"}
AUTOMATION_POPUP_CONFIGURATION_ADD_FORMDATA_YES = {"xpath" : "//span[@class='w-full max-w-full whitespace-nowrap text-ellipsis overflow-hidden'][normalize-space()='Yes']"}
AUTOMATION_POPUP_CONFIGURATION_ADD_FORMDATA_NO = {"xpath" : "//span[@class='w-full max-w-full whitespace-nowrap text-ellipsis overflow-hidden'][normalize-space()='No']"}
AUTOMATION_POPUP_CONFIGURATION_ADD_REVIEWDATA = {"xpath" : "//p-select[@id='pn_id_132']"}
AUTOMATION_POPUP_CONFIGURATION_ADD_REVIEWDATA_YES = {"xpath" : "//span[@class='w-full max-w-full whitespace-nowrap text-ellipsis overflow-hidden'][normalize-space()='Yes']"}
AUTOMATION_POPUP_CONFIGURATION_ADD_REVIEWDATA_NO = {"xpath" : "//span[@class='w-full max-w-full whitespace-nowrap text-ellipsis overflow-hidden'][normalize-space()='No']"}
AUTOMATION_POPUP_CONFIGURATION_PAUSE_AUTOMATION = {"xpath" : "//p-select[@id='pn_id_166']"}
AUTOMATION_POPUP_CONFIGURATION_PAUSE_AUTOMATION_YES = {"xpath" : "//p-select[@id='pn_id_166']"}
AUTOMATION_POPUP_CONFIGURATION_PAUSE_AUTOMATION_NO = {"xpath" : "//span[@class='w-full max-w-full whitespace-nowrap text-ellipsis overflow-hidden'][normalize-space()='No']"}
AUTOMATION_POPUP_CONFIGURATION_PAUSE_AUTOMATION_COUNT = {"xpath" : "//input[@placeholder='50']"}
AUTOMATION_POPUP_CONFIGURATION_NOTIFY = {"xpath" : "//p-select[@id='pn_id_168']"}
AUTOMATION_POPUP_CONFIGURATION_NOTIFY_YES = {"xpath" : "//span[@class='w-full max-w-full whitespace-nowrap text-ellipsis overflow-hidden'][normalize-space()='Yes']"}
AUTOMATION_POPUP_CONFIGURATION_NOTIFY_NO = {"xpath" : "//span[@class='w-full max-w-full whitespace-nowrap text-ellipsis overflow-hidden'][normalize-space()='No']"}
AUTOMATION_POPUP_CONFIGURATION_NOTIFY_EMAIL = {"xpath" : "//input[@placeholder='support@brij.it']"}
AUTOMATION_POPUP_SAVE_ACTIVATE = {"xpath" : "//span[normalize-space()='Save & Activate']"}
AUTOMATION_POPUP_SAVE_EXIST = {"xpath" : "//span[normalize-space()='Save & Exit']"}
AUTOMATION_POPUP_UNSAVE_EXIST = {"xpath" : "//span[normalize-space()='Exit Without Saving']"}
AUTOMATION_POPUP_SAVE_PAUSE = {"xpath" : "//span[normalize-space()='Save & Pause']"}
AUTOMATION_POPUP_SAVE_LIVE = {"xpath" : "//span[normalize-space()='Save & Live']"}
AUTOMATION_POPUP_CROSS = {"xpath" : "/html/body/p-dynamicdialog/div/div/div[2]/app-automations-edit/svg-icon/svg"}
AUTOMATION_POPUP_YES = {"xpath" : "//span[normalize-space()='Yes']"}
AUTOMATION_POPUP_NO = {"xpath" : "//span[normalize-space()='No']"}
AUTOMATION_ROWPERPAGE_OPTION = {"xpath":"//div[@aria-label='dropdown trigger']"}
AUTOMATION_ROWPERPAGE_20 = {"xpath":"//span[@class='ng-star-inserted'][normalize-space()='20']"}
AUTOMATION_ROWPERPAGE_100 = {"xpath":"//span[normalize-space()='100']"}
AUTOMATION_ROWPERPAGE_1000 = {"xpath":"//span[normalize-space()='1000']"}


### EXPERIENCE PAGE ####
EXPERIENCE_OPTION = {"css selector", "body > app-root:nth-child(1) > app-brand-main:nth-child(4) > div:nth-child(1) > div:nth-child(1) > nav:nth-child(1) > ul:nth-child(1) > li:nth-child(4) > span:nth-child(2)"}
EXPERIENCE_PAGE_OPTION = {"xpath", "//span[normalize-space()='Experiences']"}
EXPERIENCE_TITLE = {"//h1[normalize-space()='Experiences']"}
EXPERIENCE_COUNT = { "//h6[normalize-space()='Total Experiences']"}
EXPERIENCE_STATUS_FILTER = {"//div[contains(text(),'All Statuses')]"}
EXPERIENCE_PAGE_FILTER_SEARCH = {"//input[@placeholder='Search...']"}
EXPERIENCE_FILTER_SELECTALL = {"//label[normalize-space()='Select All']"}
EXPERIENCE_FILTER_ALL_STATUS = {"//label[normalize-space()='All Statuses']"}
EXPERIENCE_FILTER_ALL_CATEGORY = {"//label[normalize-space()='All Categories']"}
EXPERIENCE_FILTER_ALL_TYPE = {"//label[normalize-space()='All Types']"}
EXPERIENCE_STATUS_FILTER_OPTION_ACTIVE = {"//div[@title='Active']"}
EXPERIENCE_STATUS_FILTER_OPTION_INACTIVE = {"//div[@title='Inactive']"}
EXPERIENCE_FILTER_CROSS = {"xpath":"//span[@class='p-button-icon pi pi-times']"}
EXPERIENCE_CATEGORY_FILTER = {"//div[contains(text(),'All Categories')]"}
EXPERIENCE_TYPE_WebApp = {"//div[@title='App Experience']"}
EXPERIENCE_TYPE_Rebate = {"//div[@title='Rebate']"}
EXPERIENCE_TYPE_DigitalHub = {"/html/body/p-dynamicdialog/div/div/div/app-experience-landing-page/div[2]/div[1]/div[2]/div/span"}
EXPERIENCE_TYPE_DynamicLink = {"//div[@title='Dynamic Link']"}
EXPERIENCE_TYPE_FILTER = {"//div[contains(text(),'All Types')]"}
EXPERIENCE_SEARCH_BAR = {"//input[@placeholder='Search Items...']"}
EXPERIENCE_FIELDS_BUTTON = { "//button[normalize-space()='Fields']"}
EXPERIENCE_UNSELECT_ALL_CHECKBOX = {"xpath" : "//app-checkbox[@name='tableHeaderCheckbox']"}
EXPERIENCE_SELECT_ALL_CHECKBOX = {"(//div[@class='p-checkbox-box'])[4]"}
EXPERIENCE_EXPERIENCE_NAME_HEADING = { "#productName"}
EXPERIENCE_TITLE_HEADING = {"css selector":"#title"}
EXPERIENCE_LIST_KEBAB_MENU2 = {"xpath":"#(//app-row-options)[1]"}
EXPERIENCE_LIST_KEBAB_MENU = {"xpath":"//body[1]/app-root[1]/app-brand-main[1]/div[1]/div[1]/div[2]/div[2]/div[1]/app-products-listing[1]/p-table[1]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[11]/app-row-options[1]/div[1]/img[1]"}
EXPERIENCE_NEW_EXPERIENCE = {"//button[normalize-space()='New Experience']"}
EXPERIENCE_CHOOSE_EXPERIENCE_BUTTON = {"//button[normalize-space()='Choose Experience']"}
EXPERIENCE_POPUP_EXPERIENCE_NAME = {"//input[@id='product1']"}
EXPERIENCE_POPUP_EXPERIENCE_NAME_SAVE = {"button[class='primary small undefined p-button p-component']"}
EXPERIENCE_POPUP_EXPERIENCE_SUBTITLE = {"//input[@id='subtlte']"}
EXPERIENCE_POPUP_EXPERIENCE_PRODUCTSKU = {"//*[@id='product2']"}
EXPERIENCE_POPUP_EXPERIENCE_PRICE = {"(//input[@id='product2'])[2]"}
EXPERIENCE_POPUP_EXPERIENCE_PRODUCTURL = {"//input[@id='product3']"}
EXPERIENCE_POPUP_EXPERIENCE_RETAIL_CHANNEL = {"//div[@id='retail-dropdown-product']"}
EXPERIENCE_POPUP_EXPERIENCE_RETAIL_CHANNEL_NEW = {"//label[normalize-space()='New Channel']"}
EXPERIENCE_POPUP_EXPERIENCE_RETAIL_CHANNEL_NEW_NAME = {"//input[@id='name']"}
EXPERIENCE_POPUP_EXPERIENCE_RETAIL_CHANNEL_NEW_NAME_SAVE = {"//button[@class='full-width full-width-button medium primary p-button p-component']"}
EXPERIENCE_POPUP_EXPERIENCE_RETAIL_CHANNEL_SEARCH = {"//input[@placeholder='Search...']"}
EXPERIENCE_POPUP_EXPERIENCE_CATEGORY_2 = {"//div[contains(text(),'Auto Category')]"}
EXPERIENCE_POPUP_EXPERIENCE_RETAIL_CHANNEL_2 = {"//div[contains(text(),'Auto Channel')]"}
EXPERIENCE_POPUP_EXPERIENCE_RETAIL_CHANNEL_CROSS = {"//span[@class='p-button-icon pi pi-times']"}
EXPERIENCE_POPUP_EXPERIENCE_RETAIL_CHANNEL_All = {"//label[normalize-space()='All Channels']"}
EXPERIENCE_POPUP_EXPERIENCE_RETAIL_SELECT_All = {"//label[normalize-space()='Select All']"}
EXPERIENCE_POPUP_EXPERIENCE_CATEGORY = {"//div[@id='category-dropdown-product']"}
EXPERIENCE_POPUP_EXPERIENCE_CATEGORY_NEW = {"//label[normalize-space()='New Category']"}
EXPERIENCE_POPUP_EXPERIENCE_CATEGORY_NEW_NAME = {"//input[@id='name']"}
EXPERIENCE_POPUP_EXPERIENCE_CATEGORY_NEW_NAME_SAVE = {"//button[@class='full-width full-width-button medium primary p-button p-component']"}
EXPERIENCE_POPUP_EXPERIENCE_CATEGORY_SEARCH = {"//input[@placeholder='Search...']"}
EXPERIENCE_POPUP_EXPERIENCE_CATEGORY_All = {"//label[normalize-space()='All Categories']"}
EXPERIENCE_POPUP_EXPERIENCE_CATEGORY_SELECT_All = {"//label[normalize-space()='Select All']"}
EXPERIENCE_POPUP_EXPERIENCE_PRODUCT_DESCRIPTION = {"//textarea[@placeholder='Enter product description...']"}
EXPERIENCE_POPUP_EXPERIENCE_ADVANCE_SETTING_BUTTON = {"//button[normalize-space()='Advanced Settings']"}
EXPERIENCE_POPUP_EXPERIENCE_AS_SHOW_SOCIAL = {"//label[normalize-space()='Show Social Icons']"}
EXPERIENCE_POPUP_EXPERIENCE_AS_DESKTOP_VIEW = {"//label[normalize-space()='Enable Desktop View']"}
EXPERIENCE_POPUP_EXPERIENCE_AS_CONTENT_GATE = {"//label[normalize-space()='Enable Content Gate']"}
EXPERIENCE_POPUP_EXPERIENCE_AS_CONTENT_GATE_DROPDOWN = {"(//span[@class='ng-star-inserted'][normalize-space()='Click to select'])[1]"}
EXPERIENCE_POPUP_EXPERIENCE_AS_CONTENT_GATE_DROPDOWN_OPTION = {"xpath":"//span[contains(text(),'test Content Gate')]"}
EXPERIENCE_POPUP_EXPERIENCE_AS_CONTENT_GATE_NEW = {"//span[@class='w-full max-w-full whitespace-nowrap text-ellipsis overflow-hidden text-primary']"}
EXPERIENCE_POPUP_EXPERIENCE_AS_CONTENT_GATE_NAME = {"//input[@placeholder='Enter name...']"}
EXPERIENCE_POPUP_EXPERIENCE_AS_CONTENT_GATE_DESCRIPTION = {"//div[@class='fr-element fr-view default-styles-2']//p"}
EXPERIENCE_POPUP_EXPERIENCE_AS_CONTENT_GATE_SHOW_BACKGROUND = {"//span[@class='second-part ng-tns-c2456472750-47']"}
EXPERIENCE_POPUP_EXPERIENCE_AS_CONTENT_GATE_VERIFY_AGE = {"//label[normalize-space()='Verify Age']"}
EXPERIENCE_POPUP_EXPERIENCE_AS_CONTENT_GATE_AGE = {"//input[@placeholder='Enter minimum age']"}
EXPERIENCE_POPUP_EXPERIENCE_AS_CONTENT_GATE_BIRTHDAY = {"//label[normalize-space()='Require Birthdate Entry']"}
EXPERIENCE_POPUP_EXPERIENCE_AS_CONTENT_GATE_SAVE = {"(//button[@type='button'][normalize-space()='Save'])[2]"}
EXPERIENCE_POPUP_EXPERIENCE_AS_CONTENT_GATE_BACK = {"//label[normalize-space()='Content Gate']"}
EXPERIENCE_POPUP_EXPERIENCE_AS_ALTERNATELOGO = {"//label[normalize-space()='Use Alternate Logo']"}
EXPERIENCE_POPUP_EXPERIENCE_AS_SECONDARY_MODULE = {"//label[normalize-space()='Customize Secondary Modules Button']"}
EXPERIENCE_POPUP_EXPERIENCE_AS_SECONDARY_MODULE_TEXT = {"//input[@id='CTAInput']"}
EXPERIENCE_POPUP_EXPERIENCE_AS_SECONDARY_MODULE_THEME = {"//label[normalize-space()='Customize Secondary Modules Button Theme']"}
EXPERIENCE_POPUP_EXPERIENCE_AS_CHANGE_BACKGROUND = {"//label[normalize-space()='Change Background Image After Registration']"}
EXPERIENCE_POPUP_EXPERIENCE_AS_AUTO_RECEIPT = {"//label[normalize-space()='Auto-Verify Receipts']"}
EXPERIENCE_POPUP_EXPERIENCE_AS_VERIFICATION_CRITERIA = {"//span[contains(text(),'Select Verification Criteria')]"}
EXPERIENCE_POPUP_EXPERIENCE_AS_VERIFICATION_CRITERIA_SEARCH = {"//input[@placeholder='Search...']"}
EXPERIENCE_POPUP_EXPERIENCE_AS_VERIFICATION_CRITERIA_NEW = {"//span[@class='w-full max-w-full whitespace-nowrap text-ellipsis overflow-hidden text-primary']"}
EXPERIENCE_POPUP_EXPERIENCE_AS_VERIFICATION_CRITERIA_NAME = {"//input[@placeholder='Enter name...']"}
EXPERIENCE_POPUP_EXPERIENCE_AS_VERIFICATION_CRITERIA_RETAILER = {"//label[normalize-space()='Verify Retailers']"}
EXPERIENCE_POPUP_EXPERIENCE_AS_VERIFICATION_CRITERIA_INCLUDE_RETAILER = {"//label[normalize-space()='Include Retailers from Experience']"}
EXPERIENCE_POPUP_EXPERIENCE_AS_VERIFICATION_CRITERIA_ENTER_RETAILER = {"//input[@placeholder='Enter Retailers...']"}
EXPERIENCE_POPUP_EXPERIENCE_AS_VERIFICATION_CRITERIA_RETAILER_ADD = {"//img[@alt='white-plus.svg']"}
EXPERIENCE_POPUP_EXPERIENCE_AS_VERIFICATION_CRITERIA_LINE_ITEM = {"//label[normalize-space()='Verify Line Items']"}
EXPERIENCE_POPUP_EXPERIENCE_AS_VERIFICATION_CRITERIA_LINE_TEM_NAME = {"//input[@placeholder='Enter Line Item name...']"}
EXPERIENCE_POPUP_EXPERIENCE_AS_VERIFICATION_CRITERIA_LINE_TEM_NAME_ADD = {"//img[@class='ng-tns-c787443071-61']"}
EXPERIENCE_POPUP_EXPERIENCE_AS_VERIFICATION_CRITERIA_LINE_ITEM_PRICE = {"//label[normalize-space()='Verify Purchase Price']"}
EXPERIENCE_POPUP_EXPERIENCE_AS_VERIFICATION_CRITERIA_LINE_ITEM_PRICE_min = {"//div[@class='p-field-checkbox modal-checkbox my-20 ng-tns-c1842535111-228 ng-valid ng-touched ng-dirty']//div[@class='verify-product-container indent-left-7 mt-6 ng-tns-c1842535111-228 ng-trigger ng-trigger-openClose ng-star-inserted']//div[1]//div[1]//input[1]"}
EXPERIENCE_POPUP_EXPERIENCE_AS_VERIFICATION_CRITERIA_LINE_ITEM_PRICE_max = {"//label[normalize-space()='Verify Purchase Price']"}
EXPERIENCE_POPUP_EXPERIENCE_AS_VERIFICATION_CRITERIA_LINE_ITEM_QUANTITY = {"//label[normalize-space()='Verify Quantity']"}
EXPERIENCE_POPUP_EXPERIENCE_AS_VERIFICATION_CRITERIA_LINE_ITEM_NEW = {"//div[@class='line-item-btn ng-tns-c1842535111-53']"}
EXPERIENCE_POPUP_EXPERIENCE_AS_VERIFICATION_CRITERIA_LINE_ITEM_DELETE = {"//span[@class='delete-btn ng-tns-c1842535111-53']"}
EXPERIENCE_POPUP_EXPERIENCE_AS_VERIFICATION_CRITERIA_PURCHASE_DATE = {"//label[normalize-space()='Verify Purchase Date']"}
EXPERIENCE_POPUP_EXPERIENCE_AS_VERIFICATION_CRITERIA_UNIQUENESS = {"//label[normalize-space()='Verify Uniqueness']"}
EXPERIENCE_POPUP_EXPERIENCE_AS_VERIFICATION_CRITERIA_SAVE = {"//app-p-button[@class='ng-tns-c1842535111-53']//button[@type='button'][normalize-space()='Save']"}
EXPERIENCE_POPUP_EXPERIENCE_AS_VERIFICATION_CRITERIA_BACK = {"//button[@type='button']//label[contains(text(),'Verification Criteria')]"}
EXPERIENCE_POPUP_EXPERIENCE_AS_CUSTOM_THEME = {"//label[normalize-space()='Override Theme']"}
EXPERIENCE_POPUP_EXPERIENCE_AS_BACK = {"//label[normalize-space()='Advanced Settings']"}
EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION = {"//h1[normalize-space()='Registration / Sign Up']"}
EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_OPTION = {"(//div[@title='None'][normalize-space()='None'])[2]"}
EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_OPTION_NEW= {"//span[@class='w-full max-w-full whitespace-nowrap text-ellipsis overflow-hidden text-primary']"}
EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_NAME = {"//input[@placeholder='Enter module name...']"}
EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_CTA = {"//div[@title='Register']"}
EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_CTA_REGISTER = {"//span[@class='w-full max-w-full whitespace-nowrap text-ellipsis overflow-hidden'][normalize-space()='Register']"}
EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_CTA_ACTIVATE = {"//span[normalize-space()='Activate']"}
EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_CTAa = {"//div[@title='Activate']"}
EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_CTA_SIGNUP = {"//span[normalize-space()='Sign Up']"}
EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_CTAs = {"//div[@title='Sign Up']"}
EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_CTA_DONATE = {"//span[normalize-space()='Donate']"}
EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_CTAd = {"//div[@title='Donate']"}
EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_CTA_CUSTOM = {"//span[@class='w-full max-w-full whitespace-nowrap text-ellipsis overflow-hidden'][normalize-space()='Custom']"}
EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_CTA_INPUT = {"//input[@placeholder='Enter Custom Call to Action']"}
EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_DESCRIPTION = {"(//p)[2]"}
EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_FORM = {"//span[contains(text(),'Select a Module')]"}
EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_FORM_SEARCH = {"//input[@placeholder='Search...']"}
EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_FORM_SEARCH_OPTION = {"//span[contains(text(),'Registration form')]"}
EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS = {"//*[@id='style-1']/div/div[5]/div/app-p-button/button"}
EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_SHOW_OTHER = {"//label[normalize-space()='Show other modules after Registration']"}
EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_MULTIPLE = {"//label[normalize-space()='Enable Multiple Registrations']"}
EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_CUSTOM_CONFIRM = {"//label[normalize-space()='Customize Confirmation Message']"}
EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_CUSTOM_CONFIRM_TEXT = {"//textarea[@placeholder='Enter confirmation message...']"}
EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_MARKETING = {"//label[normalize-space()='Email Marketing Consent']"}
EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_MARKETING_CONSENT = {"//p[contains(text(),'Sign me up for marketing emails from Testing SQA. ')]"}
EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_MARKETING_REQUIRED = {"//label[normalize-space()='Make Required']"}
EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_MARKETING_DEFAULT = {"//*[@id='style-11']/div/div[2]/div[3]/div[2]/div[2]/app-checkbox/div/p-checkbox/div"}
EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_TERM = {"//label[normalize-space()='Terms & Privacy Consent']"}
EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_TERM_CONSENT = {"//p[contains(text(),'I confirm that i have read and agree to Testing SQ')]"}
EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_TERM_REQUIRED = {"//app-checkbox[@name='Make_Required']//p-checkbox[@class='ng-valid ng-dirty ng-touched']"}
EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_TERM_DEFAULT = {"//app-checkbox[@name='Checked_by_Default']//p-checkbox[@class='ng-valid ng-dirty ng-touched']"}
EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_PROFILE = {"//label[normalize-space()='Ask to Complete Profile']"}
EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_PROFILE_NAME = {"//label[normalize-space()='Name']"}
EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_PROFILE_PHONE = {"//label[normalize-space()='Phone Number']"}
EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_PROFILE_PHONE_CONSENT = {"//label[normalize-space()='SMS Marketing Consent']"}
EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_PROFILE_PHONE_CONSENT_TEXT = {"//p[contains(text(),'By signing up you agree to receive recurring autom')]"}
EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_PROFILE_PHONE_DEFAULT = {"//label[normalize-space()='Require Consent']"}
EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_PROFILE_PHONE_REQUIRED = {"//label[@for='I983MK']"}
EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_GOOGLE_SIGNUP = {"//label[normalize-space()='Hide Google Signup Option']"}
EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_PURCHASE = {"//label[normalize-space()='Require Purchase Details']"}
EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_PURCHASE_TEXT = {"//textarea[@placeholder='Please add purchase details to complete registration.']"}
EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_PURCHASE_NAME = {"//body[1]/p-dynamicdialog[1]/div[1]/div[1]/div[1]/app-products-edit-popup[1]/div[2]/div[2]/div[1]/app-registration-edit[1]/form[1]/div[1]/div[1]/div[1]/div[1]/div[1]/div[2]/div[8]/div[2]/div[1]/app-checkbox[1]/div[1]/p-checkbox[1]"}
EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_PURCHASE_PHONE = {"//app-checkbox[@name='purchaseTemplate.phoneNo']//p-checkbox[@class='ng-untouched ng-pristine ng-valid']"}
EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_PURCHASE_PHONE_CONSENT = {"//*[@id='style-11']/div/div[2]/div[8]/div[3]/div/div/div/app-checkbox/div/label"}
EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_PURCHASE_PHONE_CONSENT_TEXT = {"//p[contains(text(),'Sign up for texts. By checking this box, I agree t')]"}
EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_PURCHASE_PHONE_REQUIRED = {"//label[@for='66UHC6']"}
EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_PURCHASE_PHONE_DEFAULT = {"//label[@for='IUA95T']"}
EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_PURCHASE_NAME1 = {"//*[@id='style-11']/div/div[2]/div[8]/div[2]/div/app-checkbox/div/label"}
EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_PURCHASE_PDATE = {"//label[normalize-space()='Purchase Date']"}
EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_PURCHASE_PDATE_DYNAMIC = {"//label[normalize-space()='Dynamic Date Window']"}
EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_PURCHASE_PDATE_DYNAMIC_BEFORE = {"//input[@name='daysBeforeCurrentDate']"}
EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_PURCHASE_PDATE_DYNAMIC_AFTER = {"//input[@name='daysAfterCurrentDate']"}
EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_PURCHASE_PDATE_FIXED = {"//label[normalize-space()='Fixed Date Window']"}
EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_PURCHASE_QUANTITY = {"//label[normalize-space()='Quantity']"}
EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_PURCHASE_PLACE_PURCHASE = {"//label[normalize-space()='Place of Purchase']"}
EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_PURCHASE_PLACE_RETAIL_CHANNEL = {"/html/body/p-dynamicdialog/div/div/div/app-products-edit-popup/div[2]/div[2]/div[1]/app-registration-edit/form/div/div/div/div[1]/div/div[2]/div[8]/div[6]/div/div/div/app-retail-channel-dropdown/div/app-multiselect/div/p-multiselect/div[2]"}
EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_PURCHASE_PLACE_RETAIL_CHANNEL_ALL = {"//label[normalize-space()='All Channels']"}
EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_PURCHASE_PLACE_RETAIL_CHANNEL_NEW = {"//label[normalize-space()='New Channel']"}
EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_PURCHASE_PLACE_RETAIL_CHANNEL_NEW_NAME = {"//input[@id='name']"}
EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_PURCHASE_PLACE_RETAIL_CHANNEL_NEW_NAME_SAVE = {"//button[@class='full-width full-width-button medium primary p-button p-component']"}
EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_PURCHASE_PLACE_RETAIL_CHANNEL_OPTION = {"//img[@class='close-icon']"}
EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_PURCHASE_SERIAL_NUM = {"//label[normalize-space()='Serial Number']"}
EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_PURCHASE_PROOF = {"//label[normalize-space()='Proof of Purchase (Receipt Upload)']"}
EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_PURCHASE_PROOF_TEXT = {"//input[@placeholder='Call to Action...']"}
EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_REQUIRED_APPROVAL = {"//label[normalize-space()='Require Approval']"}
EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_VERIFICATION_CRITERIA = {"//span[contains(text(),'Select Verification Criteria')]"}
EXPERIENCE_POPUP_EXPERIENCE_AS_VERIFICATION_CRITERIA_OPTION = {"//span[normalize-space()='Test Criteria']"}
EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_VERIFICATION_CRITERIA_NEW = {"//span[@class='w-full max-w-full whitespace-nowrap text-ellipsis overflow-hidden text-primary']"}
EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_VERIFICATION_CRITERIA_NAME = {"//input[@placeholder='Enter name...']"}
EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_VERIFICATION_CRITERIA_RETAILER = {"//label[normalize-space()='Verify Retailers']"}
EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_VERIFICATION_CRITERIA_INCLUDE_RETAILER = {"//label[normalize-space()='Include Retailers from Experience']"}
EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_VERIFICATION_CRITERIA_ENTER_RETAILER = {"//input[@placeholder='Enter Retailers...']"}
EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_VERIFICATION_CRITERIA_RETAILER_ADD = {"//img[@alt='white-plus.svg']"}
EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_VERIFICATION_CRITERIA_LINE_ITEM = {"//label[normalize-space()='Verify Line Items']"}
EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_VERIFICATION_CRITERIA_LINE_TEM_NAME = {"//input[@placeholder='Enter Line Item name...']"}
EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_VERIFICATION_CRITERIA_LINE_TEM_NAME_ADD = {"//img[@class='ng-tns-c787443071-61']"}
EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_VERIFICATION_CRITERIA_LINE_ITEM_PRICE = {"//label[normalize-space()='Verify Purchase Price']"}
EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_VERIFICATION_CRITERIA_LINE_ITEM_PRICE_min = {"//div[@class='p-field-checkbox modal-checkbox my-20 ng-tns-c1842535111-228 ng-valid ng-touched ng-dirty']//div[@class='verify-product-container indent-left-7 mt-6 ng-tns-c1842535111-228 ng-trigger ng-trigger-openClose ng-star-inserted']//div[1]//div[1]//input[1]"}
EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_VERIFICATION_CRITERIA_LINE_ITEM_PRICE_max = {"//label[normalize-space()='Verify Purchase Price']"}
EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_VERIFICATION_CRITERIA_LINE_ITEM_QUANTITY = {"//label[normalize-space()='Verify Quantity']"}
EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_VERIFICATION_CRITERIA_LINE_ITEM_NEW = {"//div[@class='line-item-btn ng-tns-c1842535111-53']"}
EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_VERIFICATION_CRITERIA_LINE_ITEM_DELETE = {"//span[@class='delete-btn ng-tns-c1842535111-53']"}
EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_VERIFICATION_CRITERIA_PURCHASE_DATE = {"//label[normalize-space()='Verify Purchase Date']"}
EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_VERIFICATION_CRITERIA_UNIQUENESS = {"//label[normalize-space()='Verify Uniqueness']"}
EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_VERIFICATION_CRITERIA_SAVE = {"//app-p-button[@class='ng-tns-c1842535111-53']//button[@type='button'][normalize-space()='Save']"}
EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_VERIFICATION_CRITERIA_BACK = {"//button[@type='button']//label[contains(text(),'Verification Criteria')]"}
EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_SAVE = {"/html/body/p-dynamicdialog/div/div/div/app-products-edit-popup/div[2]/div[2]/div[1]/app-registration-edit/form/div/div/div/div[1]/div/div[1]/div[2]/app-p-button/button"}
EXPERIENCE_POPUP_EXPERIENCE_REGISTRATION_AS_SAVE_CONFIRM = {"//span[normalize-space()='Save']"}
EXPERIENCE_POPUP_EXPERIENCE_MODULE = {"//h1[normalize-space()='Modules']"}
EXPERIENCE_POPUP_EXPERIENCE_SAVE = {"//button[normalize-space()='Save']"}
EXPERIENCE_POPUP_EXPERIENCE_Cross = {"/html/body/p-dynamicdialog/div/div/div/app-products-edit-popup/div[1]/div[2]/button/span"}
EXPERIENCE_REBATE_OPTION = {"/html/body/p-dynamicdialog/div/div/div/app-experience-landing-page/div[2]/div[1]/div[3]"}
EXPERIENCE_REBATE_SIGNUP_OPTION = {"(//div[@title='None'][normalize-space()='None'])[2]"}
EXPERIENCE_REBATE_NEW_SIGNUP = {"//span[@class='w-full max-w-full whitespace-nowrap text-ellipsis overflow-hidden text-primary']"}
EXPERIENCE_REBATE_SIGNUP_NAME = {"//input[@placeholder='Enter module name...']"}
EXPERIENCE_REBATE_SIGNUP_SHOW_BACKGROUND = {"//img[@class='long-answer-icon ng-tns-c1952139658-368']"}
EXPERIENCE_REBATE_SIGNUP_SHOW_INSTRUCTION = {"//label[normalize-space()='Show Instructions']"}
EXPERIENCE_REBATE_SIGNUP_CARD_TITLE = {"//input[@placeholder='Enter title here...']"}
EXPERIENCE_REBATE_SIGNUP_ADD_STEP = {"//div[contains(@class, 'add-step-btn')]/span[text()='Add Step']"}
EXPERIENCE_REBATE_SIGNUP_ADD_STEPP = {"name": "Add Step"}
EXPERIENCE_REBATE_SIGNUP_REMOVE_STEP = {"//div[@class='instruction-messages ng-tns-c1952139658-42 ng-untouched ng-pristine ng-invalid ng-star-inserted']//span[@class='remove-step ng-tns-c1952139658-42'][normalize-space()='Remove Step']"}
EXPERIENCE_REBATE_SIGNUP_REMOVE_STEPP = {"name": "Remove Step"}
EXPERIENCE_REBATE_SIGNUP_DESCRIPTION = {"(//p)[2]"}
EXPERIENCE_REBATE_SIGNUP_SMS_MARKETING = {"//label[normalize-space()='SMS Marketing Consent']"}
EXPERIENCE_REBATE_SIGNUP_SMS_CONSENT = {"//p[contains(text(),'By entering your phone number or by sending us a t')]"}
EXPERIENCE_REBATE_SIGNUP_CUSTOM_CTA = {"//label[normalize-space()='Customize Button CTA']"}
EXPERIENCE_REBATE_SIGNUP_AS = {"//img[@alt='advance settings icon']"}
EXPERIENCE_REBATE_SIGNUP_AS_DISABLE_OPTION = {"//label[normalize-space()='Disable ``Text to Opt-In`` on Mobile']"}
EXPERIENCE_REBATE_SIGNUP_AS_DIM_BACKGROUND = {"//label[normalize-space()='Dim Background']"}
EXPERIENCE_REBATE_SIGNUP_AS_SOCIAL_MEDIA = {"//label[normalize-space()='Social Media Icons']"}
EXPERIENCE_REBATE_SIGNUP_AS_SEND_USER = {"//label[normalize-space()='Send Mobile Users Directly to Messaging App']"}
EXPERIENCE_REBATE_SIGNUP_AS_LEGAL_TEXT = {"//label[normalize-space()='Customize legal text']"}
EXPERIENCE_REBATE_SIGNUP_AS_LEGAL_TEXT_CONSENT = {"(//p[contains(text(),'By entering your phone number or by sending us a t')])[1]"}
EXPERIENCE_REBATE_SIGNUP_SAVE = {"//label[normalize-space()='Save']"}
EXPERIENCE_REBATE_SIGNUP_SAVE1 = {"class name": "primary small undefined p-button p-component"}
EXPERIENCE_REBATE_SIGNUP_AS_BACK = {"//label[normalize-space()='Advanced Settings']"}
EXPERIENCE_REBATE_SIGNUP_BACK = {"(//label[contains(text(),'Rebate Signup Page')])[2]"}
EXPERIENCE_REBATE_SIGNUP_BACK2 = {"//button[@type='button']//label[contains(text(),'Rebate Signup Page')]"}
EXPERIENCE_REBATE_SIGNUP_SAVE_EXIT = {"//span[normalize-space()='SAVE & EXIT']"}
EXPERIENCE_REBATE_CAMPAIGN = {"(//span[@class='ng-star-inserted'][normalize-space()='Click to select'])[1]"}
EXPERIENCE_REBATE_CAMPAIGN_NEW = {"//span[@class='w-full max-w-full whitespace-nowrap text-ellipsis overflow-hidden text-primary']"}
EXPERIENCE_REBATE_CAMPAIGN_NAME = {"//input[@placeholder='Enter module name...']"}
EXPERIENCE_REBATE_CAMPAIGN_NUMBER = {""}
EXPERIENCE_REBATE_CAMPAIGN_GRACE = {"//input[@placeholder='Enter grace period...']"}
EXPERIENCE_REBATE_CAMPAIGN_REBATE_TERM = {"//span[@aria-label='Select an option']"}
EXPERIENCE_REBATE_CAMPAIGN_REBATE_TERM_BUYX_GETCASH = {"//span[normalize-space()='Buy X Get Y Cash Back']"}
EXPERIENCE_REBATE_CAMPAIGN_REBATE_TERM_CUSTOM = {""}
EXPERIENCE_REBATE_CAMPAIGN_BUYX_GETY_QUANTITY = {"//input[@class='p-inputtext p-component register-modal-input ng-tns-c1952139658-372 ng-pristine ng-valid p-filled ng-touched']"}
EXPERIENCE_REBATE_CAMPAIGN_BUYX_GETY_QUANTITY2= {"//*[@id='style-1']/div/div[5]/div/div[1]/div/input"}
EXPERIENCE_REBATE_CAMPAIGN_BUYX_GETY_PAYOUT = {"//input[@class='p-inputtext p-component register-modal-input rebate-amount-input ng-tns-c1952139658-372 ng-pristine ng-valid ng-touched']"}
EXPERIENCE_REBATE_CAMPAIGN_BUYX_GETY_PRODUCTNAME = {"//input[@formcontrolname='requiredProduct']"}
EXPERIENCE_REBATE_CAMPAIGN_BUYX_GETY_PAYOUT_PLUS = {"//*[@id='style-1']/div/div[5]/div/div[2]/div/div/span[2]/img"}
EXPERIENCE_REBATE_CAMPAIGN_BUYX_GETY_MAX = {"//div[@class='mx-rebate-amt-input-container relative ng-tns-c1952139658-372']//input[@type='text']"}
EXPERIENCE_REBATE_CAMPAIGN_REBATE_TERM_BUYX_GETY = {"//span[normalize-space()='Buy X Get Y Free']"}
EXPERIENCE_REBATE_CAMPAIGN_REBATE_TERM_BUYX_GETY_MIN = {"//input[@class='p-inputtext p-component register-modal-input ng-tns-c1952139658-375 ng-pristine ng-valid p-filled ng-touched']"}
EXPERIENCE_REBATE_CAMPAIGN_REBATE_TERM_BUYX_GETY_MAX = {"//input[@class='p-inputtext p-component register-modal-input ng-tns-c1952139658-375 ng-pristine ng-valid p-filled ng-touched']"}
EXPERIENCE_REBATE_CAMPAIGN_REBATE_TERM_BUYX_GETY_GET_BACK = {"//div[@class='flex gap-5 ng-tns-c1952139658-375 ng-star-inserted']//div[1]//div[1]//input[1]"}
EXPERIENCE_REBATE_CAMPAIGN_REBATE_TERM_BUYX_GETY_REQUIRED_PRODUCT = {"//input[@formcontrolname='requiredProduct']"}
EXPERIENCE_REBATE_CAMPAIGN_REBATE_TERM_BUYX_GETY_REBATE_AMOUNT = {"//input[@class='p-inputtext p-component register-modal-input rebate-amount-input ng-tns-c1952139658-375 ng-pristine ng-valid ng-touched']"}
EXPERIENCE_REBATE_CAMPAIGN_REBATE_TERM_BUYX_GETY_REGENERATE = {"(//span[@class='regenerate-section ng-tns-c1952139658-375'][normalize-space()='Regenerate Text'])[1]"}
EXPERIENCE_REBATE_CAMPAIGN_SAVE = {"(//button[@class='primary small undefined p-button p-component'])[1]"}
EXPERIENCE_REBATE_CAMPAIGN_AS = {"//img[@alt='advance settings icon']"}
EXPERIENCE_REBATE_CAMPAIGN_AS_REMINDER = {"//label[normalize-space()='Enable Reminder Messages']"}
EXPERIENCE_REBATE_CAMPAIGN_AS_CUSTOMIZE_AI = {"//label[normalize-space()='Customize AI Settings']"}
EXPERIENCE_REBATE_CAMPAIGN_AS_CUSTOMIZE_AI_OPTION = {"(//span[@aria-label='Select an option'])[1]"}
EXPERIENCE_REBATE_CAMPAIGN_AS_CUSTOMIZE_AI_TEXT = {"//span[normalize-space()='Validate receipt / On text message']"}
EXPERIENCE_REBATE_CAMPAIGN_AS_CUSTOMIZE_AI_TEXT2 = {"//div[@title='Validate receipt / On text message']"}
EXPERIENCE_REBATE_CAMPAIGN_AS_CUSTOMIZE_AI_RECEIPT = {"//span[normalize-space()='Validate receipt / On invalid receipt']"}
EXPERIENCE_REBATE_CAMPAIGN_AS_CUSTOMIZE_AI_RECEIPT2 = {"//div[@title='Validate receipt / On invalid receipt']"}
EXPERIENCE_REBATE_CAMPAIGN_AS_CUSTOMIZE_AI_ERROR = {"//span[normalize-space()='Validate receipt / On error']"}
EXPERIENCE_REBATE_CAMPAIGN_AS_CUSTOMIZE_AI_ERROR2 = {"//div[@title='Validate receipt / On error']"}
EXPERIENCE_REBATE_CAMPAIGN_AS_CUSTOMIZE_AI_VALID_RECEIPT = {"//span[normalize-space()='Validate receipt / On valid receipt']"}
EXPERIENCE_REBATE_CAMPAIGN_AS_CUSTOMIZE_AI_VALID_RECEIPT2 = {"//div[@title='Validate receipt / On valid receipt']"}
EXPERIENCE_REBATE_CAMPAIGN_AS_APPROVAL = {"//label[normalize-space()='Rebate Auto-Approval']"}
EXPERIENCE_REBATE_CAMPAIGN_AS_VERIFICATION_CRITERIA = {"//span[contains(text(),'Select Verification Criteria')]"}
EXPERIENCE_REBATE_CAMPAIGN_AS_VERIFICATION_CRITERIA_NEW = {"//span[@class='w-full max-w-full whitespace-nowrap text-ellipsis overflow-hidden text-primary']"}
EXPERIENCE_REBATE_CAMPAIGN_AS_VERIFICATION_CRITERIA_NAME = {"//input[@placeholder='Enter name...']"}
EXPERIENCE_REBATE_CAMPAIGN_AS_VERIFICATION_CRITERIA_RETAILER = {"//label[normalize-space()='Verify Retailers']"}
EXPERIENCE_REBATE_CAMPAIGN_AS_VERIFICATION_CRITERIA_INCLUDE_RETAILER = {"//label[normalize-space()='Include Retailers from Experience']"}
EXPERIENCE_REBATE_CAMPAIGN_AS_VERIFICATION_CRITERIA_ENTER_RETAILER = {"//input[@placeholder='Enter Retailers...']"}
EXPERIENCE_REBATE_CAMPAIGN_AS_VERIFICATION_CRITERIA_RETAILER_ADD = {"//img[@alt='white-plus.svg']"}
EXPERIENCE_REBATE_CAMPAIGN_AS_VERIFICATION_CRITERIA_LINE_ITEM = {"//label[normalize-space()='Verify Line Items']"}
EXPERIENCE_REBATE_CAMPAIGN_AS_VERIFICATION_CRITERIA_LINE_TEM_NAME = {"//input[@placeholder='Enter Line Item name...']"}
EXPERIENCE_REBATE_CAMPAIGN_AS_VERIFICATION_CRITERIA_LINE_TEM_NAME_ADD = {"//img[@class='ng-tns-c787443071-61']"}
EXPERIENCE_REBATE_CAMPAIGN_AS_AUTO_RECEIPT = {"//label[normalize-space()='Rebate Auto-Approval']"}
EXPERIENCE_REBATE_CAMPAIGN_AS_VERIFICATION_CRITERIA_LINE_ITEM_ADD= {"//img[@class='ng-tns-c787443071-61']"}
EXPERIENCE_REBATE_CAMPAIGN_AS_VERIFICATION_CRITERIA_LINE_ITEM_PRICE = {"//label[normalize-space()='Verify Purchase Price']"}
EXPERIENCE_REBATE_CAMPAIGN_AS_VERIFICATION_CRITERIA_LINE_ITEM_PRICE_min = {"//div[@class='p-field-checkbox modal-checkbox my-20 ng-tns-c1842535111-228 ng-valid ng-touched ng-dirty']//div[@class='verify-product-container indent-left-7 mt-6 ng-tns-c1842535111-228 ng-trigger ng-trigger-openClose ng-star-inserted']//div[1]//div[1]//input[1]"}
EXPERIENCE_REBATE_CAMPAIGN_AS_VERIFICATION_CRITERIA_LINE_ITEM_PRICE_max = {"//label[normalize-space()='Verify Purchase Price']"}
EXPERIENCE_REBATE_CAMPAIGN_AS_VERIFICATION_CRITERIA_LINE_ITEM_QUANTITY = {"//label[normalize-space()='Verify Quantity']"}
EXPERIENCE_REBATE_CAMPAIGN_AS_VERIFICATION_CRITERIA_LINE_ITEM_NEW = {"//div[@class='line-item-btn ng-tns-c1842535111-53']"}
EXPERIENCE_REBATE_CAMPAIGN_AS_VERIFICATION_CRITERIA_LINE_ITEM_DELETE = {"//span[@class='delete-btn ng-tns-c1842535111-53']"}
EXPERIENCE_REBATE_CAMPAIGN_AS_VERIFICATION_CRITERIA_PURCHASE_DATE = {"//label[normalize-space()='Verify Purchase Date']"}
EXPERIENCE_REBATE_CAMPAIGN_AS_VERIFICATION_CRITERIA_UNIQUENESS = {"//label[normalize-space()='Verify Uniqueness']"}
EXPERIENCE_REBATE_CAMPAIGN_AS_VERIFICATION_CRITERIA_SAVE = {"//app-p-button[@class='ng-tns-c1842535111-53']//button[@type='button'][normalize-space()='Save']"}
EXPERIENCE_REBATE_CAMPAIGN_AS_VERIFICATION_CRITERIA_BACK  = {"//button[@type='button']//label[contains(text(),'Verification Criteria')]"}
EXPERIENCE_REBATE_CAMPAIGN_AS_SAVE = {"(//button[@type='button'][normalize-space()='Save'])[2]"}
EXPERIENCE_REBATE_CAMPAIGN_AS_BACK = {"//label[normalize-space()='Advanced Settings']"}
EXPERIENCE_REBATE_CAMPAIGN_BACK = {"//label[normalize-space()='Rebate Campaign']"}
EXPERIENCE_REBATE_CAMPAIGN_SAVE_CHANGES = {"//span[normalize-space()='SAVE & EXIT']"}
EXPERIENCE_REBATE_CAMPAIGN_DISCARD = {"(//span[normalize-space()='DON'T SAVE'])[1]"}
EXPERIENCE_REBATE_AS = {"//button[normalize-space()='Advanced Settings']"}
EXPERIENCE_REBATE_AS_CONTENT_GATE = {"//label[normalize-space()='Enable Content Gate']"}
EXPERIENCE_REBATE_AS_CONTENT_GATE_NEW = {"//span[@class='w-full max-w-full whitespace-nowrap text-ellipsis overflow-hidden text-primary']"}
EXPERIENCE_REBATE_AS_CONTENT_GATE_NAME = {"//input[@placeholder='Enter name...']"}
EXPERIENCE_REBATE_AS_CONTENT_GATE_DESCRIPTION = {"//div[@class='fr-element fr-view default-styles-9']//p"}
EXPERIENCE_REBATE_AS_CONTENT_GATE_SHOW_BACKGROUND = {"//span[@class='second-part ng-tns-c2456472750-382']"}
EXPERIENCE_REBATE_AS_CONTENT_GATE_VERIFY_AGE = {"//label[normalize-space()='Verify Age']"}
EXPERIENCE_REBATE_AS_CONTENT_GATE_AGE = {"//input[@placeholder='Enter minimum age']"}
EXPERIENCE_REBATE_AS_CONTENT_GATE_BIRTHDAY = {"//label[normalize-space()='Require Birthdate Entry']"}
EXPERIENCE_REBATE_AS_CONTENT_GATE_SAVE = {"(//button[@type='button'][normalize-space()='Save'])[2]"}
EXPERIENCE_REBATE_AS_CONTENT_GATE_BACK = {"//label[normalize-space()='Content Gate']"}
EXPERIENCE_REBATE_AS_ALTERNATELOGO = {"//label[normalize-space()='Use Alternate Logo']"}
EXPERIENCE_REBATE_AS_AUTO_RECIEPT = {"//label[normalize-space()='Auto-Verify Receipts']"}
EXPERIENCE_REBATE_AS_VERIFICATION_CRITERIA = {"//span[contains(text(),'Select Verification Criteria')]"}
EXPERIENCE_REBATE_AS_VERIFICATION_CRITERIA_NEW = {"//span[@class='w-full max-w-full whitespace-nowrap text-ellipsis overflow-hidden text-primary']"}
EXPERIENCE_REBATE_AS_VERIFICATION_CRITERIA_NAME = {"//input[@placeholder='Enter name...']"}
EXPERIENCE_REBATE_AS_VERIFICATION_CRITERIA_RETAILER = {"//label[normalize-space()='Verify Retailers']"}
EXPERIENCE_REBATE_AS_VERIFICATION_CRITERIA_INCLUDE_RETAILER = {"//label[normalize-space()='Include Retailers from Experience']"}
EXPERIENCE_REBATE_AS_VERIFICATION_CRITERIA_ENTER_RETAILER = {"//input[@placeholder='Enter Retailers...']"}
EXPERIENCE_REBATE_AS_VERIFICATION_CRITERIA_RETAILER_ADD = {"//img[@alt='white-plus.svg']"}
EXPERIENCE_REBATE_AS_VERIFICATION_CRITERIA_LINE_ITEM = {"//label[normalize-space()='Verify Line Items']"}
EXPERIENCE_REBATE_AS_VERIFICATION_CRITERIA_LINE_ITEM_ADD = {"//div[@class='line-item-btn ng-tns-c1842535111-390']"}
EXPERIENCE_REBATE_AS_VERIFICATION_CRITERIA_LINE_TEM_NAME = {"//input[@placeholder='Enter Line Item name...']"}
EXPERIENCE_REBATE_AS_VERIFICATION_CRITERIA_LINE_TEM_NAME_ADD = {"//span[@class='add-btn ng-tns-c787443071-394']"}
EXPERIENCE_REBATE_AS_VERIFICATION_CRITERIA_LINE_ITEM_PRICE = {"//label[normalize-space()='Verify Purchase Price']"}
EXPERIENCE_REBATE_AS_VERIFICATION_CRITERIA_LINE_ITEM_QUANTITY = {"//label[normalize-space()='Verify Quantity']"}
EXPERIENCE_REBATE_AS_VERIFICATION_CRITERIA_LINE_ITEM_NEW = {"//div[@class='line-item-btn ng-tns-c1842535111-390']"}
EXPERIENCE_REBATE_AS_VERIFICATION_CRITERIA_LINE_ITEM_DELETE = {"//div[@class='ng-tns-c1842535111-390']//div[2]//div[1]//div[1]//span[2]"}
EXPERIENCE_REBATE_AS_VERIFICATION_CRITERIA_PURCHASE_DATE = {"//label[normalize-space()='Verify Purchase Date']"}
EXPERIENCE_REBATE_AS_VERIFICATION_CRITERIA_UNIQUENESS = {"//label[normalize-space()='Verify Uniqueness']"}
EXPERIENCE_REBATE_AS_VERIFICATION_CRITERIA_SAVE = {"(//button[@type='button'][normalize-space()='Save'])[2]"}
EXPERIENCE_REBATE_AS_VERIFICATION_CRITERIA_BACK = {"//button[@type='button']//label[contains(text(),'Verification Criteria')]"}
EXPERIENCE_REBATE_AS_SAVE = {"//button[@class='full-width full-width-button medium primary product-save-btn p-button p-component']"}
EXPERIENCE_REBATE_AS_BACK = {"//label[normalize-space()='Advanced Settings']"}
EXPERIENCE_DYNAMIC_LINK_OPTION = {"//span[normalize-space()='Dynamic Link']"}
EXPERIENCE_DYNAMIC_LINK_TYPE = {"//app-dropdown[@placeholder='Click to select']//div[@class='primeng']"}
EXPERIENCE_DYNAMIC_LINK_TYPE_LINK = {"//div[contains(text(),'Link')]"}
EXPERIENCE_DYNAMIC_LINK_TYPE_LINK_DESTINATION_TYPE = {"//span[@aria-label='Select destination type']"}
EXPERIENCE_DYNAMIC_LINK_TYPE_LINK_DESTINATION_TYPE_BRIJURL = {"//span[normalize-space()='Brij Experience']"}
EXPERIENCE_DYNAMIC_LINK_TYPE_LINK_DESTINATION_TYPE_BRIJURL_DESTINATION = {"//span[@aria-label='Select experience']"}
EXPERIENCE_DYNAMIC_LINK_TYPE_LINK_DESTINATION_TYPE_BRIJURL_DESTINATION_SEARCH = {"//input[@placeholder='Search...']"}
EXPERIENCE_DYNAMIC_LINK_TYPE_LINK_DESTINATION_TYPE_BRIJURL_DESTINATION_SEARCH_OPTION = {"//span[normalize-space()='Test IT services (SGFL)']"}
EXPERIENCE_DYNAMIC_LINK_TYPE_LINK_DESTINATION_TYPE_selected = {"//div[@title='Brij Experience']"}
EXPERIENCE_DYNAMIC_LINK_TYPE_LINK_DESTINATION_TYPE_CUSTOMURL = {"//span[normalize-space()='Custom URL']"}
EXPERIENCE_DYNAMIC_LINK_TYPE_LINK_DESTINATION_TYPE_CUSTOMURL_URL = {"//input[@placeholder='Enter a URL...']"}
EXPERIENCE_DYNAMIC_LINK_TYPE_Selected = {"//div[@title='Link']"}
EXPERIENCE_DYNAMIC_LINK_TYPE_PROBABILITY = {"//div[contains(text(),'Probability')]"}
EXPERIENCE_DYNAMIC_LINK_TYPE_PROBABILITY_DESTINATION_TYPE = {"(//span[@aria-label='Select destination type'])[1]"}
EXPERIENCE_DYNAMIC_LINK_TYPE_PROBABILITY_DESTINATION_TYPE_BRIJURL = {"//span[normalize-space()='Brij Experience']"}
EXPERIENCE_DYNAMIC_LINK_TYPE_PROBABILITY_DESTINATION_TYPE_BRIJURL_DESTINATION = {"//span[contains(text(),'Select experience')]"}
EXPERIENCE_DYNAMIC_LINK_TYPE_PROBABILITY_DESTINATION_TYPE_BRIJURL_DESTINATION_SEARCH = {"//input[@placeholder='Search...']"}
EXPERIENCE_DYNAMIC_LINK_TYPE_PROBABILITY_DESTINATION_TYPE_BRIJURL_DESTINATION_SEARCH_OPTION = {"//span[normalize-space()='Test IT services (SGFL)']"}
EXPERIENCE_DYNAMIC_LINK_TYPE_PROBABILITY_DESTINATION_TYPE_selected= {"//div[@title='Brij Experience']"}
EXPERIENCE_DYNAMIC_LINK_TYPE_PROBABILITY_DESTINATION_TYPE_CUSTOMURL = {"//span[normalize-space()='Custom URL']"}
EXPERIENCE_DYNAMIC_LINK_TYPE_PROBABILITY_DESTINATION_TYPE_CUSTOMURL_URL = {"//input[@placeholder='Enter a URL...']"}
EXPERIENCE_DYNAMIC_LINK_TYPE_PROBABILITY2_DESTINATION_TYPE = {"//span[@class='ng-star-inserted']"}
EXPERIENCE_DYNAMIC_LINK_TYPE_PROBABILITY2_DESTINATION_TYPE_BRIJURL = {"//span[normalize-space()='Brij Experience']"}
EXPERIENCE_DYNAMIC_LINK_TYPE_PROBABILITY2_DESTINATION_TYPE_BRIJURL_DESTINATION = {"//span[@aria-label='Select experience']"}
EXPERIENCE_DYNAMIC_LINK_TYPE_PROBABILITY2_DESTINATION_TYPE_BRIJURL_DESTINATION_SEARCH = {"//input[@placeholder='Search...']"}
EXPERIENCE_DYNAMIC_LINK_TYPE_PROBABILITY2_DESTINATION_TYPE_BRIJURL_DESTINATION_SEARCH_OPTION = {"//span[normalize-space()='Test IT services (SGFL)']"}
EXPERIENCE_DYNAMIC_LINK_TYPE_PROBABILITY2_DESTINATION_TYPE_selected= {"//div[@title='Brij Experience']"}
EXPERIENCE_DYNAMIC_LINK_TYPE_PROBABILITY2_DESTINATION_TYPE_CUSTOMURL = {"//span[normalize-space()='Custom URL']"}
EXPERIENCE_DYNAMIC_LINK_TYPE_PROBABILITY2_DESTINATION_TYPE_CUSTOMURL_URL = {"//input[@placeholder='Enter a URL...']"}
EXPERIENCE_DYNAMIC_LINK_TYPE_SelectedP = {"//div[@title='Probability']"}
EXPERIENCE_DYNAMIC_LINK_TYPE_GEO_LOCATION = {"//div[contains(text(),'Geolocation')]"}
EXPERIENCE_DYNAMIC_LINK_TYPE_GEO_LOCATION_COUNTRY = {"(//div[@class='p-multiselect-label-container'])[4]"}
EXPERIENCE_DYNAMIC_LINK_TYPE_GEO_LOCATION_COUNTRY_SEARCH = {"//input[@placeholder='Search...']"}
EXPERIENCE_DYNAMIC_LINK_TYPE_GEO_LOCATION_COUNTRY_SEARCH_OPTION = {"//div[@title='Asia']"}
EXPERIENCE_DYNAMIC_LINK_TYPE_GEO_LOCATION_DESTINATION_TYPE = {"(//span[@class='ng-star-inserted'][normalize-space()='Select destination type'])[1]"}
EXPERIENCE_DYNAMIC_LINK_TYPE_GEO_LOCATION_DESTINATION_TYPE_BRIJURL = {"//span[normalize-space()='Brij Experience']"}
EXPERIENCE_DYNAMIC_LINK_TYPE_GEO_LOCATION_DESTINATION_TYPE_BRIJURL_DESTINATION = {"//span[contains(text(),'Select experience')]"}
EXPERIENCE_DYNAMIC_LINK_TYPE_GEO_LOCATION_DESTINATION_TYPE_BRIJURL_DESTINATION_SEARCH = {"//input[@placeholder='Search...']"}
EXPERIENCE_DYNAMIC_LINK_TYPE_GEO_LOCATION_DESTINATION_TYPE_BRIJURL_DESTINATION_SEARCH_OPTION = {"//span[normalize-space()='Test IT services (SGFL)']"}
EXPERIENCE_DYNAMIC_LINK_TYPE_GEO_LOCATION_DESTINATION_TYPE_selected= {"//div[@title='Brij Experience']"}
EXPERIENCE_DYNAMIC_LINK_TYPE_GEO_LOCATION_DESTINATION_TYPE_CUSTOMURL = {"//span[normalize-space()='Custom URL']"}
EXPERIENCE_DYNAMIC_LINK_TYPE_GEO_LOCATION_DESTINATION_TYPE_CUSTOMURL_URL = {"//input[@placeholder='Enter a URL...']"}
EXPERIENCE_DYNAMIC_LINK_TYPE_GEO_LOCATION_DESTINATION2_TYPE = {"//span[@aria-label='Select destination type']"}
EXPERIENCE_DYNAMIC_LINK_TYPE_GEO_LOCATION_DESTINATION2_TYPE_BRIJURL = {"//span[normalize-space()='Brij Experience']"}
EXPERIENCE_DYNAMIC_LINK_TYPE_GEO_LOCATION_DESTINATION2_TYPE_BRIJURL_DESTINATION2 = {"//span[contains(text(),'Select experience')]"}
EXPERIENCE_DYNAMIC_LINK_TYPE_GEO_LOCATION_DESTINATION2_TYPE_BRIJURL_DESTINATION2_SEARCH = {"//input[@placeholder='Search...']"}
EXPERIENCE_DYNAMIC_LINK_TYPE_GEO_LOCATION_DESTINATION2_TYPE_BRIJURL_DESTINATION2_SEARCH_OPTION = {"//span[normalize-space()='Test IT services (SGFL)']"}
EXPERIENCE_DYNAMIC_LINK_TYPE_GEO_LOCATION_DESTINATION2_TYPE_selected= {"//div[@title='Brij Experience']"}
EXPERIENCE_DYNAMIC_LINK_TYPE_GEO_LOCATION_DESTINATION2_TYPE_CUSTOMURL = {"//span[normalize-space()='Custom URL']"}
EXPERIENCE_DYNAMIC_LINK_TYPE_GEO_LOCATION_DESTINATION2_TYPE_CUSTOMURL_URL = {"//input[@placeholder='Enter a URL...']"}
EXPERIENCE_DYNAMIC_LINK_TYPE_SelectedG = {"//div[@title='Geolocation']"}
EXPERIENCE_DYNAMIC_LINK_TYPE_LANGUAGE = {"(//div[contains(text(),'Language')])[2]"}
EXPERIENCE_DYNAMIC_LINK_TYPE_LANGUAGE_LANGUAGE = {"(//div[@class='p-multiselect-label-container'])[4]"}
EXPERIENCE_DYNAMIC_LINK_TYPE_LANGUAGE_LANGUAGE_SEARCH = {"//input[@placeholder='Search...']"}
EXPERIENCE_DYNAMIC_LINK_TYPE_LANGUAGE_LANGUAGE_SEARCH_OPTION = {"//div[@title='English']"}
EXPERIENCE_DYNAMIC_LINK_TYPE_LANGUAGE_DESTINATION_TYPE = {"//span[contains(text(),'Select destination type')]"}
EXPERIENCE_DYNAMIC_LINK_TYPE_LANGUAGE_DESTINATION_TYPE_BRIJURL = {"//span[normalize-space()='Brij Experience']"}
EXPERIENCE_DYNAMIC_LINK_TYPE_LANGUAGE_DESTINATION_TYPE_BRIJURL_DESTINATION = {"//span[contains(text(),'Select experience')]"}
EXPERIENCE_DYNAMIC_LINK_TYPE_LANGUAGE_DESTINATION_TYPE_BRIJURL_DESTINATION_SEARCH = {"//input[@placeholder='Search...']"}
EXPERIENCE_DYNAMIC_LINK_TYPE_LANGUAGE_DESTINATION_TYPE_BRIJURL_DESTINATION_SEARCH_OPTION = {"//span[normalize-space()='Test IT services (SGFL)']"}
EXPERIENCE_DYNAMIC_LINK_TYPE_LANGUAGE_DESTINATION_TYPE_selected= {"//div[@title='Brij Experience']"}
EXPERIENCE_DYNAMIC_LINK_TYPE_LANGUAGE_DESTINATION_TYPE_CUSTOMURL = {"//span[normalize-space()='Custom URL']"}
EXPERIENCE_DYNAMIC_LINK_TYPE_LANGUAGE_DESTINATION_TYPE_CUSTOMURL_URL = {"//input[@placeholder='Enter a URL...']"}
EXPERIENCE_DYNAMIC_LINK_ADD_CONDITION = {"//span[normalize-space()='Add Condition']"}
EXPERIENCE_DYNAMIC_LINK_REMOVE_COMPONENT_KEBAB = {"//body[1]/p-dynamicdialog[1]/div[1]/div[1]/div[1]/app-products-edit-popup[1]/div[2]/div[2]/div[1]/div[1]/app-modules-list[1]/div[1]/app-dynamic-link[1]/form[1]/div[1]/div[1]/div[1]/div[3]/div[1]/div[2]/div[1]/div[1]/div[2]/img[1]"}
EXPERIENCE_DYNAMIC_LINK_REMOVE_COMPONENT = {"//li[@class='mt-12']"}
EXPERIENCE_DIGITAL_HUB_OPTION = {"(//span[contains(text(),'Digital Hub')])[3]"}
EXPERIENCE_DIGITAL_HUB_WEBSITE_LINK = {"//span[normalize-space()='Website Link']"}
EXPERIENCE_DIGITAL_HUB_WEBSITE_LINK_BUTTONTEXT = {"//input[@placeholder='Enter button text']"}
EXPERIENCE_DIGITAL_HUB_AREA = {"xpath":"//*[@id='cdk-drop-list-16']/span"}
EXPERIENCE_DIGITAL_HUB_WEBSITE_LINK_URL = {"//input[@placeholder='Enter URL...']"}
EXPERIENCE_DIGITAL_HUB_WEBSITE_LINK_IMAGE = {"//img[@alt='hide image']"}
EXPERIENCE_DIGITAL_HUB_WEBSITE_LINK_IMAGE_ADD = {"//img[@alt='hide image']"}
EXPERIENCE_DIGITAL_HUB_EXPERIENCE_INDEX = {"//div[@aria-label='1']//div[@class='cdk-drag module-container ng-tns-c2799104018-443 w-130 ng-star-inserted']"}
EXPERIENCE_DIGITAL_HUB_EXPERIENCE_INDEX_DROPDOWN = {"//div[contains(text(),'All Experiences')]"}
EXPERIENCE_DIGITAL_HUB_EXPERIENCE_INDEX_DROPDOWN_SEARCH = {"//input[@placeholder='Search...']"}
EXPERIENCE_DIGITAL_HUB_EXPERIENCE_INDEX_DROPDOWN_SELECT_ALL = {"//label[normalize-space()='Select All']"}
EXPERIENCE_DIGITAL_HUB_EXPERIENCE_INDEX_DROPDOWN_ALL_EXPERIENCE = {"//label[normalize-space()='All Experiences']"}
EXPERIENCE_DIGITAL_HUB_EXPERIENCE_INDEX_DROPDOWN_CROSS = {"//span[@class='p-button-icon pi pi-times']"}
EXPERIENCE_DIGITAL_HUB_EXPERIENCE_INDEX_DROPDOWN_SEARCHED_OPTIO = {"//div[@title='test none (2QAC)']"}
EXPERIENCE_DIGITAL_HUB_EXPERIENCE = {"//span[normalize-space()='Experience']"}
EXPERIENCE_DIGITAL_HUB_EXPERIENCE_DROPDOWN = {"//span[contains(text(),'Select product to include...')]"}
EXPERIENCE_DIGITAL_HUB_EXPERIENCE_DROPDOWN_SEARCH = {"//input[@placeholder='Search...']"}
EXPERIENCE_DIGITAL_HUB_EXPERIENCE_DROPDOWN_CROSS = {"//span[@class='p-button-icon pi pi-times']"}
EXPERIENCE_DIGITAL_HUB_EXPERIENCE_DROPDOWN_SEARCHED_OPTION = {"//div[@title='SQAE Release WebApp (RFZR)']"}
EXPERIENCE_DIGITAL_HUB_CUSTOM_CONTENT = {"//span[normalize-space()='Custom Content']"}
EXPERIENCE_DIGITAL_HUB_CUSTOM_CONTENT_RTE = {"//div[contains(@class,'fr-element fr-view default-styles-6')]//p"}
EXPERIENCE_DIGITAL_HUB_AS = {"//button[normalize-space()='Advanced Settings']"}
EXPERIENCE_DIGITAL_HUB_AS_SHOW_SOCIAL = {"//label[normalize-space()='Show Social Icons']"}
EXPERIENCE_DIGITAL_HUB_AS_DESKTOP_VIEW = {"//label[normalize-space()='Enable Desktop View']"}
EXPERIENCE_DIGITAL_HUB_AS_DIM = {"//label[normalize-space()='Dim Background']"}
EXPERIENCE_DIGITAL_HUB_AS_CONTENT_GATE = {"//label[normalize-space()='Enable Content Gate']"}
EXPERIENCE_DIGITAL_HUB_AS_CONTENT_GATE_drop = {"//app-dropdown[@class='mb-10 spread search-dropdown ng-tns-c2956244965-126 open-above ng-untouched ng-pristine ng-invalid']//div[@class='primeng']"}
EXPERIENCE_DIGITAL_HUB_AS_CONTENT_GATE_NEW = {"//span[@class='w-full max-w-full whitespace-nowrap text-ellipsis overflow-hidden text-primary']"}
EXPERIENCE_DIGITAL_HUB_AS_CONTENT_GATE_NAME = {"//input[@placeholder='Enter name...']"}
EXPERIENCE_DIGITAL_HUB_AS_CONTENT_GATE_DESCRIPTION = {"//div[@class='fr-element fr-view default-styles-1']//p"}
EXPERIENCE_DIGITAL_HUB_AS_CONTENT_GATE_SHOW_BACKGROUND = {"//span[@class='second-part ng-tns-c2456472750-133']"}
EXPERIENCE_DIGITAL_HUB_AS_CONTENT_GATE_VERIFY_AGE = {"//label[normalize-space()='Verify Age']"}
EXPERIENCE_DIGITAL_HUB_AS_CONTENT_GATE_AGE = {"//input[@placeholder='Enter minimum age']"}
EXPERIENCE_DIGITAL_HUB_AS_CONTENT_GATE_BIRTHDAY = {"//label[normalize-space()='Require Birthdate Entry']"}
EXPERIENCE_DIGITAL_HUB_AS_CONTENT_GATE_SAVE = {"//app-p-button[@label='Save']"}
EXPERIENCE_DIGITAL_HUB_AS_CONTENT_GATE_BACK = {"//label[normalize-space()='Content Gate']"}
EXPERIENCE_DIGITAL_HUB_AS_ALTERNATELOGO = {"//label[normalize-space()='Use Alternate Logo']"}
EXPERIENCE_DIGITAL_HUB_AS_SECONDARY_MODULE_THEME = {"//label[normalize-space()='Override Theme']"}
EXPERIENCE_DIGITAL_HUB_AS_AUTO_RECIEPT = {"//label[normalize-space()='Auto-Verify Receipts']"}
EXPERIENCE_DIGITAL_HUB_AS_AUTO_RECIEPT_drop = {"//span[contains(text(),'Select Verification Criteria')]"}
EXPERIENCE_DIGITAL_HUB_AS_VERIFICATION_CRITERIA_NEW = {"//span[@class='w-full max-w-full whitespace-nowrap text-ellipsis overflow-hidden text-primary']"}
EXPERIENCE_DIGITAL_HUB_AS_VERIFICATION_CRITERIA_NAME = {"//input[@placeholder='Enter name...']"}
EXPERIENCE_DIGITAL_HUB_AS_VERIFICATION_CRITERIA_RETAILER = {"//label[normalize-space()='Verify Retailers']"}
EXPERIENCE_DIGITAL_HUB_AS_VERIFICATION_CRITERIA_INCLUDE_RETAILER = {"//label[normalize-space()='Include Retailers from Experience']"}
EXPERIENCE_DIGITAL_HUB_AS_VERIFICATION_CRITERIA_ENTER_RETAILER = {"//input[@placeholder='Enter Retailers...']"}
EXPERIENCE_DIGITAL_HUB_AS_VERIFICATION_CRITERIA_RETAILER_ADD = {"//img[@alt='white-plus.svg']"}
EXPERIENCE_DIGITAL_HUB_AS_VERIFICATION_CRITERIA_LINE_ITEM = {"//label[normalize-space()='Verify Line Items']"}
EXPERIENCE_DIGITAL_HUB_AS_VERIFICATION_CRITERIA_LINE_ITEM_ADD = {"//div[@class='line-item-btn ng-tns-c1842535111-390']"}
EXPERIENCE_DIGITAL_HUB_AS_VERIFICATION_CRITERIA_LINE_TEM_NAME = {"//input[@placeholder='Enter Line Item name...']"}
EXPERIENCE_DIGITAL_HUB_AS_VERIFICATION_CRITERIA_LINE_TEM_NAME_ADD = {"//span[@class='add-btn ng-tns-c787443071-394']"}
EXPERIENCE_DIGITAL_HUB_AS_VERIFICATION_CRITERIA_LINE_ITEM_PRICE = {"//label[normalize-space()='Verify Purchase Price']"}
EXPERIENCE_DIGITAL_HUB_AS_VERIFICATION_CRITERIA_LINE_ITEM_QUANTITY = {"//label[normalize-space()='Verify Quantity']"}
EXPERIENCE_DIGITAL_HUB_AS_VERIFICATION_CRITERIA_LINE_ITEM_NEW = {"//div[@class='line-item-btn ng-tns-c1842535111-390']"}
EXPERIENCE_DIGITAL_HUB_AS_VERIFICATION_CRITERIA_LINE_ITEM_DELETE = {"//div[@class='ng-tns-c1842535111-390']//div[2]//div[1]//div[1]//span[2]"}
EXPERIENCE_DIGITAL_HUB_AS_VERIFICATION_CRITERIA_PURCHASE_DATE = {"//label[normalize-space()='Verify Purchase Date']"}
EXPERIENCE_DIGITAL_HUB_AS_VERIFICATION_CRITERIA_UNIQUENESS = {"//label[normalize-space()='Verify Uniqueness']"}
EXPERIENCE_DIGITAL_HUB_AS_VERIFICATION_CRITERIA_SAVE = {"(//button[@type='button'][normalize-space()='Save'])[2]"}
EXPERIENCE_DIGITAL_HUB_AS_VERIFICATION_CRITERIA_BACK = {"//button[@type='button']//label[contains(text(),'Verification Criteria')]"}
EXPERIENCE_POPUP_CLOSE  = {"xpath":"//timesicon[@class='p-component p-iconwrapper ng-tns-c787154972-127 ng-star-inserted']//*[name()='svg']"}
EXPERIENCE_Expander = { "//body[1]/app-root[1]/app-brand-main[1]/div[1]/div[1]/div[2]/div[2]/div[1]/app-users-listing[1]/p-table[1]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[2]/img[2]"}
EXPERIENCE_ICON = { "img[class='cursor-pointer arrow-btn img-border ng-star-inserted']"}
EXPERIENCE_RESET_GOOGLE_PERMISSION = {"//button[normalize-space()='Reset Google Sheet']"}
EXPERIENCE_VIEW_IN_GOOGLE_SHEET = { "//button[normalize-space()='View in Google Sheet']"}
EXPERIENCE_EXPORT_BUTTON = {"xpath" : "//button[normalize-space()='Export CSV']"}
EXPERIENCE_EXPORT_CANCEL = {"xpath":"//span[normalize-space()='Cancel']"}
EXPERIENCE_EXPORT_CLOSE = {"xpath":"(//*[name()='svg'][@class='p-icon'])[1]"}
EXPERIENCE_EXPORT_EXPORT = {"xpath":"//span[normalize-space()='Export']"}
EXPERIENCE_STATUS_ACTIVE= {"xpath":"//div[@title='Active']"}
EXPERIENCE_STATUS_PENDING= {"xpath":"//div[@title='Pending']"}
EXPERIENCE_STATUS_INCOMPLETE= {"xpath":"//div[@title='Incomplete']"}
EXPERIENCE_STATUS_DENIED= {"xpath":"//div[@title='Denied']"}
EXPERIENCE_STATUS_EXPIRED= {"xpath":"//div[@title='Expired']"}
EXPERIENCE_STATUS_ALL= {"xpath":"//label[normalize-space()='All EXPERIENCE Statuses']"}
EXPERIENCE_EXPERIENCE_SOURCE_ALL = {"xpath":"//label[normalize-space()='All EXPERIENCE Sources']"}
EXPERIENCE_EXPERIENCE_SOURCE_BRIJ = {"xpath":"//div[@title='Brij']"}
EXPERIENCE_EXPERIENCE_SOURCE_OTHERS = {"xpath":"//div[@title='Other']"}
EXPERIENCE_ROWPERPAGE_OPTION = {"xpath":"//div[@aria-label='dropdown trigger']"}
EXPERIENCE_ROWPERPAGE_20 = {"xpath":"//span[@class='ng-star-inserted'][normalize-space()='20']"}
EXPERIENCE_ROWPERPAGE_100 = {"xpath":"//span[normalize-space()='100']"}
EXPERIENCE_ROWPERPAGE_1000 = {"xpath":"//span[normalize-space()='1000']"}
EXPERIENCE_EDIT_PRODUCT = {"xpath":"//span[normalize-space()='Edit Product']"}
EXPERIENCE_ADD_NEW_VARIANT = {"xpath":"//span[normalize-space()='Add New Variant']"}
EXPERIENCE_GET_EMBED_CODE = {"xpath":"//span[normalize-space()='Get Embed Code']"}
EXPERIENCE_GET_EMBED_CODE_COPY = {"xpath":"//button[normalize-space()='Copy']"}
EXPERIENCE_GET_EMBED_CODE_cross = {"xpath":"//img[@alt='close']"}
EXPERIENCE_LIST_TR1 = {"xpath":"//tbody/tr[1]/td[1]"}

EXPERIENCE_DUPLICATE = {"xpath":"//span[normalize-space()='Duplicate']"}
EXPERIENCE_DEACTIVATE = {"xpath":"//span[normalize-space()='Deactivate']"}
EXPERIENCE_ACTIVATE = {"xpath":"//span[normalize-space()='Activate']"}
EXPERIENCE_ANALYTICS = {"xpath":"//span[@class='text'][normalize-space()='Analytics']"}
EXPERIENCE_VIEW_ALL_CODES = {"xpath":"//span[normalize-space()='View All Codes']"}
EXPERIENCE_DELETE_PRODUCT = {"xpath":"//span[normalize-space()='Delete Product']"}
EXPERIENCE_SHOW_VARIANT_HOVER = {"xpath":"//span[normalize-space()='Show Variants']"}
EXPERIENCE_SHOW_QR_CODE_HOVER = {"xpath":"//tbody/tr[1]/td[10]/div[1]/div[2]"}
EXPERIENCE_SHOW_QR_CODE_HOVER_LINK = {"xpath":""}
EXPERIENCE_SYNC_ANALYTICS = {"xpath":"//span[normalize-space()='Sync Analytics']"}
# EXPERIENCE_SHOW_QR_CODE_HOVER_PNG = {"xpath":""}
# EXPERIENCE_SHOW_QR_CODE_HOVER_SVG = {"xpath":""}
# EXPERIENCE_ANALYTICS_HOVER = {"xpath":""}
EXPERIENCE_ANALYTICS_HOVER_REDIRECT = {"xpath":"//tbody/tr[1]/td[10]/div[1]/div[2]"}



# Profile

PROFILE_OPTION = {"xpath":"//body/app-root/app-brand-main[@class='ng-star-inserted']/div[@class='adminDashboardContainerWrapper']/div[@id='adminDashboardContainer']/nav[@class='main-menu ng-star-inserted']/ul/li[@class='ng-star-inserted is-active']/*/*[1]"}
PROFILE_HEADER = {"xpath":"//h1[normalize-space()='Profile']"}
PROFILE_BRAND_LOGO = {"xpath":"//span[@class='upload-text']"}
PROFILE_BRAND_LOGO_REMOVE = {"xpath":""}
PROFILE_LOGO = {"xpath":""}
PROFILE_LOGO_REMOVE = {"xpath":""}
PROFILE_BRAND_NAME = {"xpath":"//input[@placeholder='Brand Name']"}
PROFILE_BRAND_URL = {"xpath":"//input[@placeholder='Enter website URL...']"}
PROFILE_BRAND_HYPERLINK = {"xpath":"//label[normalize-space()='Hyperlink Logo to Website Homepage']"}
PROFILE_X = {"xpath":"//*[@id='mainContent']/div[2]/div/app-profile/form/div/div[1]/div[1]/div/div[4]/app-social-media/div/div[1]/div[1]/svg-icon/svg"}
PROFILE_X_LINK = {"xpath":"//input[@placeholder='Enter X URL']"}
PROFILE_FACEBOOK = {"xpath":"//*[@id='mainContent']/div[2]/div/app-profile/form/div/div[1]/div[1]/div/div[4]/app-social-media/div/div[1]/div[2]"}
PROFLE_FACEBOOK_LINK = {"xpath":"//input[@placeholder='Enter Facebook URL']"}
PROFILE_INSTAGRAM = {"xpath":"//*[@id='mainContent']/div[2]/div/app-profile/form/div/div[1]/div[1]/div/div[4]/app-social-media/div/div[1]/div[3]/i"}
PROFILE_INSTAGRAM_LINK = {"xpath":"//input[@placeholder='Enter Instagram URL']"}
PROFILE_TIKTOK = {"xpath":"//*[@id='mainContent']/div[2]/div/app-profile/form/div/div[1]/div[1]/div/div[4]/app-social-media/div/div[1]/div[4]/i"}
PROFILE_TIKTOK_LINK = {"xpath":"//input[@placeholder='Enter Tiktok URL']"}
PROFILE_THREAD = {"xpath":"//*[@id='mainContent']/div[2]/div/app-profile/form/div/div[1]/div[1]/div/div[4]/app-social-media/div/div[1]/div[5]/svg-icon/svg"}
PROFILE_THREAD_LINK = {"xpath":"//input[@placeholder='Enter Threads URL']"}
PROFILE_DISCORD = {"xpath":"//*[@id='mainContent']/div[2]/div/app-profile/form/div/div[1]/div[1]/div/div[4]/app-social-media/div/div[1]/div[6]/svg-icon/svg/g/path"}
PROFILE_DISCORD_LINK = {"xpath":"//input[@placeholder='Enter Discord URL']"}
PROFILE_PHONE = {"xpath":"//*[@id='mainContent']/div[2]/div/app-profile/form/div/div[1]/div[1]/div/div[4]/app-social-media/div/div/div[7]/i"}
PROFILE_PHONE_LINK = {"xpath":"//input[@placeholder='Enter Phone Number']"}
PROFILE_EMAIL = {"xpath":"//*[@id='mainContent']/div[2]/div/app-profile/form/div/div[1]/div[1]/div/div[4]/app-social-media/div/div/div[8]/i"}
PROFILE_EMAIL_LINK = {"xpath":"//input[@placeholder='Enter Email']"}
PROFILE_LINKEDIN = {"xpath":"//*[@id='mainContent']/div[2]/div/app-profile/form/div/div[1]/div[1]/div/div[4]/app-social-media/div/div/div[9]/i"}
PROFILE_LINKEDIN_LINK = {"xpath":"//input[@placeholder='Enter LinkedIn URL']"}
PROFILE_YOUTUBE = {"xpath":"//*[@id='mainContent']/div[2]/div/app-profile/form/div/div[1]/div[1]/div/div[4]/app-social-media/div/div/div[10]/i"}
PROFILE_YOUTUBE_LINK = {"xpath":"//input[@placeholder='Enter Youtube URL']"}
PROFILE_WHATSAPP = {"xpath":"//*[@id='mainContent']/div[2]/div/app-profile/form/div/div[1]/div[1]/div/div[4]/app-social-media/div/div/div[11]/i"}
PROFILE_WHATSAPP_LINK = {"xpath":"//input[@placeholder='Enter Whatsapp Number']"}
PROFILE_CHANGE_PASSWORD = {"xpath":"//button[normalize-space()='Change Password']"}
PROFILE_CHANGE_PASSWORD_NEW = {"xpath":"//input[@id='float-input']"}
PROFILE_CHANGE_PASSWORD_CONFIRMNEW = {"xpath":"//input[@id='float-input1']"}
PROFILE_CHANGE_PASSWORD_CONFIRM = {"xpath":"//button[@type='submit'][normalize-space()='Change Password']"}
PROFILE_CHANGE_PASSWORD_CANCEL = {"xpath":"//*[@id='pc341']/div/app-change-password/div/div/div/span/img"}
PROFILE_LOGOUT = {"xpath":"//button[normalize-space()='Log Out']"}
PROFILE_TERMANDPRIVACY = {"xpath":"//button[normalize-space()='View Terms & Privacy']"}
PROFILE_TERMS = {"xpath":"//span[normalize-space()='Brij Inc. - Terms & Conditions']"}
PROFILE_POLICY = {"xpath":"//span[normalize-space()='Brij Inc. - Privacy Policy']"}
PROFILE_DISABLE2FA = {"xpath":""}
PROFILE_ENABLE2FA = {"xpath":""}
PROFILE_2FACONFIRM = {"xpath":""}
PROFILE_2FACANCEL = {"xpath":""}
PROFILE_DELETE_PROFILE = {"xpath":"//button[normalize-space()='Delete Profile']"}
PROFILE_DELETE_PROFILE_CONFIRM = {"xpath":"//span[normalize-space()='Delete']"}
PROFILE_DELETE_PROFILE_CANCEL = {"xpath":"//span[normalize-space()='Cancel']"}
PROFILE_CI_FIRSTNAME = {"xpath":"//input[@placeholder='Enter first name...']"}
PROFILE_CI_LASTNAME = {"xpath":"//input[@placeholder='Enter last name...']"}
PROFILE_CI_EMAIL = {"xpath":"//input[@placeholder='Enter email...']"}
PROFILE_CI_PHONE = {"xpath":"//input[@placeholder='Enter phone number...']"}
PROFILE_CI_ADDRESS1 = {"xpath":"//input[@placeholder='Enter address line 1...']"}
PROFILE_CI_ADDRESS2 = {"xpath":"//input[@placeholder='Enter address line 2...']"}
PROFILE_CI_CITY = {"xpath":"//input[@placeholder='Enter city...']"}
PROFILE_CI_STATE = {"xpath":"//input[@placeholder='Enter state...']"}
PROFILE_CI_ZIP = {"xpath":"//input[@placeholder='Enter ZIP...']"}
PROFILE_LC_LEGAL_NAME = {"xpath":"//input[@formcontrolname='brandLegalName']"}
PROFILE_LC_TERMS = {"xpath":"//input[@class='p-inputtext p-component register-modal-input ng-pristine ng-valid ng-touched']"}
PROFILE_LC_PRIVACY = {"xpath":"//input[@formcontrolname='privacyPolicyURL']"}
PROFILE_SAVE = {"xpath":"//*[name()='button' and contains(@type,'submit')]"}
PROFILE_TOAST = {"xpath" : "/html/body/app-root/app-toast[1]/div/p-toast/div/p-toastitem/div/div/div[1]/div[2]"}
PROFILE_BRAND_ICON  = {"xpath":"//img[@alt='brand-logo']"}