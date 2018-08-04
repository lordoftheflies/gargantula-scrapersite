
elements = {}
elements.departure_popup = "#search-container > div:nth-child(1) > div > form > div.col-flight-search-left > div > div > div.col-departure-airport > div:nth-child(2) > div:nth-child(5) > div > div.disabled-wrap > input"
elements.departure_country = "#search-container > div:nth-child(1) > div > form > div.col-flight-search-left > div > div > div.col-departure-airport > div.core-route-selector.popup-departure-airport.opened > div > div > div.content > popup-content > core-linked-list > div.pane.left > div > div.core-list-item.core-list-item-rounded.clicked"
elements.departure_airport = "#search-container > div:nth-child(1) > div > form > div.col-flight-search-left > div > div > div.col-departure-airport > div.core-route-selector.popup-departure-airport.opened > div > div > div.content > popup-content > core-linked-list > div.pane.right > div.core-list-small > div.core-list-item.core-list-item-rounded.clicked > span"
elements.arrival_popup = "#search-container > div:nth-child(1) > div > form > div.col-flight-search-left > div > div > div.col-destination-airport > div:nth-child(2) > div:nth-child(5) > div > div.disabled-wrap > input"
elements.arrival_country = "#search-container > div:nth-child(1) > div > form > div.col-flight-search-left > div > div > div.col-destination-airport > div.core-route-selector.popup-destination-airport.opened > div > div > div.content > popup-content > core-linked-list > div.pane.left > div > div:nth-child(4)"
elements.arrival_airport = "#search-container > div:nth-child(1) > div > form > div.col-flight-search-left > div > div > div.col-destination-airport > div.core-route-selector.popup-destination-airport.opened > div > div > div.content > popup-content > core-linked-list > div.pane.right > div.core-list-small > div:nth-child(3) > span"
elements.pax_popup = "#row-dates-pax > div.col-passengers > div:nth-child(2) > div:nth-child(5) > div > div.value"
elements.increase_pax = "#row-dates-pax > div.col-passengers > div.popup-passenger-input.opened > div > div > div.content > popup-content > div:nth-child(6) > div > div.details-controls > core-inc-dec > button.core-btn.inc.core-btn-wrap"
elements.departure_date_popup = "#row-dates-pax > div:nth-child(1) > div > div.container-from > div > div.ng-pristine.ng-untouched.ng-empty.ng-invalid.ng-invalid-required > div.focused > div"
elements.departure_date = "#row-dates-pax > div:nth-child(1) > div > div.container-from > div > div.core-date-range.popup-start-date.opened > div > div > div.content > popup-content > core-datepicker > div > div.datepicker-wrapper.r.six-rows.scrollable > ul > li:nth-child(1) > ul.days > li:nth-child(20) > span"
elements.arrival_date_popup = "#row-dates-pax > div:nth-child(1) > div > div.container-to > div > div.core-date-range.popup-end-date.opened > div > div > div.content > popup-content > core-datepicker > div > div.datepicker-wrapper.r.scrollable.six-rows > ul > li:nth-child(2) > ul.days > li:nth-child(20) > span"
elements.arrival_date = "#search-container > div:nth-child(1) > div > form > div.col-flight-search-right > button:nth-child(2)"
elements.go = "#flight-FRe 8415e  e e BUDe 09f 09f 2017 20a 20e CRLe 09f 09f 2017 22a 25e > div > div.flight-header__min-price.hide-mobile"
elements.departure_choose_price = "#flight-FRe 8416e  e e CRLe 10f 14f 2017 17a 55e BUDe 10f 14f 2017 19a 55e > div > div.flight-header__min-price.hide-mobile > flights-table-price > div > div.core-btn-primary"
elements.departure_lowest_price = "#booking-selection > article > div.cart.cart-empty > section > div.trips-basket.trips-cnt > button"
elements.arrival_choose_price = "body > div.FR > main > div.body-section > extras-panels > section > article > leaderboard > div > extras-card:nth-child(3) > ng-include > div > div.action > button.core-btn-primary.add"
elements.arrival_lowest_price = "#dialog-body-slot > dialog-body > bag-selection > div > div.transfer-side-content > div.equipment-wrapper > div.equipment-passengers > bags-per-person > div > div.bags-info > div:nth-child(1) > single-bag-in-row > div:nth-child(1) > bags-selector-icon:nth-child(1) > div"
elements.next = "#dialog-body-slot > dialog-body > bag-selection > div > div.transfer-side-content > div.equipment-wrapper > div.equipment-passengers > bags-per-person > div > div.bags-info > div:nth-child(1) > single-bag-in-row > div:nth-child(1) > bags-selector-icon:nth-child(1) > div"
elements.baggage_popup = "#dialog-body-slot > dialog-body > bag-selection > div > div.transfer-side-content > div.equipment-wrapper > div.equipment-passengers > bags-per-person > div > div.bags-info > div:nth-child(1) > single-bag-in-row > div:nth-child(1) > bags-selector-icon:nth-child(1) > div"
elements.bag_weight = "#dialog-body-slot > dialog-body > bag-selection > div > div.transfer-side-content > div.equipment-wrapper > div.equipment-passengers > bags-per-person > div > div.bags-info > div:nth-child(1) > single-bag-in-row > div:nth-child(2) > bags-size-selector > div > ul > li:nth-child(1) > span.bag-item__weight"
elements.bag_price = "#dialog-body-slot > dialog-body > bag-selection > div > div.transfer-side-content > div.equipment-wrapper > div.equipment-passengers > bags-per-person > div > div.bags-info > div:nth-child(1) > single-bag-in-row > div:nth-child(2) > bags-size-selector > div > ul > li:nth-child(2) > span.bag-item__price"
elements.apply = "#dialog-body-slot > dialog-body > bag-selection > div > div.transfer-side-content > div.equipment-wrapper > div.equipment-passengers > bags-per-person > div > div.bags-info > div:nth-child(1) > single-bag-in-row > div:nth-child(1) > bags-selector-icon:nth-child(1) > div"
elements.lowest_price = "#booking-selection > article > div.cart.cart-empty > section > div.trips-basket.trips-total > trips-breakdown > div.breakdown > div > div.price-number.notranslate.short-price"

