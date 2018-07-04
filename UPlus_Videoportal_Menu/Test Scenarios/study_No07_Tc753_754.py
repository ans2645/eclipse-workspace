# -*- coding: utf-8 -*- 

from UPlus_VideoPortal_LIB.PluginModule import stepResult

def TestMain():
    TC753_754()
    
@stepResult(descriptionMsg=u"교과 > 교과 화면 내에서 하단에 월정액 팝업이 발생되는지 확인")       
def TC753_754():
    '''
    -교과월정액명과 안내문구, 요금 버튼 제공
    -버튼 선택 시 요금제 상세페이지로 이동
    '''
    searchingText = u"고등"
    rc, result = DEV1.UIWaitForText(searchingText, 5000, 0, UITarget.TopWindow)
    if rc != AT_SUCCESS:
        System.Debug(u"Fail to UIWaitForName")
        return rc
    
    #찾으면 클릭
    rc = DEV1.UIClickByText(u"고등")
    if rc != AT_SUCCESS:
        return rc
    
    rc, result = DEV1.UIWaitForName('join_layout', 5000)
    if rc != AT_SUCCESS:
        System.Debug(u"Fail to UIWaitForName")
        return rc
    
    rc, result = DEV1.UIWaitForName('join_layout_title', 5000)
    if rc != AT_SUCCESS:
        System.Debug(u"Fail to UIWaitForName")
        return rc
    
    rc, result = DEV1.UIWaitForName('join_layout_btn_join', 5000)
    if rc != AT_SUCCESS:
        System.Debug(u"Fail to UIWaitForName")
        return rc
   
    
    #찾으면 클릭
    rc = DEV1.UIClickByName("join_layout_btn_join")
    if rc != AT_SUCCESS:
        return rc
    
    return AT_SUCCESS
    