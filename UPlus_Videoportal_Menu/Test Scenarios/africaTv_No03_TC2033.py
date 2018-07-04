# -*- coding: utf-8 -*- 

from UPlus_VideoPortal_LIB.PluginModule import stepResult

def TestMain():
    TC2033()
    
@stepResult(descriptionMsg=u"아프리카TV > 메인지면 > 제휴관 타이틀 > 편성된 제휴관 타이틀로 노출되는지 확인.")       
def TC2033():
    
    #아프리카TV 타이틀 찾기
    rc, result = DEV1.UIWaitForText(u"아프리카TV", 5000)
    if rc != AT_SUCCESS:
        return rc
         
    if result == False:
        return AT_NOT_FOUND
    
    #검색버튼 확인
    rc, result = DEV1.UIWaitForName(u"btn_search", 5000)
    if rc != AT_SUCCESS:
        return rc
         
    if result == False:
        return AT_NOT_FOUND
    
    
    return AT_SUCCESS
    
    
    