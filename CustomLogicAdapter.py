from chatterbot.logic import LogicAdapter

class CT_Adapter(LogicAdapter):

    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)
    
    def can_process(self, statement):
        """
        Returns True if the input statement contains 'computational' and 'thinking'.
        """
        words = ['computational', 'thinking']

        if all(x in statement.text.split() for x in words):
            return True
        else:
            return False
    
    def process(self, input_statement, additional_response_selection_parameters=None):
        from chatterbot.conversation import Statement

        confidence = 1

        response_statement = Statement(text="Computational thinking is a way of life")

        return response_statement