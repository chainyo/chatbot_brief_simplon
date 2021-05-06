import motor.motor_asyncio

class DB :

    @classmethod
    def connexion(cls) :
        cls.client = motor.motor_asyncio.AsyncIOMotorClient("mongodb+srv://TJLL:M3G4H377ABot@chatbotcluster.zblke.mongodb.net/?retryWrites=true&w=majority")
        cls.db = cls.client['ChatBD']

    @classmethod
    async def find_answer(cls, tag):
        cls.connexion()
        data = await cls.db.intents.find_one({"tag": tag}, {'_id': 0})
        return data
