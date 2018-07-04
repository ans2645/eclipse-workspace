# -*- coding: utf-8 -*- 

from UPlus_VideoPortal_LIB.PluginModule import stepResult

def TestMain():
    TC265()
    
@stepResult(descriptionMsg=u"영상카드 > 카드 > 각 콘텐츠 조회수 제공")
def TC265():
    #조회수 있는지 확인
    rc, result = DEV1.UIGetObjectByTypeIndex("avwObject", 9006)
    if rc != AT_SUCCESS:
        System.Finish(ExecutionResult.T_FAILED, rc)
    
    return AT_SUCCESS
    