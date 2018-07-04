# -*- coding: utf-8 -*- 

from UPlus_VideoPortal_LIB.PluginModule import stepResult

def TestMain():
    TC234()
    
@stepResult(descriptionMsg=u"영상카드 > 카테고리 선택 Combo box 영역 외 다른 영역을 tap하거나 필터버튼(▲)을 tap하면 Combo box가 닫힘 (카테고리를 선택해도 닫힐 수 있음)")
def TC234():
    
    rc, result = DEV1.UIWaitForText(u"홈", 5000)
    if rc != AT_SUCCESS:  # API가 성공적으로 수행되었는지 확인
        return rc
    
    if result == False:   # 오브젝트가 나타났는지 확인
        return AT_NOT_FOUND
    
    # Combo box 영역 외 다른 영역을 tap하거나 필터버튼(▲) 클릭 불가 
    rc = DEV1.UIClickByText(u"홈")
    if rc != AT_SUCCESS:
        return rc
    
    rc, result = DEV1.UIWaitForText(u"홈", 5000)
    if rc != AT_SUCCESS:  # API가 성공적으로 수행되었는지 확인
        return rc
    
    if result == False:   # 오브젝트가 나타났는지 확인
        return AT_NOT_FOUND
    
    # Combo box 영역 외 다른 영역을 tap하거나 필터버튼(▲) 클릭 불가 
    #rc = DEV1.UIClickByText(u"홈")
    #if rc != AT_SUCCESS:
       # return rc
    
    rc, result = DEV1.UIWaitForText(u"영화", 5000)
    if rc != AT_SUCCESS:  # API가 성공적으로 수행되었는지 확인
        return rc
    
    if result == False:   # 오브젝트가 나타났는지 확인
        return AT_NOT_FOUND
    
    rc, result = DEV1.UIWaitForText(u"홈", 5000)
    if rc != AT_SUCCESS:  # API가 성공적으로 수행되었는지 확인
        return rc
    
    if result == False:   # 오브젝트가 나타났는지 확인
        return AT_NOT_FOUND
    
    rc = DEV1.UIClickByText(u"홈")
    if rc != AT_SUCCESS:
        return rc
    
    return AT_SUCCESS