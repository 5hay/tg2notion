import os
import datetime
from notion.client import NotionClient
from notion.block import TextBlock
from notion.collection import NotionDate
from pytz import timezone

def addTodoEntry(name, dueDate=False, desc=False):
    if "TG2N_NOTION_TOKEN" not in os.environ:
        return
    client = NotionClient(token_v2=os.environ['TG2N_NOTION_TOKEN'], start_monitoring=False)

    if "TG2N_NOTION_CV_LINK" not in os.environ:
        return
    cv = client.get_collection_view(os.environ['TG2N_NOTION_CV_LINK'])

    row = cv.collection.add_row()
    row.todo = name

    if dueDate:
        if " " in dueDate:
            dueDate = datetime.datetime.strptime(dueDate, '%Y%m%d %H%M')
        else:
            dueDate = datetime.datetime.strptime(dueDate, '%Y%m%d')

        tz = "Europe/Berlin"
        if "TG2N_TIMEZONE" in os.environ:
            tz = os.environ['TG2N_TIMEZONE']
        row.reminder = NotionDate(dueDate, None, timezone(os.environ['TG2N_TIMEZONE']))
    
    if desc:
        todoEntryPageId = row.id
        todoEntryPage = client.get_block(todoEntryPageId)
        child = todoEntryPage.children.add_new(TextBlock, title=desc)
