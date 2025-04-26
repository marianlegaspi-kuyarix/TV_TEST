class TV:
    #Constant values
    MIN_CHL = 1
    MAX_CHL = 120
    MIN_VOL = 1
    MAX_VOL = 7
    
    def __init__(self):
        self.channel = TV.MIN_CHL
        self.volume_level = TV.MIN_VOL
        self.on = False
     
    def turn_on(self):
        self.on = True
    
    def turn_off(self):
        self.on = False
    
    #TV channel functions
    def get_channel(self):
        return self.channel
    
    def set_channel(self, channel):
        if self.on and TV.MIN_CHL <= channel <= TV.MAX_CHL:
            self.channel = channel

    def channel_up(self):
        if self.on and self.channel < TV.MAX_CHL:
            self.channel += 1

    def channel_down(self):
        if self.on and self.channel > TV.MIN_CHL:
            self.channel -= 1

    #TV volume functions
    def get_volume(self):
        return self.volume_level
    
    def set_volume(self, volume_level):
        if self.on and TV.MIN_VOL <= volume_level <= TV.MAX_VOL:
            self.volume_level = volume_level
    
    def volume_up(self):
        if self.on and self.volume_level < TV.MAX_VOL:
            self.volume_level += 1

    def volume_down(self):
        if self.on and self.volume_level > TV.MIN_VOL:
            self.volume_level -= 1
  