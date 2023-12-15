import allure
from selene import browser, have, by
from selene.support.shared.jquery_style import s


def test_github_with():
    with allure.step('Открываем страницу https://github.com'):
        browser.open('https://github.com')

    with allure.step('Ищем нужный репозиторий'):
        s('.header-search-button').click()
        s('#query-builder-test').type('sergei-chunosov/qa_guru_9_9').press_enter()
        s(by.link_text('sergei-chunosov/qa_guru_9_9')).click()

    with allure.step('Кликаем в issues'):
        s('#issues-tab').click()
    with allure.step('Проверяем налиие нужного ишью'):
        s('#issue_1_link').should(have.exact_text('Hello Kitty!'))
