def get_color(card):
    print(card)
    parts = card.split('/')
    c = parts[-1].split('.')
    return c[0]

def scrape_card(driver):
    attributes = driver.find_elements_by_xpath('//table[@class="status"]/tbody/tr/td')

    kana = attributes[1].find_element_by_xpath('./span[@class="kana"]').text
    name = kana if kana else None

    card_no = attributes[2].text if attributes[2].text else ""
    rarity = attributes[3].text if attributes[3].text else ""
    expansion = attributes[4].text if attributes[4].text else ""
    card_type = attributes[6].text if attributes[6].text else ""

    color = get_color(attributes[7].find_element_by_xpath('./img').get_attribute("src"))


    level =  -1 if attributes[8].text == "-" else int(attributes[8].text)
    cost = -1 if attributes[9].text == "-" else int(attributes[9].text)
    power = -1  if attributes[10].text == "-" else int(attributes[10].text)

    soul = len(attributes[11].find_elements_by_xpath('./img[contains(@src, "../partimages/soul.gif")]'))

    traits = attributes[13].text if attributes[13].text else ""
    text = attributes[14].text if attributes[14].text else ""
    flavor = attributes[15].text if attributes[15].text else ""


    card_dict = {
        "name": name,
        "set_code": card_no,
        "rarity": rarity,
        "expansion": expansion,
        "card_type": map_card_type(card_type),
        "color": map_color(color),
        "level": level,
        "cost": cost,
        "power": power,
        "soul": soul,
        "traits": traits,
        "text": text,
        "flavor": flavor
    }

    return card_dict

def map_color(color):
    if color == "yellow": return 1
    if color == "green": return 2
    if color == "red": return 3
    return 4

def map_card_type(card_type):
    if card_type.lower() == "character": return 1
    if card_type.lower() == "event": return 2
    if card_type.lower() == "climax": return 3