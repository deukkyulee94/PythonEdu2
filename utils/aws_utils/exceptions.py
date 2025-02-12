class AWSUtilsError(Exception):
    """AWS 유틸리티 기본 예외 클래스"""
    pass

class AWSServiceInitError(AWSUtilsError):
    """AWS 서비스 초기화 실패시 발생하는 예외"""
    pass 