# -*- coding: utf-8 -*- 

from UPlus_VideoPortal_LIB.PluginModule import stepResult

def TestMain():
    TC2034()
    TC2035()
    
@stepResult(descriptionMsg=u"아프리카TV > 메인지면 > 데이터요금안내 > 진입 시 데이터 요금안내 팝업 노출")       
def TC2034():
   
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
    
    #아프리카TV 메뉴 찾기
    rc, result = DEV1.UIWaitForText(u"아프리카TV", 5000)
    if rc != AT_SUCCESS:
        return rc
         
    if result == False:
        return AT_NOT_FOUND
    
    #아프리카TV 메뉴 클릭
    rc = DEV1.UIClickByText(u"아프리카TV")
    if rc != AT_SUCCESS:
        return rc
    
    
    #데이터 요금안내 찾기
    rc, result = DEV1.UIWaitForText(u"데이터 요금안내", 5000)
    if rc != AT_SUCCESS:
        return rc
         
    if result == False:
        return AT_NOT_FOUND
    
    #다시보지 않기 체크박스 확인
    rc, result = DEV1.UIWaitForName("check_flag", 5000)
    if rc != AT_SUCCESS:
        return rc
         
    if result == False:
        return AT_NOT_FOUND
    
    #다시보지 않기 체크박스 클릭
    rc = DEV1.UIClickByName(u"check_flag")
    if rc != AT_SUCCESS:
        return rc
    
    
    return AT_SUCCESS
    
    
    
@stepResult(descriptionMsg=u"아프리카TV > 메인지면 > 데이터요금안내 > [확인] Tab 시 팝업 닫히는지 확인")       
def TC2035():
    
    #확인 찾기
    rc, result = DEV1.UIWaitForText(u"확인", 5000)
    if rc != AT_SUCCESS:
        return rc
         
    if result == False:
        return AT_NOT_FOUND
    
    #확인 클릭 (터치 안됨)
    rc = DEV1.UIClickByText(u"확인")
    """if rc != AT_SUCCESS:
        return rc"""
    
    return AT_SUCCESS