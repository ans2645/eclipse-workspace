# -*- coding: utf-8 -*- 

from UPlus_VideoPortal_LIB.PluginModule import stepResult

def TestMain():
    TC260()
    
@stepResult(descriptionMsg=u"영상카드 > 카드 > 에디터별 대표 이미지 / 팔로우 여부 아이콘 / 에디터명 제공")
def TC260():
    #에디터별 대표 이미지 확인
    rc, result = DEV1.UIGetObjectByTypeIndex("avwObject", 9003)
    if rc != AT_SUCCESS:
        System.Finish(ExecutionResult.T_FAILED, rc)
        
    #팔로우 여부 아이콘 확인
    rc, result = DEV1.UIGetObjectByTypeIndex("avwObject", 9005)
    if rc != AT_SUCCESS:
        System.Finish(ExecutionResult.T_FAILED, rc)
        
    #에디터명 제공 확인
    rc, result = DEV1.UIGetObjectByTypeIndex("avwObject", 9004)
    if rc != AT_SUCCESS:
        System.Finish(ExecutionResult.T_FAILED, rc)
        
    return AT_SUCCESS
        
