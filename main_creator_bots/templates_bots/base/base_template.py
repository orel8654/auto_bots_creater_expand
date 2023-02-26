
class Base:
    def __init__(self, JSON: dict):
        self.JSON = JSON

class BaseButtons(Base):
    def __init__(self, JSON: dict):
        super().__init__(JSON)
        self.buttons = self.JSON['buttons']

class BaseText(Base):
    def __init__(self, JSON: dict):
        super().__init__(JSON)
        self.texts = self.JSON['texts']

class BaseConnections(Base):
    def __init__(self, JSON: dict):
        super(Base, self).__init__(JSON)
        self.connections = self.JSON['connections']

class BaseOwner(Base):
    def __init__(self, JSON: dict):
        super().__init__(JSON)
        self.owner = self.JSON['owner']

class CollectBase(BaseButtons, BaseText, BaseConnections, BaseOwner):
    def __init__(self, JSON):
        super().__init__(JSON)