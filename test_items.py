import pytest
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_guest_should_see_add_to_cart_button(browser):
    browser.get(link)

#1 вариант решения, выдавая ошибку если кнопка найдена
    #len(str()) используется потому, что у меня выпадала ошибка: нельзя использовать len() с find_element.
    button_add=len(str(browser.find_element_by_css_selector("button.btn-add-to-basket")))
    #выдает ошибку если корзина НАЙДЕНА
    assert button_add==0, '!!!Кнопка найдена!!!'

#2 вариант решения, выдает ошибку если не найдена кнопка
    button = len(browser.find_elements_by_css_selector("button.btn-add-to-basket"))
    assert button > 0, '!!!Кнопка НЕ найдена!!!'
