# -*- coding: utf-8 -*- 

from UPlus_VideoPortal_LIB.PluginModule import stepResult

def TestMain():
    TC261()
    
@stepResult(descriptionMsg=u"영상카드 > 카드 > 로그인 상태인 경우, tap 시 기존 팔로우 여부에 따라 팔로우 신청/취소 팝업 제공")
def TC261():
    #팔로우 클릭
    rc = DEV1.UIClickByName('_btn_follow_')
    if rc != AT_SUCCESS:
        return rc
    
    #알림 확인
    rc, result = DEV1.UIWaitForText(u"알림", 3000)
    if rc != AT_SUCCESS:  # API가 성공적으로 수행되었는지 확인
        return rc
    
    if result == False:   # 텍스트가 나타났는지 확인
        return AT_NOT_FOUND
    
    #닫기 확인
    rc, result = DEV1.UIWaitForText(u"닫기", 3000)
    if rc != AT_SUCCESS:  # API가 성공적으로 수행되었는지 확인
        return rc
    
    if result == False:   # 텍스트가 나타났는지 확인
        return AT_NOT_FOUND
    
    #팔로우 하기 확인
    rc, result = DEV1.UIWaitForText(u"팔로우 하기", 3000)
    if rc != AT_SUCCESS:  # API가 성공적으로 수행되었는지 확인
        return rc
    
    if result == False:   # 텍스트가 나타났는지 확인
        return AT_NOT_FOUND
    
    #닫기가 너무 빨라서 인식을 잘 못함
    rc = DEV1.UIClickByText(u"닫기")
    
    
    return AT_SUCCESS