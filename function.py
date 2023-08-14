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
    array = file_operation.read_file()
    logic = True
    for notes in array:
        if id == Note.Note.get_id(notes):
            logic = False
            if text == 'edit':
                note = ui.create_note(number)
                Note.Note.set_title(notes, note.get_title())
                Note.Note.set_body(notes, note.get_body())
                Note.Note.set_date(notes)
                print('Заметка изменена...')
            if text == 'del':
                array.remove(notes)
                print('Заметка удалена...')
            if text == 'show':
                print(Note.Note.map_note(notes))
    if logic == True:
        print('Такой заметки нет, возможно, вы ввели неверный id')
    file_operation.write_file(array, 'a')