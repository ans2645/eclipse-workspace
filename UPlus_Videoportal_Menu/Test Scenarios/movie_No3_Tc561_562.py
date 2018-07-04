# -*- coding: utf-8 -*- 

from UPlus_VideoPortal_LIB.PluginModule import stepResult

def TestMain():
    TC561_562()
    
@stepResult(descriptionMsg=u"영화 > 장르별 > 세로 메뉴로 하위 카테고리 제공확인")       
def TC561_562():
   
    #상단에 장르별 텍스트 있는지 확인
    rc, result = DEV1.UIWaitForText(u"장르별", 3000)
    if rc != AT_SUCCESS:  # API가 성공적으로 수행되었는지 확인
        return rc
    
    if result == False:   # 텍스트가 나타났는지 확인
        return AT_NOT_FOUND
    
    #장르별 진입
    rc = DEV1.UIClickByText(u"장르별")
    if rc != AT_SUCCESS:
        return rc
    
    
    HELP_TEXT = (u"액션",u"SF\n판타지",u"코미디",u"로맨스",u"드라마")
    
    for searchingObj in HELP_TEXT: 
        rc, result = DEV1.UIWaitForText(searchingObj, 500)
        
        if rc != AT_SUCCESS:
            System.Debug(u"Fail to UIWaitForName")
            return rc
             
        if result == False:
            System.Debug(u"Failed to find the object : "+searchingObj)
            return AT_NOT_FOUND
    
    #
    rc = DEV1.ScrollDown("avwScrollView", 9000)
    if rc != AT_SUCCESS:
        System.Finish(ExecutionResult.T_FAILED, rc)
            
       
    MAIN_END = (u"수사\n스릴러",u"공포",u"어린이\n가족",u"다큐\n멘터리")
    for searchingText in MAIN_END:
        waitTimeout = 5000
        rc, result = DEV1.UIWaitForText(searchingText, waitTimeout, 0, UITarget.TopWindow)
        if rc != AT_SUCCESS:
            System.Debug(u"Failed to UIWaitForText")
            return rc
        
        if result == False:
            System.Debug(u"Failed to find the text : "+searchingText)
            return AT_NOT_FOUND
        
    
    rc = DEV1.ScrollDown("avwScrollView", 9000)
    if rc != AT_SUCCESS:
        System.Finish(ExecutionResult.T_FAILED, rc)    
        
        
    MAIN_END = (u"성인",u"영어자막",u"소장용\nVOD")
    for searchingText in MAIN_END:
        waitTimeout = 5000
        rc, result = DEV1.UIWaitForText(searchingText, waitTimeout, 0, UITarget.TopWindow)
        if rc != AT_SUCCESS:
            System.Debug(u"Failed to UIWaitForText")
            return rc
        
        if result == False:
            System.Debug(u"Failed to find the text : "+searchingText)
            return AT_NOT_FOUND
    
     
    return AT_SUCCESS
        
        