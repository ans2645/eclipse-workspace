# -*- coding: utf-8 -*- 

from UPlus_VideoPortal_LIB.PluginModule import stepResult

def TestMain():
    TC233()
    
@stepResult(descriptionMsg=u"영상카드 > 카테고리 필터버튼(▼)을 누르면 카테고리를 선택할 수 있는 Combo box가 노출")
def TC233():
    #필터버튼 찾기
    rc, result = DEV1.UIWaitForName("select_category_arrow", 3000)
    if rc != AT_SUCCESS:  # API가 성공적으로 수행되었는지 확인
        return rc
    
    if result == False:   # 오브젝트가 나타났는지 확인
        return AT_NOT_FOUND
    
    #필터버튼 클릭
    rc = DEV1.UIClickByTypeIndex('avwImageView', 9000)
    if rc != AT_SUCCESS:
        return rc
    
    rc = DEV1.UIClickByText(u"홈")
    if rc != AT_SUCCESS:
        return rc
    
    return AT_SUCCESS

