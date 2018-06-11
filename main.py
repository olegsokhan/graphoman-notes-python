import aiohttp_jinja2
import asyncpg
import jinja2
from aiohttp import web
from utils import WordUtils
import asyncio


@aiohttp_jinja2.template('index.html')
async def create_note_page(request):
    if request.method == 'POST':
        data = await request.post()
        note = data['note']
        if note is not None and len(note.strip()) > 0:
            unique_words_qty = len(WordUtils().get_unique_words_with_filters_off(text=note))
            pool = request.app['pool']
            async with pool.acquire() as connection:
                async with connection.transaction():
                    await connection.execute('''
                            INSERT INTO notes(unique_words_qty, note) VALUES($1, $2)
                        ''', unique_words_qty, note)
        else:
            return {'noteIsEmpty': True}
    return {}


@aiohttp_jinja2.template('notes.html')
async def list_notes_page(request):
    pool = request.app['pool']
    async with pool.acquire() as connection:
        async with connection.transaction():
            rows = await connection.fetch('SELECT note FROM notes ORDER BY unique_words_qty DESC;')
            return {'notes': rows}
    return {}


async def init_app():
    app = web.Application()
    app['pool'] = await asyncpg.create_pool(
        user='postgres', database='graphoman', host='185.188.183.228', password='1q2w3e4r', port='5432')

    async with app['pool'].acquire() as connection:
        async with connection.transaction():
            await connection.execute('''
                    CREATE TABLE IF NOT EXISTS notes 
                    (id serial PRIMARY KEY, unique_words_qty integer NOT NULL, note text NOT NULL);
                ''')
            await connection.execute('''
                    CREATE INDEX IF NOT EXISTS unique_words_qty_idx ON notes(unique_words_qty);
                ''')

    app.add_routes([
        web.get('/', create_note_page),
        web.post('/', create_note_page),
        web.get('/notes', list_notes_page)
    ])
    return app

loop = asyncio.get_event_loop()
app = loop.run_until_complete(init_app())
aiohttp_jinja2.setup(app, loader=jinja2.FileSystemLoader('templates'))
web.run_app(app, host='185.188.183.228', port=8080)
