# -*- coding: utf-8 -*- 

from UPlus_VideoPortal_LIB.PluginModule import stepResult

def TestMain():
    TC239()
    
@stepResult(descriptionMsg=u"영상카드 > 콘텐츠 이미지/텍스트 통합되어 보여지는지 확인")
def TC239():
    rc, result = DEV1.UIGetObjectByTypeIndex("avwImageView", 9001)
    if rc != AT_SUCCESS:
        System.Finish(ExecutionResult.T_FAILED, rc)
    
    rc, result = DEV1.UIGetObjectByTypeIndex("avwStaticText", 9002)
    if rc != AT_SUCCESS:
        System.Finish(ExecutionResult.T_FAILED, rc)
        
    return AT_SUCCESS