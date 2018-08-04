
args = {}
args.url = 'https://www.ryanair.com/gb/en/'
args.elements = {}

elements = args.elements or {}
elements.departure_popup = "#search-container > div:nth-child(1) > div > form > div.col-flight-search-left > div > div > div.col-departure-airport > div:nth-child(2) > div:nth-child(5) > div > div.disabled-wrap > input"
elements.departure_country = "#search-container > div:nth-child(1) > div > form > div.col-flight-search-left > div.row-airports > div > div.col-departure-airport > div.core-route-selector.popup-departure-airport.opened > div > div > div.content > popup-content > core-linked-list > div.pane.left > div > div.core-list-item.core-list-item-rounded.clicked"
elements.departure_airport = "#search-container > div:nth-child(1) > div > form > div.col-flight-search-left > div > div > div.col-departure-airport > div.core-route-selector.popup-departure-airport.opened > div > div > div.content > popup-content > core-linked-list > div.pane.right > div.core-list-small > div:nth-child(3) > span"
elements.arrival_popup = "#search-container > div:nth-child(1) > div > form > div.col-flight-search-left > div > div > div.col-destination-airport > div:nth-child(2) > div:nth-child(5) > div > div.disabled-wrap > input"
elements.arrival_country = "#search-container > div:nth-child(1) > div > form > div.col-flight-search-left > div > div > div.col-destination-airport > div.core-route-selector.popup-destination-airport.opened > div > div > div.content > popup-content > core-linked-list > div.pane.left > div > div:nth-child(4)"
elements.arrival_airport = "#search-container > div:nth-child(1) > div > form > div.col-flight-search-left > div > div > div.col-destination-airport > div.core-route-selector.popup-destination-airport.opened > div > div > div.content > popup-content > core-linked-list > div.pane.right > div.core-list-small > div:nth-child(3) > span"
elements.departure_date = "#row-dates-pax > div:nth-child(1) > div > div.container-from > div > div.popup-start-date > div > div > div.content > popup-content > core-datepicker > div > div.datepicker-wrapper > ul > li.calendar-view > ul.days > li:nth-child(35)"
elements.arrival_date = "#row-dates-pax > div:nth-child(1) > div > div.container-to > div > div.popup-end-date > div > div > div.content > popup-content > core-datepicker > div > div.datepicker-wrapper > ul > li:nth-child(2) > ul.days > li:nth-child(20)"
elements.pax_popup = "#row-dates-pax > div.col-passengers > div:nth-child(2) > div:nth-child(5) > div > div.value"
elements.increase_pax = "#row-dates-pax > div.col-passengers > div.popup-passenger-input.opened > div > div > div.content > popup-content > div:nth-child(6) > div > div.details-controls > core-inc-dec > button.core-btn.inc.core-btn-wrap"
elements.departure_choose_price = "flights-table-header > div > div.flight-header__min-price > flights-table-price > div > div.core-btn-primary"
elements.departure_lowest_price = "#outbound > form > div.flight-list-wrapper > div > flights-table > div > div.flights-table__rows > div > div > flights-table-fares > div > div.flights-table-fares__wrapper > div.flights-table-fares__fare > div.flights-table-fares__fare-price"
elements.arrival_choose_price = "flights-table-header > div > div.flight-header__min-price.hide-mobile > flights-table-price > div > div.core-btn-primary"
elements.arrival_lowest_price = "#inbound > form > div.flight-list-wrapper > div > flights-table > div > div.flights-table__rows > div > div > flights-table-fares > div > div.flights-table-fares__wrapper > div.flights-table-fares__fare > div.flights-table-fares__fare-price"
elements.go = "#search-container > div:nth-child(1) > div > form > div.col-flight-search-right > button:nth-child(2)"
elements.next = "#booking-selection > article > div.cart > section > div.trips-basket > button"
elements.lowest_price = "#booking-selection > article > div.cart.cart-empty > section > div.trips-basket.trips-total > trips-breakdown > div.breakdown > div > div.price-number.notranslate.short-price"
elements.baggage_popup = "body > div.FR > main > div.body-section > pt-extras-panel > div > div > div:nth-child(1) > pt-extras-section > section > div.pt-section__body > pt-extras-card:nth-child(2) > div > div"
elements.bag_weight = "#dialog-body-slot > dialog-body > bag-selection > div > div > .equipment-wrapper > .equipment-passengers > bags-per-person:nth-child(1) > div > .bags-info > div:nth-child(1) > single-bag-in-row > div:nth-child(1) > bags-selector-icon:nth-child(1) > div > .bag-icon-description > span:nth-child(1) > span > .description-label > span:nth-child(2)"
elements.bag_price = "#dialog-body-slot > dialog-body > bag-selection > div > div > div.equipment-wrapper > div.equipment-passengers > bags-per-person:nth-child(1) > div > div.bags-info > div:nth-child(1) > single-bag-in-row > div:nth-child(1) > bags-selector-icon:nth-child(1) > div > div.bag-icon-description > span:nth-child(1) > span > span:nth-child(1)"

splash.private_mode_enabled = false 

splash:go(args.url)
splash:wait(10.0)

splash:png{width=320, height=240}

splash:select(elements.departure_popup):mouse_click() 
splash:wait(1.0)

splash:select(elements.departure_country):mouse_click() 
splash:wait(1.0)

splash:select(elements.departure_airport):mouse_click() 
splash:wait(1.0)

splash:png{width=320, height=240}

splash:select(elements.arrival_country):mouse_click() 
splash:wait(1.0)

splash:select(elements.arrival_airport):mouse_click() 
splash:wait(1.0)

splash:png{width=320, height=240}

splash:select(elements.departure_date):mouse_click() 
splash:wait(1.0)

splash:select(elements.arrival_date):mouse_click() 
splash:wait(1.0)

splash:png{width=320, height=240}

splash:select(elements.pax_popup):mouse_click() 
splash:wait(1.0)

splash:select(elements.increase_pax):mouse_click() 
splash:wait(1.0)

splash:png{width=320, height=240}

splash:select(elements.go):mouse_click() 
splash:wait(10.0)

splash:png{width=320, height=240}

splash:select(elements.departure_choose_price):mouse_click() 
splash:wait(10.0)

splash:select(elements.departure_lowest_price):mouse_click() 
splash:wait(1.0)

splash:png{width=320, height=240}

splash:select(elements.arrival_choose_price):mouse_click() 
splash:wait(5.0) 

splash:select(elements.arrival_lowest_price):mouse_click() 
splash:wait(5.0)

splash:png{width=320, height=240}

splash:select(elements.next):mouse_click() 
splash:wait(5.0)

splash:png{width=320, height=240}

lowest_price=splash:select(elements.lowest_price):text()
assert(lowest_price)

splash:select(elements.baggage_popup):mouse_click() 
splash:wait(5.0)

splash:png{width=320, height=240}

bag_weight = splash:select(elements.bag_weight):text()
assert(bag_weight)

bag_price = splash:select(elements.bag_price):text()
assert(bag_price)

cookies=splash:get_cookies()

html=splash:html()

image=splash:png()

result = {}
result.lowest_price = lowest_price
result.bag_price = bag_price
result.bag_weight = bag_weight

result.html = html
result.image = image
