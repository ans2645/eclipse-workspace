# -*- coding: utf-8 -*- 

from UPlus_VideoPortal_LIB.PluginModule import stepResult

def TestMain():
    TC593()
    
@stepResult(descriptionMsg=u"대박영상 > 테마추천 > 제공 섹션의 타이틀 제공 ")       
def TC593():
#- 영상 스틸컷 / 재생시간 / 제목 / 조회수 / 공유하기 / 찜하기 버튼 
    #스틸컷
    rc, result = DEV1.UIGetObjectByTypeIndex("avwImageView", 9004)
    if rc != AT_SUCCESS:
        System.Finish(ExecutionResult.T_FAILED, rc)
    #재생시간 찾기    
    rc, result = DEV1.UIGetObjectByTypeIndex("avwStaticText", 9010)
    if rc != AT_SUCCESS:
        System.Finish(ExecutionResult.T_FAILED, rc)
        
    #하이라이트명 찾기   
    rc, result = DEV1.UIGetObjectByTypeIndex("avwStaticText", 9011)
    if rc != AT_SUCCESS:
        System.Finish(ExecutionResult.T_FAILED, rc)
     
    #공유하기
    rc, result = DEV1.UIGetObjectByTypeIndex("avwImageView", 9006)
    if rc != AT_SUCCESS:
        System.Finish(ExecutionResult.T_FAILED, rc)
    #찜
    rc, result = DEV1.UIGetObjectByTypeIndex("avwImageView", 9007)
    if rc != AT_SUCCESS:
        System.Finish(ExecutionResult.T_FAILED, rc)
        
    #조회수찾기
    rc, result = DEV1.UIGetObjectByTypeIndex("avwSubWindow", 9038)
    if rc != AT_SUCCESS:
        System.Finish(ExecutionResult.T_FAILED, rc)

    return AT_SUCCESS