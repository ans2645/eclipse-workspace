# -*- coding: utf-8 -*- 

from UPlus_VideoPortal_LIB.PluginModule import stepResult

def TestMain():
    TC334()
    
@stepResult(descriptionMsg=u"영상카드 > 카드 > 등록된 컨텐츠 명 / 컨텐츠 스틸컷 이미지 노출")
def TC334():
    #등록된 컨텐츠 명 확인
    rc, result = DEV1.UIGetObjectByTypeIndex("avwObject", 9007)
    if rc != AT_SUCCESS:
        System.Finish(ExecutionResult.T_FAILED, rc)
        
        
    #컨텐츠 스틸컷 이미지 노출 확인
    rc, result = DEV1.UIGetObjectByTypeIndex("avwObject", 9002)
    if rc != AT_SUCCESS:
        System.Finish(ExecutionResult.T_FAILED, rc)
        
        
    return AT_SUCCESS