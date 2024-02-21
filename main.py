from chatterbot import ChatBot

chatbot = ChatBot(
    'Mr. Cool Ice',
    storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'CustomLogicAdapter.CT_Adapter'
        },
        {
            'import_path': 'chatterbot.logic.BestMatch'
        }
    ],
    database_uri='sqlite:///database.sqlite3'
)