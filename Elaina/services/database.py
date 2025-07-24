from supabase import create_client, Client
from services.config import SUPABASE_URL, SUPABASE_KEY

supabase: Client = create_client(SUPABASE_URL, SUPABASE_KEY)

def insert_chat(session_id: str, user_message: str, elaina_message: str, emotional: str):
    data = {
        "session_id": session_id,
        "user_message": user_message,
        "elaina_message": elaina_message,
        "emotional": emotional
    }
    response = supabase.table("chat").insert(data).execute()

def query_chat(session_id: str):
    response = supabase.table("chat").select("user_message, elaina_message, emotional").eq("session_id", session_id).order("id").limit(1000).execute()
    return response.data