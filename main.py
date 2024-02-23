from chatterbot import ChatBot

chatbot = ChatBot(
    'SimpliCT',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    preprocessors=[
        'chatterbot.preprocessors.clean_whitespace',
        'chatterbot.preprocessors.unescape_html',
        'chatterbot.preprocessors.convert_to_ascii',
        'CustomPreprocessors.ignore_special_characters'
    ],
    logic_adapters=[
        'CustomLogicAdapter.CT_Adapter',
        'chatterbot.logic.BestMatch'
    ],
    database_uri='sqlite:///database.sqlite3'
)