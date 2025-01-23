

def test_loc(page):
    page.goto('https://zimaev.github.io/text_input/')
    page.get_by_label("Email address").fill("qa@example.com")
    page.get_by_title("username").fill("Anton")
    page.get_by_placeholder('password').fill("secret")
    page.get_by_role('checkbox').click()


# def test_or(page):
#     selector = page.locator("input").or_(page.locator("text"))
#     selector.fill("Hello Stepik")


def test_locator_and(page):
    page.goto("https://zimaev.github.io/locatorand/")
    selector = page.get_by_role("button", name="Sing up").and_(page.get_by_title("Sing up today"))
    selector.click()


def test_with_few_elements(page):
    page.goto('https://zimaev.github.io/checks-radios/')
    checkboxes = page.locator("input")
    for checkbox in checkboxes.all():
        checkbox.check()


def test_with_filter(page):
    page.goto('https://zimaev.github.io/filter/')
    row_locator = page.locator("tr")
    row_locator.filter(has_not_text="helicopter").filter(has=page.get_by_role("button", name="Edit")).click()


def test_actions_with_check(page):
    page.goto('https://zimaev.github.io/checks-radios/')
    page.locator("text=Default checkbox").check()
    page.locator("text=Checked checkbox").check()
    page.locator("text=Default radio").check()
    page.locator("text=Default checked radio").check()
    page.locator("text=Checked switch checkbox input").check()

def test_actions_with_click(page):
    page.goto('https://zimaev.github.io/checks-radios/')
    page.locator("text=Default checkbox").click()
    page.locator("text=Checked checkbox").click()
    page.locator("text=Default radio").click()
    page.locator("text=Default checked radio").click()
    page.locator("text=Checked switch checkbox input").click()