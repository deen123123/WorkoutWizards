import typer
import csv
# from tabulate import tabulate
# from sqlmodel import select
from app.database import create_db_and_tables, get_cli_session, drop_all
from app.models import *
#from app.auth import encrypt_password

cli = typer.Typer()

@cli.command()
def initialize():
    with get_cli_session() as db: # Get a connection to the database
        drop_all() # delete all tables
        create_db_and_tables() #recreate all tables