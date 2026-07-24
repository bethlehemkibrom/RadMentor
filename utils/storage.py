
from utils.supabase_client import supabase


def load_cases():

    response = (
        supabase
        .table("cases")
        .select("*")
        .order("created_at", desc=True)
        .execute()
    )

    return response.data or []



def save_cases(cases):
    return True



def add_case(case):

    response = (
        supabase
        .table("cases")
        .insert(case)
        .execute()
    )

    return response.data



def delete_case(case_id):

    response = (
        supabase
        .table("cases")
        .delete()
        .eq("id", case_id)
        .execute()
    )

    return response.data



def get_total_cases():

    return len(load_cases())



def clear_cases():

    (
        supabase
        .table("cases")
        .delete()
        .neq("id", "")
        .execute()
    )
