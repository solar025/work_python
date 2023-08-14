import work_file
import Notes
import Menu

number = 6  # сколько знаков МИНИМУМ может быть в тексте заметки


def add():
    note = Menu.create_note(number)
    array = work_file.read_file()
    for notes in array:
        if Notes.Note.get_id(note) == Notes.Note.get_id(notes):
            Notes.Note.set_id(note)
    array.append(note)
    work_file.write_file(array, 'a')
    print('Заметка добавлена...')


def show(text):
    logic = True
    array = work_file.read_file()
    if text == 'date':
        date = input('Введите дату в формате dd.mm.yyyy: ')
    for notes in array:
        if text == 'all':
            logic = False
            print(Notes.Note.map_note(notes))
        if text == 'id':
            logic = False
            print('ID: ' + Notes.Note.get_id(notes))
        if text == 'date':
            logic = False
            if date in Notes.Note.get_date(notes):
                print(Notes.Note.map_note(notes))
    if logic == True:
        print('Нет ни одной заметки...')


def id_edit_del_show(text):
    id = input('Введите id необходимой заметки: ')
    array = work_file.read_file()
    logic = True
    for notes in array:
        if id == Notes.Note.get_id(notes):
            logic = False
            if text == 'edit':
                note = Menu.create_note(number)
                Notes.Note.set_title(notes, note.get_title())
                Notes.Note.set_body(notes, note.get_body())
                Notes.Note.set_date(notes)
                print('Заметка изменена...')
            if text == 'del':
                array.remove(notes)
                print('Заметка удалена...')
            if text == 'show':
                print(Notes.Note.map_note(notes))
    if logic == True:
        print('Такой заметки нет, возможно, вы ввели неверный id')
    work_file.write_file(array, 'a')