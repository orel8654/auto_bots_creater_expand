from main_creator_bots.templates_bots.base.base_template import CollectBase
from main_creator_bots.templates_bots.questions_answers_templates.qa_base import CollectQA
from main_creator_bots.templates_bots.support_templates.support_base import CollectSupport
from main_creator_bots.database_bots import *
from main_creator_bots.collector_bots import *
from main_creator_bots.constructor_bots import *

class DefinitionBase(CollectBase):
    def __init__(self, JSON: dict):
        super().__init__(JSON)
        self.JSON = JSON

class DefinitionQA(CollectQA):
    def __init__(self, JSON: dict):
        super().__init__(JSON)
        self.JSON = JSON

class DefinitionSupport(CollectSupport):
    def __init__(self, JSON: dict):
        super().__init__(JSON)
        self.JSON = JSON

if __name__ == '__main__':
    w = DefinitionBase({
        'buttons': 'b',
        'texts': 't',
        'connections': 'c',
        'owner': 'o',
    })