args = {}
args.url = 'https://www.ryanair.com/gb/en/'

splash.private_mode_enabled = false 

splash:go(args.url)
splash:wait(10.0)

splash:png()

splash:select(elements.departure_popup):mouse_click() 
splash:wait(1.0)

splash:png()

splash:select(elements.departure_country):mouse_click() 
splash:wait(1.0)

splash:png()

splash:select(elements.departure_airport):mouse_click() 
splash:wait(1.0) 

splash:png()

splash:select(elements.arrival_popup):mouse_click() 
splash:wait(1.0)

splash:png()

splash:select(elements.arrival_country):mouse_click() 
splash:wait(1.0)

splash:png()

splash:select(elements.arrival_airport):mouse_click() 
splash:wait(1.0)

splash:png()

splash:select(elements.pax_popup):mouse_click() 
splash:wait(1.0)

splash:png()

splash:select(elements.increase_pax):mouse_click() 
splash:wait(1.0)

splash:png()

splash:select(elements.departure_date_popup):mouse_click() 
splash:wait(1.0)

splash:png()

splash:select(elements.departure_date):mouse_click() 
splash:wait(1.0)

splash:png()

splash:select(elements.arrival_date_popup):mouse_click() 
splash:wait(1.0)

splash:png()

splash:select(elements.arrival_date):mouse_click() 
splash:wait(1.0)

splash:png()

splash:select(elements.go):mouse_click() 
splash:wait(10.0)

splash:png()

splash:select(elements.departure_choose_price):mouse_click() 
splash:wait(10.0)

splash:png()

splash:select(elements.departure_lowest_price):mouse_click() 
splash:wait(1.0)

splash:png()

splash:select(elements.arrival_choose_price):mouse_click() 
splash:wait(10.0) 

splash:png()

splash:select(elements.arrival_lowest_price):mouse_click() 
splash:wait(1.0)

splash:png()

splash:select(elements.next):mouse_click() 
splash:wait(10.0)

splash:png()

splash:select(elements.baggage_popup):mouse_click() 
splash:wait(10.0)

splash:png()

bag_weight=splash:select(elements.bag_weight):text()

bag_price=splash:select(elements.bag_price):text()

splash:select(elements.apply):mouse_click() 
splash:wait(5.0)

splash:png()

lowest_price=splash:select(elements.lowest_price):text(),

cookies=splash:get_cookies()

html=splash:html()

image=splash:png()

result = {}
result.lowest_price = lowest_price
result.bag_price = bag_price
result.bag_weight = bag_weight

result

result.html = html
result.image = image

image

%load_ext sql
