from Vse_Instrumenti.search_link_collector import SearchLinkCollector


class ParserVseInstr:
    def __init__(self):
        pass

    def run(self):
        search_phrase = 'ергия pro'
        get_search_data = SearchLinkCollector(search_phrase)
        get_search_data.run()
