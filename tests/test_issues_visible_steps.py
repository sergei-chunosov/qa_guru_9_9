import allure
from selene import browser, have, by
from selene.support.shared.jquery_style import s


def test_decorator_spets():
    open_main_page('https://github.com')
    search_repo('sergei-chunosov/qa_guru_9_9')
    just_click()
    check_issue()


@allure.step('Открываем страницу {page}')
def open_main_page(page):
    browser.open(page)


@allure.step('Ищем нужный репозиторий {repo}')
def search_repo(repo):
    s('.header-search-button').click()
    s('#query-builder-test').type(repo).press_enter()
    s(by.link_text(repo)).click()


@allure.step('Кликаем в issues')
def just_click():
    s('#issues-tab').click()


@allure.step('Проверяем issue')
def check_issue():
    s('#issue_1_link').should(have.exact_text('Hello Kitty!'))
