class Television:
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self) -> None:
        """
        Initializes the Television class with default values
        :param __muted: Volume set to MIN_VOLUME
        :param __volume: Starting volume
        :param __status: Power status starting value
        :param __channel: Starting channel
        :param __previous_volume: Previous value after muting
        """
        self.__muted: bool = False
        self.__volume: int = Television.MIN_VOLUME
        self.__status: bool = False
        self.__channel: int = Television.MIN_CHANNEL
        self.__previous_volume: int = self.__volume

    def power(self) -> None:
        """
        Toggles __status
        """
        self.__status = not self.__status

    def mute(self) -> None:
        """
        Mutes or unmutes the television. When muted, the volume is set to MIN_VOLUME.
        When unmuted, the volume is restored to the previous volume.
        """
        if self.__status:
            if not self.__muted:
                self.__previous_volume = self.__volume
                self.__volume = Television.MIN_VOLUME
                self.__muted = True
            else:
                self.__volume = self.__previous_volume
                self.__muted = False

    def channel_up(self) -> None:
        """
        Increases channel by 1. If channel goes above max_channel, wraps around to min_channel
        """
        if self.__status:
            if self.__channel < Television.MAX_CHANNEL:
                self.__channel += 1
            else:
                self.__channel = Television.MIN_CHANNEL

    def channel_down(self) -> None:
        """
        Decreases channel by 1. If channel goes below min_channel, wraps around to max_channel
        """
        if self.__status:
            if self.__channel > Television.MIN_CHANNEL:
                self.__channel -= 1
            else:
                self.__channel = Television.MAX_CHANNEL

    def volume_up(self) -> None:
        """
        Increases volume by 1. if muted, volume restored to value and then increases. cannot go above maximum volume
        """
        if self.__status:
            if self.__muted:
                self.__volume = self.__previous_volume
                self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """
        Decreases volume by 1. if muted, volume restored to value and then decreases. cannot go below minimum volume
        """
        if self.__status:
            if self.__muted:
                self.__volume = self.__previous_volume
                self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        if self.__muted:
            volume = Television.MIN_VOLUME
        else:
            volume = self.__volume
        return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
