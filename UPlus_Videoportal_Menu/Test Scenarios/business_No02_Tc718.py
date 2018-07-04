# -*- coding: utf-8 -*- 

from UPlus_VideoPortal_LIB.PluginModule import stepResult

def TestMain():
    DEV1.StopApp()
    TC718()
    
@stepResult(descriptionMsg=u"인문/경영 > sub카테고리 > 카테고리 별 화면 및 리스트 정상 제공 확인")       
def TC718():
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
    
    #GNB 진입    
    rc = DEV1.ClickMainMenuGNB()
    if rc != AT_SUCCESS:
        return rc
    
    #GNB 진입 확인
    rc = DEV1.CheckMainMenuGNBLoaded()
    if rc != AT_SUCCESS:
        return rc
    
    result = False
    for i in range(0,55):
        rc = DEV1.ScrollDown("avwSubWindow", 9085)
        if rc != AT_SUCCESS:
            System.Finish(ExecutionResult.T_FAILED, rc)
            
        searchingText = u"인문/경영"
        rc, result = DEV1.UIWaitForText(searchingText, 2000, 0, UITarget.TopWindow)
        if rc != AT_SUCCESS:
            System.Debug(u"Failed to UIWaitForText")
            return rc
        
        if result == True:
            break
        
    if result == False:
        System.Debug(u"Failed to find the text : "+searchingText)
        return AT_NOT_FOUND
    
    #찾으면 클릭
    rc = DEV1.UIClickByText(u"인문/경영")
    if rc != AT_SUCCESS:
        return rc
    
    #지식채널e 클릭 -> 인문/경영  진입
    rc = DEV1.UIClickByText(u"지식채널e")
    if rc != AT_SUCCESS:
        return rc
    
    #인문/경영 타이틀 확인
    rc, result = DEV1.UIWaitForText(u"인문/경영", 5000)
    if rc != AT_SUCCESS:
        return rc
    
    if result == False:
        return AT_NOT_FOUND
    
    
    HUMAN_TV = (u"지식채널e", u"15분특강", u"CEO의 서재", u"경영전략", u"명사특강", u"철학/심리학" ,u"지식 월정액",u"테마추천")        
    
    #튜플 이용해 인문/경영 서브타이틀 카테고리 확인
    for searchingObj in HUMAN_TV: 
        rc, result = DEV1.UIWaitForText(searchingObj, 5000)
        
        if rc != AT_SUCCESS:
            System.Debug(u"Fail to UIWaitForName")
            return rc
             
        if result == False:
            System.Debug(u"Failed to find the object : "+searchingObj)
            return AT_NOT_FOUND
    
        rc = DEV1.UIClickByText(searchingObj)
        if rc != AT_SUCCESS:
            return rc
    
    return AT_SUCCESS
    