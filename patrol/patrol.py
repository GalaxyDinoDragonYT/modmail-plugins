def __init__(self, bot):  # in the class init
    self.coll = bot.api.get_plugin_partition(self)
