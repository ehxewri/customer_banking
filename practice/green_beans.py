class Coffee:
    def __init__(self, name,origin,organic,vendor,settings,date_of_roast,brew_methood):
        self.name           = name
        self.origin         = origin
        self.organic        = organic
        self.vendor         = vendor
        self.settings       = settings
        self.date_of_roast  = date_of_roast
        self.brew_methood   = brew_methood
    def add_new(self):
        print('add new bean')
    def Modify(self):
        print('modify bean')
    def remove_bean(self):
        print('remove')
