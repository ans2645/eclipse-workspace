# -*- coding: utf-8 -*- 

from UPlus_VideoPortal_LIB.PluginModule import stepResult

def TestMain():
    TC245()
    
@stepResult(descriptionMsg=u"영상카드 > 다시 보지 않기 체크시 이후 팝업 비노출")
def TC245():
    result = False
    for i in range(0,6):
        rc = DEV1.UIClickByTypeIndex('avwImageView',9001+i)
        if rc != AT_SUCCESS:
            return rc
    #wifi가 아닌 LTE or 3G 사용 중 외부 연동을 통해 서비스되는 동영상 콘텐츠를 선택 시 데이터 요금안내 팝업을 제공
            
        searchingText = u"데이터 요금안내"
        rc, result = DEV1.UIWaitForText(searchingText, 2000, 0, UITarget.TopWindow)
        if rc != AT_SUCCESS:
            System.Debug(u"Failed to UIWaitForText")
            return rc
        
        if result == True:
            break
        
        DEV1.KeyPressByAlias('back')
        
    System.Sleep(3000)
    
    rc, result = DEV1.UIWaitForText(u"확인", 3000)
    if rc != AT_SUCCESS:  # API가 성공적으로 수행되었는지 확인
        return rc
    
    if result == False:   # 텍스트가 나타났는지 확인
        return AT_NOT_FOUND
    
    #다시보지 않기 체크
    rc = DEV1.UIClickByName('check_flag')
    if rc != AT_SUCCESS:  # API가 성공적으로 수행되었는지 확인
        return rc
    
    
    #[확인]버튼 tap 시 팝업닫히며 영상 플레이 가능한 상태로 바뀜
    rc = DEV1.UIClickByName('dialog_confirm_btn')
    rc, result = DEV1.UIWaitForName("content", 3000)
    if rc != AT_SUCCESS:  # API가 성공적으로 수행되었는지 확인
        return rc
    
    if result == False:   # 오브젝트가 나타났는지 확인
        return AT_NOT_FOUND
        
    if result == False:
        System.Debug(u"Failed to find the text : "+searchingText)
        return AT_NOT_FOUND
    
    return AT_SUCCESS