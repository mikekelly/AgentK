from dotenv import load_dotenv
load_dotenv()

from agents import hermes
from uuid import uuid4
        
uuid = str(uuid4())
hermes.hermes(uuid)