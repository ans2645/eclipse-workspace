# -*- coding: utf-8 -*- 

from UPlus_VideoPortal_LIB.PluginModule import stepResult

def TestMain():
    DEV1.StopApp()
    TC588()
    TC589()
    
@stepResult(descriptionMsg=u"대박영상 > 진입 > 장르별 / 테마추천 확인 - 좌/우 Swipe 또는 tab 영역 선택으로 tab 이동")       
def TC588():
    rc = DEV1.ClearAppData()
    if rc != AT_SUCCESS:
        return rc
    
    rc = DEV1.LauchApp()
    if rc != AT_SUCCESS:
        return rc
    
    rc = DEV1.ClearAppDataAgree()
    if rc != AT_SUCCESS:
        return rc

    rc = DEV1.CheckMainDisplayLoaded()
    if rc != AT_SUCCESS:
        return rc
    
    System.Sleep(1000)
    
    
    #더보기 나타났는지
    rc = DEV1.CheckMoreMenuShown()
    if rc != AT_SUCCESS:
        return rc
    
    
    #더보기 클릭
    rc = DEV1.ClickMoreMenu()
    if rc != AT_SUCCESS:
        return rc 
    
    #대박영상 메뉴 클릭
    rc = DEV1.ClickDaebakVideoMenu()
    if rc != AT_SUCCESS:
        return rc
    
    
    #대박영상 메뉴 진입 확인
    rc = DEV1.CheckDaebakVideoMenuSubHomeShown()
    if rc != AT_SUCCESS:
        return rc  
    
    rc = DEV1.UIClickByText(u"장르별")
    if rc != AT_SUCCESS:
        return rc
    
    
    #영상스틸컷
    rc, result = DEV1.UIGetObjectByTypeIndex("avwImageView", 9002)
    if rc != AT_SUCCESS:
        System.Finish(ExecutionResult.T_FAILED, rc)
        
    #재생시간
    rc, result = DEV1.UIGetObjectByTypeIndex("avwSubWindow", 9044)
    if rc != AT_SUCCESS:
        System.Finish(ExecutionResult.T_FAILED, rc)
        
        
    #제목
    rc, result = DEV1.UIGetObjectByTypeIndex("avwStaticText", 9016)
    if rc != AT_SUCCESS:
        System.Finish(ExecutionResult.T_FAILED, rc)
        
    #조회수
    rc, result = DEV1.UIGetObjectByTypeIndex("avwStaticText", 9017)
    if rc != AT_SUCCESS:
        System.Finish(ExecutionResult.T_FAILED, rc)
        
    #공유버튼
    rc, result = DEV1.UIGetObjectByTypeIndex("avwImageView", 9004)
    if rc != AT_SUCCESS:
        System.Finish(ExecutionResult.T_FAILED, rc)
        
    return AT_SUCCESS


@stepResult(descriptionMsg=u"대박영상 > 진입 > 찜하기")       
def TC589():
    
    rc, result = DEV1.UIWaitForName("item_jjim", 500)
    if rc != AT_SUCCESS:
        System.Debug(u"Fail to UIWaitForName")
        return rc
         
    if result == False:
        System.Debug(u"Failed to find the object : item_jjim")
        return AT_NOT_FOUND
    
    #찜하기
    #name : item_jjim , type : avwImageView , index : 9005
    rc = DEV1.UIClickByName("item_jjim")
    if rc != AT_SUCCESS:
        return rc
    """
    for i in range(0,6):
        DEV1.StoreImage("item_jjim"+str(i))
    
    
        """
    return AT_SUCCESS
    
    