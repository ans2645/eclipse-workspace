# -*- coding: utf-8 -*- 

from UPlus_VideoPortal_LIB.PluginModule import stepResult

def TestMain():
    TC236_238()
    
@stepResult(descriptionMsg=u"영상카드 > 스토리텔링 콘텐츠 좌/우 2개 노출되는지 확인")
def TC236_238():
    rc, result = DEV1.UIGetObjectByTypeIndex("avwSubWindow", 9013)
    if rc != AT_SUCCESS:
        System.Finish(ExecutionResult.T_FAILED, rc)
        
    rc, result = DEV1.UIGetObjectByTypeIndex("avwSubWindow", 9014)
    if rc != AT_SUCCESS:
        System.Finish(ExecutionResult.T_FAILED, rc)
        
    return AT_SUCCESS