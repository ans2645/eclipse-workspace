# -*- coding: utf-8 -*- 

from UPlus_VideoPortal_LIB.PluginModule import stepResult

def TestMain():
    TC566()
    
@stepResult(descriptionMsg=u"영화 > 특집/할인 > 배너 tap하여 연결 시 LTE비디오포털 특집관 연동되는지 확인")       
def TC566():

#- 상단에 상세 화면 가이드 문구 제공
    #베너 tap
    rc = DEV1.UIClickByTypeIndex('avwImageView', 9000)
    if rc != AT_SUCCESS:
        return rc
    
    System.Sleep(2000)
    

    #특집관 연동 텍스트 확인
    rc, result = DEV1.UIWaitForName("list_description_title", 3000)
    if rc != AT_SUCCESS:  # API가 성공적으로 수행되었는지 확인
        return rc
    
    if result == False:   # 오브젝트가 나타났는지 확인
        return AT_NOT_FOUND
    
#- 영화 포스터, 제목, 개봉일, 상영시간, 감독, 주연
    BUTTONS = ("poster", "title","actor","director","open_date")
    
    for searchingObj in BUTTONS: 
        rc, result = DEV1.UIWaitForName(searchingObj, 500)
        
        if rc != AT_SUCCESS:
            System.Debug(u"Fail to UIWaitForName")
            return rc
             
        if result == False:
            System.Debug(u"Failed to find the object : "+searchingObj)
            return AT_NOT_FOUND
        
    BUTTONS = (u"주연", u"감독", u"개봉일")
    
    for searchingObj in BUTTONS: 
        rc, result = DEV1.UIWaitForText(searchingObj, 500)
        
        if rc != AT_SUCCESS:
            System.Debug(u"Fail to UIWaitForName")
            return rc
             
        if result == False:
            System.Debug(u"Failed to find the object : "+searchingObj)
            return AT_NOT_FOUND
        
        
#- 컨텐츠 선택 시 상세페이지로 이동
    rc = DEV1.UIClickByTypeIndex('avwImageView', 9000)
    if rc != AT_SUCCESS:
        return rc
    
    System.Sleep(2000)
    
    
    DEV1.KeyPressByAlias('back')
    
    return AT_SUCCESS
    
