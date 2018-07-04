# -*- coding: utf-8 -*- 

from UPlus_VideoPortal_LIB.PluginModule import stepResult

def TestMain():
    TC333_336()
    
@stepResult(descriptionMsg=u"영상카드 > 카드 > 제일 마지막에 추천 콘텐츠, 연관 스토리텔링이 노출 , 이미지 노출")
def TC333_336():
    # 추천 콘텐츠 
    
    for i in range(0,30):
        rc = DEV1.ScrollRight("avwObject", 9001)
        if rc != AT_SUCCESS:
            System.Finish(ExecutionResult.T_FAILED, rc)
            

    rc, result = DEV1.UIGetObjectByTypeIndex("avwObject", 9008)
    if rc != AT_SUCCESS:
        System.Finish(ExecutionResult.T_FAILED, rc)
    
    rc = DEV1.ScrollDown("avwSubWindow", 9000)
    if rc != AT_SUCCESS:
        System.Finish(ExecutionResult.T_FAILED, rc)
    
    #연관 스토리 텔링
    rc, result = DEV1.UIGetObjectByTypeIndex("avwObject", 9017)
    if rc != AT_SUCCESS:
        System.Finish(ExecutionResult.T_FAILED, rc)
    
    #스크롤 다시 원상 복귀 
    rc = DEV1.ScrollUp("avwSubWindow", 9000)
    if rc != AT_SUCCESS:
        System.Finish(ExecutionResult.T_FAILED, rc)
    
    System.Sleep(5000)
    #메인화면으로 돌아가서     
    DEV1.KeyPressByAlias('back')
    System.Sleep(5000)
    DEV1.KeyPressByAlias('back')
    
    System.Sleep(3000)
    #더보기 눌렀던거 원상 복귀 
    rc = DEV1.CheckMenuCloseShown()
    if rc != AT_SUCCESS:
        return rc
    
    rc = DEV1.ClickMenuClose()
    if rc != AT_SUCCESS:
        return rc
    
    
        
    return AT_SUCCESS