from .choices import *
from .foreign_key import *
from .primary_key import *
from .many_to_many import *

# init에 클래스를 import하지 않았을 경우
# models.choices.Person

# import한 경우
# models.Person

# 각 model에 __all__ 매직 메서드를 정의 해줬을 시에 * 로 모든 클래스를 import 해올 수 있음
