from playwright.sync_api import sync_playwright, Page, expect
import os


def test_loc(page: Page):
    page.goto('https://zimaev.github.io/text_input/')
    page.get_by_label('Email address').fill('qa@example.com')
    page.get_by_title('username').fill('Anton')
    page.get_by_placeholder('password').fill('secret')
    page.get_by_role('checkbox').click()


'''
def test_or(page: Page):
    selector = page.locator("input").or_(page.locator("text"))
    selector.fill("Hello Stepik")
'''


def test_locator_and(page: Page):
    page.goto('https://zimaev.github.io/locatorand/')
    selector = page.get_by_role('button', name='Sing up').and_(page.get_by_title('Sing up today'))
    selector.click()


def test_with_few_elements(page: Page):
    page.goto('https://zimaev.github.io/checks-radios/')
    checkboxes = page.locator('input')
    for checkbox in checkboxes.all():
        checkbox.check()


def test_with_filter(page: Page):
    page.goto('https://zimaev.github.io/filter/')
    row_locator = page.locator('tr')
    row_locator.filter(has_not_text='helicopter').filter(has=page.get_by_role('button', name='Edit')).click()


def test_actions_with_check(page: Page):
    page.goto('https://zimaev.github.io/checks-radios/')
    page.locator('text=Default checkbox').check()
    page.locator('text=Checked checkbox').check()
    page.locator('text=Default radio').check()
    page.locator('text=Default checked radio').check()
    page.locator('text=Checked switch checkbox input').check()


def test_actions_with_click(page: Page):
    page.goto('https://zimaev.github.io/checks-radios/')
    page.locator('text=Default checkbox').click()
    page.locator('text=Checked checkbox').click()
    page.locator('text=Default radio').click()
    page.locator('text=Default checked radio').click()
    page.locator('text=Checked switch checkbox input').click()


def test_select(page: Page):
    page.goto('https://zimaev.github.io/select/')
    page.select_option('#floatingSelect', value='3')
    page.select_option('#floatingSelect', index=1)
    page.select_option('#floatingSelect', label='Нашел и завел bug')


def test_select_multiple(page: Page):
    page.goto('https://zimaev.github.io/select/')
    page.select_option('#skills', value=['playwright', 'python'])


def test_drag_and_drop(page: Page):
    page.goto('https://zimaev.github.io/draganddrop/')
    page.drag_and_drop('#drag', '#drop')


def test_dialogs_1(page: Page):
    page.goto('https://zimaev.github.io/dialog/')
    page.get_by_text('Диалог Alert').click()
    page.on('dialog', lambda dialog: dialog.accept())
    page.get_by_text('Диалог Confirmation').click()
    page.on('dialog', lambda dialog: dialog.dismiss())
    page.get_by_text('Диалог Confirmation').click()
    page.get_by_text('Диалог Prompt').click()


'''
dialog.accept() - закрыть диалоговое окно нажав кнопку «OK»
dialog.default_value - возвращает значение подсказки по умолчанию, в случае если тип диалога prompt
dialog.dismiss() - закрыть диалоговое окно нажав кнопку «Отмена/Cancel»
dialog.message - возвращает сообщение отображаемое в диалоговом окне.
dialog.type - возвращает тип диалогового окна
'''


def test_upload_file_1(page: Page):
    page.goto('https://zimaev.github.io/upload/')
    page.set_input_files('#formFile', 'hello.txt')
    page.locator('#file-submit').click()


def test_upload_file_2(page: Page):
    page.goto('https://zimaev.github.io/upload/')
    page.on('filechooser', lambda file_chooser: file_chooser.set_files('hello.txt'))
    page.locator('#formFile').click()


def test_upload_file_3(page: Page):
    page.goto('https://zimaev.github.io/upload/')
    with page.expect_file_chooser() as fc_info:
        page.locator('#formFile').click()
    file_chooser = fc_info.value
    file_chooser.set_files('hello.txt')


'''
Download

Example:
- page.on('download', lambda download: print(download.path()))

- with page.expect_download() as download_info:
    page.locator('a:has-text("Download")').click()
    
    
download.cancel() - отменяет загрузку
download.delete() - удаляет загруженный файл
download.failure() - возвращает ошибку загрузки, если таковая имеется.
download.page - возвращает объект страницы, к которой принадлежит загрузка.
download.path() - возвращает путь к загруженному файлу
download.save_as(path) - скопирует загруженный файл по указанному пути
download.suggested_filename - возвращает имя файла
download.url - возвращает загруженный URL-адрес
'''


def test_download(page: Page):
    page.goto('https://demoqa.com/upload-download')

    with page.expect_download() as download_info:
        page.locator('a:has-text("Download")').click()

    download = download_info.value
    file_name = download.suggested_filename
    destination_folder_path = './Downloads'
    download.save_as((os.path.join(destination_folder_path, file_name)))


def test_new_tab(page: Page):
    page.goto('https://zimaev.github.io/tabs/')
    with page.context.expect_page() as tab:
        page.get_by_text('Переход к Dashboard').click()
    new_tab = tab.value
    assert new_tab.url == 'https://zimaev.github.io/tabs/dashboard/index.html?'
    sigh_out = new_tab.locator('.nav-link', has_text='Sign out')
    assert sigh_out.is_visible()


'''
Expects:

expect(locator).to_be_checked()	Checkbox  установлен
expect(locator).to_be_disabled()	Веб-элемент отключен
expect(locator).to_be_editable()	Веб-элемент возможно редактировать 
expect(locator).to_be_empty()	Веб-элемент пустой
expect(locator).to_be_enabled()	Веб-элемент включен/активен
expect(locator).to_be_focused()	Веб-элемент находится в фокусе
expect(locator).to_be_hidden()	Веб-элемент не отображается
expect(locator).to_be_visible()	Веб-элемент видим/отображается
expect(locator).to_contain_text()	Веб-элемент содержит текст(текст передается аргументом к проверке)
expect(locator).to_have_attribute()	Веб-элемент имеет атрибут(атрибут передается аргументом к проверке)
expect(locator).to_have_class()	Элемент имеет класс (класс передается аргументом к проверке)
expect(locator).to_have_count()	Список имеет указанное количество/длину
expect(locator).to_have_css()	Элемент имеет CSS свойство (свойство передается аргументом к проверке)
expect(locator).to_have_id()	Элемент имеет идентификатор (идентификатор передается аргументом к проверке)
expect(locator).to_have_js_property()	Элемент имеет JavaScript свойство (свойство передается аргументом к проверке)
expect(locator).to_have_text()	Элемент имеет текст (проверяемый текст передается аргументом к проверке)
expect(locator).to_have_value()	Input имеет значение (проверяемое значение передается аргументом к проверке)
expect(locator).to_have_values()	Select имеет опции для выбора (опция передается аргументом к проверке)
expect(page).to_have_title()	Страница имеет  title (текст  title передается аргументом к проверке)
expect(page).to_have_url()	Страница имеет URL (URL передается аргументом к проверке)
expect(api_response).to_be_ok()	Ответ имеет статус OK
'''


def test_todo(page: Page):
    page.goto('https://demo.playwright.dev/todomvc/#/')
    expect(page).to_have_url('https://demo.playwright.dev/todomvc/#/')
    input_field = page.get_by_placeholder('What needs to be done?')
    expect(input_field).to_be_empty()
    input_field.fill('Playwright')
    input_field.press('Enter')
    input_field.fill('Python')
    input_field.press('Enter')
    todo_item = page.get_by_test_id('todo-item')
    expect(todo_item).to_have_count(2)
    todo_item.get_by_role('checkbox').nth(0).click()
