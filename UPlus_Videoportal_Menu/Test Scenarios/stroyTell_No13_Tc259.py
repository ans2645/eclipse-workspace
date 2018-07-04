# -*- coding: utf-8 -*- 

from UPlus_VideoPortal_LIB.PluginModule import stepResult

def TestMain():
    TC259()
    
@stepResult(descriptionMsg=u"영상카드 > 카드 > 카드형 등록일 YYYY.MM.DD 형태로 노출")
def TC259():
    #등록일 확인
    rc, result = DEV1.UIGetObjectByTypeIndex('avwObject', 9008)
    if rc != AT_SUCCESS:
        System.Finish(ExecutionResult.T_FAILED, rc)
        
    return AT_SUCCESS