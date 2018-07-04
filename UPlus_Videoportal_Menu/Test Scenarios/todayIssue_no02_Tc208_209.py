# -*- coding: utf-8 -*- 

from UPlus_VideoPortal_LIB.PluginModule import stepResult

def TestMain():
    TC208_209()
    
@stepResult(descriptionMsg=u"대박영상 > default 화면  > 오늘의 화제 > 상단 메뉴들이 노출 되며 좌, 우 flcking 가능 7개의 메뉴를 선택할 수 있는 것을 확인")       
def TC208_209():
    
    
    LIFE_INFO = (u"오늘의 화제", u"인기영상", u"하이라이트", u"뉴스클립")        
    
    #튜플 이용해 게임 상단에 홈버튼, 검색  , GNB 있는지 확인
    for searchingObj in LIFE_INFO: 
        rc, result = DEV1.UIWaitForText(searchingObj, 500)
        
        if rc != AT_SUCCESS:
            System.Debug(u"Fail to UIWaitForText")
            return rc
             
        if result == False:
            System.Debug(u"Failed to find the object : "+searchingObj)
            return AT_NOT_FOUND
        
        rc = DEV1.UIClickByText(searchingObj)
        if rc != AT_SUCCESS:
            return rc
    
    rc = DEV1.ScrollRight("avwObject", 9001)
    if rc != AT_SUCCESS:
        return rc
    
    LIFE_INFO = ( u"웹예능", u"웹드라마")        
    
    #튜플 이용해 게임 상단에 홈버튼, 검색  , GNB 있는지 확인
    for searchingObj in LIFE_INFO: 
        rc, result = DEV1.UIWaitForText(searchingObj, 500)
        
        if rc != AT_SUCCESS:
            System.Debug(u"Fail to UIWaitForText")
            return rc
             
        if result == False:
            System.Debug(u"Failed to find the object : "+searchingObj)
            return AT_NOT_FOUND
        
        rc = DEV1.UIClickByText(searchingObj)
        if rc != AT_SUCCESS:
            return rc
        
    LIFE_INFO = (u"웹드라마", u"웹예능",  u"뉴스클립")        
    
    #튜플 이용해 게임 상단에 홈버튼, 검색  , GNB 있는지 확인
    for searchingObj in LIFE_INFO: 
        rc, result = DEV1.UIWaitForText(searchingObj, 500)
        
        if rc != AT_SUCCESS:
            System.Debug(u"Fail to UIWaitForText")
            return rc
             
        if result == False:
            System.Debug(u"Failed to find the object : "+searchingObj)
            return AT_NOT_FOUND
        
        rc = DEV1.UIClickByText(searchingObj)
        if rc != AT_SUCCESS:
            return rc
        
    rc = DEV1.ScrollLeft("avwObject", 9001)
    if rc != AT_SUCCESS:
        return rc
    
    LIFE_INFO = (u"하이라이트", u"인기영상", u"오늘의 화제" )        
    
    #튜플 이용해 게임 상단에 홈버튼, 검색  , GNB 있는지 확인
    for searchingObj in LIFE_INFO: 
        rc, result = DEV1.UIWaitForText(searchingObj, 500)
        
        if rc != AT_SUCCESS:
            System.Debug(u"Fail to UIWaitForText")
            return rc
             
        if result == False:
            System.Debug(u"Failed to find the object : "+searchingObj)
            return AT_NOT_FOUND
        
        rc = DEV1.UIClickByText(searchingObj)
        if rc != AT_SUCCESS:
            return rc
    
    return AT_SUCCESS
    
    
    