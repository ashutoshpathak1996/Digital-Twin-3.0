from django.urls import path
from . import views


urlpatterns = [
    path('tpgCE/', views.tpgCE, name='tpgCE'), #For tool path generation and cost evaluation service
    path('costeval/', views.costeval, name='costeval'), #For tool path generation and cost evaluation service

    path('queriesmain/', views.queriesmain, name='queriesmain'), #For cost evaluation service 
    path('freemachines/', views.freemachines, name='freemachines'), #For planning-> freemachines service
    path('purchase_requirements/', views.purchase_requirements, name='purchase_requirements'), #For Inventory -> PurchaseRequirements
    path('purchase_requirements_conn/', views.purchase_requirements_conn, name='purchase_requirements_conn'), #For Inventory -> PurchaseRequirements
    path('raw_materials_details/', views.raw_materials_details, name='raw_materials_details'), #For Inventory -> Available raw materials
    path('raw_material_floor/', views.raw_material_floor, name='raw_material_floor'), #For Inventory -> Available raw materials
    path('raw_material_machine/', views.raw_material_machine, name='raw_material_machine'), #For Inventory -> Available raw materials
    path('wip_details/', views.wip_details, name='wip_details'), #For Inventory -> wip_details
    path('wipdetail_conn/', views.wipdetail_conn, name='wipdetail_conn'), #For Inventory -> wip_details
    path('finish_goods_details/', views.finish_goods_details, name='finish_goods_details'), #For Inventory -> finish_goods_details
    path('finishedgooddetail_conn/', views.finishedgooddetail_conn, name='finishedgooddetail_conn'), #For Inventory -> finish_goods_details
    path('order_alldetails/', views.order_alldetails, name='order_alldetails'), #For Inventory -> finish_goods_details
    path('order_alldetails_conn/', views.order_alldetails_conn, name='order_alldetails_conn'), #For Inventory -> finish_goods_details
    path('maint_alldetails/', views.maint_alldetails, name='maint_alldetails'), 
    path('maint_alldetails_conn/', views.maint_alldetails_conn, name='maint_alldetails_conn'), 
    path('notifier_service/', views.notifier_service, name='notifier_service'), 
    path('addprovider_notifier/', views.addprovider_notifier, name='addprovider_notifier'), 
    path('remove_service/', views.remove_service, name='remove_service'), 
    path('removedata/', views.removedata, name='removedata'), 
    path('analyticsmain/', views.analyticsmain, name='analyticsmain'), #For Analytics Services installed
    path('machinealldetails/', views.machinealldetails, name='machinealldetails'), #For Accessing Analytics Agent Data
    path('machine_alldetails_conn/', views.machine_alldetails_conn, name='machine_alldetails_conn'), #For Inventory -> finish_goods_details
    path('toolalldetails/', views.toolalldetails, name='toolalldetails'), #For Accessing Analytics Agent Data
    path('tool_alldetails_conn/', views.tool_alldetails_conn, name='tool_alldetails_conn'), #For Inventory -> finish_goods_details
    path('alarmsmain.html/', views.alarmsmain, name='alarmsmain'), #For Inventory -> finish_goods_details
    path('alarmsmachine.html/', views.alarmsmachine, name='alarmsmachine'), #For Inventory -> finish_goods_details
    path('alarmstool.html/', views.alarmstool, name='alarmstool'), #For Inventory -> finish_goods_details
    path('recommendation_service.html/', views.recommendation_service, name='recommendation_service'), #For Inventory -> finish_goods_details
    path('recommendation_service_conn.html/', views.recommendation_service_conn, name='recommendation_service_conn'), #For Inventory -> finish_goods_details

]