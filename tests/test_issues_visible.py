from selene import browser, have, by
from selene.support.shared.jquery_style import s


def test_github():
    browser.open('https://github.com')

    s('.header-search-button').click()
    s('#query-builder-test').type('sergei-chunosov/qa_guru_9_9').press_enter()
    s(by.link_text('sergei-chunosov/qa_guru_9_9')).click()

    s('#issues-tab').click()

    s('#issue_1_link').should(have.exact_text('Hello Kitty!'))

